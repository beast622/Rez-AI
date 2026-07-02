import json
import os

# Get the folder where memory.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
PROFILE_FILE = os.path.join(BASE_DIR, "profile.json")
KNOWLEDGE_FILE = os.path.join(BASE_DIR, "knowledge.json")

# In-memory data
conversation_history = []
user_profile = {}


# ==========================
# HISTORY FUNCTIONS
# ==========================

def load_history():
    global conversation_history

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            conversation_history = json.load(file)
            print("✅ History loaded.")
    except FileNotFoundError:
        conversation_history = []
        print("⚠️ history.json not found. Starting with empty memory.")
    except json.JSONDecodeError:
        conversation_history = []
        print("⚠️ history.json is empty or corrupted. Starting with empty memory.")


def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(conversation_history, file, indent=4, ensure_ascii=False)

    print(f"💾 History saved to: {HISTORY_FILE}")


def add_message(role, message):
    conversation_history.append({
        "role": role,
        "message": message
    })

    save_history()


def get_history():
    return conversation_history


# ==========================
# PROFILE FUNCTIONS
# ==========================

def load_profile():
    global user_profile

    try:
        with open(PROFILE_FILE, "r", encoding="utf-8") as file:
            user_profile = json.load(file)
            print("✅ Profile loaded.")
    except FileNotFoundError:
        user_profile = {}
        print("⚠️ profile.json not found. Starting with empty profile.")
    except json.JSONDecodeError:
        user_profile = {}
        print("⚠️ profile.json is empty or corrupted. Starting with empty profile.")


def save_profile():
    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(user_profile, file, indent=4, ensure_ascii=False)

    print(f"💾 Profile saved to: {PROFILE_FILE}")


def get_profile():
    return user_profile


def set_profile(key, value):
    """
    Save or update a value in the user's profile.
    Example:
        set_profile("name", "Mehran")
    """
    global user_profile

    user_profile[key] = value
    save_profile()


def get_profile_value(key):
    """
    Get a value from the user's profile.
    Example:
        get_profile_value("favorite_team")
    """
    return user_profile.get(key)