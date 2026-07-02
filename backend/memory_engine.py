import json
from chatbot import ask_gemini
from config import client


def analyze_memory(message):
    prompt = f"""
You are an AI memory analyzer.

Your job is to decide whether the user's message contains long-term information that should be remembered.

If it should be remembered, return ONLY valid JSON like:

{{
    "remember": true,
    "key": "name",
    "value": "Mehran"
}}

If it should NOT be remembered, return ONLY:

{{
    "remember": false
}}

User message:
"{message}"
"""

    print(prompt)