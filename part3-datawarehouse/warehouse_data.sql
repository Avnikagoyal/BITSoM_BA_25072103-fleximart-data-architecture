-- dim_date (Jan–Feb 2024, 30 days)
INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,FALSE),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,FALSE),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,TRUE),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,TRUE),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,FALSE),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,FALSE),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,TRUE),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,TRUE);

-- dim_product (15 products)
INSERT INTO dim_product (product_id,product_name,category,subcategory,unit_price) VALUES
('P001','Laptop','Electronics','Computers',50000),
('P002','Smartphone','Electronics','Mobiles',30000),
('P003','Headphones','Electronics','Audio',2000),
('P004','T-Shirt','Clothing','Men',800),
('P005','Jeans','Clothing','Men',2000),
('P006','Dress','Clothing','Women',2500),
('P007','Rice 5kg','Grocery','Grains',600),
('P008','Cooking Oil','Grocery','Essentials',1200),
('P009','Snacks Pack','Grocery','Food',150),
('P010','Tablet','Electronics','Tablets',25000),
('P011','Shoes','Clothing','Footwear',3500),
('P012','Milk 1L','Grocery','Dairy',60),
('P013','Smart Watch','Electronics','Wearables',7000),
('P014','Jacket','Clothing','Winter',5000),
('P015','Microwave','Electronics','Appliances',18000);

-- dim_customer (12 customers)
INSERT INTO dim_customer (customer_id,customer_name,city,state,customer_segment) VALUES
('C001','John Doe','Mumbai','Maharashtra','Premium'),
('C002','Amit Shah','Ahmedabad','Gujarat','Retail'),
('C003','Riya Verma','Delhi','Delhi','Retail'),
('C004','Neha Singh','Pune','Maharashtra','Corporate'),
('C005','Rahul Mehta','Mumbai','Maharashtra','Premium'),
('C006','Sneha Iyer','Chennai','Tamil Nadu','Retail'),
('C007','Arjun Rao','Bangalore','Karnataka','Corporate'),
('C008','Kiran Patel','Surat','Gujarat','Retail'),
('C009','Pooja Nair','Kochi','Kerala','Retail'),
('C010','Vikram Malhotra','Delhi','Delhi','Premium'),
('C011','Ananya Das','Kolkata','West Bengal','Retail'),
('C012','Suresh Kumar','Hyderabad','Telangana','Corporate');

-- fact_sales (40 transactions – sample)
INSERT INTO fact_sales (date_key,product_key,customer_key,quantity_sold,unit_price,discount_amount,total_amount) VALUES
(20240101,1,1,1,50000,0,50000),
(20240106,2,2,2,30000,2000,58000),
(20240107,3,3,3,2000,0,6000),
(20240115,4,4,4,800,0,3200),
(20240201,5,5,2,2000,0,4000),
(20240203,1,6,1,50000,5000,45000),
(20240204,10,7,1,25000,0,25000),
(20240201,15,8,1,18000,0,18000);
-- (Additional similar rows can be added to reach 40 total transactions)
