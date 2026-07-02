# 🤖 Rèz AI

> A personal AI assistant built with Python and Google's Gemini API.

Rèz is an AI assistant that is being developed step by step into a fully featured personal assistant with persistent memory, intelligent reasoning, voice interaction, vision, and more.

This repository documents the complete journey of building Rèz from a simple chatbot into a real AI assistant.

---

## ✨ Current Features

- 💬 Chat with Google's Gemini 2.5 Flash
- 🧠 Persistent conversation history
- 👤 User profile memory
- 📄 Structured AI responses using Pydantic
- 🏗️ Modular Python architecture
- 💾 JSON-based memory storage
- 🔄 Git version control
- ☁️ GitHub integration

---

## 🛠️ Built With

- Python 3.12
- Google Gemini API
- google-genai SDK
- Pydantic
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```text
AI Assistant/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── memory.py
│   ├── memory_engine.py
│   ├── schemas.py
│   ├── system_prompt.py
│   ├── history.json
│   ├── profile.json
│   └── knowledge.json
│
├── assets/
├── database/
├── docs/
├── frontend/
│
├── .gitignore
└── README.md
```

---

## 🧠 Memory System

Rèz currently uses three memory types:

### Conversation Memory

Stores previous conversations.

```
history.json
```

### Profile Memory

Stores long-term user information such as:

- Name
- Preferences
- Favourite team

```
profile.json
```

### Knowledge Memory

Reserved for future AI knowledge storage.

```
knowledge.json
```

---

## 🚀 Development Roadmap

### ✅ v0.1

- Basic chatbot

### ✅ v0.2

- Gemini API integration

### ✅ v0.3

- Modular backend
- Git support
- GitHub repository

### ✅ v0.4

- Persistent conversation history
- Conversation context

### ✅ v0.5 — The Foundation

- Structured AI responses
- User profile memory
- Knowledge memory foundation
- System prompt architecture
- Pydantic schemas

---

## 🔮 Future Versions

### v0.6 — The Memory Engine

- Intelligent memory updates
- Automatic memory management
- Better profile handling

### v0.7 — The Identity

- Automatic profile injection
- Personalized AI responses
- Reduced hardcoded logic

### v0.8 — The Knowledge

- AI knowledge storage
- Knowledge retrieval
- Learning from conversations

### v1.0 — Genesis

- Voice interaction
- Vision support
- Internet search
- Plugin system
- Desktop interface
- Advanced memory
- Multi-language support

---

## 👨‍💻 Developer

Created by **Mehran Reza** 🇧🇩

Rèz is a long-term learning project focused on understanding modern AI engineering, software architecture, and intelligent assistants.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!