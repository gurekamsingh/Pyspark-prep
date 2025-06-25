import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

os.environ["PYSPARK_PYTHON"] = sys.executable

spark = SparkSession.builder.appName("BroadcastJoinExample").getOrCreate()

# Large dataset: people
people_data = [
    (1, "Alice", "IT"),
    (2, "Bob", "Finance"),
    (3, "Charlie", "HR"),
    (4, "David", "IT"),
    (5, "Eve", "Finance")
]
people_cols = ["id", "name", "department"]

people_df = spark.createDataFrame(people_data, people_cols)

# Small dataset: departments
dept_data = [
    ("IT", "Information Technology"),
    ("Finance", "Financial Services"),
    ("HR", "Human Resources")
]
dept_cols = ["dept_code", "dept_full_name"]

dept_df = spark.createDataFrame(dept_data, dept_cols)

result_df = people_df.join(broadcast(dept_df), people_df.department == dept_df.dept_code, "inner")

# Select and show
result_df.select("id", "name", "department", "dept_full_name").show()
