from pyspark.sql  import SparkSession
 

spark = SparkSession.builder.appName("ReadCsv").getOrCreate()
people_df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

people_df.printSchema()
people_df.show()
people_df.limit(5).show()
