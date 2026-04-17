FROM apache/airflow:2.8.0-python3.10

USER root
RUN apt-get update && apt-get install -y default-jre && apt-get clean

USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt\n