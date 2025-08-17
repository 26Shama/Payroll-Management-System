import sqlite3

# Establish connection and cursor
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Define SQL statements for creating tables with primary keys and foreign keys
create_employee_table = """
CREATE TABLE IF NOT EXISTS Employee (
    EID INTEGER PRIMARY KEY,
    FName TEXT,
    LName TEXT,
    PhNo INTEGER
);
"""

create_department_table = """
CREATE TABLE IF NOT EXISTS Department (
    DID INTEGER PRIMARY KEY,
    DName TEXT,
    Salary_range TEXT,
    EID INTEGER,
    FOREIGN KEY(EID) REFERENCES Employee(EID)
);
"""

create_leave_table = """
CREATE TABLE IF NOT EXISTS Leave1 (
    LID INTEGER PRIMARY KEY,
    Date DATE,
    Reason TEXT,
    EID INTEGER,
    FOREIGN KEY(EID) REFERENCES Employee(EID)
);
"""

create_salary_table = """
CREATE TABLE IF NOT EXISTS Salary (
    SID INTEGER PRIMARY KEY,
    Amount DECIMAL(10, 2),
    Bonus DECIMAL(10, 2),
    EID INTEGER,
    DID INTEGER,
    FOREIGN KEY (EID) REFERENCES Employee(EID),
    FOREIGN KEY (DID) REFERENCES Department(DID)
);
"""

create_bank_details_table = """
CREATE TABLE IF NOT EXISTS Bank_Details (
    BID INTEGER PRIMARY KEY,
    BName TEXT,
    Address TEXT,
    IFSC_Code TEXT,
    AccountNo TEXT,
    EID INTEGER,
    FOREIGN KEY (EID) REFERENCES Employee(EID)
);
"""

create_payroll_table = """
CREATE TABLE IF NOT EXISTS Payroll (
    PID INTEGER PRIMARY KEY,
    Date DATE,
    Total_Amount DECIMAL(10, 2),
    Tax DECIMAL(10, 2),
    EID INTEGER,
    DID INTEGER,
    LID INTEGER,
    SID INTEGER,
    FOREIGN KEY (EID) REFERENCES Employee(EID),
    FOREIGN KEY (DID) REFERENCES Department(DID),
    FOREIGN KEY (LID) REFERENCES Leave1(LID),
    FOREIGN KEY (SID) REFERENCES Salary(SID)
);
"""

create_dependent_table = """
CREATE TABLE IF NOT EXISTS Dependent (
    DepID INTEGER PRIMARY KEY,
    Name TEXT,
    DOB DATE,
    Age INTEGER,
    Relationship TEXT,
    EID INTEGER,
    FOREIGN KEY (EID) REFERENCES Employee(EID)
);
"""

create_login_table = """
CREATE TABLE IF NOT EXISTS Login (
    Username TEXT PRIMARY KEY,
    Password TEXT
);
"""

# Execute table creation queries
cursor.execute(create_employee_table)
cursor.execute(create_department_table)
cursor.execute(create_leave_table)
cursor.execute(create_salary_table)
cursor.execute(create_bank_details_table)
cursor.execute(create_payroll_table)
cursor.execute(create_dependent_table)
cursor.execute(create_login_table)

# Commit changes and close connection
conn.commit()
conn.close()