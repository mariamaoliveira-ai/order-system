# Order System Infrastructure

Local development scaffold for an order system using PostgreSQL, Apache Kafka, FastAPI, a separate Python consumer, React with Vite, and Prometheus. PostgreSQL, Kafka, and Prometheus run in Docker; application processes run locally.

## Prerequisite

Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).

## Configuration

Create a local environment file from the example:

```sh
cp .env.example .env
```

Change `POSTGRES_PASSWORD` before using the stack outside local development. The `.env` file is ignored by Git.

Install application dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e 'backend[test]'
python -m pip install -e 'consumer[test]'
cd frontend && npm install && cd ..
cd functional-test && npm install && cd ..
```

## Start and stop

Start the services in the background:

```sh
docker compose up -d
```

View service status and health:

```sh
docker compose ps
```

View logs:

```sh
docker compose logs -f postgres kafka prometheus
```

Stop containers without removing data:

```sh
docker compose stop
```

Restart the stack:

```sh
docker compose restart
```

Remove containers and the network:

```sh
docker compose down
```

Remove containers, the network, and all named data volumes:

```sh
docker compose down -v
```

The `down -v` command permanently removes local PostgreSQL, Kafka, and Prometheus data.

## Services

| Service | Host address | Docker address |
| --- | --- | --- |
| PostgreSQL | `localhost:5432` | `postgres:5432` |
| Kafka | `localhost:9092` | `kafka:19092` |
| Prometheus | `http://localhost:9090` | `http://prometheus:9090` |

The PostgreSQL connection string format is:

```text
postgresql://<user>:<password>@localhost:5432/<database>
```

Host applications should use `localhost:9092` as the Kafka bootstrap server. Applications added as Compose services should use `kafka:19092`.

## Prometheus

Prometheus scrapes itself at `localhost:9090`. The configuration is mounted read-only from `prometheus/prometheus.yml`. When a backend exposes `/metrics`, add its Docker service name and port to that file, then restart Prometheus:

```sh
docker compose restart prometheus
```

## Validation

Validate interpolation and the Compose model without starting containers:

```sh
docker compose config
```

After startup, confirm PostgreSQL and Kafka are healthy:

```sh
docker compose ps
```

Open `http://localhost:9090/-/healthy` or the Prometheus web interface to confirm Prometheus is running.

## Application development

Run the API in one terminal:

```sh
cd backend
uvicorn order_system.main:app --app-dir src --reload
```

Run the consumer in another terminal:

```sh
cd consumer
python -m order_consumer.main
```

Run the Vite frontend:

```sh
cd frontend
npm run dev
```

The current application code is intentionally scaffolding. Order creation, persistence, Kafka processing, status transitions, and polling are to be implemented with TDD.

## Tests and quality

```sh
cd backend && python -m pytest
cd ../consumer && python -m pytest
cd ../frontend && npm test
cd frontend && npm run lint && npm run build
cd functional-test && npm run cypress:run
```

The functional-test suite expects the Vite development server at `http://localhost:5173`. Start it with `npm run dev` in `frontend/` before running functional tests.
