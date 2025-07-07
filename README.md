# PhysioConnect
# How to Build a Simple Exercise Management App using AWS RDS, EC2, and Python

In this tutorial, you'll learn how to:
- Create an AWS RDS SQL Server instance
- Launch an EC2 instance and set up access
- Connect to RDS from EC2 using Python (`pyodbc`)
- Build a simple CLI app to add, list, and delete exercises

---

## 1. Setting Up AWS RDS (SQL Server)

**Step 1.1:** Go to the [AWS RDS Console](https://console.aws.amazon.com/rds/).

**Step 1.2:** Click **"Create database"**.

- **Engine type:** Microsoft SQL Server (Express is fine for demo)
- **Templates:** Free tier (if eligible)
- **DB Instance Identifier:** `physiotherapy-db`
- **Master username:** `admin`
- **Master password:** choose a secure password

**Step 1.3:** In "Connectivity", make sure to:
- Choose a VPC (default is fine)
- **Public access:** Yes (for testing; restrict in production)
- **VPC security group:** Create new or use existing

**Step 1.4:** Click **"Create database"** and wait for status to become **"Available"**.

**Step 1.5:** Note the **endpoint** (e.g., `physiotherapy-db.xxxxxxxx.eu-north-1.rds.amazonaws.com`).

---

## 2. Setting Up AWS EC2

**Step 2.1:** Go to the [AWS EC2 Console](https://console.aws.amazon.com/ec2/).

**Step 2.2:** Click **"Launch Instance"**.

- **AMI:** Ubuntu Server (20.04 or later recommended)
- **Instance type:** t2.micro (free tier)
- **Key pair:** Create/download for SSH
- **Network:** Same VPC as RDS
- **Security group:** Allow SSH (port 22) and **outbound** on port 1433 (SQL Server)

**Step 2.3:** Launch the instance and note its public IP.

---

## 3. Configure Security Groups

- In **RDS security group**: Add an **inbound rule** to allow traffic on port **1433** from the EC2 instance's private IP or its security group.
- In **EC2 security group**: SSH (22) from your IP.

---

## 4. Connect to EC2 and Install Dependencies

**Step 4.1:** SSH into your EC2 instance:

```bash
ssh -i path/to/key.pem ubuntu@<ec2-public-ip>
```

**Step 4.2:** Install Python, pip, and ODBC driver:

```bash
sudo apt-get update
sudo apt-get install -y python3-pip
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev
pip3 install pyodbc
```

---

## 5. Initialize the RDS Database

**Step 5.1:** If you haven't already created your exercises table, you can do it from Python.

---

## 6. Python Script: Exercise Manager

Create a file called `exercises_app.py`:

```python name="exercises_app.py"
import pyodbc

# RDS connection details
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=physiotherapy-db.xxxxxxxx.eu-north-1.rds.amazonaws.com;'  # Replace with your endpoint
    'DATABASE=physiotherapy-db;'
    'UID=admin;'
    'PWD=yourpassword'
)
cursor = conn.cursor()

# Create table if it doesn't exist
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
```

---

## 7. Run the Script

```bash
python3 exercises_app.py
```

You can now **add**, **list**, and **delete** exercises!

---

## 8. Security Best Practices (For Production)

- Never hard-code credentials. Use environment variables or AWS Secrets Manager.
- Restrict RDS access to EC2's security group, not 0.0.0.0/0.
- Rotate passwords regularly.

---

## 9. Troubleshooting

- If you get "Login failed for user", double-check username, password, and database name.
- If "Cannot connect", check security group rules and VPC/subnet settings.
- Use SSMS, DBeaver, or Azure Data Studio to inspect your database if needed.

---

## 10. Example: Adding a Leg Stretch Exercise

When prompted, enter:

- **Exercise name:** Hamstring Stretch
- **Description:** Sit on the floor, extend legs, reach for toes, hold for 20 seconds.

---

**Congratulations!**  
You now have a working Python CLI app using AWS RDS and EC2.

---

*If you found this useful, follow me for more cloud and Python tutorials!*