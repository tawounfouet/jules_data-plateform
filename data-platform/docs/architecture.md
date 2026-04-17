# Architecture Overview

This Unified Data Platform architecture is based on the Open Data Lakehouse pattern. It integrates best-in-class open-source components for storage, computation, orchestration, governance, and observability.

## Core Components

1. **Storage Layer (MinIO + Iceberg)**
   - **MinIO** acts as an S3-compatible object storage layer, divided into zones: `bronze` (raw), `silver` (cleaned), `gold` (aggregated), and `quarantine` (rejected data).
   - **Apache Iceberg** is the table format, providing ACID transactions, time travel, and schema evolution on top of MinIO.

2. **Compute & Processing Layer (Apache Spark + Trino)**
   - **Apache Spark** is used for heavy-duty ETL processes (batch and streaming) moving data from bronze to silver to gold.
   - **Trino** serves as the distributed SQL query engine for ad-hoc analytics and BI over the lakehouse data.

3. **Data Catalog (Project Nessie)**
   - **Nessie** provides a git-like version control system for data catalogs, enabling isolated branches and commits for data ingestion and transformations.

4. **Orchestration Layer (Apache Airflow)**
   - **Airflow** orchestrates all the data pipelines and machine learning workflows, managing dependencies, retries, and scheduling.

5. **Machine Learning Layer (MLflow)**
   - **MLflow** handles experiment tracking, model registry, and metadata logging for ML workloads trained on the gold layer.

6. **Governance & Data Trust (Great Expectations)**
   - **Great Expectations** is embedded in the pipeline to validate data quality and schema contracts at both the ingestion (PySpark) and analytical (Trino) levels.

7. **Observability (Prometheus + Grafana)**
   - **Prometheus** scrapes metrics from Spark, Airflow, and Trino.
   - **Grafana** provides dashboards for monitoring platform health, pipeline duration, and storage limits.

8. **Security (Keycloak + NGINX)**
   - **Keycloak** acts as the Identity Provider (IdP) for centralized authentication.
   - **NGINX** handles reverse proxying and TLS termination for all services.\n