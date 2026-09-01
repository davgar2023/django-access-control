# 🚪 Access Control API

RESTful API to manage access points and register people entry events. Built with Django and Django REST Framework, PostgreSQL, and Docker.

---

## 🔧 What it does

This service provides an API to register physical access points (doors, gates, turnstiles, etc.) and record access events when people enter or exit. It includes JWT-based authentication, admin UI for managing records, and Docker-based deployment for local development.

Main features:
- Register and manage access points (create, read, update, delete).
- Record access events tied to an authenticated user and an access point.
- JWT authentication (access + refresh tokens).
- Admin interface to manage users, access points and events.

---

## ⚙️ Tech stack

- Python 3.12
- Django 4.x
- Django REST Framework
- PostgreSQL 15
- SimpleJWT (JWT authentication)
- Docker & Docker Compose
- python-decouple for environment configuration

---

## 📦 Project structure

```
access-control/
├── docker-compose.yml
├── .env
├── db/                   # PostgreSQL volume
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    ├── access_control/   # Django project
    └── access/           # App with models and logic
```

---

## Prerequisites

- Docker and Docker Compose installed (v2 recommended)
- Git

---

## 🚀 Quick start (Docker)

1. Clone the repository

```bash
git clone https://github.com/davgar2023/django-access-control.git
cd django-access-control
```

2. Create a `.env` file in the repository root (example values below). The application reads configuration from environment variables.

```env
SECRET_KEY=your_django_secret_key
DEBUG=1
ALLOWED_HOSTS=*
POSTGRES_DB=access_db
POSTGRES_USER=access_user
POSTGRES_PASSWORD=access_pass
DB_HOST=db
DB_PORT=5432
```

3. Build and run the services

```bash
docker compose up --build
```

The API will be available at: http://localhost:8000/api/
The Django admin will be available at: http://localhost:8000/admin/

4. Apply migrations and create a superuser (if needed)

If you need to run management commands after the containers are up:

```bash
# Apply migrations
docker compose exec backend python manage.py migrate

# Create a superuser
docker compose exec backend python manage.py createsuperuser
```

---

## Environment variables (common)

- SECRET_KEY: Django secret key
- DEBUG: 1 or 0
- ALLOWED_HOSTS: comma-separated hosts or `*`
- POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD: database credentials
- DB_HOST, DB_PORT: database host and port

Adjust these values for production and do not commit sensitive secrets to the repository.

---

## 🔐 Authentication

This project uses JWT (SimpleJWT). Endpoints:

| Action           | Endpoint                         |
|------------------|----------------------------------|
| Register         | `POST /api/auth/register/`       |
| Login (token)    | `POST /api/auth/token/`          |
| Refresh token    | `POST /api/auth/token/refresh/`  |

Protected endpoints require the header: `Authorization: Bearer <access_token>`.

Notes:
- Access token lifetime: 60 minutes (default in this project)
- Refresh token lifetime: 7 days

---

## 🔍 Main API endpoints

### Access Points
Base: `/api/access-points/`
- `GET /api/access-points/` – List access points (paginated)
- `POST /api/access-points/` – Create a new access point
- `GET /api/access-points/{id}/` – Retrieve details for an access point
- `PATCH /api/access-points/{id}/` – Partially update
- `DELETE /api/access-points/{id}/` – Delete

### Access Events
Base: `/api/access-events/`
- `GET /api/access-events/` – List access events
- `POST /api/access-events/` – Record a new access event
- `GET /api/access-events/{id}/` – Retrieve event details

Behavior:
- When an authenticated user creates an access event, the event is automatically associated with that user.

---

## Examples (curl)

Register a user (example payload depends on the implementation):

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass"}'
```

Obtain tokens:

```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass"}'
```

Create an access event (replace <ACCESS_TOKEN> and <ACCESS_POINT_ID>):

```bash
curl -X POST http://localhost:8000/api/access-events/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"access_point": <ACCESS_POINT_ID>, "event_type": "enter", "metadata": "optional"}'
```

---

## Postman

A Postman collection is included: `access-control.postman_collection.json`. Import it into Postman to test the API endpoints and workflows.

---

## Admin

Use the Django admin at `/admin/` to manage users, access points and events. Create a superuser as shown in the Quick start section.

---

## Testing

If the project includes Django tests, run them with:

```bash
docker compose exec backend python manage.py test
```

Add unit and integration tests to cover the API endpoints and authentication flows.

---

## Troubleshooting

- Database connection errors: ensure the `db` service is running and the `.env` DB credentials match.
- Port conflicts: the default Django port is 8000; change it in `docker-compose.yml` if needed.
- Static files in production: collect static files and configure a web server (e.g., Nginx) to serve them.

---

## Contributing

Contributions, issues and feature requests are welcome. Please open an issue or submit a pull request.

Suggested workflow:
1. Fork the repository
2. Create a feature branch (git checkout -b feature/your-feature)
3. Commit your changes and push
4. Open a pull request

---

## License

MIT © David Garcia

---

## Author / Contact

David Garcia — https://github.com/davgar2023

If you want additional documentation (OpenAPI/Swagger, example Postman walkthrough, or CI setup), tell me which you'd like and I can add it to the README or create the files.