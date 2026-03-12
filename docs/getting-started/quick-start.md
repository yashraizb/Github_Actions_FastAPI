# Getting Started – Quick Start

Run a few curl commands against the running API:

```bash
# create a user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"jane@example.com","name":"Jane","age":28}'

# list users
curl http://localhost:8000/users

# update a user
curl -X PUT http://localhost:8000/users/jane@example.com \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe"}'

# delete
curl -X DELETE http://localhost:8000/users/jane@example.com
```

Responses are JSON; see the [API reference](../api/endpoints.md)
for full schemas.
