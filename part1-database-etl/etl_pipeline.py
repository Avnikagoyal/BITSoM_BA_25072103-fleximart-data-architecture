import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="fleximart"
)
cursor = conn.cursor()

# ---------------- TRUNCATE TABLES ----------------
print("Truncating tables...")
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("TRUNCATE TABLE order_items")
cursor.execute("TRUNCATE TABLE orders")
cursor.execute("TRUNCATE TABLE customers")
cursor.execute("TRUNCATE TABLE products")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()

# ---------------- REPORT ----------------
report = []

# ---------------- LOAD CSV FILES ----------------
customers = pd.read_csv("./data/customers_raw.csv")
products = pd.read_csv("./data/products_raw.csv")
transactions = pd.read_csv("./data/sales_raw.csv")

# ================= CUSTOMERS =================
cust_before = len(customers)
customers.drop_duplicates(inplace=True)
customers.dropna(subset=['email'], inplace=True)

# Clean phone numbers
customers['phone'] = customers['phone'].astype(str).str.replace(r'\D', '', regex=True)
customers['phone'] = "+91-" + customers['phone']

# Normalize registration dates
customers['registration_date'] = pd.to_datetime(
    customers['registration_date'], errors='coerce', dayfirst=True
)
customers.dropna(subset=['registration_date'], inplace=True)
customers['registration_date'] = customers['registration_date'].dt.strftime('%Y-%m-%d')

cust_after = len(customers)

# Map to store CSV customer_id -> DB customer_id
customer_id_map = {}

for _, row in customers.iterrows():
    cursor.execute("""
        INSERT INTO customers
        (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['first_name'],
        row['last_name'],
        row['email'],
        row['phone'],
        row['city'],
        row['registration_date']
    ))
    conn.commit()
    db_id = cursor.lastrowid
    customer_id_map[row['customer_id']] = db_id  # Map CSV ID to DB ID

report.append(f"Customers Loaded: {cust_after}")
report.append(f"Customers Removed: {cust_before - cust_after}\n")

# ================= PRODUCTS =================
prod_before = len(products)
products.drop_duplicates(inplace=True)
products.dropna(subset=['price'], inplace=True)
products['stock_quantity'] = products['stock_quantity'].fillna(0)
products['category'] = products['category'].str.strip().str.lower().str.capitalize()
prod_after = len(products)

# Map to store CSV product_id -> DB product_id
product_id_map = {}

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products
        (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """, (
        row['product_name'].strip(),
        row['category'],
        row['price'],
        int(row['stock_quantity'])
    ))
    conn.commit()
    db_id = cursor.lastrowid
    product_id_map[row['product_id']] = db_id  # Map CSV ID to DB ID

report.append(f"Products Loaded: {prod_after}")
report.append(f"Products Removed: {prod_before - prod_after}\n")

# ================= TRANSACTIONS =================
trans_before = len(transactions)
transactions.drop_duplicates(inplace=True)
transactions.dropna(subset=['customer_id', 'product_id'], inplace=True)
transactions = transactions[transactions['status'] == 'Completed']

# Normalize transaction dates
transactions['transaction_date'] = pd.to_datetime(
    transactions['transaction_date'], errors='coerce', dayfirst=True
)
transactions.dropna(subset=['transaction_date'], inplace=True)
transactions['transaction_date'] = transactions['transaction_date'].dt.strftime('%Y-%m-%d')

trans_after = len(transactions)

for _, row in transactions.iterrows():
    csv_cust_id = row['customer_id']
    csv_prod_id = row['product_id']

    # Skip if mapping doesn't exist (should not happen after dropna)
    if csv_cust_id not in customer_id_map or csv_prod_id not in product_id_map:
        continue

    db_cust_id = customer_id_map[csv_cust_id]
    db_prod_id = product_id_map[csv_prod_id]

    # Insert order
    cursor.execute("""
        INSERT INTO orders
        (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
    """, (
        db_cust_id,
        row['transaction_date'],
        row['quantity'] * row['unit_price'],
        row['status']
    ))
    conn.commit()
    order_id = cursor.lastrowid

    # Insert order item
    cursor.execute("""
        INSERT INTO order_items
        (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        order_id,
        db_prod_id,
        int(row['quantity']),
        row['unit_price'],
        row['quantity'] * row['unit_price']
    ))
    conn.commit()

report.append(f"Transactions Loaded: {trans_after}")
report.append(f"Transactions Removed: {trans_before - trans_after}\n")

# ---------------- WRITE REPORT ----------------
with open("data_quality_report.txt", "w") as f:
    f.write("\n".join(report))

cursor.close()
conn.close()
print("ETL Pipeline executed successfully.")
