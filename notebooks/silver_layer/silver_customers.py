from pyspark.sql.functions import *

customers_df = spark.table("logistics.bronze.customers")


customers_clean = (
    customers_df
    .dropDuplicates()
    .dropna(subset=["customer_id"])
    .withColumn("customer_name", initcap(trim(col("customer_name"))))
    .withColumn("city", initcap(trim(col("city"))))
    .withColumn("state", initcap(trim(col("state"))))
    .withColumn("email", lower(trim(col("email"))))
)


customers_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.customers")

display(spark.table("logistics.silver.customers"))