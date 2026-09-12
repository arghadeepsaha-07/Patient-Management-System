# 🏥 Patient Management System API

A secure and modular **Patient Management REST API** built with **FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, Authorization, Email Notifications, and Alembic**.

This project demonstrates a complete backend workflow where users can register and log in securely, receive an email notification after registration, and manage their own patient records through protected CRUD APIs.

---

## 🚀 Features

### 🔐 Authentication & Authorization

- User Registration
- User Login
- Secure password hashing using `pwdlib`
- JWT-based authentication
- JWT token expiration
- Protected API endpoints
- User-based authorization
- Authenticated user identification
- Patient data ownership

### 👨‍⚕️ Patient Management

- Create patient records
- Retrieve all patients
- Retrieve patient by ID
- Update patient information
- Delete patient records
- User-specific patient data
- PostgreSQL Foreign Key relationships
- Cascade deletion for associated patient records

### 📧 Email Notification System

After a client successfully registers, the application sends a registration email to the email address provided by the client.

The project uses:

- SMTP
- Gmail
- FastAPI `BackgroundTasks`
- Email notifications after successful registration

The email is processed in the background so the API can return the registration response without waiting for the email operation to complete.

### 🗄️ Database

- PostgreSQL
- SQLAlchemy ORM
- Foreign Key relationships
- Database constraints
- Cascade delete
- Automatic table creation
- Alembic database migrations

### 📚 API Documentation

FastAPI automatically provides:

- Swagger UI
- ReDoc
- OpenAPI documentation

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend Programming |
| ⚡ FastAPI | REST API Framework |
| 🐘 PostgreSQL | Relational Database |
| 🧩 SQLAlchemy | ORM |
| 🔑 JWT | Authentication |
| 🔒 pwdlib | Password Hashing |
| 📧 SMTP / Gmail | Email Notifications |
| 🔄 Alembic | Database Migrations |
| 📋 Pydantic | Data Validation |
| 📖 OpenAPI | API Documentation |
| 🐙 Git & GitHub | Version Control |

---

# 📁 Project Structure

```text
Patient-Management-System/
│
├── Authentication/
│   ├── bases.py
│   ├── controller.py
│   ├── database_models.py
│   ├── engines.py
│   ├── pydantic_models.py
│   ├── router.py
│   └── settings.py
│
├── Mail/
│   └── mail.py
│
├── Routers/
│   ├── connect_security_with_crud.py
│   ├── database_models.py
│   ├── delete_router.py
│   ├── get_router.py
│   ├── post_router.py
│   ├── put_router.py
│   ├── pydantic_models.py
│   └── router_all.py
│
├── migration/
│   ├── versions/
│   └── env.py
│
├── .gitignore
├── alembic.ini
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication Flow

```text
                    ┌──────────────────┐
                    │      Client      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Register     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Hash Password   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    PostgreSQL    │
                    │   User Database  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  BackgroundTasks │
                    │   Email Task     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Client Gmail   │
                    └──────────────────┘


                         LOGIN
                           │
                           ▼
                  ┌─────────────────┐
                  │ Verify Username │
                  │ & Password      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Generate JWT    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Authorization   │
                  │ Header          │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Verify JWT      │
                  │ & User          │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Protected       │
                  │ Patient APIs    │
                  └─────────────────┘
```

---

# 👤 User-Based Authorization

Every patient is associated with the authenticated user who created the record.

```text
┌────────────────────────┐
│     database_model     │
│                        │
│ id                     │
│ name                   │
│ username               │
│ email                  │
└───────────┬────────────┘
            │
            │ id
            ▼
┌────────────────────────┐
│   patients_database    │
│                        │
│ id                     │
│ name                   │
│ age                    │
│ gender                 │
│ problem                │
│ user_id                │
└────────────────────────┘
```

The patient table contains:

```python
user_id = Column(
    Integer,
    ForeignKey("database_model.id", ondelete="CASCADE")
)
```

When a patient is created, the authenticated user's ID is stored:

```python
user_id = user.id
```

This allows the application to associate patient records with the authenticated user.

For user-specific access, patient records can be filtered using:

```python
Patient_Database.user_id == user.id
```

This prevents users from accessing patient records belonging to other users when the corresponding authorization filter is applied to the CRUD operation.

---

# 📧 Email Registration System

When a new client registers, the application:

1. Receives registration information.
2. Checks whether the username already exists.
3. Checks whether the email already exists.
4. Hashes the password.
5. Creates the user in PostgreSQL.
6. Commits the user to the database.
7. Refreshes the database object.
8. Adds an email task to FastAPI `BackgroundTasks`.
9. Sends an email to the registered Gmail address.

### Registration Email Flow

```text
POST /register
      │
      ▼
Validate User
      │
      ▼
