# Django rest api

## Description

A Django rest project with base functions that an api uses.

## Features

- Django REST framework api
- Postgres database on docker
- Automation tests
- Environment configuration

## Prerequisites

Ensure you have the following installed:

- Make
- Python
- Pip
- Docker
- Docker Compose
- Linux system

## Tech Stack

**Server:** Python, Django, Django Rest

**Database:** Postgres, Docker

## Installation

1. **Clone this repository**
    ```bash
      git clone git@github.com:pcmpaulo/django-api.git
    ```
2. **Create a .env file based on .env.example:**
    ```bash
      cp .env.example .env
    ```
3. **Configure environment:**
    ```bash
      make configure-env # create virtual env

      make install-dependencies-dev # Install all dependencies
    ```

## Run application

1. **Start the local postgres database:**
    ```bash
      make start-database
    ```
2. **Run migrations on database:**
    ```bash
      make apply-migrations
    ```
3. **Run server locally:**
    ```bash
      make run-dev
    ```

# Environment Variables

The ```.env```.env file should include:

```bash
    DEBUG=True
    DJANGO_SECRET_KEY=django_secret_key
    POSTGRES_PASSWORD=admin
    POSTGRES_USER=admin
    POSTGRES_DATABASE=postgres
    POSTGRES_HOST=localhost
```

# Running Tests

Run tests with coverage:
```bash
   make test   
```