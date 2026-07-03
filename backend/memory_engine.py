from memory import (
    set_profile,
    get_profile
)

from memory_policy import (
    ALLOWED_MEMORY_KEYS,
    KEY_ALIASES
)

from memory_router import get_category


def normalize_key(key: str) -> str:
    key = key.strip().lower()

    if key in KEY_ALIASES:
        key = KEY_ALIASES[key]

    key = key.replace(" ", "_")
    key = key.replace("-", "_")

    while "__" in key:
        key = key.replace("__", "_")

    return key


def normalize_value(value: str) -> str:
    return value.strip()


def should_save(memory):
    return memory.remember


def should_update(key):
    profile = get_profile()
    return key in profile


def process_memory(memory):

    if not should_save(memory):
        return "🧠 Nothing to remember."

    key = normalize_key(memory.key)
    value = normalize_value(memory.value)

    # Let Python decide the category
    category = get_category(key)

    if category is None:
        return (
            f"⚠️ Unknown memory key ignored:\n"
            f"{key}"
        )

    if key not in ALLOWED_MEMORY_KEYS:
        return (
            f"⚠️ Unknown memory key ignored:\n"
            f"{key}"
        )

    profile = get_profile()

    if should_update(key):

        old_value = profile[key]

        if old_value.lower() == value.lower():
            return (
                f"📂 Category: {category}\n"
                "🧠 Memory already exists."
            )

        set_profile(key, value)

        return (
            f"📂 Category: {category}\n"
            f"🔄 Updated memory:\n"
            f"{key}: {old_value} → {value}"
        )

    set_profile(key, value)

    return (
        f"📂 Category: {category}\n"
        f"🧠 Remembered:\n"
        f"{key}: {value}"
    )