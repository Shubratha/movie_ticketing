# User

Uses Django User model and Basic Authentication

### API:

**1. User signup**

Registers a new user

Mandatory fields:
- username (unique field)
- email ID
- password

```commandline
curl --location --request POST 'http://127.0.0.1:8000/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "<username>", "email": "<email_id>", "password": "<password>", "firstname": "<first_name>", "lastname": "<last_name>"}'
```
Sample response:
```json
{
    "status": true,
    "message": "User Created"
}
```

```json
{
    "status": false,
    "message": "",
    "error": "UNIQUE constraint failed: auth_user.username"
}
```
