# ACEest Fitness Tracker

[![CI/CD Pipeline](https://github.com/9kiran/ACEest_Fitness/actions/workflows/main.yml/badge.svg)](https://github.com/9kiran/ACEest_Fitness/actions)

## Overview
This is a simple **Flask-based fitness tracker application** for ACEest Fitness and Gym.  
It allows users to add workouts with duration and view logged workouts.

The project demonstrates DevOps practices:
- Flask web application development
- Unit testing with Pytest
- Docker containerization
- Continuous Integration / Continuous Delivery (CI/CD) using GitHub Actions

---

## Setup and Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/9kiran/ACEest_Fitness.git
cd ACEest_Fitness
````

### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

If your Flask app is inside the `aceest_fitness` folder:

```bash
python -m aceest_fitness.app
```

The app will run at [http://localhost:5000](http://localhost:5000)

---

## Running Tests Locally

This project uses **Pytest**.

Run:

```bash
pytest
```

Expected result: All tests pass ✅

---

## Running with Docker (Optional)

Build Docker image:

```bash
docker build -t aceest_fitness .
```

Run container:

```bash
docker run -p 5000:5000 aceest_fitness
```

Open: [http://localhost:5000](http://localhost:5000)

---

## GitHub Actions Pipeline

The pipeline is defined in `.github/workflows/main.yml`.

### Trigger

* Runs automatically on every commit to **any branch**
* Runs on pull requests

### Steps

1. **Checkout code** – Pulls the repo into the GitHub runner
2. **Set up Python** – Installs Python 3.10
3. **Install dependencies** – Installs requirements from `requirements.txt`
4. **Run tests** – Executes Pytest to ensure application works
5. **Build Docker image** – Builds a container image for the Flask app

✅ This ensures code is tested and build-ready on every commit.