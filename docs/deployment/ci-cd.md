# Deployment – CI/CD

This project is CI/CD‑focused. the following example uses **GitHub Actions** but
you can adapt it to other systems.

## Workflow overview

1. **Lint & test** on every push/pull request.
2. **Build Docker image** and run smoke tests.
3. **Push image** to registry on `main` (e.g. Docker Hub, GitHub Container Registry).

## Example `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: python-version: '3.11'
      - run: pip install -r requirements.txt black flake8
      - run: black --check .
      - run: flake8 app/

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: python-version: '3.11'
      - run: pip install -r requirements.txt pytest
      - run: pytest

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - uses: docker/build-push-action@v4
        with:
          push: true
          tags: user-api:latest
          # set registry/name via secrets or repo settings
```

> Store credentials in `secrets.DOCKER_USERNAME` and `secrets.DOCKER_PASSWORD`.

## Local simulation

You can mimic the pipeline by running the lint/test commands locally and
building the Docker image. Use `act` or similar tools to run GitHub Actions
offline.

## Notes

- Expand the workflow to publish releases, deploy to Kubernetes/ECS, etc.
- Add unit/integration tests under `tests/` and update `pytest` step.
- Keep secrets out of source control.

> See [deployment/docker.md](docker.md) for container runtime details.
