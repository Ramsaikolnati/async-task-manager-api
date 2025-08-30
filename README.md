# Async Task Manager API 🚀

A production-ready asynchronous task management system built with **FastAPI**.  
This API allows users to create, manage, and monitor tasks efficiently using async endpoints, JWT authentication, and role-based access.
Async Task Manager API — Python+ FastAPI + Celery + Redis + PostgreSQL + Docker

---

## 🔧 Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** SQL (PostgreSQL/SQLite supported)
- **Authentication:** JWT-based auth with role-based access control
- **Containerization:** Docker
- **Documentation:** Swagger / OpenAPI

---

## ✨ Features
- Create, update, and delete tasks
- Asynchronous endpoints for efficient request handling
- Background task execution
- Secure login/signup with JWT authentication
- Role-based access control (admin/user)
- Task scheduling (basic support)
- Auto-generated API docs with Swagger UI
- Containerized deployment with Docker

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Ramsaikolnati/async-task-manager-api.git
cd async-task-manager-api


## Quickstart (SQLite)
```bash
# 1) Create .env (optional)
echo SECRET_KEY=change-me > .env

# 2) Run locally
uvicorn app.main:app --reload

# or with Docker
docker compose up --build
```

- Open docs: http://localhost:8000/docs
- Signup: POST /auth/signup
- Login: POST /auth/login (use email as username in the OAuth2 form)
- Use the Bearer token to call /tasks endpoints
