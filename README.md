FirstFastAPI
============

A small example FastAPI project demonstrating basic CRUD-style endpoints using an in-memory list of books.

Requirements
------------
- Python 3.13+
- The dependencies are declared in `pyproject.toml` (FastAPI and Uvicorn).

Quick start (macOS / Linux)
--------------------------
1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

This project supports installing dependencies with the `uv` package manager. The following commands show how to use `uv` to install the dependencies declared in `pyproject.toml` or install packages directly.

Using `uv` to install dependencies from `pyproject.toml`:

```bash
# upgrade uv if available (optional)
uv upgrade

# install dependencies listed in pyproject.toml
uv install -r <(python - <<PY
import tomllib, sys
with open('pyproject.toml', 'rb') as f:
    data = tomllib.load(f)
deps = data.get('project', {}).get('dependencies', [])
for d in deps:
    print(d)
PY
)
```

Alternatively, install the runtime packages directly with `uv`:

```bash
uv install "fastapi>=0.136.1" "uvicorn[standard]>=0.47.0"
```

3. Run the app with uvicorn (from project root)

```bash
uvicorn books:app --reload
```

- The API will be available at: http://127.0.0.1:8000
- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- Alternative API docs (ReDoc): http://127.0.0.1:8000/redoc

Project layout
--------------
- `books.py` - FastAPI app and endpoints
- `main.py` - optional app entrypoint (if present)
- `pyproject.toml` - project metadata and dependencies
- `books_notes.txt` - learning notes generated from `books.py`

Notes
-----
- This project uses an in-memory list for storage; all data will be lost when the server restarts.
- For production use, integrate a database (Postgres, SQLite, etc.) and use Pydantic models for request/response validation.

Contributing
------------
Feel free to open issues or PRs. If you plan to extend this project, please add tests and update the README with any additional setup steps.
