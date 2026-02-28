import sqlite3

# Step 1: Connect to database (or create if doesn't exist)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Step 2: Create Students table
table = """
CREATE TABLE IF NOT EXISTS Students (
    name TEXT,
    class TEXT,
    marks INTEGER,
    company TEXT
)
"""
cursor.execute(table)

# Step 3: Insert records
cursor.execute("INSERT INTO Students VALUES ('Sijo', 'BTech', 75, 'JSW')")
cursor.execute("INSERT INTO Students VALUES ('Lijo', 'MTech', 69, 'TCS')")
cursor.execute("INSERT INTO Students VALUES ('Rijo', 'BSc', 79, 'WIPRO')")
cursor.execute("INSERT INTO Students VALUES ('Sibin', 'MSc', 89, 'INFOSYS')")
cursor.execute("INSERT INTO Students VALUES ('Dilsha', 'MCom', 99, 'Cyient')")

print("✅ Inserted records successfully.")

# Step 4: Retrieve and display data
df = cursor.execute("SELECT * FROM Students")
print("\n📋 Retrieved records:")
for row in df:
    print(row)

# Step 5: Save and close
conn.commit()
conn.close()
