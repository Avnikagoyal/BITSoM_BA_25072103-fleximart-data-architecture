# FlexiMart ETL & Analytics Project

## Overview

This project cleans raw customer, product, and sales CSV data and loads it into a MySQL/PostgreSQL database. It also documents the database schema and answers key business questions using SQL.

## Contents

- **etl_pipeline.py**  
  Extracts, cleans, transforms, and loads CSV data into the database

- **data_quality_report.txt**  
  Summary of duplicates removed, missing values handled, and records loaded

- **schema_documentation.md**  
  Database schema explanation, relationships, and normalization

- **business_queries.sql**  
  SQL queries for customer insights, product sales, and monthly trends

## How to Run

1. Create the database using the provided schema  
2. Update database credentials in `etl_pipeline.py`  
3. Run the ETL pipeline:

   ```bash
   python etl_pipeline.py
