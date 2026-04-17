from airflow import DAG
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
    'ecommerce_lakehouse_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['lakehouse', 'ecommerce']
) as dag:

    bronze_to_silver = SparkSubmitOperator(
        task_id='bronze_to_silver',
        application='/opt/airflow/jobs/bronze_to_silver.py',
        conn_id='spark_default',
        name='ecommerce_bronze_to_silver'
    )

    silver_to_gold = SparkSubmitOperator(
        task_id='silver_to_gold',
        application='/opt/airflow/jobs/silver_to_gold.py',
        conn_id='spark_default',
        name='ecommerce_silver_to_gold'
    )

    bronze_to_silver >> silver_to_gold\n