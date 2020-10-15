# Todolist
Todolist with user login and JWTAuth written in Python using Django framework.

This is a mini project while I'm learning about Django framework and implemented REST API.
This project is considered finish (all basic functionality of todolist had been implemented), However there are some enhancements like Web UI, etc. that is nice to be implemented as well later.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

1. Clone repository: `git clone git@github.com:varydabe/django-todo.git`
2. Create and use a virtual environment and install dependencies.
 ```python
 virtualenv venv
 \venv\Scripts\Activate          #Windows User
 pip install -r requirements.txt
 ```

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

### Run Project

Running project:

`python manage.py runserver`

## Directory Structure

This repository is organized in the following directory structure.

```
django-todo
|-- todo                                   # 
|   |-- migrations                         # 
|   |-- __init__                           #
|   |-- admin                              #
|   |-- apps                               #
|   |-- models                             #
|   |-- tests                              #
|   |-- transformer                        #
|   |-- urls                               #
|   |-- views                              #
|-- todoproject                            # 
|   |-- .env                               # 
|   |-- __init__                           #
|   |-- asgi                               #
|   |-- jwt                                #
|   |-- middleware                         #
|   |-- response                           #
|   |-- settings                           #
|   |-- urls                               #
|   |-- wsgi                               #
|-- user                                   # 
|   |-- migrations                         # 
|   |-- templates                          # 
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
