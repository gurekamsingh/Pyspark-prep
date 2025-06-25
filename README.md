# Pyspark-prep

This project contains a set of 8 PySpark practice scripts designed to help prepare for data engineering interviews. Each script covers a different concept or commonly asked topic using PySpark.

## 📁 Folder Structure

```
PySpark-prep/
├── datasets/
│   └── people.csv
├── src/
│   ├── 01_second_highest_order_customer.py
│   ├── 02_dense_rank_example.py
│   ├── 03_window_functions_top2_salary.py
│   ├── 04_json_parsing_struct.py
│   ├── 05_json_parsing_get_json_object.py
│   ├── 06_json_data_fix_and_run.py
│   ├── 07_broadcast_join_example.py
│   └── 08_broadcast_join.py
└── README.md
```

## 📄 Dataset: `people.csv`

This CSV file contains sample employee data, including a `json_data` column with JSON-formatted strings:

```csv
id,name,age,country,salary,department,joining_date,json_data
1,Alice,25,USA,60000,IT,2021-01-15,"{"project": "X", "hours": 40}"
...
```

## 📚 Questions and Script Overview

### 1. `01_second_highest_order_customer.py`
- **Topic**: SQL subquery and `JOIN`
- **Goal**: Find the customer who placed the second highest order.

### 2. `02_dense_rank_example.py`
- **Topic**: `dense_rank()`
- **Goal**: Apply dense ranking by salary to identify position within a department.

### 3. `03_window_functions_top2_salary.py`
- **Topic**: `rank`, `dense_rank`, `row_number`
- **Goal**: Fetch top 2 earners by department using window functions.

### 4. `04_json_parsing_struct.py`
- **Topic**: `from_json()` with schema
- **Goal**: Parse `json_data` into structured columns.

### 5. `05_json_parsing_get_json_object.py`
- **Topic**: `get_json_object()`
- **Goal**: Extract JSON fields without a schema.

### 6. `06_json_data_fix_and_run.py`
- **Topic**: Correct JSON parsing issue
- **Goal**: Adjust file formatting and successfully extract fields.

### 7. `07_broadcast_join_example.py`
- **Topic**: Broadcast join
- **Goal**: Efficiently join a large and a small dataset using broadcast.

### 8. `08_broadcast_join.py`
- **Topic**: Reuse of the broadcast join
- **Goal**: Demonstrate inner joins with explicit broadcasting.

## ▶️ How to Run

Make sure you have PySpark installed in a virtual environment.

```bash
source .venv/bin/activate        # Or use Windows equivalent
pip install pyspark              # If not already installed
python src/01_second_highest_order_customer.py
```

Repeat for each script (02, 03, ..., 08).

## ⚙️ Environment Notes

- Spark may log warnings (e.g., native Hadoop library).
- If you face `SocketTimeoutException`, try:
  - Increasing worker timeout
  - Restarting Python environment
  - Checking that `.venv` and Spark versions are compatible

---

Happy learning and good luck with your interviews! ✨