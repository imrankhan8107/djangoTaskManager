## Task Manager API

This is a Django-based Task Manager API that allows users to manage tasks with features like creating, updating, retrieving, and deleting tasks. It also supports authentication via email/password and Google OAuth using django-allauth.

## Features

- User Authentication (Email/Password and Google OAuth).
- Task Management:
  Create tasks.
  Retrieve all tasks or specific tasks.
  Update tasks.
  Delete tasks.

API secured with token-based authentication.
RESTful API built with Django REST Framework (DRF).

## Setup Instructions

1. Clone the Repository

git clone
cd task-manager-api 2. Create and Activate a Virtual Environment

python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate 3. Install Dependencies

pip install -r requirements.txt 4. Create a .env File
Create a .env file in the project directory to store sensitive information like database credentials and secret keys:

# An api key needs to be generated at sendgrid portal(https://sendgrid.com/en-us) and given to EMAIL_API in env file

.env
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_API=

5. Set Up the Database
   Run the following commands to apply migrations and set up the database:

python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
   Create an admin user to manage the application via the admin panel:

python manage.py createsuperuser

7. Run the Development Server
   Start the Django development server:

   python manage.py runserver

8. API Endpoints

- Authentication
  Sign Up (Email/Password):

* POST /accounts/signup/
  Body: {
  "username": "your_username",
  "email": "your_email@example.com",
  "password1": "your_password",
  "password2": "your_password"
  }

* Login (Email/Password):
  POST /accounts/login/
  Body: {
  "login": "your_email@example.com",
  "password": "your_password"
  }

* Login with Google: Visit /accounts/login/ and click "Sign in with Google."

- Tasks

* List All Tasks (GET):
  GET /api/tasks/

* Create a Task (POST):
  POST /api/tasks/
  Body: {
  "title": "Task Title",
  "description": "Task Description",
  "completed": false
  }

* Retrieve a Task (GET):
  GET /api/tasks/{task_id}/

* Update a Task (PUT):
  PUT /api/tasks/{task_id}/
  Body: {
  "title": "Updated Title",
  "description": "Updated Description",
  "completed": true
  }

* Delete a Task (DELETE):
  DELETE /api/tasks/{task_id}/
  Testing the API

* Run the server:
  python manage.py runserver
