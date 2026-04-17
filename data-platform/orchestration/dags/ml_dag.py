from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-science',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'ecommerce_ml_pipeline',
    default_args=default_args,
    schedule_interval='@weekly',
    catchup=False,
    tags=['ml', 'ecommerce']
) as dag:

    @task
    def train_model():
        import mlflow
        import mlflow.sklearn
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.datasets import make_classification
        import pandas as pd

        mlflow.set_tracking_uri("http://mlflow:5000")
        mlflow.set_experiment("ecommerce_churn_prediction")

        with mlflow.start_run():
            X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
            clf = RandomForestClassifier(n_estimators=100, random_state=42)
            clf.fit(X, y)

            mlflow.log_param("n_estimators", 100)
            mlflow.log_metric("accuracy", clf.score(X, y))
            mlflow.sklearn.log_model(clf, "model")

    train_task = train_model()\n