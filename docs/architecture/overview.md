# Architecture Overview

This service is a simple Python **FastAPI** backend.

- `main.py` – application entrypoint, exception handlers,
  health & root endpoints.
- `app/routes.py` – `APIRouter` with `/users` CRUD endpoints.
- `app/models.py` – Pydantic models (`User`, `UserCreate`,
  `UserUpdate`).
- `app/database.py` – `UserService` providing in‑memory storage.
- `app/exceptions.py` – custom `HTTPException` subclasses.
