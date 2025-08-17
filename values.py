import sqlite3

def insert_initial_values():
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Insert statements for Employee table
    employees = [
        (1, 'John', 'Doe', 123),
        (2, 'Jane', 'Smith', 456),
        (3, 'Jim', 'Beam', 122),
        (4, 'Jack', 'Daniels', 111),
        (5, 'Johnny', 'Walker', 121),
        (6, 'Emma', 'Brown', 131),
        (7, 'Olivia', 'Davis', 567),
        (8, 'Ava', 'Martinez', 789),
        (9, 'Isabella', 'Garcia', 876),
        (10, 'Sophia', 'Rodriguez', 235)
    ]

    cursor.executemany("INSERT INTO Employee (EID, FName, LName, PhNo) VALUES (?, ?, ?, ?)", employees)

    # Insert statements for Department table
    departments = [
        (1, 'HR', '50000-70000', 1),
        (2, 'IT', '60000-80000', 2),
        (3, 'Finance', '55000-75000', 3),
        (4, 'Marketing', '52000-72000', 4),
        (5, 'Operations', '51000-71000', 5),
        (6, 'Sales', '53000-73000', 6),
        (7, 'R&D', '58000-78000', 7),
        (8, 'Support', '50000-68000', 8),
        (9, 'Logistics', '49000-69000', 9),
        (10, 'Administration', '48000-68000', 10)
    ]

    cursor.executemany("INSERT INTO Department (DID, DName, Salary_range, EID) VALUES (?, ?, ?, ?)", departments)

    # Insert statements for Leave1 table
    leaves = [
        (1, '2024-01-01', 'Sick Leave', 1),
        (2, '2024-02-01', 'Personal Leave', 2),
        (3, '2024-03-01', 'Vacation', 3),
        (4, '2024-04-01', 'Maternity Leave', 4),
        (5, '2024-05-01', 'Paternity Leave', 5),
        (6, '2024-06-01', 'Sick Leave', 6),
        (7, '2024-07-01', 'Personal Leave', 7),
        (8, '2024-08-01', 'Vacation', 8),
        (9, '2024-09-01', 'Maternity Leave', 9),
        (10, '2024-10-01', 'Paternity Leave', 10)
    ]

    cursor.executemany("INSERT INTO Leave1 (LID, Date, Reason, EID) VALUES (?, ?, ?, ?)", leaves)

    # Insert statements for Salary table
    salaries = [
        (1, 5000, 500, 1, 1),
        (2, 6000, 600, 2, 2),
        (3, 7000, 700, 3, 3),
        (4, 8000, 800, 4, 4),
        (5, 9000, 900, 5, 5),
        (6, 10000, 1000, 6, 6),
        (7, 11000, 1100, 7, 7),
        (8, 12000, 1200, 8, 8),
        (9, 13000, 1300, 9, 9),
        (10, 14000, 1400, 10, 10)
    ]

    cursor.executemany("INSERT INTO Salary (SID, Amount, Bonus, EID, DID) VALUES (?, ?, ?, ?, ?)", salaries)

    # Insert statements for Payroll table
    payroll = [
        (1, '2024-01-01', 5000, 500, 1, 1, 1, 1),
        (2, '2024-02-01', 6000, 600, 2, 2, 2, 2),
        (3, '2024-03-01', 7000, 700, 3, 3, 3, 3),
        (4, '2024-04-01', 8000, 800, 4, 4, 4, 4),
        (5, '2024-05-01', 9000, 900, 5, 5, 5, 5),
        (6, '2024-06-01', 10000, 1000, 6, 6, 6, 6),
        (7, '2024-07-01', 11000, 1100, 7, 7, 7, 7),
        (8, '2024-08-01', 12000, 1200, 8, 8, 8, 8),
        (9, '2024-09-01', 13000, 1300, 9, 9, 9, 9),
        (10, '2024-10-01', 14000, 1400, 10, 10, 10, 10)
    ]
    cursor.executemany("INSERT INTO Payroll (PID, Date, Total_Amount, Tax, EID, DID, LID, SID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", payroll)

    # Insert statements for Bank_Details table
    bank_details = [
        (1,'Bank A', '123 Main St', '001', '111111', 1),
        (2,'Bank B', '456 Elm St', '002', '222222', 2),
        (3,'Bank C', '789 Oak St', '003', '333333', 3),
        (4,'Bank D', '101 Pine St', '004', '444444', 4),
        (5,'Bank E', '202 Maple St', '005', '555555', 5),
        (6,'Bank F', '303 Cedar St', '006', '666666', 6),
        (7,'Bank G', '404 Birch St', '007', '777777', 7),
        (8,'Bank H', '505 Spruce St', '008', '888888', 8),
        (9,'Bank I', '606 Fir St', '009', '999999', 9),
        (10,'Bank J', '707 Redwood St', '010', '101010', 10)
    ]

    cursor.executemany("INSERT INTO Bank_Details (BID,BName, Address, IFSC_Code, AccountNo, EID) VALUES (?,?, ?, ?, ?, ?)", bank_details)

    # Insert statements for Dependent table
    dependents = [
        ('Emily', '2015-05-15', 9, 'Daughter', 1),
        ('Sophia', '2017-08-20', 7, 'Daughter', 2),
        ('Michael', '2010-10-10', 14, 'Son', 3),
        ('Daniel', '2012-12-25', 12, 'Son', 4),
        ('Emma', '2019-01-01', 5, 'Daughter', 5),
        ('Oliver', '2016-06-15', 8, 'Son', 6),
        ('Lucas', '2014-04-20', 10, 'Son', 7),
        ('Ava', '2018-03-15', 6, 'Daughter', 8),
        ('Mia', '2020-02-25', 4, 'Daughter', 9),
        ('Sophia', '2019-01-15', 5, 'Daughter', 10)
    ]

    cursor.executemany("INSERT INTO Dependent (Name, DOB, Age, Relationship, EID) VALUES (?, ?, ?, ?, ?)", dependents)

    # Insert statements for Login table
    logins = [
        ('admin', 'admin'),
        ('user1', 'password456'),
        ('user2', 'password789'),
        ('shama','shama@121')
    ]

    cursor.executemany("INSERT INTO Login (Username, Password) VALUES (?, ?)", logins)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to insert initial values
insert_initial_values()