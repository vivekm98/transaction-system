Thanks for the updated code! Based on your current CLI banking application, here’s an updated and accurate `README.md` file you can include in your GitHub repository:

---

````markdown
# 🏦 Python CLI Banking System

This project is a command-line banking system built using Python and MySQL. It allows users to register, login, check balance, withdraw, deposit, and transfer funds to other users. The system ensures data is persisted securely using MySQL.

## 📦 Features

- User registration with input validation
- Login system using phone number and 4-digit PIN
- Balance inquiry
- Withdraw with minimum balance check
- Deposit functionality
- Money transfer between users
- Transaction history is stored in the database

## 🧰 Tech Stack

- **Language**: Python 3
- **Database**: MySQL
- **Libraries**: `mysql-connector-python`, `getpass`

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-banking-system.git
cd python-banking-system
````

### 2. Install Requirements

Install the required Python package:

```bash
pip install mysql-connector-python
```

### 3. Configure MySQL

Ensure you have a MySQL server running and update the credentials in the `__init__` method of the `Vip` class:

```python
self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",     # Change to your MySQL password
    database="python",   # Make sure this database exists
    auth_plugin="mysql_native_password"
)
```

> 💡 Create the `python` database if it doesn't exist:
>
> ```sql
> CREATE DATABASE python;
> ```

### 4. Run the Application

```bash
python your_file_name.py
```

> Replace `your_file_name.py` with the actual filename of your script.

## 📋 User Flow

* On startup, the user sees the main menu:

  ```
  1: Register
  2: Login
  3: Exit
  ```

* Once logged in, users can:

  * Check balance
  * Withdraw money (maintains a ₹100 minimum balance)
  * Deposit funds
  * Transfer money to other registered users

## 🗃️ Database Tables

* **user\_info**: Stores user data including username, phone number, PIN, and balance
* **info**: Stores user transaction logs (deposit/withdraw)
* **info2**: Stores money transfer logs

These tables are automatically created when the program runs for the first time.

## 🚧 Limitations

* No password encryption (use hashing for production)
* No input sanitation for SQL (vulnerable to injection)
* Console-based interface only
* No admin panel in current version

## 📄 License

This project is for learning purposes and is open-source. You are free to modify and use it.

---

> 💡 Tip: Make sure MySQL is running and the credentials are correctly configured before running the app.

```

---

```
