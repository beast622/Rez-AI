from memory import (
    add_message,
    get_history,
    load_history,
    load_profile
)

from chatbot import ask_gemini
from config import client
from memory_engine import process_memory
from memory_search import debug_profile
from router import handle_request

print("====================================")
print("🤖 Welcome to Rèz v0.8.2")
print("====================================")

load_history()
load_profile()

# -----------------------------
# DEBUG PROFILE (TEMPORARY)
# -----------------------------
debug_profile()

while True:

    user = input("\nYou: ")

    add_message("user", user)

    if user.lower() == "exit":
        print("Rèz: Goodbye! 👋")
        break

    try:

        # -----------------------------
        # ROUTER
        # -----------------------------
        route = handle_request(user)

        if route["handled"]:
            print(f"\nRèz: {route['response']}")
            continue

        # -----------------------------
        # GEMINI CHAT
        # -----------------------------
        history = get_history()

        response = ask_gemini(
            client,
            history
        )

        print("\nRèz:", response.reply)

        add_message(
            "assistant",
            response.reply
        )

        # -----------------------------
        # MEMORY ENGINE
        # -----------------------------
        result = process_memory(
            response.memory
        )

        print("\n" + result)

    except Exception as e:

        error = str(e)

        if "503" in error:
            print("\n🤖 Rèz: Gemini is currently busy.")
            print("Please try again in a few seconds.")
        else:
            print("\nError:", e)