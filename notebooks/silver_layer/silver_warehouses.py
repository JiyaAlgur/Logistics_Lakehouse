from pyspark.sql.functions import *

warehouses_df = spark.table("logistics.bronze.warehouses")

warehouses_clean = (
    warehouses_df
    .dropDuplicates()
    .dropna(subset=["warehouse_id"])
    .withColumn("warehouse_name", initcap(trim(col("warehouse_name"))))
    .withColumn("city", initcap(trim(col("city"))))
    .withColumn("state", initcap(trim(col("state"))))
    .filter(col("capacity") > 0)
)

warehouses_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.warehouses")
display(spark.table("logistics.silver.warehouses"))

