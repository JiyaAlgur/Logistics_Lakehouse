from pyspark.sql.functions import *

suppliers_df = spark.table("logistics.bronze.suppliers")

suppliers_clean = (
    suppliers_df
    .dropDuplicates()
    .dropna(subset=["supplier_id"])
    .withColumn("supplier_name", initcap(trim(col("supplier_name"))))
    .withColumn("city", initcap(trim(col("city"))))
    .withColumn("state", initcap(trim(col("state"))))
)

suppliers_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.suppliers")
display(spark.table("logistics.silver.suppliers"))
