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
cd task-manager-api
2. Create and Activate a Virtual Environment
bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Create a .env File
Create a .env file in the project directory to store sensitive information like database credentials and secret keys:

env
Copy code
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
5. Set Up the Database
Run the following commands to apply migrations and set up the database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser
Create an admin user to manage the application via the admin panel:

bash
Copy code
python manage.py createsuperuser
7. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
API Endpoints
Authentication
Sign Up (Email/Password):

css
Copy code
POST /accounts/signup/
Body: {
    "username": "your_username",
    "email": "your_email@example.com",
    "password1": "your_password",
    "password2": "your_password"
}
Login (Email/Password):

css
Copy code
POST /accounts/login/
Body: {
    "login": "your_email@example.com",
    "password": "your_password"
}
Login with Google: Visit /accounts/login/ and click "Sign in with Google."

Tasks
List All Tasks (GET):

bash
Copy code
GET /api/tasks/
Create a Task (POST):

bash
Copy code
POST /api/tasks/
Body: {
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
}
Retrieve a Task (GET):

bash
Copy code
GET /api/tasks/{task_id}/
Update a Task (PUT):

bash
Copy code
PUT /api/tasks/{task_id}/
Body: {
    "title": "Updated Title",
    "description": "Updated Description",
    "completed": true
}
Delete a Task (DELETE):

bash
Copy code
DELETE /api/tasks/{task_id}/
Testing the API
Using Postman
Set up Postman for the API URL (e.g., http://127.0.0.1:8000/api/).
Use the endpoints mentioned above.
For authentication, include the token in the Authorization header:
makefile
Copy code
Authorization: Bearer <your_token>
Using DRF Browsable API
Run the server:
bash
Copy code
python manage.py runserver
Navigate to http://127.0.0.1:8000/api/tasks/ in your browser.
Use the web interface to perform CRUD operations.