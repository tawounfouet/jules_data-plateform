from airflow import DAG
from airflow.decorators import task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ecommerce_ingestion_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['ingestion', 'ecommerce']
) as dag:

    @task
    def extract_mock_data():
        import json
        import os
        # Simulate API extraction
        data = [
            {"user_id": 1, "event": "click", "timestamp": "2023-10-01T10:00:00Z"},
            {"user_id": 2, "event": "purchase", "timestamp": "2023-10-01T10:05:00Z"}
        ]
        os.makedirs('/tmp/ecommerce', exist_ok=True)
        with open('/tmp/ecommerce/events.json', 'w') as f:
            for row in data:
                f.write(json.dumps(row) + '\n')
        return "/tmp/ecommerce/events.json"

    extract_task = extract_mock_data()

    load_to_bronze = SparkSubmitOperator(
        task_id='load_to_bronze',
        application='/opt/airflow/jobs/ingest_to_bronze.py',
        conn_id='spark_default',
        name='ecommerce_ingest_bronze',
        conf={
            "spark.jars.packages": "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.2,org.projectnessie.nessie-integrations:nessie-spark-extensions-3.5_2.12:0.74.0,org.apache.hadoop:hadoop-aws:3.3.4",
        }
    )

    extract_task >> load_to_bronze\n