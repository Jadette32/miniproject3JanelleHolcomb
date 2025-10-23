# Mini Project 3 – Flask Web App

**Author:** Janelle Holcomb  
**Class:** INF601 - Advanced Programming in Python (Mini Project 3)

---

## Project Overview
This Flask app was built for my INF601 class. It includes authentication, a form with GET and POST, a SQLite database with a foreign key, and a Bootstrap modal. I kept the layout simple and clean, added a small footer with my name, and organized the pages so everything flows easily. It meets all of the project requirements while still reflecting my own minimal style.

---

### Pages
1. **Home** (`/`) – public landing page  
2. **About** (`/about`) – explains the project and process  
3. **Reflections** (`/notes`) – list of user notes/reflections with a **Bootstrap modal** to view details  
4. **Add Reflection** (`/notes/add`) – **form with GET and POST** for creating reflections  
5. **Dashboard** (`/dashboard`) – protected page after login

---

## Unique Touches
- Renamed “Notes” to **Reflections** to make it feel more personal  
- Added a **live search bar** to filter reflections by title or text  
- Included a **word counter** on the Add Reflection form  
- Soft, minimal color tweaks for a calmer look  
- Added a small footer with my name and class info

---

## Requirements
Before running, make sure you have:
- Python **3.11+**
- `pip` (Python package manager)  
- `venv` (for creating a virtual environment)

---

## Installation and Setup 

### 1. Create and activate a virtual environment 
```bash
python -m venv .venv
```
## Windows
```bash
.venv\Scripts\activate
```

## macOS/Linux
```bash
source .venv/bin/activate
```
### 2. Install all dependencies
```bash
pip install -r requirements.txt
```
This installs all required packages such as flask, flask-login, and SQLAlchemy.

### 3. Initialize the SQLite DB in the instance/ folder
```bash
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all(); print('Database initialized')"
```

### 4. Run the Flask development server
```bash
python run.py
```
## Then open your web browser and go to:
```cpp 
http://127.0.0.1:5000/
```
You will be able to register, log in, and add reflections.

## Environment Variables
The app can use a .env file for settings. Example:
``` ini
FLASK_DEBUG=1
SECRET_KEY=change-me
```

## Tech Details
- **Template Structure:** `base.html` provides the main layout with Bootstrap JS & CSS. All other pages extend this file for consistency.  
- **Form (GET/POST):** The `Add Reflection` page uses WTForms. The GET method loads the form, and POST saves the reflection to the database.  
- **Database:** SQLite database with a one-to-many relationship between `User` and `Note` (foreign key `user_id`).  
- **Authentication:** Managed through `Flask-Login` for user registration, login, logout, and session handling.  
- **Bootstrap:** Used for responsive design, the navigation bar, layout containers, and a **modal** feature on the Reflections page for viewing entries.  
- **Styling:** Custom CSS in `static/css/styles.css` adds soft neutral colors, rounded buttons, and a footer with my name and class info.

## Updating Dependencies
If new packages are added later, update the requirements file:
```bash
pip freeze > requirements.txt
```
## Next Steps
If I continue building on this project for my final, I’d like to keep improving it without changing what already works.  
Some ideas I have:
- **Let users edit or delete their reflections**
- **Add categories or tags for organization**
- **Improve the search to make older entries easier to find**
- **Add a simple profile page or stats section**
- **Include custom error pages for a cleaner experience**

This version meets all the Mini Project 3 requirements and gives me a strong starting point for my final project.

## Instructor Header Reminder
Add this to the **top of every .py** file:
```python
# INF601 - Advanced Programming in Python
# (Your name here)
# Mini Project 3
```
