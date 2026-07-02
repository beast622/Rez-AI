from memory import (
    add_message,
    get_history,
    load_history,
    load_profile,
    set_profile,
    get_profile_value
)
from chatbot import ask_gemini
from config import client

print("====================================")
print("🤖 Welcome to Rèz v0.5")
print("====================================")

load_history()
load_profile()

while True:
    user = input("\nYou: ")

    add_message("user", user)

    if user.lower() == "exit":
        print("Rèz: Goodbye! 👋")
        break

    try:

        # Temporary memory test (we'll remove this soon)
        if user.lower() == "what's my name?" or user.lower() == "what is my name?":
            name = get_profile_value("name")

            if name:
                print(f"\nRèz: Your name is {name}. 😊")
            else:
                print("\nRèz: I don't know your name yet.")

            continue

        history = get_history()
        response = ask_gemini(client, history)

        print("\nRèz:", response.reply)
        add_message("assistant", response.reply)

        # AI decides what to remember
        if response.memory.remember:
            set_profile(
                response.memory.key,
                response.memory.value
            )

            print(
                f"\n🧠 Remembered: "
                f"{response.memory.key} = {response.memory.value}"
            )
        else:
            print("\n🧠 Nothing to remember.")

    except Exception as e:
        error = str(e)

        if "503" in error:
            print("\n🤖 Rèz: Gemini is currently busy.")
            print("Please try again in a few seconds.")

        else:
            print("\nError:", e)