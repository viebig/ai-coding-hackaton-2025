# ai-builder-hackthon-2025-victor — Scorecard para Jurados (0–5)

Repositório: https://github.com/viebig/ai-coding-hackaton-2025


## Resumo Executivo
- Desafio: 1
- TL;DR (1 linha): API SAC com FastAPI + Gemini, arquitetura e documentação profissionais, testes e segurança por API key.
- Status: Funciona
- Demo: Sem evidências
- Rodar local: `pip install -r requirements.txt && uvicorn src.main:app --reload`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: FastAPI, Uvicorn, Pydantic, google-generativeai (Gemini)
- Infra/Deploy: `.env.example`, pytest/httpx, scripts

## Alinhamento ao Desafio
- Desafio 1 (API de SAC) com rotas, validação de API key, orquestração e chamada real ao Gemini.

## Originalidade (sinais objetivos)
- PRD/PLAN detalhados, pasta `_agents` descrevendo papéis e arquitetura; implementação com camadas e injeção de dependências.

## MVP — O que funciona agora
- Endpoint SAC com integração real a Gemini.
- Segurança via API key e middlewares de CORS/log.
- Testes e exemplos de uso.

## Lacunas — O que não está pronto
- Sem demo público.
- Integrações externas (ERP/pedidos) simuladas/local.

## Riscos e Próximos Passos
- Adicionar fonte de verdade (pedidos/políticas) e tracing.
- Publicar demo (Railway/Fly/Vercel + serverless compatível).
- Observabilidade básica (logs estruturados, correlação).

## Pontuação (0–5)
- Alinhamento ao desafio: 1.0/1.0
- Originalidade e escolhas autorais: 1.5/1.5
- Execução técnica proporcional ao tempo: 1.5/1.5
- Prontidão de demo/clareza: 0.9/1.0
- Nota final: 4.9/5.0

