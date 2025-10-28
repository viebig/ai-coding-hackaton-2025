# delivery_hackathon — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 4
- TL;DR (1 linha): Jornada de compra por WhatsApp com Supabase Edge Functions + OpenAI (Responses/Conversations), orquestração e PRD completos.
- Status: Funciona
- Demo: Sem evidências
- Rodar local: `supabase functions serve` + configurar secrets; ver README

## Ferramentas Utilizadas
- IDEs/Plataformas: Supabase (Edge Functions)
- Frameworks/Libs: Deno serve em functions; OpenAI Responses/Whisper; webhooks WhatsApp (WAME)
- Infra/Deploy: Supabase (Postgres, Auth), secrets e migrations SQL; retries e logging

## Alinhamento ao Desafio
- Desafio 4 (Chat Commerce) via canal WhatsApp, incluindo orquestrador, transcrição, validação de pedido e finalização com tools.

## Originalidade (sinais objetivos)
- Uso avançado das APIs novas da OpenAI (Responses/Conversations) e retries exponenciais; PRD detalhado.

## MVP — O que funciona agora
- Funções: propor-pedido, adicionar-item-carrinho, transcrever áudio, validar pedido por áudio, finalizar pedido com function calling.

## Lacunas — O que não está pronto
- Sem link de demo público; dependente de chaves/infra externas (WAME/OpenAI/Supabase) para rodar.

## Riscos e Próximos Passos
- Provisionar ambiente demo com logs acessíveis e seed de cardápio.
- Observabilidade (tracing por conversation_id) e tetos de custo.
- Testes end‑to‑end com cenários WhatsApp reais.

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.4/1.5
- Execução técnica proporcional ao tempo: 1.5/1.5
- Prontidão de demo/clareza: 0.7/1.0
- Nota final: 4.6/5.0

