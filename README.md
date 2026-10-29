# FastAPI Product Management Practice

A learning project for practicing FastAPI backend development while following a
YouTube lecture. It includes a React inventory interface adapted from an
AI-backend project so it can be used as a visual companion to the API work.

This is a work in progress intended for learning and demonstration, not a
production-ready application.

## What this project covers

- FastAPI route handlers for basic product operations
- Pydantic models for product request and response data
- PostgreSQL-backed product CRUD using SQLAlchemy
- FastAPI dependency injection for request-scoped database sessions
- Environment-based database configuration using `python-dotenv`
- Automatic table creation and initial sample data
- A React interface for viewing, searching, sorting, adding, editing, and
  deleting products
- FastAPI's interactive API documentation

## Technology

- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy, python-dotenv
- **Database:** PostgreSQL
- **Frontend:** React, Axios

## Project structure

```text
.
├── .env.example          # Database configuration template (no real credentials)
├── .gitignore            # Excludes local secrets and generated files
├── database_config.py    # Environment-based SQLAlchemy engine and sessions
├── database_models.py    # SQLAlchemy product table
├── main.py               # FastAPI app, database dependency, and CRUD routes
├── models.py             # Pydantic product schema
└── frontend/              # React application
```

## Run locally

### 1. Configure PostgreSQL

You will need Python, PostgreSQL, and (for the frontend) Node.js with npm.
Install and start PostgreSQL, then create a database for the project.

From the project root, copy the configuration template:

```powershell
Copy-Item .env.example .env
```

If you already have a local `.env`, edit it instead of overwriting it. Set
`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, and `DB_NAME` to your local
PostgreSQL connection details. Use the actual password; the configuration code
URL-encodes it when building the connection URL.

The backend loads these values using `python-dotenv`. Keep real credentials in
the ignored `.env` file and commit only the placeholder `.env.example`.

### 2. Start the backend

From the project root, create and activate a virtual environment, then install
the backend dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

Start the API:

```powershell
python -m uvicorn main:app --reload
```

The backend runs at <http://localhost:8000>. Interactive API documentation is
available at <http://localhost:8000/docs>, with the alternative documentation
at <http://localhost:8000/redoc>.

On startup, the app creates the `products` table if needed and inserts seven
sample products if the table is empty. The PostgreSQL database itself must
already exist and be reachable. Product routes now read from and write to
PostgreSQL, so committed changes survive application restarts.

Use `/docs` to exercise the backend independently while frontend integration
is still in progress.

### 3. Start the frontend

In a second terminal:

```powershell
cd frontend
npm install
npm start
```

The React development server will open in your browser. The frontend's Axios
client currently targets `http://localhost:8000` directly. Although a development
proxy is also configured, these absolute requests do not use it. See the
integration limitations below before testing through the UI.

## Backend routes currently implemented

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/` | Return a greeting |
| `GET` | `/item` | List products |
| `GET` | `/item/{id}` | Find a product by ID |
| `POST` | `/item` | Add a product |
| `PUT` | `/item?id={id}` | Update a product's name, description, price, and quantity |
| `DELETE` | `/item?id={id}` | Delete a product |

Product data uses the fields `id`, `name`, `description`, `price`, and
`quantity`.

`POST` and `PUT` accept a JSON body with all five fields. For updates, the
query parameter selects the existing product; its ID is not changed by the
body's `id` value.

Example request body:

```json
{
  "id": 8,
  "name": "Practice product",
  "description": "Created while learning FastAPI",
  "price": 199.5,
  "quantity": 10
}
```

## Latest learning progress

- Replaced in-memory CRUD operations with SQLAlchemy database queries.
- Added a `get_db` dependency that provides a session to each product route
  and closes it after the request.
- Added database commits for product creation, updates, and deletion.
- Retained the sample list only for seeding an empty products table.

## Current development notes

- The React interface was taken/adapted from an AI-backend project; the
  FastAPI backend is being developed by following a YouTube lecture.
- The frontend currently requests `/products/` and
  `/products/{id}`, while this backend currently provides `/item` routes.
  Update and delete request shapes also differ. The two parts therefore need
  API route alignment before the UI can work end-to-end.
- The backend does not currently configure CORS. The frontend's direct API
  requests from a different origin also require CORS configuration or a change
  to relative requests through the development proxy.
- Missing products currently return text messages rather than HTTP 404
  responses. Database error handling and validation beyond the basic Pydantic
  field types remain areas for improvement.
- This project is being used to learn and improve the API/database integration;
  authentication, production deployment, and other production concerns are
  outside its current scope.
