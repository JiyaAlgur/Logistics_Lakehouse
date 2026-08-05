from pyspark.sql.functions import *

shipments_df = spark.table("logistics.bronze.shipments")

shipments_clean = (
    shipments_df
    .dropDuplicates()
    .dropna(subset=["shipment_id"])
    .withColumn("shipment_status", initcap(trim(col("shipment_status"))))
)

shipments_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.shipments")
display(spark.table("logistics.silver.shipments"))