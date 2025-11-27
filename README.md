# Final Project - Flask Web App: Mindful Moments Tracker 

**Author:** Janelle Holcomb  
**Class:** INF601 - Advanced Programming in Python (Final Project)

---

## Project Overview
This final project expands my Mini Project 3 into a more complete emotional-wellness web application called **Mindful Moments Tracker**. Users can log daily reflections, choose a mood for each entry, and see simple charts that show how their mood changes over time. I focused on keeping the layout calm and minimal while also adding more structure and features based on the instructor’s feedback.

This version includes user authentication, a mood-based quote system using the ZenQuotes API, a weekly mood heatmap, reflection dates, mood suggestions, and a more useful dashboard that pulls everything together in one place.

---

## Pages
1. **Home** (`/`) – public welcome page that introduces the app and sets the tone  
2. **About** (`/about`) – explains what the app does, what tools it uses, and how it supports the user  
3. **Dashboard** (`/dashboard`) – protected page with:  
   - Total number of reflections  
   - Most recent reflection summary  
   - Mood-based quote from the ZenQuotes API  
   - Overall mood bar chart  
   - Weekly mood heatmap  
   - Gentle suggestions based on the user’s current mood  
4. **Reflections** (`/notes`) – list of all saved reflections, sorted by most recent, showing title, reflection date, and text  
5. **Add Reflection** (`/notes/add`) – form where users can enter:  
   - Title  
   - Reflection body  
   - Mood (happy, sad, anxious, tired, calm)  
   - Reflection date (so they can back-fill missed days)  
6. **Register / Login / Logout** – authentication system using Flask-Login  

---

## Unique Touches
- Renamed “Notes” to **Reflections** to make the space feel more personal and reflective  
- Added a **mood field** and **reflection date** to each entry  
- Added a **mood-based quote** using the ZenQuotes API that updates with the user’s latest mood  
- Created a **weekly mood heatmap** so users can see which moods show up across the last seven days  
- Added gentle **mood suggestions** (for sad, anxious, tired, calm, and happy) to support the user in simple, practical ways  
- Used a soft, neutral color palette and simple card layout for a calm, uncluttered feel  

---

## Requirements
To run this project you will need:

- Python **3.11+**  
- `pip`  
- `venv` (for creating a virtual environment)  
- An internet connection (for the ZenQuotes API)

---

## Installation and Setup

All commands below should be run from the root folder of this project.

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
This will install Flask, Flask-Login, SQLAlchemy, WTForms, Requests, and Matplotlib plus any other needed packages.

### 3. Initialize the SQLite DB in the instance/ folder
```bash
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all(); print('Database initialized')"
```
After this, an instance/ folder will be created (if it does not already exist) and an app.db file will be generated inside it. You only need to do this again if you delete the database or change the models in a way that requires recreating everything from scratch.

### 4. Run the Flask development server
```bash
python run.py
```
## Then open your web browser and go to:
```cpp 
http://127.0.0.1:5000/
```
You will be able to register, log in, add reflections, and view your dashboard.



## Tech Details
- **Folder / Template Structure:**  
  - Uses Blueprints (`main` and `auth`) for cleaner separation of routes  
  - `base.html` holds the main layout (navigation bar, container, footer)  
  - All other templates extend `base.html` for consistency  

- **Forms (GET/POST):**  
  - `Add Reflection` uses WTForms and supports both GET (show form) and POST (save data)  
  - Each reflection stores: title, body, mood, reflection date, user reference  

- **Database:**  
  - SQLite database created through SQLAlchemy  
  - `User` table for authentication  
  - `Note` table that includes a foreign key (`user_id`) linking each reflection to its user

### Note About Configuration
This project does *not* require an `.env` file. All settings needed to run the app are already included in the code.

- **Authentication:**  
  - Implemented using Flask-Login  
  - Includes register, login, logout, and session management  

- **API Integration (ZenQuotes):**  
  - A helper function calls the ZenQuotes API and selects a quote that matches the user’s current mood  
  - The dashboard displays the quote tied to the most recent reflection mood  

- **Charts and Visualization:**  
  - `mood_chart.png`: bar chart showing how often each mood appears  
  - `weekly_mood_heatmap.png`: 7-day heatmap showing which moods appeared on which days  
  - Charts are generated with Matplotlib and saved into the `static/` folder

- **Styling:**  
  - Uses Bootstrap for layout and responsive behavior  
  - Custom CSS in `static/css/styles.css` adds soft colors, rounded cards, and a gentle, calm look  

## Future Steps
If I continue building on this project, I’d like to keep improving it without changing what already works.  
Some ideas I have:
- **Let users edit or delete their reflections**
- **Add categories or tags for organization**
- **Improve the search to make older entries easier to find**
- **Add a small profile area with personal goals or intentions**
- **Export reflections or mood history as a PDF or CSV**

This version meets the Final Project requirements and grows directly out of my Mini Project 3, while adding more structure, more visuals, and a clearer emotional focus.

## Instructor Header Reminder
Add this to the **top of every .py** file:
```python
# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Final Project
```
