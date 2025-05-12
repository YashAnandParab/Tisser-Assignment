# 📋 Worker Management Dashboard

A simple web-based Worker Management System built with Python, Streamlit, and MySQL. This app allows you to manage worker records, insert new data, and search existing records. It also calculates and displays the total hours worked and the total amount paid (hours_worked × paid) for a given worker.

📁 **Project Structure**

worker-management-dashboard/
├── Assignment.py # Main Streamlit app
├── Assignment.sql # SQL script to create the 'users' table
├── Worker Record Dashboard/ # Folder for Power BI dashboards or assets
└── README.md # Project documentation

✅ **MYSQL Features**:
- Add new worker records (name, gender, email, phone, hours, professional status, pay rate)
- Search for a worker by name (with auto-trim to fix spacing issues)
- View all matching records in a styled table
- Display total hours worked and total amount paid

📦 **Requirements**:
Install dependencies:
pip install streamlit pymysql pandas
    
Setup Instructions:
    git clone https://github.com/your-username/worker-management-dashboard.git
    cd worker-management-dashboard
    
2)Create the MySQL database using Assignment.sql:
    CREATE DATABASE workerrecords;
    USE workerrecords;
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(255),
        gender VARCHAR(10),
        email VARCHAR(255),
        phone_number VARCHAR(20),
        hours_worked FLOAT,
        professional VARCHAR(10),
        paid INT
    );

3) Update MySQL credentials in Assignment.py:
    db = UserManager(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="workerrecords"
    )

4)Run the Streamlit app:
streamlit run Assignment.py

If you have a Power BI dashboard, place it inside the Worker Record Dashboard folder and connect it to the same MySQL database.
