# Event Management API

This is a Django-based Event Management API built using Django REST Framework (DRF) that allows users to create, read, update, and delete events. Users can only manage their own events and authenticate using JWT tokens.

## Setup

### Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (for JWT authentication)

### Install Dependencies

1. Clone the repository and navigate to the project directory.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Migration

1. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Running the Server

Start the server:
```bash
python manage.py runserver
