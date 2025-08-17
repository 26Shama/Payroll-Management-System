import streamlit as st
import mysql.connector
import pandas as pd 

# Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shama@121",
        database="shamadb"
    )

# Function to execute query and return results
def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    return pd.DataFrame(data, columns=columns)

# Function to execute an update/insert query
def run_action(query, values):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    conn.close()

# Streamlit App
st.title("Payroll Management System Admin Panel")

# Sidebar Navigation
pages = ["Employee", "Department", "Payroll", "Leave", "Dependent", "Bank_Details", "Salary"]
page = st.sidebar.selectbox("Choose a page", pages)

# Employee CRUD Operations
if page == "Employee":
    st.header("Employee")
    action = st.selectbox("Choose action", ["View", "Add", "Edit", "Delete"])

    if action == "View":
        df = run_query("SELECT * FROM Employee")
        st.write(df)

    elif action == "Add":
        with st.form("Add Employee"):
            eid = st.number_input("EID", min_value=1, step=1)
            fname = st.text_input("First Name")
            lname = st.text_input("Last Name")
            phno = st.number_input("Phone Number", min_value=1, step=1)
            accno = st.number_input("Account Number", min_value=1, step=1)
            submitted = st.form_submit_button("Add Employee")
            if submitted:
                run_action("INSERT INTO Employee (EID, FName, LName, PhNo, AccNo) VALUES (%s, %s, %s, %s, %s)", 
                           (eid, fname, lname, phno, accno))
                st.success("Employee added successfully")

    elif action == "Edit":
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}
        employee_name = st.selectbox("Choose an employee to edit", list(employee_dict.keys()))
        eid = employee_dict[employee_name]
        employee = run_query(f"SELECT * FROM Employee WHERE EID = {eid}").iloc[0]

        with st.form("Edit Employee"):
            fname = st.text_input("First Name", value=employee['FName'])
            lname = st.text_input("Last Name", value=employee['LName'])
            phno = st.number_input("Phone Number", value=employee['PhNo'], min_value=1, step=1)
            accno = st.number_input("Account Number", value=employee['AccNo'], min_value=1, step=1)
            submitted = st.form_submit_button("Update Employee")
            if submitted:
                run_action("UPDATE Employee SET FName = %s, LName = %s, PhNo = %s, AccNo = %s WHERE EID = %s", 
                           (fname, lname, phno, accno, eid))
                st.success("Employee updated successfully")

    elif action == "Delete":
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}
        employee_name = st.selectbox("Choose an employee to delete", list(employee_dict.keys()))
        eid = employee_dict[employee_name]

        if st.button("Delete Employee"):
            run_action("DELETE FROM Employee WHERE EID = %s", (eid,))
            st.success("Employee deleted successfully")

# Department CRUD Operations
elif page == "Department":
    st.header("Department")
    action = st.selectbox("Choose action", ["View", "Add", "Edit", "Delete"])

    if action == "View":
        df = run_query("SELECT * FROM Department")
        st.write(df)

    elif action == "Add":
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}
        with st.form("Add Department"):
            did = st.number_input("DID", min_value=1, step=1)
            dname = st.text_input("Department Name")
            salary_range = st.text_input("Salary Range")
            employee_name = st.selectbox("Employee", list(employee_dict.keys()))
            submitted = st.form_submit_button("Add Department")
            if submitted:
                eid = employee_dict[employee_name]
                run_action("INSERT INTO Department (DID, DName, Salary_Range, EID) VALUES (%s, %s, %s, %s)", 
                           (did, dname, salary_range, eid))
                st.success("Department added successfully")

    elif action == "Edit":
        departments = run_query("SELECT DID, DName FROM Department")
        department_dict = {row['DName']: row['DID'] for index, row in departments.iterrows()}
        department_name = st.selectbox("Choose a department to edit", list(department_dict.keys()))
        did = department_dict[department_name]
        department = run_query(f"SELECT * FROM Department WHERE DID = {did}").iloc[0]
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}

        with st.form("Edit Department"):
            dname = st.text_input("Department Name", value=department['DName'])
            salary_range = st.text_input("Salary Range", value=department['Salary_Range'])
            employee_name = st.selectbox("Employee", list(employee_dict.keys()))
            submitted = st.form_submit_button("Update Department")
            if submitted:
                eid = employee_dict[employee_name]
                run_action("UPDATE Department SET DName = %s, Salary_Range = %s, EID = %s WHERE DID = %s", 
                           (dname, salary_range, eid, did))
                st.success("Department updated successfully")

    elif action == "Delete":
        departments = run_query("SELECT DID, DName FROM Department")
        department_dict = {row['DName']: row['DID'] for index, row in departments.iterrows()}
        department_name = st.selectbox("Choose a department to delete", list(department_dict.keys()))
        did = department_dict[department_name]

        if st.button("Delete Department"):
            run_action("DELETE FROM Department WHERE DID = %s", (did,))
            st.success("Department deleted successfully")

