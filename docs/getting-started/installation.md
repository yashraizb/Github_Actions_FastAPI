# Getting Started – Installation

## Prerequisites

- Python 3.10+
- `pip` (or `poetry`/`pipenv`)
- (optional) Docker for containerized runs

## Clone & prepare

```bash
git clone https://github.com/your-org/Github_Actions_FastAPI.git
cd Github_Actions_FastAPI
python -m venv venv
source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Start the server

```bash
uvicorn main:app --reload
```

Navigate to `http://localhost:8000/docs` for the
built‑in Swagger UI.

> See [Quick Start](quick-start.md) for example requests.
