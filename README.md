# Task_Mate

This is an app that helps you to organise your tasks and execute them accordingly

# Task Management API

A Django REST Framework API for managing tasks, task categories, updates, and educational resources for technicians and administrators.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Users](#users)
  - [Tasks](#tasks)
  - [Task Categories](#task-categories)
  - [Task Updates](#task-updates)
  - [Educational Resources](#educational-resources)
- [Permissions](#permissions)
- [Filtering, Searching, and Ordering](#filtering-searching-and-ordering)
- [Notes](#notes)

---

## Features

- User registration and JWT authentication.
- CRUD operations for tasks, categories, updates, and educational resources.
- Task filtering by status, priority, category, and assigned user.
- Search and ordering functionality on multiple fields.
- Custom task actions: toggle completion, list task updates.
- Role-based permissions: admin vs. technicians.

---

## Technologies

- Python 3.13
- Django 5.2
- Django REST Framework
- Django REST Framework Simple JWT
- django-filter
- MySQL (or SQLite for development)

---

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd taskmanager_project
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your database in settings.py.

Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Running the Server
bash
Copy code
python manage.py runserver
Access the API at: http://127.0.0.1:8000/api/

Access Django admin at: http://127.0.0.1:8000/admin/

Authentication
This API uses JWT authentication.

Obtain token: POST /api/auth/login/

Refresh token: POST /api/auth/refresh/

Register user: POST /api/auth/register/

Include the token in the Authorization header for authenticated endpoints:

pgsql
Copy code
Authorization: Bearer <your-access-token>
API Endpoints
Users
GET /api/users/ – List users (admin only)

POST /api/auth/register/ – Register a new user

GET /api/users/{id}/ – Retrieve user details (admin or owner)

PUT/PATCH /api/users/{id}/ – Update user (owner or admin)

DELETE /api/users/{id}/ – Delete user (admin only)

Tasks
GET /api/tasks/ – List tasks

POST /api/tasks/ – Create a task

GET /api/tasks/{id}/ – Retrieve task

PUT/PATCH /api/tasks/{id}/ – Update task

DELETE /api/tasks/{id}/ – Delete task

Custom actions:

POST /api/tasks/{id}/toggle_completion/ – Toggle task status

GET /api/tasks/{id}/updates/ – List updates for a task

Task Categories
GET /api/categories/ – List categories

POST /api/categories/ – Create category (admin only)

GET /api/categories/{id}/ – Retrieve category

PUT/PATCH /api/categories/{id}/ – Update category (admin only)

DELETE /api/categories/{id}/ – Delete category (admin only)

Task Updates
GET /api/task-updates/ – List updates

POST /api/task-updates/ – Create an update

GET /api/task-updates/{id}/ – Retrieve update

PUT/PATCH /api/task-updates/{id}/ – Update update

DELETE /api/task-updates/{id}/ – Delete update

Educational Resources
GET /api/resources/ – List resources

POST /api/resources/ – Create resource

GET /api/resources/{id}/ – Retrieve resource

PUT/PATCH /api/resources/{id}/ – Update resource

DELETE /api/resources/{id}/ – Delete resource

Permissions
Admin – Full access

Technician – Can view tasks assigned to them and updates they made

Authenticated users – Can view categories and resources

Filtering, Searching, and Ordering
Filtering: ?status=completed&priority=high&assigned_to=2

Search: ?search=solar

Ordering: ?ordering=due_date (use - for descending)

Notes
All POST/PUT/PATCH requests require a trailing slash /.

Use Django admin for initial data creation if needed.

JWT tokens expire by default; use refresh endpoint to get new access tokens.

Author: ECONI NOEL AITA
Project: Task_Mate – Technician Task Management API
```
