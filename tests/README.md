# Tests Module Guide
This folder contains the automated API test suite.

## Files
- `conftest.py` → shared fixtures (base URL + resilient HTTP session)
- `src/api_client.py` → reusable API client abstraction used by tests
- `schemas.py` → JSON schema contracts used in validations
- `test_posts_api.py` → functional + contract tests for `/posts`
- `test_users_api.py` → functional + contract tests for `/users`
- `test_negative_cases.py` → negative test scenarios (404 behavior)
- `test_multi_resource_api.py` → parametrized checks for multiple resources

## Execution
From project root:
```powershell
pytest -v
```

## Marker-based runs
```powershell
pytest -m smoke -v
pytest -m contract -v
```

## Base URL override
```powershell
$env:BASE_URL="https://jsonplaceholder.typicode.com"
pytest -v
```

