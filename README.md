# Chatbot API de teste
Este é um projeto simples com FastAPI que simula múltiplas sessões de chat, como preparação para um projeto real com integração a chatbot e atendimento humano.

## Funcionalidades
- criação de sessões de chat via ID de usuário
- armazenamento temporário de mensagens por sessão
- API REST simples para enviar e consultar mensagens

## Tecnologias utilizadas
- [Python 3.x](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Git + GitHub

## Como executar

1. Clone o repositório:
git clone https://github.com/larissa-jungers/chatbot-api-teste.git
cd chatbot-api-teste

2. Crie e ative um ambiente virtual:
python -m venv venv
venv\Scripts\activate  # windows

3. Instale as dependências:
pip install fastapi uvicorn

4. Inicie a aplicação:
uvicorn main:app --reload

5. Acesse a API no navegador:
Documentação interativa: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


## Estrutura atual do projeto
chatbot-api-teste/
├── main.py
├── venv/ (no .gitignore)
├── .gitignore
├── README.md
└── requirements.txt

## Objetivo
Este repositório faz parte da minha jornada de aprendizado em desenvolvimento backend com Python. A ideia é criar uma base sólida para trabalhar com múltiplas sessões de chat, simulação de chatbot e integração futura com o Telegram.

Desenvolvido por Larissa Jungers