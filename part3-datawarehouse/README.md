# FlexiMart Data Warehouse (Star Schema)

## Overview

This task designs and implements a star schema data warehouse to analyze historical sales data and support analytical reporting.

## Files Included

- **star_schema_design.md**  
  Documentation of the star schema, design decisions, and sample data flow

- **warehouse_data.sql**  
  SQL script to create and populate dimension and fact tables

- **fleximart_dw**  
  Data warehouse database

## Star Schema Components

### Fact Table
- **fact_sales**  
  Sales transactions at line-item level

### Dimension Tables
- **dim_date** – Time-based analysis  
- **dim_product** – Product details and categories  
- **dim_customer** – Customer demographics  

## Key Features

- Line-item level granularity  
- Surrogate keys for performance and flexibility  
- Supports drill-down and roll-up analysis  

## How to Use

1. Create the `fleximart_dw` database  
2. Run the schema and data scripts from `warehouse_data.sql`  
3. Use SQL queries for analytical reporting  

## Tools Used

- MySQL / PostgreSQL  
- SQL
