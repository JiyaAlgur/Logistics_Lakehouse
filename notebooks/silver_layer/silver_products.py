from pyspark.sql.functions import *

products_df = spark.table("logistics.bronze.products")

products_clean = (
    products_df
    .dropDuplicates()
    .dropna(subset=["product_id"])
    .withColumn("product_name", initcap(trim(col("product_name"))))
    .withColumn("category", initcap(trim(col("category"))))
    .withColumn("brand", initcap(trim(col("brand"))))
    .filter(col("cost_price") > 0)
    .filter(col("selling_price") > 0)
    .filter(col("selling_price") >= col("cost_price"))
)

products_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.silver.products")
display(spark.table("logistics.silver.products"))