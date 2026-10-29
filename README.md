# FastAPI Product Management Practice

A learning project for practicing FastAPI backend development while following a
YouTube lecture. It includes a React inventory interface adapted from an
AI-backend project so it can be used as a visual companion to the API work.

This is a work in progress intended for learning and demonstration, not a
production-ready application.

## What this project covers

- FastAPI route handlers for basic product operations
- Pydantic models for product request and response data
- SQLAlchemy model and PostgreSQL connection setup
- A React interface for viewing, searching, sorting, adding, editing, and
  deleting products
- FastAPI's interactive API documentation

## Technology

- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** React, Axios

## Project structure

```text
.
├── database_config.py     # SQLAlchemy engine and session configuration
├── database_models.py    # SQLAlchemy product table
├── main.py               # FastAPI app and product routes
├── models.py              # Pydantic product schema
└── frontend/              # React application
```

## Run locally

### 1. Configure PostgreSQL

Install and start PostgreSQL, then create a database for the project. Update
`database_config.py` with your own local SQLAlchemy connection URL before
starting the backend. Do not commit passwords or other credentials; use
environment variables or a local, untracked configuration file if you add
credential-based settings.

### 2. Start the backend

From the project root, create and activate a virtual environment, then install
the backend dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

Start the API:

```powershell
python -m uvicorn main:app --reload
```

The backend runs at <http://localhost:8000>. Interactive API documentation is
available at <http://localhost:8000/docs>, with the alternative documentation
at <http://localhost:8000/redoc>.

### 3. Start the frontend

In a second terminal:

```powershell
cd frontend
npm install
npm start
```

The React development server will open in your browser. Its package
configuration proxies requests to `http://localhost:8000`.

## Backend routes currently implemented

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/` | Return a greeting |
| `GET` | `/item` | List products |
| `GET` | `/item/{id}` | Find a product by ID |
| `POST` | `/item` | Add a product |
| `PUT` | `/item?id={id}` | Replace a product |
| `DELETE` | `/item?id={id}` | Delete a product |

Product data uses the fields `id`, `name`, `description`, `price`, and
`quantity`.

## Current development notes

- The React interface was taken/adapted from an AI-backend project; the
  FastAPI backend is being developed by following a YouTube lecture.
- The frontend currently requests `/products/` and
  `/products/{id}`, while this backend currently provides `/item` routes.
  The two parts therefore need API route alignment before the UI can work
  end-to-end.
- SQLAlchemy models and database initialization are present, but the current
  product CRUD routes operate on an in-memory list. Changes made through those
  routes are not persisted to PostgreSQL yet.
- This project is being used to learn and improve the API/database integration;
  authentication, production deployment, and other production concerns are
  outside its current scope.
