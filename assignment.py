import streamlit as st
import pandas as pd
import pymysql as myconn


class UserManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = myconn.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except myconn.MySQLError as e:
            st.error(f"Connection error: {e}")
            self.connection = None
            self.cursor = None

    def insert_user(self, full_name, gender, email, phone_number, hours_worked, professional, paid):
        if not self.connection:
            st.warning("No database connection.")
            return
        try:
            query = """
                INSERT INTO users (
                    full_name, gender, email, phone_number, hours_worked, professional, paid
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (full_name, gender, email, phone_number, hours_worked, professional, paid)
            self.cursor.execute(query, values)
            self.connection.commit()
            st.success("User data inserted successfully.")
        except myconn.MySQLError as e:
            st.error(f"Insert error: {e}")

    def get_user_by_name(self, full_name):
        if not self.connection:
            st.warning("No database connection.")
            return
        try:
            query = "SELECT * FROM users WHERE full_name = %s"
            self.cursor.execute(query, (full_name,))
            result = self.cursor.fetchall()
            return result
        except myconn.MySQLError as e:
            st.error(f"Fetch error: {e}")
            return []

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


def main():
    st.title("Worker Management System")

    db = UserManager(
        host="localhost",
        user="root",
        password="K@ten_Ky0kot$u",  
        database="workerrecords"   
    )
    db.connect()

    menu = st.sidebar.radio("Choose Action", ["Create", "Search"])

    if menu == "Create":
        st.header("Create New worker")

        with st.form("user_form"):
            full_name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            email = st.text_input("Email")
            phone_number = st.text_input("Phone Number")
            hours_worked = st.number_input("Hours Worked", min_value=0.0, step=0.5)
            professional = st.selectbox("Professional", ["Yes", "No"])
            paid = st.selectbox("Paid", ["65", "55"])
            submitted = st.form_submit_button("Submit")

            if submitted:
                db.insert_user(full_name, gender, email, phone_number, hours_worked, professional, paid)

    elif menu == "Search":
        st.header("🔍 Search worker")

        name_to_search = st.text_input("Enter full name to search")

        if st.button("Search"):
            trimmed_name = name_to_search.strip()
            if not trimmed_name:
                st.warning("Please enter a valid name.")
            else:
                results = db.get_user_by_name(trimmed_name)
            if results:
                
                df = pd.DataFrame(results, columns=[
                    "ID", "Full Name", "Gender", "Email", "Phone Number",
                    "Hours Worked", "Professional", "Paid"
                ])

                
                df["Hours Worked"] = pd.to_numeric(df["Hours Worked"], errors="coerce")
                df["Paid"] = pd.to_numeric(df["Paid"], errors="coerce")

                
                total_hours = df["Hours Worked"].sum()
                total_paid = (df["Hours Worked"] * df["Paid"]).sum()

                
                st.markdown("<h4 style='margin-top:20px;'>User Information</h4>", unsafe_allow_html=True)
                st.dataframe(df.style.set_properties(**{
                    'font-size': '18px',
                    'text-align': 'left'
                }), height=300)

                
                st.markdown(f"""
                    <div style='margin-top:20px; font-size:18px;'>
                        <strong>Total Hours Worked:</strong> {total_hours}<br>
                        <strong>Total Amount Paid:</strong> {total_paid:,.2f}Rs
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.info("No user found with that name.")

    db.close()

if __name__ == "__main__":
    main()