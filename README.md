# Robot Cleaner Backend

FastAPI backend for the Robot Cleaner application.

## ✅ What This Project Does

Provides a single HTTP endpoint that accepts a robot movement path, calculates the number of unique grid locations visited, and stores request metrics (result, count, duration) in PostgreSQL.

---

## 🔧 Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- PostgreSQL (if running locally without Docker)

---

## 🚀 Quick Start (Docker)

### 1) Start the stack
```bash
docker-compose up --build
```

This brings up:
- **Postgres database** (`db`)
- **FastAPI app** (`api`) on `http://localhost:5000`

### 2) Stop the stack
```bash
docker-compose down
```

---

## 🧰 Local Setup (without Docker)

### 1) Create & activate virtual environment

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure PostgreSQL
Make sure a local Postgres is running and matches the `.env` settings (or edit `.env` accordingly).

Default `.env` contents:
```env
DB_USER=tibber
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=tibber_db
```

---

## ▶️ Running the API Locally

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

Then open:  
✅ `http://localhost:5000/docs` (Swagger UI)

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🧩 API Endpoint

### POST `/tibber-developer-test/enter-path`

### 1
**CURL using Terminal: **
```
curl -X POST http://localhost:5000/tibber-developer-test/enter-path \
-H "Content-Type: application/json" \
-d '{
  "start": {"x": 10, "y": 22},
  "commands": [
    {"direction": "east", "steps": 2},
    {"direction": "north", "steps": 1}
  ]
}'
```

### 2
**Body (JSON):**
```json
{
  "start": { "x": 0, "y": 0 },
  "commands": [
    { "direction": "north", "steps": 1 },
    { "direction": "east", "steps": 2 }
  ]
}
```

**Response:**
- `id`: database ID
- `timestamp`: request time
- `commands`: command count
- `result`: unique places visited
- `duration`: execution duration (seconds)

---

## 📁 Project Structure

```
docker-compose.yml
Dockerfile
requirements.txt
src/
  config/
    settings.py
  database.py
  main.py
  models/
    domain.py
    schemas.py
  routers/
    robot.py
  services/
    robot_service.py
test/
  test_robot.py
```

---

## 🔎 Notes

- The database schema is created automatically on startup using `Base.metadata.create_all(bind=engine)` (no migrations required).
- When running in Docker, `docker-compose` sets `DB_HOST=db` so FastAPI can connect to the Postgres container.

---

If you'd like, I can also add a **Postman collection** example or a **bash script** for running common API calls.
