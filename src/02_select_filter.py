from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SelectFilterAlias").getOrCreate()

people_df = spark.read.csv("datasets/people.csv", header = True, inferSchema = True)

# people_df.show()

# result_df = people_df.select("id", "name", "age", "salary").limit(5)
result_df = people_df.filter((people_df.age >25) & (people_df.country == "USA" )).select("id", "name", "Age", "Country", "salary").limit(5)

result_df.show()