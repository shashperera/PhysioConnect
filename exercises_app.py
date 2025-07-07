import pyodbc

# AWS RDS details
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=physiotherapy-db.c9ma26yckcjb.eu-north-1.rds.amazonaws.com;'
    'DATABASE=physiotherapy-db;'
    'UID=admin;'
    'PWD=shashipraba12'
)
cursor = conn.cursor()

# Create table
cursor.execute("""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='exercises' AND xtype='U')
CREATE TABLE exercises (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100),
    description NVARCHAR(255)
)
""")
conn.commit()

def add_exercise():
    name = input("Exercise name: ")
    description = input("Description: ")
    cursor.execute("INSERT INTO exercises (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    print("Exercise added!\n")

def list_exercises():
    cursor.execute("SELECT id, name, description FROM exercises")
    rows = cursor.fetchall()
    print("\n--- Exercises ---")
    for row in rows:
        print(f"{row.id}: {row.name} - {row.description}")
    print()

def delete_exercise():
    ex_id = input("Enter exercise ID to delete: ")
    cursor.execute("DELETE FROM exercises WHERE id = ?", (ex_id,))
    conn.commit()
    print("Exercise deleted!\n")

def main():
    while True:
        print("1. Add Exercise")
        print("2. List Exercises")
        print("3. Delete Exercise")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_exercise()
        elif choice == '2':
            list_exercises()
        elif choice == '3':
            delete_exercise()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
    conn.close()