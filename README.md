# FastAPI Product Management Practice

A hands-on project demonstrating FastAPI backend development through a
PostgreSQL-backed product management API. It includes a React inventory
interface adapted from an AI-backend project as a visual companion to the API.

This project is intended for learning and demonstration, not a
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
- CORS configuration for the local React development server

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

Use `/docs` to exercise the backend independently of the React interface.

### 3. Start the frontend

In a second terminal:

```powershell
cd frontend
npm install
npm start
```

The React development server normally opens at <http://localhost:3000>. The frontend's Axios
client currently targets `http://localhost:8000` directly. Although a development
proxy is also configured, these absolute requests do not use it. The backend
allows cross-origin requests from `http://localhost:3000`; if the frontend runs
on a different port or hostname, update the allowed origin accordingly.

## Backend routes currently implemented

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/` | Return a greeting |
| `GET` | `/products` | List products |
| `GET` | `/products/{id}` | Find a product by ID |
| `POST` | `/products` | Add a product |
| `PUT` | `/products/{id}` | Update a product's name, description, price, and quantity |
| `DELETE` | `/products/{id}` | Delete a product |

Product data uses the fields `id`, `name`, `description`, `price`, and
`quantity`.

`POST` and `PUT` accept a JSON body with all five fields. For updates, the
path parameter selects the existing product; its ID is not changed by the
body's `id` value.

The frontend uses `/products/` for list and create requests. FastAPI's default
trailing-slash redirects forward these requests to `/products`.

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
- Aligned backend product routes with the React interface, including ID-based
  paths for updates and deletion.
- Enabled CORS for the React development server at `http://localhost:3000`.

## Current development notes

- The primary learning focus is the FastAPI backend, database integration, and
  connecting API operations to a React interface. The frontend is adapted from
  an AI-backend project rather than presented as an original UI implementation.
- Missing products currently return text messages rather than HTTP 404
  responses. Database error handling and validation beyond the basic Pydantic
  field types remain areas for improvement.
- This project is being used to learn and improve the API/database integration;
  authentication, production deployment, and other production concerns are
  outside its current scope.
