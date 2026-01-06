# FlexiMart Data Architecture Project

**Student Name:** Avnika Goyal  
**Student ID:** BITSoM_BA_25072103  
**Email:** goyalavnika06@gmail.com  
**Date:** 06-01-2026  

## Project Overview

This project implements a complete data architecture solution for FlexiMart, including relational database ETL, NoSQL analysis, and a data warehouse for historical sales analytics. It extracts and transforms customer, product, and sales data, loads it into MySQL, and supports analytical queries for business insights. Additionally, MongoDB is used to handle semi-structured product catalog data.

## Repository Structure

├── part1-database-etl/
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ └── data_quality_report.txt
├── part2-nosql/
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
├── part3-datawarehouse/
│ ├── star_schema_design.md
│ ├── warehouse_schema.sql
│ ├── warehouse_data.sql
│ └── analytics_queries.sql
└── README.md


## Technologies Used

- Python 3.x, pandas, mysql-connector-python  
- MySQL 8.0 / PostgreSQL 14  
- MongoDB 6.0  

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings
During this project, I gained hands-on experience in building ETL pipelines to clean and transform raw data for relational databases. I learned to design star schemas for data warehouses, enabling efficient analytical queries. Additionally, working with MongoDB enhanced my understanding of handling semi-structured data. The project improved my SQL query writing, database normalization skills, and overall understanding of end-to-end data architecture.

## Challenges Faced

Handling Data Quality Issues: Raw CSV files had missing values and duplicate records. Solution: Implemented robust cleaning logic in the ETL pipeline using Python and pandas.

Schema Design for Data Warehouse: Deciding the grain and relationships for the star schema was challenging. Solution: Analyzed business requirements thoroughly and created fact and dimension tables optimized for analytical queries.

Integrating NoSQL with Relational Data: Mapping semi-structured product data from MongoDB to relational insights was tricky. Solution: Used MongoDB aggregation pipelines and JSON parsing in Python to extract insights effectively.

