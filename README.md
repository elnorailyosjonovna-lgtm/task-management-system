# Task Management System

A Django-based web application for managing tasks and projects.  
The application allows users to create projects, manage tasks, and track progress.

The project is containerized with Docker and deployed automatically using GitHub Actions CI/CD.

---

# Live Demo

Live deployed site:

http://142.93.173.177

---

# Features

- User authentication (login/logout)
- Project management
- Task creation and tracking
- Admin interface
- Automated testing
- CI/CD pipeline
- Dockerized deployment

---

# Technologies Used

Backend:
- Python
- Django

Database:
- PostgreSQL

Infrastructure:
- Docker
- Docker Compose
- Nginx
- DigitalOcean

CI/CD:
- GitHub Actions
- Docker Hub

Testing:
- Pytest
- Flake8

---

# Project Structure
task-management-system/
│
├── core/ # Django project configuration
├── tasks/ # Main application
├── nginx/ # Nginx configuration
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/workflows/ # CI/CD pipeline



---

# Running Locally

git clone https://github.com/elnorailyosjonovna-lgtm/task-management-system
cd task-management-system



### Create virtual environment
python -m venv venv
source venv/bin/activate


### Install dependencies
pip install -r requirements.txt



### Run migrations
python manage.py migrate


### Start server
python manage.py runserver



Open:
http://127.0.0.1:8000




---

# Docker Setup

Build and run containers:
docker compose up --build


The application will run in containers with:

- Django
- PostgreSQL
- Nginx

---

# CI/CD Pipeline

The project uses **GitHub Actions** for continuous integration and deployment.

Pipeline steps:

1. Run flake8 code linting
2. Run pytest tests
3. Build Docker image
4. Push image to Docker Hub
5. Deploy automatically to DigitalOcean server via SSH

Pipeline configuration:
.github/workflows/deploy.yml



---

# Environment Variables

The following variables are required:
DJANGO_SECRET_KEY
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD



These variables are stored securely in:

- `.env` file (server)
- GitHub Secrets (CI/CD)

---

# Deployment

The application is deployed on a **DigitalOcean droplet** using Docker Compose.

Deployment directory:

/opt/task-management-system



The deployment process automatically:

- pulls the latest Docker image
- restarts containers
- runs migrations
- collects static files

---

# Author

Elnora Ilyosjonovna


