from google import genai


def ask_gemini(client, message):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )

    return response.text