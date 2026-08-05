from pyspark.sql.functions import *

orders_df = spark.table("logistics.bronze.orders")

orders_clean = (
    orders_df
    .dropDuplicates()
    .dropna(subset=["order_id"])
    .filter(col("quantity") > 0)
    .filter(col("final_amount") >= 0)
    .withColumn("payment_method", initcap(trim(col("payment_method"))))
    .withColumn("order_status", initcap(trim(col("order_status"))))
)

orders_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.orders")
display(spark.table("logistics.silver.orders"))