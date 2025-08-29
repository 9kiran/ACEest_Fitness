# ACEest Fitness Tracker – DevOps Assignment 1

## Objective
This assignment demonstrates the application of fundamental DevOps practices including:
- Flask application development
- Version control with Git and GitHub
- Unit testing using Pytest
- Automated testing with GitHub Actions
- Containerization using Docker
- Continuous Integration / Continuous Delivery (CI/CD) pipeline

---

## Problem Statement
ACEest Fitness and Gym is a growing startup that requires an automated and streamlined development workflow.  
As a Junior DevOps Engineer, my task was to build a **Flask-based fitness tracker application** and implement:
- Automated testing
- Docker containerization
- GitHub Actions CI/CD pipeline

---

## Deliverables
1. **Flask Web Application** – `app.py`  
   - Allows users to log workouts with duration.  
   - Displays all logged workouts.

2. **Version Control (GitHub Repository)**  
   - Source code maintained in a public GitHub repository with meaningful commits.  

3. **Unit Testing with Pytest** – `tests/test_app.py`  
   - Tests for application routes, valid inputs, and error handling.  

4. **Dockerfile**  
   - Containerizes the Flask application for consistent deployment.  

5. **CI/CD Pipeline** – `.github/workflows/main.yml`  
   - Automated workflow triggered on push events.  
   - Steps: checkout → install dependencies → run tests → build Docker image.  

6. **README.md**  
   - Instructions on setup, running tests, Docker usage, and pipeline overview.  

---

## Setup Instructions

### Run Locally
```bash
pip install -r requirements.txt
python app.py
```

### Run Tests (Pytest)
```bash
pytest
```

### Run with Docker

Build Docker image:
```bash
docker build -t aceest_fitness .
```

Run container:
```bash
docker run -p 5000:5000 aceest_fitness
```

Access the app at 👉 http://localhost:5000