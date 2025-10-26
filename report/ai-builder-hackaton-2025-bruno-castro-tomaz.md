# ai-builder-hackaton-2025-bruno-castro-tomaz — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 1
- TL;DR (1 linha): API SAC com RAG local (LangChain + Chroma + HF Embeddings) e resposta via Gemini; código comentado, setup com issues de requirements.
- Status: Parcial
- Demo: Sem evidências
- Rodar local: `pip install -r requirements.txt && python chatSAC/app.py`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: LangChain, Chroma, HuggingFace Embeddings, Google Gemini
- Infra/Deploy: Python local

## Alinhamento ao Desafio
- Desafio 1 (API de SAC) com pipeline de contexto + geração.

## Originalidade (sinais objetivos)
- Combinação de RAG local e Gemini; estrutura autoral.

## MVP — O que funciona agora
- Geração de embeddings, busca por contexto e chamada ao Gemini.

## Lacunas — O que não está pronto
- Endpoint HTTP/API não evidenciado; README mínimo; issues de encoding em requirements.

## Riscos e Próximos Passos
- Corrigir `requirements.txt` e publicar `.env.example`.
- Expor API HTTP simples (FastAPI/Flask) para consumo externo.
- Adicionar exemplos de requisição e script de ingestão de políticas.

## Pontuação (0–5)
- Alinhamento ao desafio: 0.9/1.0
- Originalidade e escolhas autorais: 1.0/1.5
- Execução técnica proporcional ao tempo: 0.8/1.5
- Prontidão de demo/clareza: 0.4/1.0
- Nota final: 3.1/5.0

