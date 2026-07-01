def ask_gemini(client, history):
    conversation = ""

    for message in history:
        conversation += f"{message['role']}: {message['message']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation,
    )

    return response.text