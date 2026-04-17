from spark_utils import get_spark_session
from pyspark.sql.functions import col

def main():
    spark = get_spark_session("BronzeToSilver")

    df = spark.table("nessie.ecommerce.bronze_events")

    # Clean and filter
    clean_df = df.filter(col("event").isNotNull())

    # Write to Iceberg Silver
    clean_df.write.format("iceberg") \
        .mode("overwrite") \
        .save("nessie.ecommerce.silver_events")

if __name__ == "__main__":
    main()\n