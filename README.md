# 🏦 VIP Banking System (CLI-Based)

This is a simple command-line based banking system built with Python and MySQL. It allows users to register, login, check balances, withdraw, deposit, and transfer money. An admin panel is also available to monitor user activity and transactions.

## 📌 Features

- User registration with validation
- Secure login using masked PIN entry (`getpass`)
- Balance check, withdraw, deposit, and transfer functionalities
- Admin access to view all users, transactions, and transfers
- Data persistence using MySQL

## 🛠️ Technologies Used

- Python 3
- MySQL
- `mysql-connector-python` for database interaction
- `getpass` for secure PIN input

## 📋 Requirements

- Python 3.x
- MySQL server running locally
- MySQL user with access to create databases and tables

Install the required Python package:

```bash
pip install mysql-connector-python
