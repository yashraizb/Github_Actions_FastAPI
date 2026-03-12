# Deployment – Docker & Runtime

## Docker

The `Dockerfile` builds a lightweight image:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
```

Build and run:

```bash
docker build -t user-api .
docker run -p 8000:8000 user-api
```

> API docs remain available at `http://localhost:8000/docs`.

## Runtime configuration

- Port, host and logging can be adjusted via environment variables.
- Add a production-ready server (e.g. Gunicorn) or swap to a proper
  database by replacing `UserService` in `app/database.py`.

### Related

- See [CI/CD pipeline](ci-cd.md) for automated builds & pushes.
- Refer to [Development setup](../development/setup.md) for local testing.
