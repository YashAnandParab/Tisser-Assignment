📋 Worker Management Dashboard
A simple web-based Worker Management System built with Python, Streamlit, and MySQL. This app allows you to manage worker records including inserting new data and searching for existing records. It also calculates and displays total hours worked and the total payment for a given worker.

🗂 Project Structure
text
Copy
Edit
📁 worker-management-dashboard/
├── Assignment.py           # Main Streamlit app
├── Assignment.sql          # SQL script to create the 'users' table
├── Worker Record Dashboard # Folder for any dashboard assets (e.g., Power BI reports, images)
└── README.md               # Project documentation
⚙️ Features
✅ Add new worker details including name, gender, email, phone number, hours worked, and pay rate.

🔍 Search for a worker by name (trims input to avoid search errors).

📊 View all matching records in a table.

📈 Calculate and display:

Total hours worked

Total amount paid = hours_worked × paid

📦 Requirements
Install the following Python packages:

bash
Copy
Edit
pip install streamlit pymysql pandas
🛠 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/worker-management-dashboard.git
cd worker-management-dashboard
Create the MySQL database:

Use Assignment.sql to create the required table:

sql
Copy
Edit
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
Update your MySQL credentials in Assignment.py:

python
Copy
Edit
db = UserManager(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="workerrecords"
)
Run the app:

bash
Copy
Edit
streamlit run Assignment.py
