
# Enterprise QA Automation Framework

Enterprise-level test automation framework for UI and API testing using Python.

## Overview

This project demonstrates a scalable and maintainable test automation architecture using modern QA engineering practices.

## Tech Stack

- Python 3.14
- Pytest
- Playwright
- Requests
- Allure Report
- JSON Schema
- Ruff
- GitHub Actions

## Project Structure

```text
enterprise-qa-automation/
├── clients/
├── config/
├── core/
├── pages/
├── tests/
│   ├── api/
│   ├── ui/
│   └── conftest.py
├── utils/
├── reports/
├── .github/
├── pyproject.toml
└── requirements.txt
```

## Automated Test Coverage

### API Testing
- Retrieve all posts
- Retrieve post by ID
- Create a post
- Update a post
- Delete a post

### UI Testing
- Add tasks
- Complete tasks
- Remove tasks
- Filter all tasks
- Filter active tasks
- Filter completed tasks

## Test Execution

Install dependencies:

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

Run all tests:

```bash
python -m pytest -v
```

Run tests with Allure:

```bash
python -m pytest --alluredir=reports/allure-results
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

## Code Quality

```bash
ruff check .
```

## Demo Applications

- UI: https://demo.playwright.dev/todomvc/
- API: https://jsonplaceholder.typicode.com

## Roadmap

- [x] UI automation
- [x] API automation
- [x] Page Object Model
- [x] Allure reporting
- [x] Environment and executor metadata
- [ ] GitHub Actions CI/CD
- [ ] Docker integration
- [ ] Advanced test coverage
