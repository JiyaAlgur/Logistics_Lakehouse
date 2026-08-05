from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


customers_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/logistics/bronze/raw_files/shipments.csv")



customers_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("logistics.bronze.shipments")