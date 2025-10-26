# ai-builder-hackathon-2025-danilomax — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 4
- TL;DR (1 linha): Chat commerce com Next.js usando Vercel AI SDK + OpenAI, integração simples e funcional.
- Status: Funciona
- Demo: Sem evidências
- Rodar local: `npm install && npm run dev`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: Next.js 15, React 19, TypeScript, Tailwind, Vercel AI SDK (`ai`), `openai`, `@ai-sdk/openai`, Supabase JS, Zod
- Infra/Deploy: Vercel (README padrão), npm

## Alinhamento ao Desafio
- Desafio 4 (Experiência de compra por chat) com foco em interface conversacional para consulta/ação.

## Originalidade (sinais objetivos)
- Uso direto do Vercel AI SDK e OpenAI, com adaptação para fluxo de compras; padrão comum mas bem aplicado.

## MVP — O que funciona agora
- Pipeline de chat com LLM operando no app Next.js.
- Tipagem e validação com Zod; setup rápido para demo.

## Lacunas — O que não está pronto
- Integração real com catálogo/pagamento não evidenciada.
- Sem link de demo público no repo.

## Riscos e Próximos Passos
- Conectar a fonte de produtos (API/DB) e retornar SKUs acionáveis.
- Adicionar ações (add-to-cart/checkout) acionadas pela resposta do LLM.
- Publicar demo na Vercel com `.env.example` claro.

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.0/1.5
- Execução técnica proporcional ao tempo: 1.5/1.5
- Prontidão de demo/clareza: 1.0/1.0
- Nota final: 4.5/5.0

