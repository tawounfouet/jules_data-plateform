FROM bitnami/spark:3.5.0

USER root

# Install required dependencies
RUN install_packages curl wget

# Download Iceberg, Nessie, and AWS S3/Hadoop jars
ENV ICEBERG_VERSION=1.4.2
ENV NESSIE_VERSION=0.74.0
ENV AWS_SDK_VERSION=2.20.18
ENV HADOOP_VERSION=3.3.4

RUN cd /opt/bitnami/spark/jars && \
    wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/${ICEBERG_VERSION}/iceberg-spark-runtime-3.5_2.12-${ICEBERG_VERSION}.jar && \
    wget https://repo1.maven.org/maven2/org/projectnessie/nessie-integrations/nessie-spark-extensions-3.5_2.12/${NESSIE_VERSION}/nessie-spark-extensions-3.5_2.12-${NESSIE_VERSION}.jar && \
    wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar && \
    wget https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/${AWS_SDK_VERSION}/bundle-${AWS_SDK_VERSION}.jar && \
    wget https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar

USER 1001\n