Check Username & Email
      │
      ▼
Hash Password
      │
      ▼
Save User
      │
      ▼
Commit Database
      │
      ▼
BackgroundTasks
      │
      ▼
Send Email
      │
      ▼
Client receives Gmail
```

---

# 🌐 API Endpoints

## 🔐 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |

---

## 👨‍⚕️ Patient Management

| Method | Endpoint | Authentication |
|--------|----------|----------------|
| GET | `/patient_data/` | Public |
| GET | `/patient_data/get` | 🔒 Required |
| GET | `/patient_data/get_id/{id}` | 🔒 Required |
| POST | `/patient_data/create` | 🔒 Required |
| PUT | `/patient_data/update` | 🔒 Required |
| DELETE | `/patient_data/delete/{id}` | 🔒 Required |

---

# 📖 Interactive API Documentation

After starting the application:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI allows you to interactively test and explore the API.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/arghadeepsaha-07/patient-management-system.git
```

```bash
cd patient-management-system
```

---

## 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate the environment on Windows:

```bash
myenv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30

MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

### ⚠️ Security

Never upload your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
myenv/
__pycache__/
*.pyc
```

For Gmail SMTP, use an appropriate **App Password** rather than exposing your normal Gmail password.

---

# 🗄️ Alembic Database Migrations

Create a migration:

```bash
alembic revision --autogenerate -m "initial migration"
```

Apply migrations:

```bash
alembic upgrade head
```

Check migration history:

```bash
alembic history
```

Check the current migration:

```bash
alembic current
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Example Registration Request

### Endpoint

```http
POST /register
```

### Request Body

```json
{
    "name": "Argha",
    "username": "argha07",
    "email": "example@gmail.com",
    "password": "your_password"
}
```

### Registration Flow

```text
User Registration
       ↓
Validate Information
       ↓
Hash Password
       ↓
Save User
       ↓
Send Background Email
       ↓
Registration Email
       ↓
Client's Gmail
```

---

# 🧪 Example Patient Request

## Create Patient

### Endpoint

```http
POST /patient_data/create
```

### Request Body

```json
{
    "name": "Argha",
    "age": 19,
    "gender": "Male",
    "height": 164,
    "weight": 70,
    "problem": "LiverProblem",
    "email": "example@gmail.com",
    "phone_no": "9876543210",
    "emergency_phone_no": "9876501234"
}
```

The authenticated user's ID is automatically associated with the patient record.

---

# 🔒 Security Features

The project implements:

- JWT authentication
- Password hashing
- Token expiration
- Protected routes
- User-based authorization
- User-specific patient records
- Foreign Key relationships
- Cascade deletion
- Pydantic input validation
- Environment-based secrets
- SMTP authentication
- Background email processing

---

# 🧠 Backend Concepts Demonstrated

This project demonstrates practical backend development concepts:

```text
FastAPI
│
├── APIRouter
├── Dependency Injection
├── Depends()
├── HTTPException
├── Response Models
├── Pydantic
└── BackgroundTasks
│
├── Authentication
│   ├── Registration
│   ├── Login
│   ├── Password Hashing
│   └── JWT
│
├── Authorization
│   ├── JWT Verification
│   ├── Current User
│   └── User-Owned Data
│
├── Database
│   ├── PostgreSQL
│   ├── SQLAlchemy
│   ├── Foreign Keys
│   ├── Constraints
│   └── Cascade Delete
│
├── Email
│   ├── SMTP
│   ├── Gmail
│   └── BackgroundTasks
│
└── Database Migration
    └── Alembic
```

---

# 📈 Future Improvements

- [ ] Role-Based Access Control
- [ ] Doctor and Admin roles
- [ ] Refresh Tokens
- [ ] Pagination
- [ ] Advanced patient search
- [ ] Patient medical history
- [ ] Automated testing with Pytest
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Production deployment
- [ ] API rate limiting
- [ ] Logging and monitoring
- [ ] Redis caching
- [ ] Frontend integration

---

# 🎯 Project Goals

The main goals of this project are:

- Build a real-world backend application.
- Practice REST API development.
- Implement secure authentication and authorization.
- Work with PostgreSQL and SQLAlchemy.
- Understand database relationships.
- Implement email notifications.
- Learn database migrations with Alembic.
- Follow modular backend architecture.
- Build a project suitable for a developer portfolio.

---

# 👨‍💻 Author

## Arghadeep Saha

Computer Science & Engineering Student

### GitHub

[https://github.com/arghadeepsaha-07](https://github.com/arghadeepsaha-07)

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📌 Project Status

**🚧 Development / Learning Project**

Built with:

**Python • FastAPI • PostgreSQL • SQLAlchemy • JWT • Alembic • SMTP • Gmail**
