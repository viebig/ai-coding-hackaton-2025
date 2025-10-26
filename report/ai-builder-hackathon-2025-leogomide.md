# ai-builder-hackathon-2025-leogomide — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 2
- TL;DR (1 linha): T3 Stack completa bem configurada; pouca adaptação ao nicho alvo.
- Status: Parcial
- Demo: Sem evidências
- Rodar local: `pnpm install && pnpm dev`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: Next.js 15, tRPC, Prisma, NextAuth, Tailwind v4, React Email
- Infra/Deploy: pnpm, Dockerfile, env validation (@t3-oss/env-nextjs)

## Alinhamento ao Desafio
- Desafio 2 (LinkedIn segmentado); sem features específicas do segmento implementadas.

## Originalidade (sinais objetivos)
- Forte uso de boilerplate T3; documentação e estrutura sólidas, mas sem diferenciais funcionais.

## MVP — O que funciona agora
- Autenticação/esqueleto de API com tRPC e Prisma configurados.
- Scripts de DB e emails de verificação.

## Lacunas — O que não está pronto
- Funcionalidades do nicho (perfis, matchmaking, oportunidades específicas).
- Demo pública.

## Riscos e Próximos Passos
- Modelar entidades do segmento e páginas de perfil/descoberta.
- Fluxos mínimos (cadastro, busca, feed) com dados seed.
- Deploy (Vercel) e instruções com `.env.example`.

## Pontuação (0–5)
- Alinhamento ao desafio: 0.6/1.0
- Originalidade e escolhas autorais: 0.4/1.5
- Execução técnica proporcional ao tempo: 0.7/1.5
- Prontidão de demo/clareza: 0.3/1.0
- Nota final: 2.0/5.0

