# ai_builder_hackathon_2025_PMOslack — Scorecard para Jurados (0–5)

Repositório: https://github.com/viebig/ai-coding-hackaton-2025


## Resumo Executivo
- Desafio: 3
- TL;DR (1 linha): Integração Slack básica (ler/enviar mensagens, gerenciar canais) sem camada de IA/PMO inteligente.
- Status: Parcial
- Demo: Sem evidências
- Rodar local: `pip install -r requirements.txt && python bot.py`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: slack-sdk, python-dotenv (Python)
- Infra/Deploy: Scripts locais

## Alinhamento ao Desafio
- Desafio 3 (PMO no Slack); faltam automações inteligentes (entendimento de status, resumos diários, prompts/LLM).

## Originalidade (sinais objetivos)
- Estrutura modular clara (SlackBot, MessageReader); sem sinais de cópia de template completo.

## MVP — O que funciona agora
- Envio/leitura de mensagens, obtenção de usuários, tentativa de join em canais.

## Lacunas — O que não está pronto
- Ausência de IA (resumos/extração de status, prompts, integração LLM).
- Sem README e demo.

## Riscos e Próximos Passos
- Adicionar README com setup do Slack App (scopes, tokens, eventos).
- Implementar rotinas de resumo diário e parsing de updates (talvez com OpenAI/Gemini).
- Persistir estado mínimo (SQLite) para threads/tarefas.

## Pontuação (0–5)
- Alinhamento ao desafio: 0.6/1.0
- Originalidade e escolhas autorais: 0.6/1.5
- Execução técnica proporcional ao tempo: 0.9/1.5
- Prontidão de demo/clareza: 0.5/1.0
- Nota final: 2.6/5.0

