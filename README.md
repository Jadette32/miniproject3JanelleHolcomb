
# Project 3 – Flask Web App

**Author:** Janelle Holcomb  
**Class:** INF601 - Advanced Programming in Python (Project 3)

## Overview
A small Flask app with authentication, a SQLite database (two tables with a foreign key), Bootstrap UI with a modal, and at least five pages using the template inheritance pattern.

### Pages
1. **Home** (`/`) – public landing page.
2. **About** (`/about`) – static template page.
3. **Notes** (`/notes`) – list user notes; includes a **Bootstrap modal** to view note details.
4. **Add Note** (`/notes/add`) – **form with GET and POST** to create a note.
5. **Dashboard** (`/dashboard`) – protected page shown after login.

## Requirements
- Python 3.11+
- pip / venv

## Installation & Run
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt

# Initialize the SQLite DB in the instance/ folder
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all(); print('DB initialized')"

# Run the dev server
python run.py
# then open http://127.0.0.1:5000/
```

## Environment
Copy `.env.example` to `.env` and edit if desired.
```
FLASK_DEBUG=1
SECRET_KEY=change-me
```

## Tech Details
- **Template structure:** `base.html` provides the layout (Bootstrap JS & CSS), pages extend it.
- **Form (GET/POST):** `Add Note` page uses WTForms; POST saves, GET displays.
- **Database:** `User` 1‑to‑many `Note` (foreign key `user_id`).
- **Auth:** `Flask-Login` for register/login/logout and `@login_required`.
- **Bootstrap:** Navbar, container layout, and a **modal** on `notes.html`.

## Recreate requirements
```bash
pip freeze > requirements.txt
```

## Instructor Header Reminder
Add this to the **top of every .py** file:
```python
# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Mini Project 3
```
