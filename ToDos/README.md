# FastAPI Todo Application

A simple Todo application built with FastAPI, SQLAlchemy, and PostgreSQL, with support for both local development and Docker deployment.

## Features

- ✅ Create, read, update, and delete todos
- ✅ FastAPI with automatic API documentation
- ✅ SQLAlchemy ORM with database migrations
- ✅ SQLite for local development
- ✅ PostgreSQL for production (Docker)
- ✅ Docker and Docker Compose support
- ✅ Database connection health checking

## Project Structure

```
TodosApp/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── models.py        # SQLAlchemy database models
│   ├── database.py      # Database configuration and connection
│   ├── requirements.txt # Python dependencies
│   └── wait_for_db.py   # Database readiness checker for Docker
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Multi-container Docker application
└── README.md           # This file
```

## Quick Start

### Option 1: Local Development (SQLite)

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   cd TodosApp/app
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Option 2: Docker with PostgreSQL

1. **Start the application:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Get all todos |
| POST | `/todos` | Create a new todo |
| GET | `/todos/{todo_id}` | Get a specific todo |
| PUT | `/todos/{todo_id}` | Update a todo |
| DELETE | `/todos/{todo_id}` | Delete a todo |

### Example API Usage

**Create a todo:**
```bash
curl -X POST "http://localhost:8000/todos" \
     -H "Content-Type: application/json" \
     -d '{"title":"Learn FastAPI","description":"Complete the FastAPI tutorial","completed":false}'
```

**Get all todos:**
```bash
curl http://localhost:8000/todos
```

**Update a todo:**
```bash
curl -X PUT "http://localhost:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{"title":"Learn FastAPI","description":"Complete the FastAPI tutorial","completed":true}'
```

**Delete a todo:**
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

## Database Configuration

The application automatically selects the appropriate database based on the environment:

- **Local development**: Uses SQLite (`todos.db` file)
- **Docker**: Uses PostgreSQL (configured in `docker-compose.yml`)

Database URL is controlled by the `DATABASE_URL` environment variable:
- SQLite: `sqlite:///./todos.db`
- PostgreSQL: `postgresql://user:password@host:port/database`

## Development

### Adding New Features

1. **Add new models** in `app/models.py`
2. **Update the database configuration** in `app/database.py` if needed
3. **Add new endpoints** in `app/main.py`
4. **Update requirements** in `app/requirements.txt`

### Database Changes

When you modify models, you may need to reset the database:

**For SQLite (local):**
```bash
rm todos.db  # Delete the database file
# Restart the application to recreate tables
```

**For Docker:**
```bash
docker-compose down -v  # Remove containers and volumes
docker-compose up --build  # Rebuild and restart
```

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Find and kill the process using port 8000
   lsof -ti:8000 | xargs kill -9
   ```

2. **Database connection errors in Docker:**
   ```bash
   # Check container logs
   docker-compose logs api
   docker-compose logs db
   ```

3. **Permission denied on wait_for_db.py:**
   ```bash
   # Make sure the Python script is executable
   chmod +x TodosApp/app/wait_for_db.py
   ```

### Logs

**Local development:**
```bash
# Application logs are shown in the terminal
uvicorn main:app --reload --log-level debug
```

**Docker:**
```bash
# View all container logs
docker-compose logs

# View specific service logs
docker-compose logs api
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f api
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Full database connection string | `sqlite:///./todos.db` |
| `DB_HOST` | Database host (Docker only) | `db` |
| `DB_PORT` | Database port (Docker only) | `5432` |
| `DB_NAME` | Database name (Docker only) | `todos` |
| `DB_USER` | Database user (Docker only) | `postgres` |
| `POSTGRES_PASSWORD` | Database password (Docker only) | `password` |

## Requirements

- Python 3.10+
- Docker and Docker Compose (for containerized deployment)

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation using Python type annotations
- **psycopg2-binary**: PostgreSQL adapter for Python (Docker only)

## License

This project is open source and available under the [MIT License](LICENSE).
