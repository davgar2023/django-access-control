# 🚪 Access Control API

API RESTful para gestionar puntos de acceso y registrar eventos de ingreso de personas. Desarrollado con Django + Django REST Framework, PostgreSQL y Docker.

---

## ⚙️ Tecnologías

- Python 3.12
- Django 4.x
- Django REST Framework
- PostgreSQL 15
- JWT Authentication (SimpleJWT)
- Docker & Docker Compose
- python-decouple para configuración segura

---

## 📦 Estructura del proyecto

```
access-control/
├── docker-compose.yml
├── .env
├── db/                   # Volumen de PostgreSQL
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    ├── access_control/   # Proyecto Django
    └── access/           # App con modelos y lógica
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/davgar2023/access-control.git
cd access-control
```

### 2. Configurar entorno

Crear archivo `.env`:

```env
SECRET_KEY=tu_clave_django
DEBUG=1
ALLOWED_HOSTS=*
POSTGRES_DB=access_db
POSTGRES_USER=access_user
POSTGRES_PASSWORD=access_pass
DB_HOST=db
DB_PORT=5432
```

### 3. Levantar el proyecto

```bash
docker compose up --build
```

Visita:

- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/

---

## 🔐 Autenticación

Usamos JWT con los siguientes endpoints:

| Acción           | Endpoint                         |
|------------------|----------------------------------|
| Registro         | `POST /api/auth/register/`       |
| Login (token)    | `POST /api/auth/token/`          |
| Refresh token    | `POST /api/auth/token/refresh/`  |

> Requiere `Bearer <access_token>` en los headers para los endpoints protegidos.

---

## 🧪 Endpoints principales

### 📍 Access Points (`/api/access-points/`)
- `GET` – Listar puntos
- `POST` – Crear punto
- `PATCH/DELETE` – Modificar o eliminar

### 📝 Access Events (`/api/access-events/`)
- `GET` – Listar eventos
- `POST` – Registrar evento

---

## 🧪 Pruebas con Postman

Importa la colección Postman desde el archivo `access-control.postman_collection.json` o usa los siguientes endpoints manualmente con los tokens correspondientes.

---

## 👤 Superusuario

Para acceder al panel admin:

```bash
docker compose exec backend python manage.py createsuperuser
```

---

## 🛑 Apagar el entorno

```bash
docker compose down
```

---

## 📌 Notas

- El token `access` tiene duración de 60 minutos.
- El token `refresh` tiene duración de 7 días.
- Los eventos de acceso se asignan automáticamente al usuario autenticado si existe.

---

## 📃 Licencia

MIT © David Garcia
