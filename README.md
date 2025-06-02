# 💰 Banking Management System (Python + MySQL)

A simple command-line banking system built in Python using MySQL. It supports user registration, login, balance inquiry, deposit, withdrawal, money transfers, and an admin panel for monitoring.

---

## 🚀 Features

### User Functions:
- 🔐 Register with phone number and PIN
- 🔓 Login with phone number and PIN
- 💼 Check current account balance
- 💸 Withdraw money
- 💰 Deposit money
- 🔄 Transfer money to another registered user

### Admin Panel:
- 👥 View all registered users
- 📄 View all transaction records
- 🔁 View all money transfers
- 🔎 View specific user transactions by phone number
- 🔍 View specific user's transfer history

---

## 🧱 Tech Stack

- **Python 3.x**
- **MySQL** (with `mysql-connector-python`)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/banking-system.git
cd banking-system
````

### 2. Install Required Python Package

```bash
pip install mysql-connector-python
```

### 3. Set Up MySQL Database

* Log in to MySQL:

  ```bash
  mysql -u root -p
  ```

* Create the database:

  ```sql
  CREATE DATABASE lol;
  ```

* Exit MySQL and run the script. Tables will be created automatically when the app starts.

### 4. Run the App

```bash
python your_script_name.py
```

> Replace `your_script_name.py` with your Python file name (e.g., `banking.py`)

---

## 🔑 Default Admin Credentials

* **Username:** `vicky`
* **PIN:** `456`

---

## 🧩 File Structure

```
banking-system/
├── your_script_name.py   # Replace with your Python file
└── README.md             # This file
```

---

## 📌 Notes

* Minimum balance of ₹100 must be maintained after withdrawal or transfer.
* All users get ₹500 initial balance upon registration.
* Phone number and username must be unique.

--
