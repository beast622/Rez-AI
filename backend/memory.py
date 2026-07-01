import json
import os

# Get the folder where memory.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full path to history.json
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

conversation_history = []


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