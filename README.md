# Django URL Shortener

A simple URL shortening service built with Django and Django Rest Framework.

The application accepts a long URL, generates a unique short code, stores the mapping in the database, and redirects users from the generated short URL to the original address.

## Tech Stack

- Python
- Django
- Django Rest Framework
- SQLite (default Django database)

## Local Setup:

1. Clone the repository:

- `git clone <repository-url>`
- `cd <project-directory>`

2. Create a virtual environment:

- `python -m venv .venv`

3. Activate it:

- Windows: `.venv\Scripts\activate`
- Linux/macOS: `source .venv/bin/activate`

3. Install dependencies:

- `pip install -r requirements.txt`

4. Apply database migrations:

- `python manage.py migrate`

6. Start the development server:

- `python manage.py runserver`

## API end-points:

### Create a short URL

- POST: `http://127.0.0.1:8000/shorten-url/`

#### Request:

{
    "original_url": "https://example.com"
}

#### Response:

{
    "message": "success",
    "short_url": "http://127.0.0.1:8000/shrt/abc123/"
}

### Redirect to original URL

- GET: `http://127.0.0.1:8000/shrt/<code>/`

#### Example:

http://127.0.0.1:8000/shrt/abc123/


## Testing:

The test suite covers:

- Unit tests
    - URL validators
    - Serializer
    - Short URL generation utilities
    - Services
- API tests
    - URL shortening endpoint behaviour
    - Request validation
    - Response handling
- E2E tests
    - Complete flow from URL creation to redirect

### Run tests:

- `python manage.py test`

## Code Quality

The project uses:

- Black for code formatting.
- Flake8 for linting.
- isort for import ordering.

### Run formatting:

- `black .`
- `isort .`

### Run linting:

- `flake8 .`
