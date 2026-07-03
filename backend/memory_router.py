"""
Rèz Memory Router

Responsible for deciding which category
a memory belongs to.
"""


PROFILE_KEYS = {
    "name",
    "nickname",
    "age",
    "birthday",
    "country",
    "city",
    "language",
    "profession",
    "school",
    "university",
}

PREFERENCE_KEYS = {
    "favorite_team",
    "favorite_player",
    "favorite_food",
    "favorite_movie",
    "favorite_game",
    "favorite_song",
    "favorite_artist",
    "favorite_color",
}

PROJECT_KEYS = {
    "current_project",
    "goal",
}

KNOWLEDGE_KEYS = {
    "knowledge",
}


def get_category(key):

    if key in PROFILE_KEYS:
        return "profile"

    if key in PREFERENCE_KEYS:
        return "preferences"

    if key in PROJECT_KEYS:
        return "projects"

    if key in KNOWLEDGE_KEYS:
        return "knowledge"

    return None