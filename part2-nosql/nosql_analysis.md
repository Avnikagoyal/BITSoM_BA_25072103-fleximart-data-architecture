# NoSQL Analysis – Product Catalog

## Step-by-Step Process

### Step 1: Understand the Existing Problem
The current system uses a relational database (MySQL) to store product catalog data. Products belong to different categories and have varying attributes (e.g., electronics vs footwear). You must analyze why a traditional RDBMS struggles with this scenario.

### Step 2: Identify RDBMS Limitations
Focus on how fixed schemas, normalization, and table relationships make it difficult to:
- Store variable attributes
- Handle frequent schema changes
- Store nested or hierarchical data like reviews

### Step 3: Introduce NoSQL (MongoDB)
Explain how MongoDB’s document-based model addresses these limitations using flexible schemas, embedded documents, and scalability.

### Step 4: Discuss Trade-offs
No system is perfect. Identify disadvantages of MongoDB when compared to MySQL, especially in terms of consistency and transactions.

### Step 5: Present the Final Analysis
Organize your answer into clearly labeled sections as required.

---

## Section A: Limitations of RDBMS (4 marks – ~150 words)

Relational databases like MySQL use a fixed schema structure, which makes them unsuitable for product catalogs where products have different attributes. For example, laptops require fields such as RAM, processor, and storage, while shoes require size, color, and material. In an RDBMS, this would either require many nullable columns or multiple related tables, increasing complexity.

Frequent schema changes are another challenge. Adding a new product type often requires altering table structures, which can be time-consuming and risky in production environments. Such changes may also lead to downtime.

Additionally, storing customer reviews as nested data is inefficient in relational databases. Reviews must be stored in separate tables and joined using foreign keys, which increases query complexity and affects performance. Overall, rigid schemas and heavy use of joins make RDBMS less flexible for evolving product catalogs.

---

## Section B: NoSQL Benefits (4 marks – ~150 words)

MongoDB addresses these challenges through its flexible, document-oriented schema. Each product is stored as a JSON-like document, allowing different products to have different attributes without altering a global schema. This makes it easy to add new product types with unique fields.

MongoDB also supports embedded documents, enabling customer reviews to be stored directly within the product document. This reduces the need for joins and improves read performance when fetching product details along with reviews.

Furthermore, MongoDB is designed for horizontal scalability. It supports sharding, which allows data to be distributed across multiple servers. This makes MongoDB well-suited for handling large and growing product catalogs with high read and write traffic.

---

## Section C: Trade-offs (2 marks – ~100 words)

One disadvantage of using MongoDB instead of MySQL is weaker support for complex transactions. While MongoDB supports transactions, MySQL provides more mature and robust ACID compliance, which is important for financial or highly consistent systems.

Another drawback is data duplication. Embedded documents can lead to redundant data storage, increasing storage requirements and making updates more complex. Additionally, enforcing strict data integrity constraints is more difficult in MongoDB compared to relational databases.

