from google.genai import types

from schemas import ChatResponse
from system_prompt import SYSTEM_PROMPT


def ask_gemini(client, history):
    conversation = ""

    for message in history:
        conversation += f"{message['role']}: {message['message']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=ChatResponse,
        ),
    )

    return response.parsed


def ask_gemini_raw(client, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text