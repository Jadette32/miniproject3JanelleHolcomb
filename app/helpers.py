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
