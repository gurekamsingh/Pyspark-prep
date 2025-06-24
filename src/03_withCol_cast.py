from pyspark.sql  import SparkSession
from pyspark.sql.functions import col, lit
 

spark = SparkSession.builder.appName("ReadCsv").getOrCreate()
people_df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

result_df = people_df.withColumn("salary_in_lakhs", col("salary")/100000) \
                     .withColumn("joining_date", col("joining_date").cast("date")) \
                     .withColumn("is_active", lit("Yes"))
result_df.limit(5).show()
