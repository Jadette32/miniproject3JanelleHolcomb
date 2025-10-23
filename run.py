# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Mini Project 3


"""
File: run.py
Description: Flask entry point
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
