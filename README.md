# Mini Project 3 – Flask Web App

**Author:** Janelle Holcomb  
**Class:** INF601 - Advanced Programming in Python (Mini Project 3)
Programming in Python (Project 3)

## Project Overview
This Flask app was built for my INF601 class. It includes authentication, a form with GET and POST, a SQLite database with a foreign key, and a Bootstrap modal. I kept the layout simple and clean, added a small footer with my name, and organized the pages so everything flows easily. It meets all of the project requirements while still reflecting my own minimal style.

### Pages
1. **Home** (`/`) – public landing page  
2. **About** (`/about`) – explains the project and process  
3. **Reflections** (`/notes`) – list of user notes/reflections with a **Bootstrap modal** to view details  
4. **Add Reflection** (`/notes/add`) – **form with GET and POST** for creating reflections  
5. **Dashboard** (`/dashboard`) – protected page after login

## Unique Touches
- Renamed “Notes” to **Reflections** to make it feel more personal  
- Added a **live search bar** to filter reflections by title or text  
- Included a **word counter** on the Add Reflection form  
- Soft, minimal color tweaks for a calmer look  
- Added a small footer with my name and class info


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
