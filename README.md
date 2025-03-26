# Task Management API

## Project Overview
A Django-based Task Management API that allows users to create tasks, assign tasks to users, and retrieve user-specific tasks.

## Features
- Create new tasks
- Assign tasks to users
- Retrieve tasks for specific users
- Mark tasks as completed
- User management

## Setup Instructions

### Prerequisites
- Python 3.9+
- pip
- virtualenv

### Installation Steps
1. Clone the repository
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Users
- `POST /api/users/`: Create a new user
- `GET /api/users/`: List all users
- `GET /api/users/{id}/`: Retrieve a specific user

### Tasks
- `POST /api/tasks/`: Create a new task
- `GET /api/tasks/`: List all tasks
- `GET /api/tasks/{id}/`: Retrieve a specific task
- `GET /api/tasks/retrieve-by-user/?user_id=<id>`: Get tasks for a specific user

## Testing
Run tests using:
```bash
python manage.py test
```

## Sample Request/Response

### Create Task
**Request:**
```json
{
    "name": "Project Review",
    "description": "Conduct quarterly project review",
    "task_type": "WORK",
    "assigned_user_ids": [1, 2]
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Project Review",
    "description": "Conduct quarterly project review",
    "created_at": "2024-03-26T10:00:00Z",
    "task_type": "WORK",
    "status": "PENDING",
    "assigned_users": [
        {"id": 1, "username": "john_doe"},
        {"id": 2, "username": "jane_smith"}
    ]
}
```

## License
MIT License
