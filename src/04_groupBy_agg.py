from pyspark.sql  import SparkSession
from pyspark.sql.functions import avg, count
 

spark = SparkSession.builder.appName("groupByagg").getOrCreate()
people_df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

result_df = people_df.groupBy("department").agg(avg("salary").alias("Average_salary"),count("id").alias("Employee_count"))
result_df.show()
