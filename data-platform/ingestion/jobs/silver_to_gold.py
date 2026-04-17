from spark_utils import get_spark_session
from pyspark.sql.functions import count

def main():
    spark = get_spark_session("SilverToGold")

    df = spark.table("nessie.ecommerce.silver_events")

    # Aggregate
    agg_df = df.groupBy("event").agg(count("*").alias("event_count"))

    # Write to Iceberg Gold
    agg_df.write.format("iceberg") \
        .mode("overwrite") \
        .save("nessie.ecommerce.gold_events_summary")

if __name__ == "__main__":
    main()\n