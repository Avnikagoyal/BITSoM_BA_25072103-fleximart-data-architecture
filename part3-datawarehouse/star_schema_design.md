# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

### FACT TABLE: fact_sales
**Grain:** One row per product per order line item  
**Business Process:** Sales transactions

**Measures (Numeric Facts):**
- **quantity_sold:** Number of units sold
- **unit_price:** Price per unit at the time of sale
- **discount_amount:** Discount applied on the line item
- **total_amount:** Final sales value (quantity_sold × unit_price − discount_amount)

**Foreign Keys:**
- **date_key** → dim_date
- **product_key** → dim_product
- **customer_key** → dim_customer

---

### DIMENSION TABLE: dim_date
**Purpose:** Enables time-based analysis such as daily, monthly, quarterly, and yearly trends  
**Type:** Conformed dimension

**Attributes:**
- **date_key (PK):** Surrogate key in YYYYMMDD format
- **full_date:** Actual calendar date
- **day_of_week:** Monday–Sunday
- **day_of_month:** 1–31
- **month:** Numeric month (1–12)
- **month_name:** January, February, etc.
- **quarter:** Q1–Q4
- **year:** Calendar year
- **is_weekend:** TRUE if Saturday/Sunday, else FALSE

---

### DIMENSION TABLE: dim_product
**Purpose:** Product information for sales analysis
**Type:** Conformed dimension

**Attributes:**
- product_key (PK): Simple auto-generated number for each product
- product_id: Original product code from the main system
- product_name: Name of the product
- category:  product category
- subcategory: Detailed product classification
- unit_price: Current list price

### DIMENSION TABLE: dim_customer
**Purpose:** Customer information for segmentation and geographic analysis
**Type:** Conformed dimension

**Attributes:**
- customer_key (PK): Simple auto-generated number for each customer
- customer_id: Original customer code from the main system
- customer_name: Full name of customer
- city: Customer's city
- state: Customer's state
- customer_segment: Business classification (Retail/Corporate)




## Section 2: Design Decisions

I selected transaction line-item granularity because it gives us maximum flexibility for analysis. This means we can answer very specific questions like "what products did customer X buy on date Y" while still being able to add up data for bigger picture reports. Going more detailed wouldn't help us, while less detail would mean losing important information.

I chose simple numbered keys instead of using the original system codes for a few good reasons. First, if the original product or customer codes ever change in the main system, our data warehouse stays stable and doesn't break. Second, using small numbers makes the database run faster when combining tables. Third, it makes handling historical changes much easier down the road.

This design supports drill-down operations through the date breakdown (year → quarter → month → day) and product breakdown (category → subcategory → product). Roll-up works the opposite way, adding up from detailed to summary levels. The star schema makes these operations simple to write using basic GROUP BY statements.

## Section 3: Sample Data Flow

**Source Transaction:**
Order #101, Customer "John Doe", Product "Laptop", Qty: 2, Price: 50000

**Becomes in Data Warehouse:**

fact_sales: {
  date_key: 20240115,
  product_key: 5,
  customer_key: 12,
  quantity_sold: 2,
  unit_price: 50000,
  discount_amount: 0,
  total_amount: 100000
}

dim_date: {
  date_key: 20240115,
  full_date: '2024-01-15',
  day_of_week: 'Monday',
  month: 1,
  month_name: 'January',
  quarter: 'Q1',
  year: 2024,
  is_weekend: FALSE
}

dim_product: {
  product_key: 5,
  product_id: 'PROD005',
  product_name: 'Laptop',
  category: 'Electronics',
  subcategory: 'Computers',
  unit_price: 50000.00
}

dim_customer: {
  customer_key: 12,
  customer_id: 'CUST012',
  customer_name: 'John Doe',
  city: 'Mumbai',
  state: 'Maharashtra',
  customer_segment: 'Retail'
}