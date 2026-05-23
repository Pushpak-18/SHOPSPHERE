# SHOPSPHERE

SHOPSPHERE is a Django-based e-commerce project with product listing, cart functionality, and user authentication features.

## Features

- User registration and login
- Profile update and password reset
- Product catalog with categories, trending items, and offers
- Cart model for storing selected products
- Static asset support for CSS and product images

## Tech Stack

- Python
- Django 6
- SQLite

## Project Structure

```text
myproject/
|-- base/
|-- user_auth/
|-- static/
|-- templates/
|-- manage.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Notes

- `db.sqlite3` is ignored in Git, so each developer should create their own local database with migrations.
- Product images are served from the local static/media setup used in this project.
