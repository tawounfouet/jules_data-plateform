# Getting Started

## Prerequisites

- Docker and Docker Compose (v2)
- Make
- A machine with at least 8GB RAM (16GB recommended)

## Setup Instructions

1. **Clone the repository and enter the directory:**
   ```bash
   cd data-platform
   ```

2. **Build custom Docker images:**
   Many components (Airflow, Spark, MLflow) use custom Dockerfiles to embed necessary dependencies (like Iceberg libraries).
   ```bash
   make build
   ```

3. **Start the platform:**
   This will start all modular docker-compose files in detached mode.
   ```bash
   make up
   ```

4. **Initialize MinIO buckets:**
   Wait for the services to boot up. The `minio-init` container will automatically create the `bronze`, `silver`, `gold`, and `quarantine` buckets.

## Accessing Services

Once the stack is running, you can access the various UIs at the following endpoints:

- **Airflow UI:** `http://localhost:8083` (Credentials: `admin` / `admin`)
- **MinIO Console:** `http://localhost:9001` (Credentials: `admin` / `password`)
- **Trino UI:** `http://localhost:8082`
- **MLflow UI:** `http://localhost:5000`
- **Grafana UI:** `http://localhost:3000` (Credentials: `admin` / `admin`)
- **Keycloak UI:** `http://localhost:8080` (Credentials: `admin` / `admin`)

## Stopping the Platform

To shut down all services and remove the containers:
```bash
make down
```

*Note: Volumes like PostgreSQL data and MinIO storage will persist across restarts. To perform a full clean, remove the volumes manually.*\n