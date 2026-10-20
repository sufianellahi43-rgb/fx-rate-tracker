import sqlite3

conn = sqlite3.connect("fx.db")
cursor = conn.cursor()

query = """
SELECT currency, MAX(rate), MIN(rate), AVG(rate) 
FROM rates
GROUP BY currency
"""
cursor.execute(query)
results = cursor.fetchall()

print(results)
