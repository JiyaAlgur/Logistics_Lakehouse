from pyspark.sql.functions import *

inventory_df = spark.table("logistics.bronze.inventory")

inventory_clean = (
    inventory_df
    .dropDuplicates()
    .dropna(subset=["inventory_id"])
    .filter(col("quantity") >= 0)
    .filter(col("reorder_level") >= 0)
    .withColumn("stock_status", initcap(trim(col("stock_status"))))
)

inventory_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.inventory")
display(spark.table("logistics.silver.inventory"))
