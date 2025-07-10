import pyodbc

def get_db_connection():
    """
    Establish and return a connection to the AWS RDS SQL Server database.
    """
    connection_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=physiotherapy-db.*****.eu-north-1.rds.amazonaws.com;'
        'DATABASE=physiotherapy-db;'
        'UID=admin;'
        'PWD=******'
    )
    return pyodbc.connect(connection_str)
