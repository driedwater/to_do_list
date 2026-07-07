# To-Do List Application

This is a simple to-do list application written in Python.

## How to run the application

### With Python

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

### With Docker

1. Clone the repository.
2. Build the Docker image: `docker-compose build app`
3. Run the application: `docker-compose run app`

## How to run the tests

### With Python

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the tests: `python -m unittest discover -s .`

### With Docker

1. Clone the repository.
2. Build the Docker image: `docker-compose build tests`
3. Run the tests: `docker-compose run tests`
