from memory import add_message, get_history, load_history
from chatbot import ask_gemini
from config import client

print("====================================")
print("🤖 Welcome to Rèz v0.3")
print("====================================")

load_history()

while True:
    user = input("\nYou: ")
    add_message("user", user)

    if user.lower() == "exit":
        print("Rèz: Goodbye! 👋")
        break

    try:
        history = get_history()
        reply = ask_gemini(client, history)

        print("\nRèz:", reply)
        add_message("assistant", reply)

    except Exception as e:
        print("\nError:", e)