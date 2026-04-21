# 🐍 Discord.py SQLAlchemy Starter

Este projeto é um boilerplate (modelo inicial) robusto para o desenvolvimento de bots de Discord. O objetivo principal é eliminar o trabalho repetitivo de configuração inicial, entregando uma estrutura pronta com banco de dados, sistema de migrações e cache de alta performance.

## ✨ Funcionalidades

- Persistencia de dados com SQLAlchemy
- Cache de dados e filas com Redis
- Gestão de banco de dados com Alembic
- Qualidade de código com Mypy e Ruff

## 🛠️ Stack

- discord.py
- SQLAlchemy
- Alembic
- Redis
- Ruff
- Mypy

## 🚀 Como rodar o projeto

Independente do projeto, sempre rode os comandos abaixo:

```bash
git clone https://github.com/paulocvieirajunior/discord-py-sqlalchemy-starter
cd discord-py-sqlalchemy-starter
# No Windows:
copy .env.example .env
# No Linux/Mac:
cp .env.example .env
```

### 🐳 Com Docker (recomendado)

**Requisitos**
- Docker

```bash
docker compose up -d --build
```

### 💻 Sem Docker

**Requisitos**
- Python 3.13
- PostgreSQL 16
- Redis 7.2

```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
# Instalar dependências:
pip install -r requirements.txt
# Rodar o bot:
python app/main.py
```