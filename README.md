# Python Memory Test – Django Odd/Even API

This project is a simple Django-based API created while learning Python fundamentals and Django basics.  
It demonstrates how to:

- Write pure Python logic
- Convert Python logic into a Django view
- Expose the result as a JSON API endpoint

Currently, the API separates **odd and even numbers** from a list and returns both the values and their counts.

---

## 🚀 Features

- Pure Python function to classify odd and even numbers
- Django view to expose results as JSON
- Clean project and app structure
- Beginner-friendly setup

---

## 🛠 Tech Stack

- Python 3.14
- Django 5+
- SQLite (default Django database)
- VS Code

---

## ✅ Setup Instructions

### 1. Clone the repository

2. Create a virtual environment

`python -m venv venv`
`venv\Scripts\activate`   # Windows


3. Install Django

`pip install django`


4. Run migrations

`python manage.py migrate`

5. Start the Django server

`python manage.py runserver`

---
## 📁 Project Structure

mysite/
├─ manage.py
├─ db.sqlite3
├─ mysite/
│ ├─ settings.py
│ ├─ urls.py
│ ├─ asgi.py
│ └─ wsgi.py
└─ numapp/
├─ views.py
├─ urls.py
├─ models.py
├─ migrations/
└─ apps.py

🌐 API Endpoint

`http://127.0.0.1:8000/odd-even/`


## ✅ Sample JSON Response
`{
  "odd_numbers": [1, 3, 5, 7, 9],
  "even_numbers": [2, 4, 6, 8, 10],
  "odd_count": 5,
  "even_count": 5
}`

