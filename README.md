

# Student Management System (S_M_S)

A Django-based project for managing students, teachers, and courses, with API endpoints built using Django REST Framework (DRF).

## Features

- User authentication and authorization (admin, teacher, student)
- JWT-based login and logout
- CRUD operations for students, teachers, and courses
- ID generation and validation utilities
- Admin-only views for restricted actions

## Project Structure

Project Root: S_M_S
│
├─ manage.py           <-- Django command-line utility
├─ .env                <-- Environment variables
├─ db.sqlite3          <-- Database
│
├─ Notes/              <-- Study notes (e.g., URL routing)
│
├─ student_management_system/   <-- Main App
│   ├─ models/                <-- Database models
│   │   ├─ course_model.py
│   │   ├─ student_models.py
│   │   ├─ Teacher_table.py
│   │   └─ user_models.py
│   │
│   ├─ serializers/           <-- Converts models to JSON and vice versa
│   │   ├─ course_serializers.py
│   │   ├─ student_serializer.py
│   │   ├─ teacher_serializer.py
│   │   ├─ User_serializer.py
│   │   └─ login/logout_serializers.py
│   │
│   ├─ views/                 <-- Business logic / API endpoints
│   │   ├─ admin_only_view.py
│   │   ├─ userlogin_view.py
│   │   ├─ userlogout_views.py
│   │   └─ user_view.py
│   │
│   ├─ utils/                 <-- Helper functions
│   │   ├─ hasher.py
│   │   ├─ id_generators.py
│   │   ├─ student_id_generator.py
│   │   └─ validations.py
│   │
│   ├─ migrations/           <-- Database schema migrations
│   ├─ admin.py
│   ├─ urls.py               <-- App-level URLs
│   ├─ apps.py
│   ├─ models.py             <-- (Optional main model file)
│   └─ tests.py
│
└─ S_M_S/                   <-- Project configuration
    ├─ settings.py          <-- Project settings (DB, apps, middleware)
    ├─ urls.py              <-- Root URL router
    ├─ wsgi.py              <-- Deployment (WSGI)
    └─ asgi.py              <-- Deployment (ASGI)


# TO clone
1. Clone the repository:  https://github.com/sammy508/Learn-D-jango.git
2. Create virtual env: 
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Apply Migrations
    python manage.py migrate

5. Run the development server:
    python manage.py runserver


# Usage

    Access APIs through the endpoints defined in student_management_system/urls.py.

    Admin panel available at /admin (create superuser with python manage.py createsuperuser).

# Notes

    Environment variables (like SECRET_KEY) should be defined in .env.

    Utilities in utils/ handle ID generation, password hashing, and validation.