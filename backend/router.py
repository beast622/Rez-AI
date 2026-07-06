from memory_search import (
    get_memory,
    format_memories
)

from intent_recognizer import recognize_intent


def handle_request(user_text: str):
    """
    Central router for all user requests.

    Returns:
        {
            "handled": bool,
            "response": str | None
        }
    """

    # -----------------------------
    # Memory Lookup
    # -----------------------------
    intent = recognize_intent(user_text)

    if intent["intent"] == "memory_lookup":

        value = get_memory(intent["key"])

        if value:
            return {
                "handled": True,
                "response": value
            }

        return {
            "handled": True,
            "response": "I don't know that yet."
        }

    # -----------------------------
    # Memory Dump
    # -----------------------------
    if user_text.lower() in [
        "what do you remember about me?",
        "show my memories"
    ]:

        return {
            "handled": True,
            "response": format_memories()
        }

    # -----------------------------
    # Nobody handled it
    # -----------------------------
    return {
        "handled": False,
        "response": None
    }