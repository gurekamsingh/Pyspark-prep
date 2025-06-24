from pyspark.sql import SparkSession
from pyspark.sql.window  import Window
from pyspark.sql.functions import rank,dense_rank,row_number

 

spark = SparkSession.builder.appName("windowfunctions").getOrCreate()
people_df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

windowspec = Window.partitionBy("department").orderBy(people_df.salary.desc())

result_df = people_df.withColumn("rank", rank().over(windowspec))\
                     .withColumn("dense_rank", dense_rank().over(windowspec)) \
                     .withColumn("row_number", row_number().over(windowspec))

finaldf = result_df.filter("rank<=3")

finaldf.select("name", "department", "salary", "rank", "dense_rank", "row_number").distinct().show()