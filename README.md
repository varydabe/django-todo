# Todolist
Todolist with user login and JWTAuth written in Python using Django framework.

This is a mini project while I'm learning about Django framework and implemented REST API development.
This project is considered finish (all basic functionality of todolist had been implemented), However there are some enhancements like Web UI, etc. that is nice to be implemented as well later.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

1. Clone repository: `git clone git@github.com:varydabe/django-todo.git`
2. Create and use a virtual environment and install dependencies.
 ```python
 mkvirtualenv venv
 \venv\Scripts\Activate
 pip install -r requirements.txt
 ```
 
### Run Project

Running project:

`python manage.py runserver`

### Migrations

When running in Local, you need to setup the app's database for your local machine.

1. Go to directory `todoproject`.
2. Open file .env and change `[YOUR_USERNAME]` and `[YOUR_PASSWORD]` to your database username and password.
3. Create database `todolist`.
4. Sync and migrate the database
```python
python ./manage.py syncdb
python ./manage.py migrate
```

## Directory Structure

This repository is organized in the following directory structure.

```
django-todo
|-- todo                                   # Contains todo App
|   |-- migrations                         # Contains migrations for db
|   |-- __init__                           #
|   |-- admin                              #
|   |-- apps                               #
|   |-- models                             #
|   |-- tests                              #
|   |-- transformer                        #
|   |-- urls                               #
|   |-- views                              #
|-- todoproject                            # Contains main project file
|   |-- .env                               # Environtment setting
|   |-- __init__                           #
|   |-- asgi                               #
|   |-- jwt                                #
|   |-- middleware                         #
|   |-- response                           #
|   |-- settings                           #
|   |-- urls                               #
|   |-- wsgi                               #
|-- user                                   # Contains user App
|   |-- migrations                         # Contains migrations for db
|   |-- templates                          # templates for frontend (not used right now)
|   |-- __init__                           #
|   |-- admin                              #
|   |-- apps                               #
|   |-- models                             #
|   |-- tests                              #
|   |-- transformer                        #
|   |-- urls                               #
|   |-- views                              #
|-- manage                                 # 

```

## Tech Stacks

- Python (Django)
- MySQL
