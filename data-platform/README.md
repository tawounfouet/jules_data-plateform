# Unified Data Platform Architecture

This is a complete production-grade repository skeleton for an Open Data Lakehouse platform.
It uses Docker Compose to run a local cluster of services including MinIO, Spark, Nessie, Trino, Airflow, MLflow, and more.

## Architecture

- **Data Lakehouse**: MinIO (S3) + Spark (ETL) + Nessie (Catalog) + Trino (Query Engine) + Iceberg (Table Format)
- **Control Plane**: Airflow (Orchestration) + MLflow (ML Tracking)
- **Trust Layer**: Great Expectations + Schema Contracts
- **Observability**: Prometheus + Grafana

## Quick Start

1. Build custom images:
   ```bash
   make build
   ```

2. Start the platform:
   ```bash
   make up
   ```

3. Access the services:
   - Airflow UI: http://localhost:8083 (admin/admin)
   - MinIO Console: http://localhost:9001 (admin/password)
   - Trino UI: http://localhost:8082
   - MLflow UI: http://localhost:5000
   - Grafana UI: http://localhost:3000 (admin/admin)
   - Keycloak: http://localhost:8080 (admin/admin)\n