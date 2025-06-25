from pyspark.sql import SparkSession
from pyspark.sql.functions import col, get_json_object, from_json, regexp_replace
from pyspark.sql.types import StructType, IntegerType, StringType
 

spark = SparkSession.builder.appName("getjson").getOrCreate()
df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

# json_schema = StructType().add("project", StringType()).add("hours", IntegerType())

# # Parse JSON column
# parsed_df = df.withColumn("parsed_json", from_json(col("json_data"), json_schema)) \
#               .withColumn("project", col("parsed_json.project")) \
#               .withColumn("hours", col("parsed_json.hours")) \
#               .drop("parsed_json")

# parsed_df.select("name", "department", "json_data", "project", "hours").show()
# Step 1: Remove outer quotes from json_data
df_cleaned = df.withColumn("json_clean", regexp_replace("json_data", r'^"|"$', ""))

finaal_df = df.withColumn("project", get_json_object(col("json_data"), "$.project")) \
              .withColumn("hours", get_json_object(col("json_data"), "$.hours"))


finaal_df.select("name", "age", "id", "project", "hours").distinct().show()

