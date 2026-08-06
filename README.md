# Movies API

API de filmes construída com Django 6.0 e Django Rest Framework. Autenticação via JWT (SimpleJWT). Banco de dados SQLite3.

## Requisitos

- Python 3.14+
- pip

## Instalação

```bash
git clone <repo-url>
cd movies-api

python -m venv venv
venv\Scripts\activate

pip install django djangorestframework djangorestframework-simplejwt
```

## Executando

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://localhost:8000/admin/ para o painel administrativo do Django.

## Autenticação

A API usa JWT para autenticação. Inclua o token no header `Authorization: Bearer <access_token>` em todas as requisições protegidas.

### Obter token

```bash
POST /api/v1/authentication/token/
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

Resposta:

```json
{
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

- `access_token` — válido por **5 minutos**
- `refresh_token` — válido por **10 dias**

Para renovar o token: `POST /api/v1/authentication/token/refresh/` com `{"refresh": "<refresh_token>"}`.

## Apps

### Genres

Gerencia os gêneros de filmes.

**Model `Genre`:**

| Campo | Tipo       | Restrições   |
|-------|------------|--------------|
| `name` | CharField | max_length=100 |

### Actors

Gerencia os atores.

**Model `Actor`:**

| Campo         | Tipo       | Restrições                                     |
|---------------|------------|------------------------------------------------|
| `name`        | CharField | max_length=200                                  |
| `birthday`    | DateField | null=True, blank=True                           |
| `nationality` | CharField | max_length=100, choices: BR / USA, null/blank |

### Movies

Gerencia os filmes.

**Model `Movie`:**

| Campo          | Tipo          | Restrições                              |
|----------------|---------------|-----------------------------------------|
| `title`        | CharField     | max_length=500                          |
| `genre`        | ForeignKey    | Genre, on_delete=PROTECT                |
| `release_date` | DateField     | null=True, blank=True                   |
| `actors`       | ManyToManyField | Actor                                  |
| `resume`       | TextField     | null=True, blank=True, max 200 chars    |

O campo `rate` (média das avaliações) é computado automaticamente pelo serializer.

### Reviews

Gerencia as avaliações dos filmes.

**Model `Review`:**

| Campo    | Tipo         | Restrições                         |
|----------|--------------|------------------------------------|
| `movie`  | ForeignKey   | Movie, on_delete=PROTECT           |
| `stars`  | IntegerField | validators: MinValue(0), MaxValue(5) |
| `comment`| TextField    | null=True, blank=True              |

## Endpoints

### Autenticação

| Método | Rota                                   | Descrição               | Autenticação |
|--------|----------------------------------------|-------------------------|--------------|
| POST   | `/api/v1/authentication/token/`         | Obter token JWT         | Não          |
| POST   | `/api/v1/authentication/token/refresh/` | Renovar access token    | Não          |
| POST   | `/api/v1/authentication/token/verify/`  | Verificar token         | Não          |

### Genres

| Método | Rota                   | Descrição       | Autenticação |
|--------|------------------------|-----------------|--------------|
| GET    | `/api/v1/genres/`      | Listar gêneros  | Sim          |
| POST   | `/api/v1/genres/`      | Criar gênero    | Sim          |
| GET    | `/api/v1/genres/<id>/` | Detalhar gênero | Sim          |
| PUT    | `/api/v1/genres/<id>/` | Atualizar gênero| Sim          |
| PATCH  | `/api/v1/genres/<id>/` | Atualizar parcial| Sim          |
| DELETE | `/api/v1/genres/<id>/` | Excluir gênero  | Sim          |

### Actors

| Método | Rota                   | Descrição      | Autenticação |
|--------|------------------------|----------------|--------------|
| GET    | `/api/v1/actors/`      | Listar atores  | Sim          |
| POST   | `/api/v1/actors/`      | Criar ator     | Sim          |
| GET    | `/api/v1/actors/<id>/` | Detalhar ator  | Sim          |
| PUT    | `/api/v1/actors/<id>/` | Atualizar ator | Sim          |
| PATCH  | `/api/v1/actors/<id>/` | Atualizar parcial| Sim         |
| DELETE | `/api/v1/actors/<id>/` | Excluir ator   | Sim          |

### Movies

| Método | Rota                   | Descrição       | Autenticação |
|--------|------------------------|-----------------|--------------|
| GET    | `/api/v1/movies/`      | Listar filmes   | Sim          |
| POST   | `/api/v1/movies/`      | Criar filme     | Sim          |
| GET    | `/api/v1/movies/<id>/` | Detalhar filme  | Sim          |
| PUT    | `/api/v1/movies/<id>/` | Atualizar filme | Sim          |
| PATCH  | `/api/v1/movies/<id>/` | Atualizar parcial| Sim         |
| DELETE | `/api/v1/movies/<id>/` | Excluir filme   | Sim          |

### Reviews

| Método | Rota                    | Descrição          | Autenticação |
|--------|-------------------------|--------------------|--------------|
| GET    | `/api/v1/reviews/`      | Listar avaliações  | Sim          |
| POST   | `/api/v1/reviews/`      | Criar avaliação    | Sim          |
| GET    | `/api/v1/reviews/<id>/` | Detalhar avaliação | Sim          |
| PUT    | `/api/v1/reviews/<id>/` | Atualizar avaliação| Sim          |
| PATCH  | `/api/v1/reviews/<id>/` | Atualizar parcial  | Sim          |
| DELETE | `/api/v1/reviews/<id>/` | Excluir avaliação  | Sim          |

### Admin

| Método | Rota      | Descrição                 |
|--------|-----------|---------------------------|
| GET    | `/admin/` | Painel administrativo Django |

## Estrutura do projeto

```
movies-api/
├── actors/           # App de atores
├── app/              # Configuração principal (settings, urls, wsgi)
├── authentication/   # App de autenticação JWT
├── genres/           # App de gêneros
├── movies/           # App de filmes
├── reviews/          # App de avaliações
├── manage.py         # Script de gerenciamento do Django
├── db.sqlite3        # Banco de dados SQLite
├── venv/             # Ambiente virtual
└── README.md
```

## Banco de dados

SQLite3 (`db.sqlite3`). Execute `python manage.py migrate` para criar as tabelas.
