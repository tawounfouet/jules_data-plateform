FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000\n