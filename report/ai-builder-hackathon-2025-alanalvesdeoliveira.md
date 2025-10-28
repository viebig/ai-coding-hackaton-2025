# ai-builder-hackathon-2025-alanalvesdeoliveira — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 4
- TL;DR (1 linha): AutoParts AI — chat commerce para peças automotivas com Next.js e integração real com Gemini (diagnóstico e cotação).
- Status: Funciona
- Demo: Sem evidências
- Rodar local: `npm install && npm run dev`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: Next.js (App Router), TypeScript, Tailwind, Zod
- Infra/Deploy: Gemini Pro (google‑generative‑ai), rotas API Next, persistência via DB (descrita no README)

## Alinhamento ao Desafio
- Desafio 4 (experiência de compra por chat) com foco em B2C de autopeças.

## Originalidade (sinais objetivos)
- Extração de problema/peças e detecção de intenção de cotação; prompts dinâmicos versionados em DB.

## MVP — O que funciona agora
- Rotas API de prompts/cotações conversacionais; fluxo de chat Gemini; páginas dedicadas para visualizar cotações.

## Lacunas — O que não está pronto
- Link de demo público ausente.
- Integrações de pagamento/logística não evidenciadas.

## Riscos e Próximos Passos
- Publicar `.env.example` e demo Vercel.
- Amarrar fluxo de checkout (carrinho/pagamento) e SKUs reais.
- Logs estruturados e limites de custo por conversa.

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.2/1.5
- Execução técnica proporcional ao tempo: 1.4/1.5
- Prontidão de demo/clareza: 0.8/1.0
- Nota final: 4.4/5.0

