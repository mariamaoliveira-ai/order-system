# Order System Development Guide

## Architecture

- `backend/` contains the FastAPI HTTP application.
- `consumer/` contains the separate Python Kafka consumer process.
- `frontend/` contains the React + Vite + TypeScript application.
- PostgreSQL, Kafka, and Prometheus run through the root Docker Compose stack.
- Host applications connect to PostgreSQL at `localhost:5432` and Kafka at `localhost:9092`.

## TDD workflow

Use red-green-refactor for every behavior:

1. Add a focused failing test that expresses one acceptance criterion.
2. Implement the smallest behavior that makes the test pass.
3. Refactor while keeping the test suite green.

Do not implement business behavior without a test. Keep unit tests close to the owning application and use Cypress only for user-visible workflows.

## Commands

- Backend tests: `cd backend && python -m pytest`
- Consumer tests: `cd consumer && python -m pytest`
- Frontend tests: `cd frontend && npm test`
- Frontend lint/build: `cd frontend && npm run lint && npm run build`
- Functional tests: `cd functional-test && npm run cypress:run`
- Infrastructure: `docker compose up -d`

## Conventions

- Use Python type hints and small FastAPI dependencies.
- Keep database access behind the backend persistence boundary.
- Keep Kafka producer behavior in the backend and consumer behavior in `consumer/`.
- Read connection details from environment variables; never commit secrets.
- Add Alembic migrations with each persistence model change.
- Preserve the configured topic and consumer group unless a test or design decision changes them.
- Use TypeScript strict mode and accessible semantic HTML in the frontend.

## Scope boundary

The current repository is scaffolding. The order model, `/orders/create`, Kafka publishing/consumption, status transitions, polling, and business UI must be implemented in later TDD changes.
