"""
Rèz Memory Policy

Defines which long-term memories Rèz is allowed to store.
"""

ALLOWED_MEMORY_KEYS = {

    # Identity
    "name",
    "nickname",
    "age",
    "birthday",
    "country",
    "city",
    "language",

    # Preferences
    "favorite_team",
    "favorite_player",
    "favorite_food",
    "favorite_movie",
    "favorite_game",
    "favorite_song",
    "favorite_artist",
    "favorite_color",

    # Projects
    "current_project",
    "goal",

    # User
    "profession",
    "school",
    "university",

    # Devices
    "computer",
    "gpu",
    "cpu",
    "phone",
}


KEY_ALIASES = {

    # Favorite Team
    "favorite team": "favorite_team",
    "favourite team": "favorite_team",
    "fav_team": "favorite_team",
    "football_team": "favorite_team",

    # Favorite Player
    "favorite player": "favorite_player",
    "favourite player": "favorite_player",

    # Current Project
    "project": "current_project",
    "current project": "current_project",

    # Name
    "full_name": "name",

    # Language
    "preferred language": "language",
}