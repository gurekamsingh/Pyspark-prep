import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

# Ensure Spark uses the correct Python interpreter
os.environ["PYSPARK_PYTHON"] = sys.executable

spark = SparkSession.builder.appName("ReadCsv").getOrCreate()

data = [
    (1, "Alice", "Python,SQL,Spark"),
    (2, "Bob", "Java,Scala"),
    (3, "Charlie", "Python,Spark")
]


 #list of tuples
columns = ["id", "name", "skills"]

# explode(column)
# Takes an array column and creates a new row for each element in the array.

df = spark.createDataFrame(data, columns)

df_array = df.withColumn("skills_array", split(df.skills, ","))

exploded_df = df_array.select("id","name", explode("skills_array").alias("skills"))

exploded_df.show()