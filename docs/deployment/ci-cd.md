# Deployment – CI/CD

This project uses **GitHub Actions** for automated CI/CD. The workflow builds a Docker image, pushes it to Docker Hub, and deploys to an EC2 instance.

## Workflow overview

1. **Build & push** Docker image on every push to `main`.
2. **Deploy to EC2** via SSH, replacing the running container.
3. **Health check** to verify deployment success.

The actual workflow is in [`.github/workflows/deploy.yml`](../../../.github/workflows/deploy.yml).

## Key features

- **Multi-arch builds** with QEMU and Buildx for cross-platform support.
- **Tagged images**: `latest` and SHA-based tags for versioning.
- **SSH deployment** to EC2 with container replacement and restart policy.
- **Health verification** via `/health` endpoint with retries.

## Secrets required

Set these in your repository secrets:

- `DOCKERHUB_USERNAME` & `DOCKERHUB_TOKEN` for registry access.
- `EC2_SSH_KEY`, `EC2_USER`, `EC2_HOST` for deployment.

## Local simulation

Test locally by running:

```bash
docker build -t gha-fastapi:test .
docker run -p 8000:8000 gha-fastapi:test
curl http://localhost:8000/health
```

## Notes

- Uses `workflow_dispatch` for manual triggers.
- Environment protection with `Dev` environment.
- Automatic rollback on health check failure.

> See [deployment/docker.md](docker.md) for container runtime details.
