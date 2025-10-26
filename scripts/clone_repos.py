#!/usr/bin/env python3

import argparse
import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple
from urllib.parse import urlparse


def find_first_url(cells: Iterable[str]) -> Optional[str]:
    for cell in cells:
        value = (cell or "").strip()
        if value.startswith("http://") or value.startswith("https://"):
            return value
    return None


def derive_repo_dir_name(repo_url: str) -> str:
    parsed = urlparse(repo_url)
    last_segment = Path(parsed.path).name
    if last_segment.endswith(".git"):
        last_segment = last_segment[:-4]
    return last_segment or "repository"


def run_command(command: List[str], cwd: Optional[Path] = None) -> Tuple[int, str, str]:
    env = os.environ.copy()
    # Avoid interactive prompts in case of auth-required repos
    env.setdefault("GIT_TERMINAL_PROMPT", "0")
    process = subprocess.Popen(
        command,
        cwd=str(cwd) if cwd is not None else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


def clone_repo(repo_url: str, dest_dir: Path) -> Tuple[bool, str]:
    # Use GitHub CLI to ensure authenticated cloning
    code, out, err = run_command([
        "gh",
        "repo",
        "clone",
        repo_url,
        str(dest_dir),
        "--",
        "--depth",
        "1",
    ])
    if code == 0:
        return True, out.strip()
    return False, (err or out).strip()


def update_repo(repo_dir: Path) -> Tuple[bool, str]:
    """Update an existing repository to match its remote.

    Strategy (best-effort, non-interactive):
      1) git fetch --all --prune
      2) git pull --ff-only
      3) If ff-only fails, try to unshallow then ff-only again
      4) If it still fails, hard reset to the upstream (destructive)
    """

    logs: List[str] = []

    # Step 1: fetch
    code, out, err = run_command(["git", "fetch", "--all", "--prune"], cwd=repo_dir)
    logs.append((out or "") + (err or ""))
    if code != 0:
        return False, "fetch failed: " + (err or out).strip()

    # Step 2: try fast-forward pull
    code, out, err = run_command(["git", "pull", "--ff-only"], cwd=repo_dir)
    logs.append((out or "") + (err or ""))
    if code == 0:
        return True, "".join(logs).strip()

    # Step 3: attempt to unshallow (in case initial clone was shallow)
    code_us, out_us, err_us = run_command(["git", "fetch", "--unshallow", "--tags"], cwd=repo_dir)
    # Some repos are already complete; git returns error in that case. Ignore non-zero here.
    logs.append((out_us or "") + (err_us or ""))

    code, out, err = run_command(["git", "pull", "--ff-only"], cwd=repo_dir)
    logs.append((out or "") + (err or ""))
    if code == 0:
        return True, "".join(logs).strip()

    # Step 4: last resort — hard reset to upstream (destructive)
    # Determine upstream; fall back to origin/<current-branch>
    code_br, out_br, err_br = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_dir)
    current_branch = (out_br or "").strip() if code_br == 0 else "main"

    code_up, out_up, err_up = run_command(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], cwd=repo_dir)
    upstream = (out_up or "").strip() if code_up == 0 else f"origin/{current_branch}"

    # Ensure we have the target upstream ref
    run_command(["git", "fetch", "--all", "--prune"], cwd=repo_dir)

    code_rs, out_rs, err_rs = run_command(["git", "reset", "--hard", upstream], cwd=repo_dir)
    logs.append((out_rs or "") + (err_rs or ""))
    if code_rs == 0:
        return True, ("ff-only failed; performed hard reset to " + upstream + "\n" + "".join(logs)).strip()

    return False, ("failed to update even after hard reset attempt\n" + "".join(logs)).strip()


def read_repo_urls(tsv_path: Path) -> List[str]:
    urls: List[str] = []
    with tsv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if not row:
                continue
            url = find_first_url(row)
            if url:
                urls.append(url)
    # de-duplicate while preserving order
    seen = set()
    deduped: List[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def ensure_gh_authenticated(host: str = "github.com") -> None:
    if shutil.which("gh") is None:
        print(
            "Error: GitHub CLI 'gh' not found. Install from https://cli.github.com/ and run 'gh auth login'.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    code, out, err = run_command(["gh", "auth", "status", "--hostname", host])
    if code != 0:
        print(f"Error: GitHub CLI not authenticated for {host}. Run: gh auth login", file=sys.stderr)
        if err or out:
            print((err or out).strip(), file=sys.stderr)
        raise SystemExit(1)


def main(argv: Optional[List[str]] = None) -> int:
    script_path = Path(__file__).resolve()
    workspace_root = script_path.parent.parent

    default_csv = workspace_root / "repos.csv"
    default_dest = workspace_root / "repos"

    parser = argparse.ArgumentParser(description="Clone or update repositories listed in a TSV (repos.csv)")
    parser.add_argument("--csv", dest="csv_path", type=Path, default=default_csv, help="Path to repos.csv (TSV format)")
    parser.add_argument("--dest", dest="dest_dir", type=Path, default=default_dest, help="Destination directory to place repositories")
    parser.add_argument("--update", action="store_true", help="If a repo already exists, update it instead of skipping")
    args = parser.parse_args(argv)

    if not args.csv_path.exists():
        print(f"Error: CSV file not found: {args.csv_path}", file=sys.stderr)
        return 1

    try:
        repo_urls = read_repo_urls(args.csv_path)
    except Exception as exc:
        print(f"Error reading CSV: {exc}", file=sys.stderr)
        return 1

    if not repo_urls:
        print("No repository URLs found in CSV. Nothing to do.")
        return 0

    # Ensure user is authenticated with gh before attempting clones
    ensure_gh_authenticated("github.com")

    args.dest_dir.mkdir(parents=True, exist_ok=True)

    num_cloned = 0
    num_updated = 0
    num_skipped = 0
    failures: List[Tuple[str, str]] = []  # (url, reason)

    for url in repo_urls:
        repo_name = derive_repo_dir_name(url)
        target_dir = args.dest_dir / repo_name

        if target_dir.exists() and (target_dir / ".git").exists():
            if args.update:
                print(f"Updating {repo_name} ...")
                ok, message = update_repo(target_dir)
                if ok:
                    num_updated += 1
                else:
                    failures.append((url, message))
                continue
            else:
                num_skipped += 1
                print(f"Skipping existing {repo_name}")
                continue

        print(f"Cloning {repo_name} from {url} ...")
        ok, message = clone_repo(url, target_dir)
        if ok:
            num_cloned += 1
        else:
            failures.append((url, message))

    print()
    print("Done.")
    print(f"Cloned: {num_cloned}")
    print(f"Updated: {num_updated}")
    print(f"Skipped: {num_skipped}")
    if failures:
        print(f"Failures: {len(failures)}")
        for url, reason in failures:
            print(f" - {url}: {reason}")

    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())

