# ACEest Fitness Tracker

[![CI/CD Pipeline](https://github.com/9kiran/ACEest_Fitness/actions/workflows/main.yml/badge.svg)](https://github.com/9kiran/ACEest_Fitness/actions)
[![Coverage Status](https://codecov.io/gh/9kiran/ACEest_Fitness/branch/main/graph/badge.svg)](https://codecov.io/gh/9kiran/ACEest_Fitness)

---

## Overview
This is a simple **Flask-based fitness tracker application** for ACEest Fitness and Gym.  
It allows users to add workouts with duration and view logged workouts.

The project demonstrates DevOps practices:
- Flask web application development
- Unit testing with Pytest
- Test coverage reporting
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

This project uses **Pytest** with coverage.

Run:

```bash
pytest --cov=aceest_fitness --cov-report=term-missing
```

Expected result: All tests pass and a coverage summary is displayed.

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

* Runs automatically on every commit to any branch
* Runs on pull requests

### Steps

1. **Checkout code** – Pulls the repo into the GitHub runner
2. **Set up Python** – Installs Python 3.10
3. **Install dependencies** – Installs requirements from `requirements.txt`
4. **Run tests with coverage** – Executes Pytest and generates coverage reports
5. **Upload coverage to Codecov** – Publishes test coverage results for tracking
6. **Build Docker image** – Builds a container image for the Flask app

This ensures that code is tested, coverage is tracked, and the app builds correctly on every commit.

---

## Troubleshooting

### Python not found

If running `python` shows an error:

* On Windows, install Python from [Python.org](https://www.python.org/downloads/) and ensure "Add to PATH" is checked during installation.
* On Linux/Mac, install via your package manager:

  ```bash
  sudo apt-get install python3 python3-venv python3-pip   # Ubuntu/Debian
  brew install python                                      # macOS (Homebrew)
  ```

### Virtual environment issues

If activation fails on Windows PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again:

```powershell
venv\Scripts\activate
```

### Pytest not found

If you see `pytest: command not found`, install it manually:

```bash
pip install pytest pytest-cov
```

### Docker not recognized

If `docker` is not recognized, install Docker Desktop:

* [Windows/Mac download](https://www.docker.com/products/docker-desktop)
* Linux:

  ```bash
  sudo apt-get install docker.io
  sudo systemctl enable --now docker
  ```

### Port already in use

If the app fails to start because port 5000 is busy:

```bash
python -m aceest_fitness.app --port=5001
```

Then access it at [http://localhost:5001](http://localhost:5001)
