from memory import get_profile


def get_all_memories():
    """
    Returns every memory Rèz knows.
    """
    return get_profile()


def has_memories():
    """
    Returns True if Rèz knows anything.
    """
    return len(get_profile()) > 0


def get_memory(key):
    """
    Returns a single memory.
    """

    profile = get_profile()

    return profile.get(key)


def format_memories():
    """
    Formats every memory into a readable string.
    """

    profile = get_profile()

    if not profile:
        return "I don't remember anything about you yet."

    result = "Here's what I remember about you:\n\n"

    for key, value in profile.items():
        pretty_key = key.replace("_", " ").title()
        result += f"• {pretty_key}: {value}\n"

    return result


# -----------------------------
# DEBUG FUNCTION (NEW)
# -----------------------------
def debug_profile():
    """
    Debug function to inspect memory state.
    """

    profile = get_profile()

    print("\n🧠 DEBUG PROFILE CONTENT:")

    for k, v in profile.items():
        print(f"{k} -> {v}")

    return profile