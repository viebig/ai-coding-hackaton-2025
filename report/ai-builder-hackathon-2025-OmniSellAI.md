# ai-builder-hackathon-2025-OmniSellAI — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 4
- TL;DR (1 linha): Plataforma completa de chat-commerce B2B (frontend React + backend Express) com IA OpenAI e catálogo/carrinho integrados.
- Status: Parcial
- Demo: Sem evidências
- Rodar local: `npm install && npm run dev` (frontend) + `npm run dev` (server)

## Ferramentas Utilizadas
- IDEs/Plataformas: Replit (arquivos .replit/replit.md)
- Frameworks/Libs: React + Vite, Express (TypeScript), TanStack Query, Zod, Drizzle ORM
- Infra/Deploy: PostgreSQL (Neon), Google Cloud Storage, OpenAI (GPT‑4o‑mini, Whisper)

## Alinhamento ao Desafio
- Desafio 4 (Experiência de compra por chat) com catálogo híbrido, IA conversacional e function calling para pedidos.

## Originalidade (sinais objetivos)
- Multi-tenant, identificação omnichannel, validação anti‑alucinação recalculando totais no backend.

## MVP — O que funciona agora
- Catálogo + chat com integração de IA e carrinho sincronizado.
- APIs de clientes/produtos/pedidos; upload e otimização de imagens.

## Lacunas — O que não está pronto
- Sem link de demo pública no repo.
- Scripts unificados de orquestração (mono) não evidenciados.

## Riscos e Próximos Passos
- Publicar demo (frontend + server) e `.env.example` completo.
- Testes e2e mínimos do fluxo comprar pelo chat.
- Hardening de auth/RBAC e limites de rate.

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.1/1.5
- Execução técnica proporcional ao tempo: 1.3/1.5
- Prontidão de demo/clareza: 0.6/1.0
- Nota final: 4.0/5.0

