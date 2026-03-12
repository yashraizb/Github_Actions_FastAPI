# Troubleshooting & FAQ

## Common Issues

### 422 Validation Error

Occurs when request body misses required fields or has invalid
types. Check the [API schemas](../api/schema.md).

### 404 Not Found

Returned by `GET`, `PUT`, `DELETE` when the email does not exist.
Example message: `User with email 'foo' not found`.

### 409 Conflict

Raised when attempting to create or rename a user to an email
that already exists.

## Tips

- Restart the server after editing Python files when not using
  `--reload`.
- Use `/docs` for interactive testing.
- For persistent storage, replace `UserService` with a database
  and update `routes.py`.

> Still stuck? Open an issue in the repo or ask on internal
> support channels.
