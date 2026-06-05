# API Testing Project Test Plan
## Objective
Validate the reliability and basic contract stability of selected public REST endpoints using automated tests.

## Scope
- Endpoint family: `/posts`
- Endpoint family: `/users`
- Negative route behavior (`404`)

## Test types included
- Functional API tests
- Contract-style schema validation tests
- Basic data-quality assertions
- Negative tests

## Out of scope
- Performance/load testing
- Security/penetration testing
- Write operations (`POST`, `PUT`, `DELETE`)

## Risks and mitigations
- Public API instability: use retry-enabled session and conservative assertions
- Network latency/transient failures: retry policy + request timeouts

## Acceptance criteria
- All tests pass in local run
- CI pipeline passes on push/pull request
- Lint checks pass with `ruff`

