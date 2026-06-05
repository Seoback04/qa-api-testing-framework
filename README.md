# API Testing Portfolio Project (Pytest + Requests + CI)
This project demonstrates a production-style API automation framework for portfolio use.

It focuses on reliability, clean structure, reusable fixtures, and CI integration.

## Project goals
- Build a reusable API testing framework in Python
- Validate REST endpoints with functional and contract assertions
- Keep tests stable with retries and explicit timeouts
- Run automated checks on every push/PR via GitHub Actions
- Keep test execution modular with markers (`smoke`, `contract`)

## Tech stack
- Python 3.9+
- pytest
- requests
- jsonschema
- ruff
- GitHub Actions

## API under test
Default target:
`https://jsonplaceholder.typicode.com`

Overridable by environment variable:
`BASE_URL`

## Complete project structure
```text
.
├── .github/
│   └── workflows/
│       └── ci.yml                 # CI pipeline (lint + test matrix)
├── docs/
│   ├── PROJECT_SUMMARY.md         # one-page project snapshot
│   ├── README.md                  # Documentation index
│   └── TEST_PLAN.md               # Testing strategy and acceptance criteria
├── src/
│   ├── __init__.py
│   └── api_client.py              # reusable API client wrapper
├── tests/
│   ├── README.md                  # Tests module guide
│   ├── conftest.py                # Shared fixtures (session + base_url)
│   ├── schemas.py                 # JSON schema contracts
│   ├── test_multi_resource_api.py # parametrized cross-resource checks
│   ├── test_negative_cases.py     # 404 and invalid-path validation
│   ├── test_posts_api.py          # /posts endpoint test suite
│   └── test_users_api.py          # /users endpoint test suite
├── .gitignore
├── pyproject.toml                 # Ruff config
├── pytest.ini                     # Pytest config
├── requirements.txt               # Dependencies
└── README.md
```

## Test coverage included
### `tests/test_posts_api.py`
- Verify `GET /posts` returns 200 and non-empty list
- Verify `GET /posts/1` passes JSON schema and data assertions
- Verify `GET /posts?userId=<id>` filters correctly (parametrized)

### `tests/test_users_api.py`
- Verify `GET /users` returns 200 and non-empty list
- Verify `GET /users/1` matches expected schema
- Verify user email basic format integrity

### `tests/test_negative_cases.py`
- Verify unknown post returns 404
- Verify invalid route returns 404
### `tests/test_multi_resource_api.py`
- Parametrized contract checks for core resources
- Smoke checks for common resources (`posts`, `users`, `comments`, `albums`, `todos`)

## Reliability decisions
- Retry-enabled session for transient HTTP issues (`429`, `5xx`)
- Explicit `timeout=10` on all calls
- Conservative assertions to reduce flaky failures
- Reusable API client wrapper to keep tests DRY

## Setup (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run locally
```powershell
pytest -v
ruff check .
```

## Run by marker
```powershell
pytest -m smoke -v
pytest -m contract -v
```

## Run with a custom API base URL
```powershell
$env:BASE_URL="https://jsonplaceholder.typicode.com"
pytest -v
```

## CI pipeline behavior
Workflow file: `.github/workflows/ci.yml`

On every push and pull request:
- Installs dependencies
- Runs `ruff check .`
- Runs `pytest -v`
- Executes across Python `3.9`, `3.10`, `3.11`, `3.12`
- Uploads JUnit test reports as workflow artifacts

## Why this strengthens a QA portfolio
- Shows framework design and reusable fixtures
- Demonstrates API contract validation approach
- Includes negative testing
- Includes CI and linting best practices
