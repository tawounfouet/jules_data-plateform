# Data Pipelines

This platform includes three primary example DAGs in Airflow demonstrating an end-to-end flow for an e-commerce domain.

## 1. Ingestion Pipeline (`ecommerce_ingestion_pipeline`)
- **Schedule:** Daily
- **Goal:** Ingest raw JSON event data into the Bronze layer.
- **Process:**
  - `extract_mock_data`: Generates mock e-commerce event JSON files (simulating an API extraction).
  - `load_to_bronze`: A PySpark job (`ingest_to_bronze.py`) that reads the JSON data, performs quick null-checks, and writes the raw data to an Iceberg table in the Nessie catalog `nessie.ecommerce.bronze_events`.

## 2. Lakehouse Processing Pipeline (`ecommerce_lakehouse_pipeline`)
- **Schedule:** Daily
- **Goal:** Transform raw events into analytical models.
- **Process:**
  - `bronze_to_silver`: A PySpark job (`bronze_to_silver.py`) that filters out corrupted data and creates cleaned records in `nessie.ecommerce.silver_events`.
  - `silver_to_gold`: A PySpark job (`silver_to_gold.py`) that performs aggregations (e.g., event counts) and writes to `nessie.ecommerce.gold_events_summary`.

## 3. Machine Learning Pipeline (`ecommerce_ml_pipeline`)
- **Schedule:** Weekly
- **Goal:** Train and log models using gold-layer data.
- **Process:**
  - `train_model`: An Airflow task leveraging the `@task` TaskFlow API. It trains a `RandomForestClassifier` on e-commerce features and logs the hyperparameters, metrics (accuracy), and the final model object into the MLflow tracking server.\n