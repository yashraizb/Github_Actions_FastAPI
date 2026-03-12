# Development Setup

After installation (see [Getting Started](../getting-started/installation.md)):

## Code layout

```
app/
  __init__.py
  database.py
  exceptions.py
  models.py
  routes.py
main.py
```

### Linting & formatting

```bash
pip install black flake8
black .
flake8 app/
```

Add pre‑commit hooks if desired.

### Testing

No tests exist yet; add files under a new `tests/` directory
and run with:

```bash
pytest
```

> Contributions are welcome – see `CONTRIBUTING.md` (TBD).
