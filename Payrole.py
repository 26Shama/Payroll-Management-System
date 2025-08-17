import streamlit as st
import sqlite3
import pandas as pd

# Function to fetch data from a table
def fetch_data(query):
    conn = sqlite3.connect('company.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Function to execute an SQL query
def execute_query(query, params=()):
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Function to check login credentials
def check_login(username, password):
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Login WHERE Username=? AND Password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Streamlit app
st.title("Payroll Management System")

# Login functionality
if not st.session_state.logged_in:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        user = check_login(username, password)
        if user:
            st.session_state.logged_in = True
            st.sidebar.success("Login successful!")
        else:
            st.sidebar.error("Invalid username or password")
else:
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    pages = ["Employees", "Departments", "Leaves","Payroll", "Salaries", "Bank Details", "Dependents"]
    page = st.sidebar.radio("Go to", pages)

    # Display data and options for Employees
    if page == "Employees":
        st.header("Employees")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("SELECT * FROM Employee")
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                eid = st.text_input("EID")
                fname = st.text_input("First Name")
                lname = st.text_input("Last Name")
                phno = st.text_input("Phone Number")
              
        
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Employee (EID, FName, LName, PhNo) VALUES (?, ?, ?, ?)"
                    execute_query(query, (eid, fname, lname, phno))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                eid = st.text_input("EID")
                fname = st.text_input("First Name")
                lname = st.text_input("Last Name")
                phno = st.text_input("Phone Number")
                
                if st.form_submit_button("Update"):
                    query = "UPDATE Employee SET FName=?, LName=?, PhNo=? WHERE EID=?"
                    execute_query(query, (fname, lname, phno, eid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                eid = st.text_input("EID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Employee WHERE EID=?"
                    execute_query(query, (eid,))
                    st.success("Record deleted successfully")

    # Display data and options for Departments
    elif page == "Departments":
        st.header("Departments")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("""
                SELECT Department.*, Employee.FName, Employee.LName
                FROM Department
                LEFT JOIN Employee ON Department.EID = Employee.EID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                did = st.text_input("DID")
                dname = st.text_input("Department Name")
                salary_range = st.text_input("Salary Range")
                eid = st.text_input("EID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Department (DID, DName, Salary_range, EID) VALUES (?, ?, ?, ?)"
                    execute_query(query, (did, dname, salary_range, eid))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                did = st.text_input("DID")
                dname = st.text_input("Department Name")
                salary_range = st.text_input("Salary Range")
                eid = st.text_input("EID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Department SET DName=?, Salary_range=?, EID=? WHERE DID=?"
                    execute_query(query, (dname, salary_range, eid, did))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                did = st.text_input("DID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Department WHERE DID=?"
                    execute_query(query, (did,))
                    st.success("Record deleted successfully")

    # Display data and options for Leaves
    elif page == "Leaves":
        st.header("Leaves")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("""
                SELECT Leave1.*, Employee.FName, Employee.LName
                FROM Leave1
                LEFT JOIN Employee ON Leave1.EID = Employee.EID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                lid = st.text_input("LID")
                date = st.date_input("Date")
                reason = st.text_input("Reason")
                eid = st.text_input("EID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Leave1 (LID, Date, Reason, EID) VALUES (?, ?, ?, ?)"
                    execute_query(query, (lid, date, reason, eid))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                lid = st.text_input("LID")
                date = st.date_input("Date")
                reason = st.text_input("Reason")
                eid = st.text_input("EID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Leave1 SET Date=?, Reason=?, EID=? WHERE LID=?"
                    execute_query(query, (date, reason, eid, lid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                lid = st.text_input("LID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Leave1 WHERE LID=?"
                    execute_query(query, (lid,))
                    st.success("Record deleted successfully")
    elif page=="Payroll":           
        st.header("Payroll")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
  
        if action == "View":
            df = fetch_data("""
                SELECT Payroll.*, Employee.FName, Employee.LName
                FROM Payroll
                LEFT JOIN Employee ON Payroll.EID = Employee.EID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                pid = st.text_input("PID")
                date = st.text_input("Date")
                total_amount = st.text_input("Total Amount")
                tax = st.text_input("Tax")
                eid = st.text_input("EID")
                did = st.text_input("DID")
                lid = st.text_input("LID")
                sid = st.text_input("SID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Payroll (PID, Date, Total_Amount, Tax, EID, DID, LID, SID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    execute_query(query, (pid, date, total_amount, tax, eid, did, lid, sid))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                pid = st.text_input("PID")
                date = st.text_input("Date")
                total_amount = st.text_input("Total Amount")
                tax = st.text_input("Tax")
                eid = st.text_input("EID")
                did = st.text_input("DID")
                lid = st.text_input("LID")
                sid = st.text_input("SID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Payroll SET Date=?, Total_Amount=?, Tax=?, EID=?, DID=?, LID=?, SID=? WHERE PID=?"
                    execute_query(query, (date, total_amount, tax, eid, did, lid, sid, pid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                pid = st.text_input("PID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Payroll WHERE PID=?"
                    execute_query(query, (pid,))
                    st.success("Record deleted successfully")
    # Display data and options for Salaries
    elif page == "Salaries":
        st.header("Salaries")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("""
                SELECT Salary.*, Employee.FName, Employee.LName, Department.DName
                FROM Salary
                LEFT JOIN Employee ON Salary.EID = Employee.EID
                LEFT JOIN Department ON Salary.DID = Department.DID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                sid = st.text_input("SID")
                amount = st.text_input("Amount")
                bonus = st.text_input("Bonus")
                eid = st.text_input("EID")
                did = st.text_input("DID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Salary (SID, Amount, Bonus, EID, DID) VALUES (?, ?, ?, ?, ?)"
                    execute_query(query, (sid, amount, bonus, eid, did))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                sid = st.text_input("SID")
                amount = st.text_input("Amount")
                bonus = st.text_input("Bonus")
                eid = st.text_input("EID")
                did = st.text_input("DID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Salary SET Amount=?, Bonus=?, EID=?, DID=? WHERE SID=?"
                    execute_query(query, (amount, bonus, eid, did, sid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                sid = st.text_input("SID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Salary WHERE SID=?"
                    execute_query(query, (sid,))
                    st.success("Record deleted successfully")

    # Display data and options for Bank Details
    elif page == "Bank Details":
        st.header("Bank Details")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("""
                SELECT Bank_Details.*, Employee.FName, Employee.LName
                FROM Bank_Details
                LEFT JOIN Employee ON Bank_Details.EID = Employee.EID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                bankid = st.text_input("BID")
                bname = st.text_input("Bank Name")
                address = st.text_input("Address")
                ifsc = st.text_input("IFSC Code")
                account_no = st.text_input("Account Number")
                eid = st.text_input("EID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Bank_Details (BID, BName, Address, IFSC_Code, AccountNo, EID) VALUES (?, ?, ?, ?, ?, ?)"
                    execute_query(query, (bankid, bname, address, ifsc, account_no, eid))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                bankid = st.text_input("BID")
                bname = st.text_input("Bank Name")
                address = st.text_input("Address")
                ifsc = st.text_input("IFSC Code")
                account_no = st.text_input("Account Number")
                eid = st.text_input("EID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Bank_Details SET BName=?, Address=?, IFSC_Code=?, AccountNo=?, EID=? WHERE BID=?"
                    execute_query(query, (bname, address, ifsc, account_no, eid,bankid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                bankid = st.text_input("BID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Bank_Details WHERE BID=?"
                    execute_query(query, (bankid,))
                    st.success("Record deleted successfully")

    # Display data and options for Dependents
    elif page == "Dependents":
        st.header("Dependents")
        action = st.selectbox("Action", ["View", "Insert", "Update", "Delete"])
        
        if action == "View":
            df = fetch_data("""
                SELECT Dependent.*, Employee.FName, Employee.LName
                FROM Dependent
                LEFT JOIN Employee ON Dependent.EID = Employee.EID
            """)
            st.dataframe(df)

        elif action == "Insert":
            with st.form("insert_form"):
                depid = st.text_input("DepID")
                name = st.text_input("Name")
                dob = st.date_input("Date of Birth")
                age = st.text_input("Age")
                relationship = st.text_input("Relationship")
                eid = st.text_input("EID")
                if st.form_submit_button("Insert"):
                    query = "INSERT INTO Dependent (DepID, Name, DOB, Age, Relationship, EID) VALUES (?, ?, ?, ?, ?, ?)"
                    execute_query(query, (depid, name, dob, age, relationship, eid))
                    st.success("Record inserted successfully")

        elif action == "Update":
            with st.form("update_form"):
                depid = st.text_input("DepID")
                name = st.text_input("Name")
                dob = st.date_input("Date of Birth")
                age = st.text_input("Age")
                relationship = st.text_input("Relationship")
                eid = st.text_input("EID")
                if st.form_submit_button("Update"):
                    query = "UPDATE Dependent SET Name=?, DOB=?, Age=?, Relationship=?, EID=? WHERE DepID=?"
                    execute_query(query, (name, dob, age, relationship, eid, depid))
                    st.success("Record updated successfully")

        elif action == "Delete":
            with st.form("delete_form"):
                depid = st.text_input("DepID")
                if st.form_submit_button("Delete"):
                    query = "DELETE FROM Dependent WHERE DepID=?"
                    execute_query(query, (depid,))
                    st.success("Record deleted successfully")

    # Logout functionality
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.sidebar.success("Logged out successfully")
