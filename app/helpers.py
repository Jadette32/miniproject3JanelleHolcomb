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

MOOD_SUGGESTIONS = {
    "happy": [
        "Enjoy this moment and notice what made today brighter.",
        "Write one good thing that happened today.",
        "Celebrate a small win or share joy with someone you love."
    ],
    "sad": [
        "Try placing a hand on your chest and take one slow breath.",
        "Let yourself feel without judgment. You are allowed to have slow days.",
        "Do one comforting thing, even if it is small."
    ],
    "anxious": [
        "Try a 4 second inhale and 6 second exhale to settle your body.",
        "Pause and relax your shoulders, unclench your jaw.",
        "Write down one worry to get it out of your head."
    ],
    "tired": [
        "Close your eyes for 30 seconds and breathe gently.",
        "Drink some water. Your body might need a small reset.",
        "Move your arms or stretch your neck for a moment."
    ],
    "calm": [
        "Enjoy this sense of ease. Let yourself stay here for a moment.",
        "Notice the quiet parts of your day.",
        "Write down something that feels grounding right now."
    ]
}

def get_suggestions_for_mood(mood):
    # fallback to calm if mood not in dictionary
    return MOOD_SUGGESTIONS.get(mood.lower(), MOOD_SUGGESTIONS["calm"])

from datetime import datetime, timedelta
import numpy as np

def create_weekly_mood_heatmap(app):
    """
    Create a 7-day mood heatmap using reflection_date instead of created_at.
    """
    with app.app_context():
        today = datetime.utcnow().date()

        # list of past 7 days (oldest → newest)
        week_dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]

        # fetch notes using reflection_date instead of created_at
        one_week_ago = today - timedelta(days=6)
        notes = Note.query.filter(
            Note.user_id == current_user.id,
            Note.reflection_date >= one_week_ago
        ).all()

        # mood order for heatmap rows
        mood_levels = ["sad", "tired", "anxious", "calm", "happy"]
        mood_index = {m: i for i, m in enumerate(mood_levels)}

        # create 5 x 7 grid
        heatmap = np.zeros((5, 7))

        # fill the heatmap using reflection_date
        for n in notes:
            day = n.reflection_date
            if day in week_dates:
                col = week_dates.index(day)
                row = mood_index.get(n.mood.lower())
                if row is not None:
                    heatmap[row][col] = 1

        # draw heatmap
        plt.figure(figsize=(7, 4))
        plt.imshow(heatmap, cmap="Greens", interpolation="nearest", aspect="auto")
        plt.title("Your Mood This Week")

        # y-axis labels
        plt.yticks(range(len(mood_levels)), mood_levels)

        # x-axis labels
        x_labels = [d.strftime("%a") for d in week_dates]
        plt.xticks(range(7), x_labels)

        plt.tight_layout()

        filename = "weekly_mood_heatmap.png"
        chart_path = os.path.join(app.static_folder, filename)

        plt.savefig(chart_path)
        plt.close()

        return filename
