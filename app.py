# fetch and print your table data
import pyodbc

conn = pyodbc.connect(
     'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=physiotherapy-db.*****.eu-north-1.rds.amazonaws.com;'
        'DATABASE=physiotherapy-db;'

    'UID=admin;'
    'PWD=******'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM exercises")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