# Add similar CRUD operations for Payroll, Leave, Dependent, Bank_Details, and Salary
# Below are the steps for Payroll table. Implement similarly for the rest.

# Payroll CRUD Operations
elif page == "Payroll":
    st.header("Payroll")
    action = st.selectbox("Choose action", ["View", "Add", "Edit", "Delete"])

    if action == "View":
        df = run_query("SELECT * FROM Payroll")
        st.write(df)

    elif action == "Add":
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        departments = run_query("SELECT DID, DName FROM Department")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}
        department_dict = {row['DName']: row['DID'] for index, row in departments.iterrows()}
        with st.form("Add Payroll"):
            pid = st.number_input("PID", min_value=1, step=1)
            date = st.date_input("Date")
            total_amount = st.number_input("Total Amount", min_value=0.0, step=0.01)
            tax = st.number_input("Tax", min_value=0.0, step=0.01)
            employee_name = st.selectbox("Employee", list(employee_dict.keys()))
            department_name = st.selectbox("Department", list(department_dict.keys()))
            lid = st.number_input("Leave ID", min_value=1, step=1)
            sid = st.number_input("Salary ID", min_value=1, step=1)
            submitted = st.form_submit_button("Add Payroll")
            if submitted:
                eid = employee_dict[employee_name]
                did = department_dict[department_name]
                run_action("INSERT INTO Payroll (PID, Date, Total_Amount, Tax, EID, DID, LID, SID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (pid, date, total_amount, tax, eid, did, lid, sid))
                st.success("Payroll added successfully")

    elif action == "Edit":
        payrolls = run_query("SELECT PID FROM Payroll")
        payroll_dict = {f"{row['PID']}": row['PID'] for index, row in payrolls.iterrows()}
        pid = st.selectbox("Choose a payroll to edit", list(payroll_dict.keys()))
        payroll = run_query(f"SELECT * FROM Payroll WHERE PID = {pid}").iloc[0]
        employees = run_query("SELECT EID, FName, LName FROM Employee")
        departments = run_query("SELECT DID, DName FROM Department")
        employee_dict = {f"{row['FName']} {row['LName']}": row['EID'] for index, row in employees.iterrows()}
        department_dict = {row['DName']: row['DID'] for index, row in departments.iterrows()}

        with st.form("Edit Payroll"):
            date = st.date_input("Date", value=payroll['Date'])
            total_amount = st.number_input("Total Amount", value=payroll['Total_Amount'], min_value=0.0, step=0.01)
            tax = st.number_input("Tax", value=payroll['Tax'], min_value=0.0, step=0.01)
            employee_name = st.selectbox("Employee", list(employee_dict.keys()))
            department_name = st.selectbox("Department", list(department_dict.keys()))
            lid = st.number_input("Leave ID", value=payroll['LID'], min_value=1, step=1)
            sid = st.number_input("Salary ID", value=payroll['SID'], min_value=1, step=1)
            submitted = st.form_submit_button("Update Payroll")
            if submitted:
                eid = employee_dict[employee_name]
                did = department_dict[department_name]
                run_action("UPDATE Payroll SET Date = %s, Total_Amount = %s, Tax = %s, EID = %s, DID = %s, LID = %s, SID = %s WHERE PID = %s", 
                           (date, total_amount, tax, eid, did, lid, sid, pid))
                st.success("Payroll updated successfully")

    elif action == "Delete":
        payrolls = run_query("SELECT PID FROM Payroll")
        payroll_dict = {f"{row['PID']}": row['PID'] for index, row in payrolls.iterrows()}
        pid = st.selectbox("Choose a payroll to delete", list(payroll_dict.keys()))

        if st.button("Delete Payroll"):
            run_action("DELETE FROM Payroll WHERE PID = %s", (pid,))
            st.success("Payroll deleted successfully")

# Implement similar CRUD operations for Leave, Dependent, Bank_Details, and Salary
