import requests
import sqlite3
response=requests.get('https://api.frankfurter.app/2026-09-08..2026-10-08?from=GBP&to=EUR,USD,TRY')                      
data=response.json()

conn = sqlite3.connect("fx.db") 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rates (
    date TEXT,
    currency TEXT ,
    rate REAL
)   
""")
for date, day_rates in data['rates'].items():
    for currency, rate in day_rates.items():
        cursor.execute("INSERT INTO rates VALUES (?, ?, ?)", (date, currency, rate))

conn.commit()
conn.close()

print('Saved')
