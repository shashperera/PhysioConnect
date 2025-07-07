#select all databases
# import pyodbc

# conn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=physiotherapy-db.c9ma26yckcjb.eu-north-1.rds.amazonaws.com;'
#     'UID=admin;'
#     'PWD=shashipraba12'
# )
# cursor = conn.cursor()
# cursor.execute("SELECT name FROM sys.databases")
# print(cursor.fetchall())
# conn.close()

# fetch and print your table data
import pyodbc

conn = pyodbc.connect(
     'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=physiotherapy-db.c9ma26yckcjb.eu-north-1.rds.amazonaws.com;'
        'DATABASE=physiotherapy-db;'

    'UID=admin;'
    'PWD=shashipraba12'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM exercises")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()