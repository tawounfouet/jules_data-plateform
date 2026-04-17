from spark_utils import get_spark_session
import sys

def main():
    spark = get_spark_session("IngestToBronze")

    # Read raw JSON
    df = spark.read.json("/tmp/ecommerce/events.json")

    # Validation step with PySpark (pseudo-GE)
    if df.filter(df.user_id.isNull()).count() > 0:
        print("Data quality check failed: Null user_ids found")
        sys.exit(1)

    # Write to Iceberg Bronze
    df.write.format("iceberg") \
        .mode("append") \
        .save("nessie.ecommerce.bronze_events")

if __name__ == "__main__":
    main()\n