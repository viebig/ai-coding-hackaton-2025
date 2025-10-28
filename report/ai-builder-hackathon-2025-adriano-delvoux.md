# ai-builder-hackathon-2025-adriano-delvoux — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 2
- TL;DR (1 linha): “PartyConnect” — LinkedIn para festas/eventos com matching em grafos (Neo4j) e web app Next.
- Status: Funciona
- Demo: Sem evidências
- Rodar local: `pnpm install && pnpm migration:up && pnpm dev`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: ElysiaJS (Bun, backend), Next.js (web), MikroORM, Zod
- Infra/Deploy: PostgreSQL, Neo4j, Swagger; bibliotecas OpenAI Agents presentes no lock (potencial IA)

## Alinhamento ao Desafio
- Desafio 2 (LinkedIn para segmento específico), com foco claro em mercado de festas/eventos.

## Originalidade (sinais objetivos)
- Arquitetura dual DB (Postgres + Neo4j) para matching; middleware e rotas bem detalhadas.

## MVP — O que funciona agora
- API documentada (Swagger), autenticação JWT, páginas Next para onboarding/interesses/feed/threads.

## Lacunas — O que não está pronto
- Link de demo ausente; não há prova de deploy.
- Sinais de IA (agents) no lock sem uso explícito no código web/api.

## Riscos e Próximos Passos
- Publicar demo e seeds; adicionar testes de matching e endpoints críticos.
- Expor métricas básicas (matches, conversões) e observabilidade.
- Descrever pipeline de dados Neo4j (jobs e sincronização) no README.

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.3/1.5
- Execução técnica proporcional ao tempo: 1.4/1.5
- Prontidão de demo/clareza: 0.5/1.0
- Nota final: 4.2/5.0

