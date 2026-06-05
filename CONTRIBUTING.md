# Contributing Guide
Thanks for contributing to this API testing portfolio project.

## Prerequisites
- Python 3.9+
- Git

## Local setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Development workflow
1. Create a branch:
```powershell
git checkout -b feature/<short-description>
```
2. Make changes.
3. Run checks:
```powershell
pytest -v
ruff check .
```
4. Commit with descriptive message.
5. Push and open pull request.

## Test conventions
- Keep tests independent and deterministic
- Prefer explicit assertions over broad assumptions
- Use fixtures from `tests/conftest.py` for session/client reuse
- Use markers:
  - `@pytest.mark.smoke` for fast health checks
  - `@pytest.mark.contract` for schema/contract checks

