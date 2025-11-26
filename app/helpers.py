import requests

# Map moods to keywords that match quote themes
MOOD_KEYWORDS = {
    "calm": ["peace", "still", "breathe", "quiet"],
    "happy": ["joy", "smile", "light", "grateful"],
    "sad": ["strength", "healing", "hope", "grow"],
    "anxious": ["courage", "breathe", "control", "calm"],
    "tired": ["rest", "slow", "restore", "gentle"]
}

def get_quote_for_mood(mood):
    """
    Fetch several quotes from ZenQuotes API,
    filter them based on mood keywords,
    and return a matching one.
    """

    try:
        # fetch 10 quotes
        response = requests.get("https://zenquotes.io/api/quotes")
        quotes = response.json()

        # get the list of keywords for the user's mood
        keywords = MOOD_KEYWORDS.get(mood, [])

        # try to find a matching quote
        for q in quotes:
            text = q.get("q", "").lower()
            if any(word in text for word in keywords):
                return text

        # fallback: return the first quote if nothing matched
        return quotes[0].get("q", "Take a deep breath. You are doing your best.")

    except Exception:
        return "Breathe. You are doing enough."

import matplotlib
matplotlib.use('Agg')  # Prevents issues on Windows with Flask
import matplotlib.pyplot as plt
import os

from .models import Note
from flask_login import current_user

def create_mood_chart(app):
    """
    Count moods for the current user and generate a bar chart saved in /static.
    """
    with app.app_context():
        notes = Note.query.filter_by(user_id=current_user.id).all()

        # count moods
        mood_counts = {}
        for n in notes:
            mood_counts[n.mood] = mood_counts.get(n.mood, 0) + 1

        # if no moods, do not create a chart
        if not mood_counts:
            return None

        moods = list(mood_counts.keys())
        counts = list(mood_counts.values())

        plt.figure(figsize=(6, 4))
        plt.bar(moods, counts, color="#88b0a8")
        plt.title("Your Mood Overview")
        plt.xlabel("Mood")
        plt.ylabel("Count")

        # save chart to static directory
        chart_path = os.path.join(app.static_folder, "mood_chart.png")
        plt.savefig(chart_path)
        plt.close()

        return "mood_chart.png"
