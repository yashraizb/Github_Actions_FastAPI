# API Reference – Schemas

Schemas are defined in `app/models.py`.

## User

```json
{
	"email": "john@example.com",
	"name": "John Doe",
	"age": 30,
	"is_active": true
}
```

Fields:

- `email` (EmailStr) – unique identifier
- `name` (string, 1‑100 chars)
- `age` (int, 0‑150)
- `is_active` (bool)

## UserCreate

Same as `User`, used for POST.

## UserUpdate

All fields optional; used for PUT.

> Example requests shown in [Quick Start](../getting-started/quick-start.md).
