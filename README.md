# Movies API

API de filmes construída com Django 6.0.

Objetivo aqui é não usar Django Rest Framework e Serializer.

## Requisitos

- Python 3.14+
- pip

## Instalação

```bash
git clone <repo-url>
cd movies-api

python -m venv venv
venv\Scripts\activate
pip install django
```

## Executando

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://localhost:8000/admin/ para o painel administrativo.

## Apps

### Genres

Gerencia os gêneros de filmes.

**Model `Genre`:**
- `name` — nome do gênero (CharField, max_length=100)

## Endpoints

| Método | Rota       | Descrição                |
|--------|------------|--------------------------|
| GET    | `/admin/`  | Painel administrativo    |
