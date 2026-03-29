# 🔐 SecureTaskManager API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge)
![PyTest](https://img.shields.io/badge/PyTest-8.0-blue?style=for-the-badge&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A production-ready REST API built with Python & FastAPI.**
JWT Authentication · Role-Based Access Control · CRUD Operations · External API Integration · Automated Tests


</div>

---

## 📖 Table of Contents

- [📌 About the Project](#-about-the-project)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [📦 Installation & Setup](#-installation--setup)
- [▶️ Running the Application](#️-running-the-application)
- [🧪 API Testing with Swagger](#-api-testing-with-swagger)
- [📮 All API Endpoints](#-all-api-endpoints)
- [🔐 Authentication Flow](#-authentication-flow)
- [🧬 Running Tests](#-running-tests)
- [🌐 External API Integration](#-external-api-integration)
- [📸 Screenshots](#-screenshots)
- [🚀 Live Demo](#-live-demo)
- [📈 Scalability Notes](#-scalability-notes)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

## 📌 About the Project

**SecureTaskManager** is a backend internship assignment project that demonstrates how to build a **scalable, secure REST API** using Python and FastAPI.

It simulates a real-world task management system where:
- Users can **register, login**, and manage their own tasks
- Admins can **view and manage all users and tasks**
- All routes are **protected with JWT tokens**
- External APIs are integrated with **retry logic and timeout handling**
- Every action is **logged** with structured JSON logging

> 💡 **Built for:** Backend Developer Intern Assignment
> 📋 **Skills demonstrated:** FastAPI · Python · PostgreSQL · JWT · REST APIs · SQL · PyTest · GitHub

---

## ✨ Features

- ✅ User Registration & Login with **BCrypt password hashing**
- ✅ **JWT Authentication** — secure token-based auth
- ✅ **Role-Based Access Control** — USER and ADMIN roles
- ✅ Full **CRUD operations** on Tasks (Create, Read, Update, Delete)
- ✅ **API Versioning** — all routes under `/api/v1/`
- ✅ **Input Validation** with Pydantic — automatic error messages
- ✅ **Global Error Handling** — clean JSON error responses
- ✅ **Structured JSON Logging** — every request is logged
- ✅ **External API Integration** — OpenWeatherMap with retry & timeout
- ✅ **Swagger UI** — auto-generated interactive API documentation
- ✅ **Automated Tests** with PyTest
- ✅ **CORS** configured for frontend integration
- ✅ Clean **layered architecture** (Routes → Services → Models)

---

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|---|---|---|
| 🐍 **Python** | Programming language | 3.11+ |
| ⚡ **FastAPI** | Web framework for REST APIs | 0.110.0 |
| 🦄 **Uvicorn** | ASGI server to run FastAPI | 0.27.1 |
| 🐘 **PostgreSQL** | Primary database | 16 |
| 🔗 **SQLAlchemy** | ORM — connects Python to PostgreSQL | 2.0.27 |
| ✅ **Pydantic** | Data validation and serialization | 2.6.1 |
| 🔐 **python-jose** | JWT token creation and validation | 3.3.0 |
| 🔒 **passlib + bcrypt** | Password hashing | 1.7.4 |
| 🌐 **httpx** | Async HTTP client for external APIs | 0.27.0 |
| 🔁 **tenacity** | Retry logic for external API calls | 8.2.3 |
| 🧪 **PyTest** | Automated testing framework | 8.0.2 |
| 📋 **python-json-logger** | Structured JSON logging | 2.0.7 |
| 🐙 **Git + GitHub** | Version control | — |

---

## 📁 Project Structure

```
secure-task-manager/
│
├── 📂 app/                              ← Main application package
│   │
│   ├── 📂 api/
│   │   ├── 📂 v1/
│   │   │   ├── 🔐 auth.py              ← Register & Login routes
│   │   │   ├── 📋 tasks.py             ← Task CRUD routes
│   │   │   └── 🌐 external.py          ← Public API routes
│   │   └── 🔑 deps.py                  ← JWT auth dependencies
│   │
│   ├── 📂 core/
│   │   ├── ⚙️  config.py               ← App settings (.env reader)
│   │   ├── 🔒 security.py              ← JWT + password hashing
│   │   └── 📝 logging_setup.py         ← Structured JSON logging
│   │
│   ├── 📂 db/
│   │   ├── 🏗️  base.py                 ← SQLAlchemy base class
│   │   ├── 🔌 session.py               ← Database connection
│   │   └── 🚀 init_db.py               ← Auto-create tables on startup
│   │
│   ├── 📂 models/
│   │   ├── 👤 user.py                  ← User database model
│   │   └── 📋 task.py                  ← Task database model
│   │
│   ├── 📂 schemas/
│   │   ├── 👤 user.py                  ← User request/response shapes
│   │   ├── 📋 task.py                  ← Task request/response shapes
│   │   └── 🎫 token.py                 ← JWT token schema
│   │
│   ├── 📂 services/
│   │   ├── 🔐 auth_service.py          ← Auth business logic
│   │   ├── 📋 task_service.py          ← Task business logic
│   │   └── 🌐 external_service.py      ← External API + retry logic
│   │
│   └── 🚀 main.py                      ← FastAPI app entry point
│
├── 📂 tests/
│   ├── ⚙️  conftest.py                 ← PyTest setup & fixtures
│   ├── 🧪 test_auth.py                 ← Auth endpoint tests
│   └── 🧪 test_tasks.py                ← Task CRUD tests
│
├── 📄 .env                             ← Environment variables (private)
├── 📄 .env.example                     ← Environment template (public)
├── 📄 requirements.txt                 ← Python dependencies
├── 📄 .gitignore                       ← Files to ignore in Git
└── 📄 README.md                        ← You are here!
```

---

## ⚙️ Prerequisites

Make sure these are installed before starting:

| Tool | Version | How to Check | Download |
|---|---|---|---|
| 🐍 Python | 3.11+ | `python --version` | [python.org](https://python.org) |
| 🐘 PostgreSQL | 16+ | Open pgAdmin | [postgresql.org](https://postgresql.org) |
| 🐙 Git | Any | `git --version` | [git-scm.com](https://git-scm.com) |
| 💻 VS Code | Any | — | [code.visualstudio.com](https://code.visualstudio.com) |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ashish-bhushan/secure-task-manager.git
cd secure-task-manager
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac/Linux
source venv/bin/activate

# You should see (venv) in your terminal ✅
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup PostgreSQL Database

Open **pgAdmin** or **psql terminal** and run:

```sql
CREATE DATABASE taskmanager_db;
```

### 5️⃣ Configure Environment Variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and update:

```env
APP_NAME=SecureTaskManager
DEBUG=True
API_V1_PREFIX=/api/v1

# Change 'postgres' to your PostgreSQL password
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taskmanager_db

# Generate a strong secret key (min 32 characters)
SECRET_KEY=your-very-long-secret-key-at-least-32-characters

ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Get free API key from openweathermap.org
WEATHER_API_KEY=your_openweather_api_key
WEATHER_BASE_URL=https://api.openweathermap.org/data/2.5
```

---

## ▶️ Running the Application

```bash
# Make sure virtual environment is active
venv\Scripts\activate

# Start the server
uvicorn app.main:app --reload --port 8000
```

### ✅ Success Output

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Started reloader process
INFO:     Server ready ✅
```

### 🌐 Available URLs

| URL | Description |
|---|---|
| `http://localhost:8000` | API Root / Health Check |
| `http://localhost:8000/docs` | 📖 Swagger UI (Interactive Docs) |
| `http://localhost:8000/redoc` | 📖 ReDoc Documentation |
| `http://localhost:8000/health` | ❤️ Health Check Endpoint |

---

## 🧪 API Testing with Swagger

FastAPI automatically generates an interactive UI at `/docs`.
No Postman needed — you can test everything in the browser!

### Step-by-Step Testing Guide

**Step 1 — Register a user:**
```json
POST /api/v1/auth/register
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Step 2 — Login:**
```json
POST /api/v1/auth/login
{
  "email": "john@example.com",
  "password": "password123"
}
→ Copy the "access_token" from response
```

**Step 3 — Authorize in Swagger:**
```
Click the 🔒 "Authorize" button (top right of /docs page)
Enter:  Bearer <paste_your_token_here>
Click:  Authorize
```

**Step 4 — Test protected routes:**
```
POST   /api/v1/tasks/       → Create a task
GET    /api/v1/tasks/my     → Get your tasks
PUT    /api/v1/tasks/{id}   → Update a task
DELETE /api/v1/tasks/{id}   → Delete a task
```

---

## 📮 All API Endpoints

### 🔐 Authentication

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | ❌ | Register new user |
| `POST` | `/api/v1/auth/login` | ❌ | Login & get JWT token |

### 📋 Tasks

| Method | Endpoint | Auth | Role |
|---|---|---|---|
| `POST` | `/api/v1/tasks/` | ✅ JWT | USER / ADMIN |
| `GET` | `/api/v1/tasks/my` | ✅ JWT | USER / ADMIN |
| `GET` | `/api/v1/tasks/all` | ✅ JWT | ADMIN only |
| `PUT` | `/api/v1/tasks/{id}` | ✅ JWT | Owner / ADMIN |
| `DELETE` | `/api/v1/tasks/{id}` | ✅ JWT | Owner / ADMIN |

### 🌐 External API

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/external/weather/{city}` | ✅ JWT | Get weather data |

### ❤️ Health

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/` | ❌ | API root info |
| `GET` | `/health` | ❌ | Health check |

---

## 🔐 Authentication Flow

```
1. User registers   →  Password hashed with BCrypt  →  Saved to DB
                                    ↓
2. User logs in     →  Password verified against hash
                                    ↓
3. Server creates   →  JWT Token (contains email + role)
                                    ↓
4. Client stores    →  Token in localStorage / memory
                                    ↓
5. Client sends     →  "Authorization: Bearer <token>" header
                                    ↓
6. Server validates →  Decodes token  →  Gets user from DB
                                    ↓
7. Route executes   →  Returns protected data ✅
```

---

## 🧬 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_auth.py -v
pytest tests/test_tasks.py -v
```

### ✅ Expected Output

```
tests/test_auth.py::test_register_success           PASSED ✅
tests/test_auth.py::test_register_duplicate_email   PASSED ✅
tests/test_auth.py::test_login_success              PASSED ✅
tests/test_auth.py::test_login_wrong_password       PASSED ✅
tests/test_tasks.py::test_create_task               PASSED ✅
tests/test_tasks.py::test_get_my_tasks              PASSED ✅
tests/test_tasks.py::test_create_task_without_token PASSED ✅
tests/test_tasks.py::test_update_task               PASSED ✅
tests/test_tasks.py::test_delete_task               PASSED ✅

9 passed in 2.34s ✅
```

> 💡 Tests use **SQLite** — no PostgreSQL setup needed for testing!

---

## 🌐 External API Integration

The project integrates with **OpenWeatherMap API** and demonstrates:

| Feature | Implementation |
|---|---|
| 🔁 **Retry Logic** | Retries up to 3 times on failure |
| ⏱️ **Timeout** | 10 second request timeout |
| 📈 **Exponential Backoff** | Waits 1s → 2s → 4s between retries |
| 🛡️ **Safe Error Handling** | Returns clean error if API is down |

**Example Response:**
```json
{
  "city": "London",
  "temperature": 15.2,
  "humidity": 78,
  "description": "light rain",
  "wind_speed": 4.1
}
```

> 🔑 Get your free API key at [openweathermap.org](https://openweathermap.org/api)

---

## 📸 Screenshots

### 📖 Swagger UI
```
📸 [Add screenshot of http://localhost:8000/docs]
```

### 🔐 Register & Login
```
📸 [Add screenshot of register/login in Swagger]
```

### 📋 Task CRUD Operations
```
📸 [Add screenshot of create, get, update, delete]
```

### 🧪 PyTest Results
```
📸 [Add screenshot of terminal showing all tests passing]
```

---



## 🤝 Contributing

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/add-new-feature

# 3. Commit your changes
git commit -m "Add: new feature description"

# 4. Push and open Pull Request
git push origin feature/add-new-feature
```

---


## 👨‍💻 Author

<div align="center">

**Ashish bhushan**
*Backend Developer Intern Candidate*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](github.com/Ashish-bhushan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](linkedin.com/in/ashish-bhushan-singh-0b626735b )
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hariomsinghswn555@outlook.com)

</div>

---

## 🗺️ Quick Reference — What Each File Does

| File | Purpose |
|---|---|
| `app/main.py` | FastAPI app startup, registers all routes |
| `app/core/config.py` | Reads `.env` settings |
| `app/core/security.py` | JWT creation + BCrypt password hashing |
| `app/core/logging_setup.py` | Structured JSON logging |
| `app/db/session.py` | PostgreSQL database connection |
| `app/db/init_db.py` | Creates tables automatically on startup |
| `app/models/user.py` | Users database table definition |
| `app/models/task.py` | Tasks database table definition |
| `app/schemas/` | Request/response data shapes (Pydantic) |
| `app/services/` | Business logic (register, login, CRUD) |
| `app/api/v1/` | HTTP route handlers |
| `app/api/deps.py` | JWT token validation dependency |
| `tests/` | Automated test files |
| `.env` | Secret config (never push to GitHub) |
| `requirements.txt` | All Python dependencies |

---

<div align="center">

⭐ **If this project helped you, please give it a star on GitHub!** ⭐

Made with ❤️ using Python & FastAPI

</div>
