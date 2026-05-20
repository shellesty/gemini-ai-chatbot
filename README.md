# Gemini AI Chatbot Journey 🤖

A step-by-step evolution of building a conversational AI chatbot using:

- Python
- Streamlit
- Gemini API
- Session State
- Streaming Responses

This repository demonstrates how a basic LLM API call evolves into a modern conversational AI assistant with memory and streaming support.

---

# 🚀 Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

# 📚 Project Evolution

---

# Episode 1 — Basic Gemini API Call

## Features

- First Gemini API integration
- Single hardcoded prompt
- Simple text generation

## Concepts Learned

- API calls
- Environment variables
- Gemini client setup

## Example Prompt

```text
What is RAG? Explain in one line.
```

## Result

_Add screenshot here_

---

# Episode 2 — Multi-turn Conversation

## Features

- Introduced conversation history
- Hardcoded multi-turn chat
- Context-aware responses

## Concepts Learned

- Chat memory
- Role-based messaging
- Conversation formatting

## Example Conversation

```text
User: I want to start learning AI. Give me 3 beginner projects.

User: Pick the best one for a Python beginner.
```

## Result
<img width="657" height="51" alt="image" src="https://github.com/user-attachments/assets/83e9201e-1311-4491-ba2e-baae61293267" />

---

# Episode 3 — Terminal Chatbot

## Features

- Infinite chatbot loop
- Dynamic user prompts
- Exit condition support

## Concepts Learned

- Interactive terminal chatbot
- Continuous conversations
- User input handling

## Example Prompt

```text
I want to start learning AI. Give me 3 beginner projects.
```

## Result

_Add screenshot here_

---

# Episode 4 — Streamlit Web App

## Features

- First web-based AI chatbot
- Streamlit UI integration
- Prompt input field
- Generate response button

## Concepts Learned

- Streamlit basics
- Web UI development
- Frontend + LLM integration

## Example Prompt

```text
I want to start learning AI. Give me 3 beginner projects.
```

## Result

_Add screenshot here_

---

# Episode 5 — Chat History UI

## Features

- Chat-style interface
- Conversation displayed in UI
- Session state support

## Concepts Learned

- Streamlit session state
- Chat message rendering
- UI-based conversation flow

## Example Conversation

```text
User: I want to start learning AI. Give me 3 beginner projects.

User: Pick the best one for a Python beginner.
```

## Note

Chat history is visible, but the AI may still forget context because only the current prompt is sent to Gemini.

## Result

_Add screenshot here_

---

# Episode 6 — Conversational Memory

## Features

- Full conversational memory
- AI understands follow-up questions
- Context-aware conversations

## Concepts Learned

- Stateful AI systems
- Sending full conversation history
- Conversational architecture

## Example Conversation

```text
User: I want to start learning AI. Give me 3 beginner projects.

User: Pick the best one for a Python beginner.

User: Can you give me a roadmap for it?
```

## Result

_Add screenshot here_

---

# Episode 7 — Professional AI Assistant UI

## Features

- Sidebar settings
- Model selector
- Clear chat button
- Improved UI structure

## Concepts Learned

- Advanced Streamlit UI
- Sidebar controls
- Dynamic model selection

## Example Conversation

```text
User: I want to start learning AI. Give me 3 beginner projects.

User: Pick the best one for a Python beginner.
```

## Result

_Add screenshot here_

---

# Episode 8 — Streaming Responses

## Features

- Real-time streaming responses
- ChatGPT-style typing effect
- Live token generation

## Concepts Learned

- Streaming APIs
- Dynamic UI updates
- Real-time response rendering

## Example Conversation

```text
User: I want to start learning AI. Give me 3 beginner projects.

User: Pick the best one for a Python beginner.

User: Can you give me a roadmap for it?
```

## Result

_Add screenshot here_

---

# 🧠 Key Learnings From This Project

- LLM API integration
- Conversational AI architecture
- Stateful chat systems
- Streamlit web applications
- Streaming responses
- Context management
- AI product evolution

---

# 🔮 Future Improvements

- PDF Chatbot (RAG)
- Vector Database Integration
- FAISS Embeddings
- Voice Input
- Authentication
- Chat Export
- Dark Mode
- AI Agents

---

# ⚙️ Run Locally

## Clone Repository

```bash
git clone https://github.com/shellesty/gemini-ai-chatbot.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Add Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Run Streamlit App

```bash
streamlit run episode_8.py
```

---

# 👨‍💻 Author

Shellesty Yalla

Building AI applications one episode at a time 🚀
