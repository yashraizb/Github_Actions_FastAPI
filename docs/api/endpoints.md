# API Reference – Endpoints

| Method | Path             | Description          | Response model     |
| ------ | ---------------- | -------------------- | ------------------ |
| GET    | `/users`         | List all users       | `List[User]`       |
| GET    | `/users/{email}` | Retrieve single user | `User`             |
| POST   | `/users`         | Create new user      | `User`             |
| PUT    | `/users/{email}` | Update existing user | `User`             |
| DELETE | `/users/{email}` | Remove user          | _(204 No Content)_ |

See [schema definitions](schema.md) for request/response bodies.

### Health & root

- `GET /health` – returns `{status: "healthy"}`
- `GET /` – basic welcome message with link to `/docs`

Exceptions return standard HTTP error codes; see
[troubleshooting](../troubleshooting/faq.md#error-codes).
