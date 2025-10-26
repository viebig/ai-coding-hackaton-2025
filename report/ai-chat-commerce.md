# ai-chat-commerce — Scorecard para Jurados (0–5)

## Resumo Executivo
- Desafio: 4
- TL;DR (1 linha): Monorepo Go + React com arquitetura completa e docs, mas sem evidência clara de MVP rodando.
- Status: Parcial
- Demo: Sem evidências
- Rodar local: `docker-compose up -d postgres redis && (cd backend && go run cmd/api/main.go) && (cd frontend && npm install && npm run dev)`

## Ferramentas Utilizadas
- IDEs/Plataformas: Sem evidências
- Frameworks/Libs: Go (Gin, GORM), React + TypeScript + Vite, Socket.io
- Infra/Deploy: PostgreSQL, Redis, Stripe, Docker/Compose, GitHub Actions

## Alinhamento ao Desafio
- Desafio 4 (Chat Commerce), cobrindo chat, catálogo e checkout tradicionais.

## Originalidade (sinais objetivos)
- Arquitetura completa e documentação extensa; padrão consolidado em projetos de e-commerce/chat.

## MVP — O que funciona agora
- Estrutura de serviços backend/frontend e instruções de execução.

## Lacunas — O que não está pronto
- Sem prova de fluxo ponta-a-ponta rodando; ausência de demo pública.
- Integração efetiva de LLM não demonstrada nos arquivos inspecionados.

## Riscos e Próximos Passos
- Publicar demo mínima (vídeo/GIF e URL) comprovando jornada de compra via chat.
- Fixar scripts make/npm para subir stack inteira.
- Validar integração OpenAI no backend com cenários reais.

## Pontuação (0–5)
- Alinhamento ao desafio: 0.8/1.0
- Originalidade e escolhas autorais: 0.5/1.5
- Execução técnica proporcional ao tempo: 0.6/1.5
- Prontidão de demo/clareza: 0.3/1.0
- Nota final: 2.2/5.0

