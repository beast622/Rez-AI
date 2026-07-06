from rapidfuzz import fuzz

# -----------------------------
# INTENT PATTERNS
# -----------------------------

INTENTS = {
    "name": [
        "what is my name",
        "whats my name",
        "who am i",
        "tell me my name"
    ],

    "favorite_team": [
        "what is my favorite team",
        "whats my favorite team",
        "what's my favourite team",
        "whats my fav team",
        "who do i support",
        "which team do i support",
        "my team",
        "favorite team",
        "favourite team"
    ],

    "current_project": [
        "what am i building",
        "what is my project",
        "current project",
        "what am i working on"
    ]
}


# -----------------------------
# SMART MATCH ENGINE
# -----------------------------

def match_intent(text: str):
    text = text.lower().strip()

    best_intent = None
    best_score = 0

    for intent, samples in INTENTS.items():
        for sample in samples:
            # Better than partial_ratio for full sentences
            score = fuzz.token_set_ratio(text, sample)

            if score > best_score:
                best_score = score
                best_intent = intent

    print(f"\n🔍 Intent Match -> {best_intent} ({best_score:.1f})")

    if best_score >= 80:
        return best_intent

    return None


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def recognize_intent(user_text: str):
    intent = match_intent(user_text)

    if intent:
        return {
            "intent": "memory_lookup",
            "key": intent
        }

    return {
        "intent": "chat"
    }