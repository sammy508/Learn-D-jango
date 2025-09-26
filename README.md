# Student Management System (S_M_S) 🎓

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-4.3-green)
![DRF](https://img.shields.io/badge/DRF-3.15-lightgrey)
![License](https://img.shields.io/badge/License-MIT-orange)

A **Django-based backend** project for managing students, teachers, courses, subjects, and semesters, with fully-featured **REST APIs** built using **Django REST Framework (DRF)**.  

Designed for role-based access control and modular architecture, suitable for production-ready deployment.  

---

## Features ✨

- **User Authentication & Authorization**
  - Admin, Teacher, Student roles
  - JWT-based login/logout
  - Admin-only restricted actions

- **CRUD Operations**
  - Students, Teachers, Courses, Subjects, Semesters
  - Student enrollment management

- **Utilities**
  - ID generators for students and courses
  - Password hashing & validation
  - Input validations

- **Project Organization**
  - Modular codebase: models, serializers, views, utilities
  - Easy to extend & maintain  

---

## Project Structure 📂

S_M_S/
│
├─ manage.py
├─ .env
├─ requirements.txt
├─ db.sqlite3
├─ Notes/
├─ student_management_system/
│ ├─ models/
│ ├─ serializers/
│ ├─ views/
│ ├─ utils/
│ ├─ auth/
│ ├─ Course/
│ ├─ Student/
│ ├─ Teacher/
│ ├─ subjects/
│ ├─ semester/
│ ├─ migrations/
│ ├─ admin.py
│ ├─ urls.py
│ └─ apps.py
└─ S_M_S/
├─ settings.py
├─ urls.py
├─ wsgi.py
└─ asgi.py



---

<details>
<summary>⚙️ Installation & Setup</summary>

1. **Clone the repository**
   ```bash
  git clone https://github.com/sammy508/Learn-D-jango.git
  cd Learn-D-jango/S_M_S
  
2. **Create and activate env**
      python -m venv venv
     Windows
    venv\Scripts\activate
     macOS/Linux
    source venv/bin/activate

   
3. **Install dependencies**
      pip install -r requirements.txt

4. **  Apply migrations**
      python manage.py migrate


5.** Run development server**
  python manage.py runserver

6. <details> <summary>🛠️ API Endpoints</summary>

  **Users**

    | Endpoint                   | Method                  | Description                     |
| -------------------------- | ----------------------- | ------------------------------- |
| `/users/`                  | GET, POST               | List all users / Create user    |
| `/users/<uuid:pk>/`        | GET, PUT, PATCH, DELETE | Retrieve / Update / Delete user |
| `/create-user/`            | POST                    | Admin-only user creation        |
| `/auth/custom-login/`      | POST                    | User login                      |
| `/auth/logout-user/`       | POST                    | User logout                     |
| `/api/auth/token/`         | POST                    | JWT token obtain                |
| `/api/auth/token/refresh/` | POST                    | JWT token refresh               |

 ** Password & Auth**

  | Endpoint                            | Method | Description                        |
| ----------------------------------- | ------ | ---------------------------------- |
| `/send_resetlink/`                  | POST   | Send password reset link           |
| `/auth/reset_password/<str:token>/` | POST   | Reset password using token         |
| `/auth/change_password/`            | POST   | Change password for logged-in user |


**Students**
| Endpoint                    | Method                  | Description                                         |
| --------------------------- | ----------------------- | --------------------------------------------------- |
| `/student/profile/`         | GET, POST               | List / Create student profiles                      |
| `/student/profile/<int:pk>` | GET, PUT, PATCH, DELETE | CRUD on student profile (delete profile image only) |


  **Subjects**
| Endpoint             | Method                  | Description                        |
| -------------------- | ----------------------- | ---------------------------------- |
| `/subjects/`         | GET, POST               | List / Create subjects             |
| `/subject/<str:pk>/` | GET, PUT, PATCH, DELETE | Retrieve / Update / Delete subject |


  **Semesters**  
| Endpoint              | Method                  | Description                         |
| --------------------- | ----------------------- | ----------------------------------- |
| `/semesters/`         | GET, POST               | List / Create semesters             |
| `/semester/<str:pk>/` | GET, PUT, PATCH, DELETE | Retrieve / Update / Delete semester |


  **Entity Diagram 🗂️**

+----------------+       +----------------+       +----------------+
|    Student     |<----->|   Enrollment   |<----->|     Course     |
+----------------+       +----------------+       +----------------+
        ^                                                  ^
        |                                                  |
        |                                                  |
+----------------+                               +----------------+
|   Semester     |<----------------------------->|   Subject      |
+----------------+                               +----------------+
        ^
        |
+----------------+
|    Teacher     |
+----------------+


 ** License 📄**

 
---

All rights reserved.  
This is a learning project shared under the **MIT License**.  
Feel free to use, copy, or change the code.  
No warranties — use at your own risk.
