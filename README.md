# EduSense (Django) - Setup, Run & Integration

This guide covers the full backend lifecycle for this repository:
**create the Django project/app → configure MySQL + settings → run migrations → run server → verify auth → integrate with the existing `edu_frontend/` frontend**.

---

## 1) Prerequisites
- Python 3.10+ (3.12 recommended)
- MySQL server

---

## 2) Create the Django project (how this repo was set up)
In the original project creation step (already done in this repo):

- Project folder: `edu_sense_backend/EduSense/`
- Project name: `EduSense`
- Entry point: `edu_sense_backend/EduSense/manage.py`

You can confirm you’re in the correct folder by checking:
- `edu_sense_backend/EduSense/EduSense/settings.py`
- `edu_sense_backend/EduSense/EduSense/urls.py`

---

## 3) Create the Django app (how this repo was set up)
This repo uses one app for authentication:
- App name: `Auth`
- App folder: `edu_sense_backend/EduSense/Auth/`

The app is wired in `EduSense/settings.py` via `INSTALLED_APPS = [..., 'Auth',]`.

---

## 4) Set up Python environment
Run from this folder:

```bash
cd edu_sense_backend/EduSense
```

Create venv:

```bash
python -m venv .venv
```

Activate (Windows / cmd):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5) Configure MySQL database
### 5.1 Create database
```sql
CREATE DATABASE edudb;
```

### 5.2 Create/grant the user used by `settings.py`
In `EduSense/settings.py` the current hardcoded defaults are:
- DB: `edudb`
- USER: `root`
- PASSWORD: `root`
- HOST: `127.0.0.1`
- PORT: `3306`

So use (or adjust to match your MySQL credentials):

```sql
CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON edudb.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

---

## 6) Apply migrations
Run from `edu_sense_backend/EduSense`:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7) Create an admin user
```bash
python manage.py createsuperuser
```

- Username field is **email** (see `AUTH_USER_MODEL = 'Auth.User'`)
- Provide `full_name`

---

## 8) Run the backend server
```bash
python manage.py runserver
```

Backend base URL:
- `http://127.0.0.1:8000/`

---

## 9) Auth API endpoints (what’s currently implemented)
Project routes:
- `EduSense/urls.py` mounts `Auth.urls` under `/api/`

So auth endpoints are:
- `POST http://127.0.0.1:8000/api/auth/register/`
- `POST http://127.0.0.1:8000/api/auth/login/`
- `POST http://127.0.0.1:8000/api/auth/logout/`
- `GET  http://127.0.0.1:8000/api/auth/me/`

### JWT behavior (important)
On successful **register** and **login**, the backend sets:
- `HttpOnly` cookie: `access_token`
- `HttpOnly` cookie: `refresh_token`

Authentication reads JWT from cookies (see `Auth/authentication.py`).

---

## 10) Quick manual test (curl)
### 10.1 Register
```bash
curl -i -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d "{\"full_name\":\"Test User\",\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

### 10.2 Login
```bash
curl -i -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

> Note: since the app stores tokens in cookies, subsequent calls (like `/api/auth/me/`) depend on cookies being preserved by your client.

---

## 11) Frontend integration (existing `edu_frontend/`)
### 11.1 CORS
`EduSense/settings.py` enables CORS for:
- `http://127.0.0.1:5500`

So run the frontend using a local server on port **5500**.

### 11.2 Frontend API base URL
`edu_frontend/api.js` uses:
- `BASE_URL = 'http://localhost:8000'`

And calls endpoints like:
- `/auth/register/` → `POST http://localhost:8000/api/auth/register/`

### 11.3 Auth payload keys
- Register expects: `full_name`, `email`, `password`
- Login expects: `email`, `password`

`Auth/views.py` also supports `fullname` as an alias for `full_name`.

---

## 12) Troubleshooting
### A) mysqlclient compilation errors
- Ensure you have MySQL dev libs installed.
- If you hit build issues, provide the exact error output.

### B) “No module named api.urls”
- This is fixed in this repo.
- Auth routes are exposed via `Auth/urls.py` and mounted in `EduSense/urls.py` under `/api/`.



