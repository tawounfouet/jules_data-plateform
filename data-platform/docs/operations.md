# Operations & Maintenance

This platform is equipped with operational scripts for routine maintenance and observability.

## Backup and Restore

Operational scripts are located in the `ops/` directory.

- **Backup (`ops/backup.sh`):**
  This script creates a PostgreSQL dump of the unified metastore database and performs a backup of MinIO metadata and raw buckets using the MinIO Client (`mc`).
  ```bash
  cd data-platform
  ./ops/backup.sh
  ```

- **Restore (`ops/restore.sh`):**
  This script restores the `metastore` database from the `.sql` dump file.
  ```bash
  cd data-platform
  ./ops/restore.sh
  ```

## Monitoring Configuration

The platform uses Prometheus to scrape metrics from critical services and Grafana to visualize them.

- **Prometheus:** Configured via `observability/prometheus/prometheus.yml` to scrape Airflow, Trino, and local metrics.
- **Grafana:** Dashboards and Datasources are automatically provisioned. See `observability/grafana/provisioning` for YAML configurations mapping to the Prometheus datasource.

## Adding Dependencies

- **Airflow:** Update `orchestration/requirements.txt` and run `make build`.
- **Spark:** Modify `shared/spark/Dockerfile` to include new Maven JARs or PyPI packages, then run `make build`.
- **MLflow:** Update `ml/requirements.txt` and run `make build`.\n