# Flask-Restful API URL shortener

This service allowes to create shortened urls without loosing url parameters data.

Main libraries used:
1. Flask - web framework.
2. Flask-RESTful - restful API library.
3. Flask-Migrate - for handling database migrations.
4. Flask-SQLAlchemy - allows using SQLAlchemy ORM

Project strucuture:
```
.
├── manage.py
├── requirements.txt
├── run.py
└── url_shortener
    ├── __init__.py
    ├── models.py
    ├── resources.py
    ├── routes.py
    └── schema.py
```

* manage.py - script for managing database operations (migrations, db initialization, etc.).
* run.py - applicatoin initialization script.
* urls_shortener - directory for holding models, RESTflu API Resources, routes and schemas.

## Installations and Setup

1. Clone repository.
2. Install dependencies: ```pip install -r requirements.txt```.
3. Run following commands:
    1. ```python manage.py db init```.
    2. ```python manage.py db migrate```.
    3. ```python manage.py db upgrade```.
4. Run the server with ```python run.py```.

## Usage
### URLs endpoint
**POST http://217.0.0.1:5000/urls**

*Request*
```json
{
    "original_url": "https://google.com",
    "expire_in": 10
}
```
*Response*
```json
{
    "shortened_url": "-i5HI",
    "created_at": "2020-10-02T13:32:47.955957",
    "original_url": "https://google.com",
    "expire_in": 10,
    "id": 1
}
```
___
**GET HTTP://127.0.0.1:5000/urls**

*Response*
```json
[
    {
        "shortened_url": "-i5HI",
        "created_at": "2020-10-02T13:32:47.955957",
        "original_url": "https://google.com",
        "expire_in": 10,
        "id": 1
    }
]
```
___
### URL Redirect endpont
**GET http://127.0.0.1:5000/-i5HI**

*Response*
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="https://google.com">https://google.com</a>.  If not click the link.
```
___
### URL endpoint
**PATCH http://127.0.0.1:5000/urls/1**

*Request*
```json
{
    "original_url": "https://google.com",
    "expire_in": 40
}
```
*Response*
```json
{
    "shortened_url": "-i5HI",
    "created_at": "2020-10-02T13:32:47.955957",
    "original_url": "https://google.com",
    "expire_in": 40,
    "id": 1
}
```
___
**GET HTTP://127.0.0.1:5000/urls/1**

*Response*
```json
{
    "shortened_url": "-i5HI",
    "created_at": "2020-10-02T13:32:47.955957",
    "original_url": "https://google.com",
    "expire_in": 40,
    "id": 1
}
```
___
**DELETE http://217.0.0.1:5000/urls/1**
```
*Response*
```json
{
    "message": "URL with id '1' was deleted"
}
```

