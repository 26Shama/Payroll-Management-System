# 💼 Payroll Management System 

The **Payroll Management System** is a mini-project built using **Python (Streamlit)** and **SQLite**.  
It automates employee payroll processes like salary calculation, leave tracking, department management, and report generation.This system reduces manual effort, prevents errors, and improves efficiency in managing payroll data.

---

## 🎯 Objective
The goal of this project is to build a **database-driven payroll management system** where:
- 👤 Employees can be added, updated, viewed, and removed.  
- 🏢 Departments and salary ranges are managed efficiently.  
- 📅 Employees can apply for and track leaves.  
- 💰 Payroll is auto-calculated with tax and bonus handling.  
- 🏦 Salary is linked with employee bank details for disbursement.  
- 📊 HR/Admin can generate reports and ensure compliance.  

---

## ✨ Features
- 🔐 **Login Authentication** for secure access.  
- 👨‍💼 **Employee Management** (CRUD operations).  
- 🏢 **Department Management** with salary ranges.  
- 📅 **Leave Management** (apply, view, track).  
- 👨‍👩‍👧 **Dependent Management** for employee families.  
- 💰 **Payroll Calculation** with tax & bonus.  
- 🏦 **Bank Details Integration** for direct salary transfer.  
- 📊 **Comprehensive Reports** for HR/management.  
- 🌐 **Streamlit-based Interactive Web UI**.  

---

## 🛠️ Tech Stack
| Layer       | Technology         | Purpose |
|-------------|-------------------|---------|
| Frontend    | Streamlit (Python)| User Interface |
| Backend     | Python + SQLite   | Business Logic & DB |
| Database    | SQLite (`company.db`) | Stores employees, payroll, departments, etc. |
| Libraries   | Pandas, SQLite3   | Data handling & DB operations |

---

## 📂 Project Structure  

company.db → SQLite database  
database.py → Database schema & setup  
values.py → Insert initial values  
Payrole.py → Main Streamlit app  
pay_rollmanagement.py → Extra payroll features  
first.py → Supporting scripts  
style.css → Custom styling  
image.jpg → Logo/Images  
README.md → Project documentation  

---

## 🚀 Installation & Setup  

1. **Clone the Repository**
```bash
git clone https://github.com/YourUsername/Payroll-Management-System.git
cd Payroll-Management-System
```

2.**Install Dependencies**
```bash
pip install streamlit pandas mysql-connector-python
```

3.**Initialize the Database**
```bash
python database.py
python values.py
```
4.**Run the Application**
```bash
streamlit run Payrole.py
```
---

## 📸 Screenshots

**🏠 Home Dashboard**

<img width="1742" height="880" alt="image" src="https://github.com/user-attachments/assets/846fecb1-96c5-4267-8fad-ef3cf6f49039" />



