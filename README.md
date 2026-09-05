# 🏥 Patient Management API

A RESTful **Patient Management API** built with **FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**. The project implements authenticated API access, complete patient CRUD operations, request and response validation, custom email-domain validation, dependency injection, HTTP exception handling, and automatic OpenAPI documentation.

## 🚀 Features

* 🔐 User authentication
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

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Pydantic**
* **Uvicorn**
* **Swagger / OpenAPI**

## 🔐 Authentication

The API includes authentication to protect the application's endpoints.

Authenticated requests require the appropriate authentication credentials before accessing protected patient-management functionality.

> Authentication is implemented separately from the patient CRUD router to keep the application modular and maintainable.

## 📡 API Endpoints

### Authentication

## 📡 API Endpoints

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint         | Description                              |
| ------ | ---------------- | ---------------------------------------- |
| `POST` | `/auth/register` | Register a new user                      |
| `POST` | `/auth/login`    | Login and receive an access token        |
| `GET`  | `/auth/is_auth`  | Verify whether the user is authenticated |

### 🏥 Patient Management

| Method   | Endpoint                 | Description                |
| -------- | ------------------------ | -------------------------- |
| `POST`   | `/patients/`             | Create a new patient       |
| `GET`    | `/patients/`             | Get all patients           |
| `GET`    | `/patients/{patient_id}` | Get a patient by ID        |
| `PUT`    | `/patients/{patient_id}` | Update patient information |
| `DELETE` | `/patients/{patient_id}` | Delete a patient           |

### 🔑 Authorization

Protected patient endpoints require a valid JWT access token.

```text
Authorization: Bearer <access_token>
```

> Update the authentication endpoint and patient paths above if your actual router prefixes differ.

## ✅ Validation

The API uses **Pydantic** for request and response validation.

### Email Validation

Patient email addresses are validated using:

* `EmailStr`
* Custom email-domain validation

Currently supported email domains:

* Gmail
* Yahoo

Invalid or unsupported email domains are rejected with a validation error.

## 🗄️ Database

The application uses **PostgreSQL** for persistent data storage and **SQLAlchemy ORM** for database interaction.

Database-related functionality is separated into the `Database/` directory.

## 💉 Dependency Injection

FastAPI's dependency injection system is used to provide dependencies such as database sessions to the API endpoints.

This keeps database management separate from the endpoint logic and improves code organization.

## ⚠️ Exception Handling

The API uses FastAPI's `HTTPException` to handle errors such as:

* Invalid requests
* Patient not found
* Authentication-related failures
* Validation failures

## 📖 Automatic API Documentation

FastAPI automatically generates interactive API documentation.

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

```Patient-Management-System/
│
├── Authentication/
│   ├── __pycache__/
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
├── .gitattributes
├── .gitignore
├── main.py
└── README.md
|__.env
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd Patient-Management-API
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

Create your PostgreSQL database and configure the database connection according to your application's database configuration.

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

Use the Swagger UI to:

1. Authenticate
2. Authorize the API request
3. Create patient records
4. Retrieve patient records
5. Update patient records
6. Delete patient records

## 🎯 Project Purpose

This project was developed to demonstrate practical backend development using **FastAPI**, with an emphasis on RESTful API design, authentication, database integration, validation, dependency injection, and modular application architecture.

## 📌 Key Concepts Demonstrated

```text
Authentication
      ↓
FastAPI Router
      ↓
Pydantic Validation
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL
```

The project demonstrates how these components work together to build a structured RESTful backend application.
