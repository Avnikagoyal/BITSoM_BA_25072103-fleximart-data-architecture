# FlexiMart Database Schema Documentation

## Overview

The FlexiMart database is designed to manage customers, products, and orders for an e-commerce system. The schema ensures data integrity, supports scalability, and follows proper normalization principles.

---

## Entity-Relationship Description

### ENTITY: customers

**Purpose:** Stores customer personal and contact information.

**Attributes:**
- **customer_id:** Unique identifier for each customer (Primary Key)
- **first_name:** Customer’s first name
- **last_name:** Customer’s last name
- **email:** Customer’s email address (Unique)
- **phone:** Customer’s contact number
- **city:** City where the customer resides
- **registration_date:** Date when the customer registered

**Relationships:**
- One customer can place many orders (1:M relationship with `orders`)

---

### ENTITY: products

**Purpose:** Stores information about products available for sale.

**Attributes:**
- **product_id:** Unique identifier for each product (Primary Key)
- **product_name:** Name of the product
- **category:** Product category
- **price:** Selling price of the product
- **stock_quantity:** Available stock quantity

**Relationships:**
- One product can appear in many order items (1:M relationship with `order_items`)

---

### ENTITY: orders

**Purpose:** Stores order-level information for customer purchases.

**Attributes:**
- **order_id:** Unique identifier for each order (Primary Key)
- **customer_id:** References the customer who placed the order (Foreign Key)
- **order_date:** Date the order was placed
- **total_amount:** Total value of the order
- **status:** Current order status (e.g., Pending, Completed)

**Relationships:**
- One order belongs to one customer
- One order can have many order items (1:M relationship with `order_items`)

---

### ENTITY: order_items

**Purpose:** Stores individual product details within an order.

**Attributes:**
- **order_item_id:** Unique identifier for each order item (Primary Key)
- **order_id:** Associated order (Foreign Key)
- **product_id:** Associated product (Foreign Key)
- **quantity:** Number of units ordered
- **unit_price:** Price per unit at the time of order
- **subtotal:** Quantity × unit price

**Relationships:**
- Many order items belong to one order
- Many order items reference one product

---

## Normalization Explanation (Third Normal Form – 3NF)

The FlexiMart database schema is designed according to **Third Normal Form (3NF)** to ensure data consistency and eliminate redundancy. Each table contains attributes that depend only on the primary key, the whole primary key, and nothing but the primary key.

### Functional Dependencies

**customers:**
- `customer_id → first_name, last_name, email, phone, city, registration_date`

**products:**
- `product_id → product_name, category, price, stock_quantity`

**orders:**
- `order_id → customer_id, order_date, total_amount, status`

**order_items:**
- `order_item_id → order_id, product_id, quantity, unit_price, subtotal`

There are no partial or transitive dependencies. For example, customer details are stored only in the `customers` table and not repeated in `orders`, preventing redundancy.

### Anomaly Prevention

- **Update anomalies** are avoided because customer or product information is stored in one place.
- **Insert anomalies** are avoided because products and customers can exist independently of orders.
- **Delete anomalies** are avoided because deleting an order does not remove customer or product data.

This structure ensures data integrity, scalability, and efficient maintenance.

---

## Sample Data Representation

### customers

| customer_id | first_name | last_name | email            | phone      | city   | registration_date |
|------------:|------------|-----------|------------------|------------|--------|-------------------|
| 1           | Puja       | Rani      | puja@gmail.com   | 9876543210 | Meerut | 2024-01-10        |
| 2           | Aayush     | Gupta     | aayush@gmail.com | 9123456780 | Delhi  | 2024-02-15        |

```sql
INSERT INTO customers (customer_id, first_name, last_name, email, phone, city, registration_date)
VALUES
(1, 'Puja', 'Rani', 'puja@gmail.com', '9876543210', 'Meerut', '2024-01-10'),
(2, 'Aayush', 'Gupta', 'aayush@gmail.com', '9123456780', 'Delhi', '2024-02-15');
```

---

### products

| product_id | product_name | category    | price  | stock_quantity |
|-----------:|--------------|-------------|--------|----------------|
| 1          | Laptop       | Electronics | 850.00 | 20             |
| 2          | Headphones   | Accessories | 50.00  | 100            |

```sql
INSERT INTO products (product_id, product_name, category, price, stock_quantity)
VALUES
(1, 'Laptop', 'Electronics', 850.00, 20),
(2, 'Headphones', 'Accessories', 50.00, 100);
```

---

### orders

| order_id | customer_id | order_date | total_amount | status    |
|---------:|------------:|------------|--------------|-----------|
| 1        | 1           | 2024-03-01 | 900.00       | Completed |
| 2        | 2           | 2024-03-05 | 50.00        | Pending   |

```sql
INSERT INTO orders (order_id, customer_id, order_date, total_amount, status)
VALUES
(1, 1, '2024-03-01', 900.00, 'Completed'),
(2, 2, '2024-03-05', 50.00, 'Pending');
```

---

### order_items

| order_item_id | order_id | product_id | quantity | unit_price | subtotal |
|--------------:|---------:|-----------:|---------:|-----------:|---------:|
| 1             | 1        | 1          | 1        | 850.00     | 850.00   |
| 2             | 1        | 2          | 1        | 50.00      | 50.00    |

```sql
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price, subtotal)
VALUES
(1, 1, 1, 1, 850.00, 850.00),
(2, 1, 2, 1, 50.00, 50.00);
```

