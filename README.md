# 🏥 Patient Management API

A RESTful **Patient Management API** built with **FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**.

The project implements **user registration, login, JWT-based authentication, complete patient CRUD operations, request and response validation, custom email-domain validation, dependency injection, HTTP exception handling, and automatic OpenAPI documentation**.

## 🚀 Features

* 🔐 User registration and login
* 🔑 JWT-based authentication
* 🛡️ Protected patient-management endpoints
* 🏥 Complete patient CRUD operations
* ➕ Create patient records
* 📋 Retrieve all patients
* 🔎 Retrieve a patient by ID
* ✏️ Update patient information
* 🗑️ Delete patient records
* 🗄️ PostgreSQL database integration
* 🔄 SQLAlchemy ORM
* ✅ Pydantic request and response validation
* 📧 Custom email-domain validation
* 💉 FastAPI dependency injection
* ⚠️ HTTP exception handling
* 📖 Automatic Swagger/OpenAPI documentation
* 📁 Modular router and application structure

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Pydantic**
* **Uvicorn**
* **Swagger / OpenAPI**

## 🔐 Authentication

The API provides user authentication through **registration, login, and JWT access tokens**.

### Authentication Flow

```text
Register
   ↓
Login
   ↓
Receive JWT Access Token
   ↓
Send Token with Protected Requests
   ↓
Access Patient Management Endpoints
```

### Register

Creates a new user account.

```text
POST /auth/register
```

### Login

Authenticates an existing user and returns an access token.

```text
POST /auth/login
```

### Authentication Check

Checks whether the current request contains valid authentication credentials.

```text
GET /auth/is_auth
```

Protected patient endpoints require a valid JWT access token.

```text
Authorization: Bearer <access_token>
```

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| `POST` | `/...`   | User authentication |

### 🏥 Patient Management

| Method   | Endpoint              | Description                 |
| -------- | --------------------- | --------------------------- |
| `GET`    | `/GET/get`            | Retrieves all patients      |
| `GET`    | `/GET/get/{id}`       | Retrieves a patient by ID   |
| `POST`   | `/CREATE/create`      | Creates a new patient       |
| `PUT`    | `/UPDATE/update/{id}` | Updates patient information |
| `DELETE` | `/DELETE/delete/{id}` | Deletes a patient           |

> **Note:** Replace these paths only if your actual FastAPI router prefixes or endpoint paths are different.

## ✅ Validation

The API uses **Pydantic** for request and response validation.

### 📧 Email Validation

Patient email addresses are validated using:

* `EmailStr`
* Custom email-domain validation

Currently supported email domains include:

* Gmail
* Yahoo

Invalid or unsupported email domains are rejected with a validation error.

## 🗄️ Database

The application uses **PostgreSQL** for persistent data storage and **SQLAlchemy ORM** for database interaction.

Database-related functionality is organized separately from the API routing layer to improve maintainability and separation of concerns.

## 💉 Dependency Injection

FastAPI's dependency injection system is used for application dependencies such as database sessions and authentication.

This keeps dependency management separate from endpoint logic and improves code organization.

## ⚠️ Exception Handling

The API uses FastAPI's `HTTPException` to handle errors such as:

* Invalid requests
* Patient not found
* Authentication failures
* Validation failures
* Unauthorized requests

## 📖 Automatic API Documentation

FastAPI automatically generates interactive API documentation using **OpenAPI**.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

These interfaces can be used to explore and test the available API endpoints.

## 📁 Project Structure

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
├── Database/
│
├── Pydantic/
│
├── Routers/
│   ├── Delete_Router/
│   ├── Get_Router/
│   ├── Post_Router/
│   └── Put_router/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

> ⚠️ **Security:** The `.env` file should be listed in `.gitignore` and should **not** be committed to GitHub. Use a `.env.example` file containing placeholder values if you want to document the required environment variables.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd Patient-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
myenv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure PostgreSQL

Create a PostgreSQL database and configure the database connection using your environment variables.

Example:

```text
DATABASE_URL=<your-database-url>
SECRET_KEY=<your-secret-key>
```

Do not commit real database credentials or secret keys to GitHub.

### 7. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 🧪 Testing the API

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Using Swagger UI, you can:

1. Register a user
2. Login
3. Obtain the JWT access token
4. Authorize protected requests
5. Create patient records
6. Retrieve patient records
7. Retrieve a patient by ID
8. Update patient information
9. Delete patient records

## 🎯 Project Purpose

This project was developed to demonstrate practical backend development using **FastAPI**, with an emphasis on:

* RESTful API design
* Authentication and authorization
* Database integration
* CRUD operations
* Request and response validation
* Dependency injection
* Exception handling
* Modular application architecture

## 📌 Key Concepts Demonstrated

```text
User Registration
       ↓
User Login
       ↓
JWT Authentication
       ↓
FastAPI Router
       ↓
Pydantic Validation
       ↓
SQLAlchemy ORM
       ↓
PostgreSQL
```

The project demonstrates how these components work together to build a structured and authenticated RESTful backend application.
