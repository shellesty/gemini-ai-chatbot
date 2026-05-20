# Gemini AI Chatbot Journey 🤖

This repository documents my step-by-step journey of building a conversational AI chatbot using the Google Gemini API, Python, and Streamlit.

The project starts with a simple single-prompt API call and gradually evolves into a fully interactive AI assistant with conversational memory, chat history, streaming responses, and a professional user interface.

Each episode focuses on introducing a new concept in Generative AI application development, making this repository both a learning journey and a practical demonstration of modern AI chatbot architecture.

Key areas covered throughout this project include:
- Gemini API integration
- Conversational AI architecture
- Stateful chat memory
- Streamlit web applications
- Real-time streaming responses
- AI assistant UI design

The progression across episodes demonstrates how modern AI applications evolve from basic LLM calls into intelligent, context-aware conversational systems.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language used to build the chatbot logic |
| Google Gemini API | Powers AI-generated conversational responses |
| Streamlit | Used to build the interactive web-based chatbot UI |
| python-dotenv | Loads API keys securely from `.env` files |
| Session State | Maintains chat history and conversational memory |
| Streaming Responses | Enables real-time ChatGPT-like response generation |
| Git & GitHub | Version control and project hosting |
| VS Code | Primary development environment used for building the project |

## Project Evolution

### Episode 1: Basic Gemini API Call

This is the starting point of the project where a single hardcoded prompt is sent to Gemini and an AI-generated response is returned.
Unlike later episodes, there is no user interaction, memory, or UI — just a simple API call and response.

#### Result
```text
"Explain LLM in one simple line"
```

<img width="1115" height="42" alt="image" src="https://github.com/user-attachments/assets/db74e412-e08e-44e1-886e-7a6d4f682c83" />

### Episode 2: Multi-turn Conversation

This episode introduces conversation history and contextual follow-up questions.
Compared to Episode 1, the chatbot can now remember previous messages and answer based on earlier context.

#### Example Conversation

```text
user_input_1 = "Who is Virat Kohli? Answer in 5 words only.
user_input_2 = "How many centuries did he make? Just number.
```

#### Result
<img width="657" height="51" alt="image" src="https://github.com/user-attachments/assets/83e9201e-1311-4491-ba2e-baae61293267" />

### Episode 3: Terminal Chatbot

This episode converts the chatbot into an interactive terminal application with continuous prompts.
Unlike Episode 2, users can now ask unlimited questions dynamically instead of relying on hardcoded conversations.

#### Result

<img width="1207" height="377" alt="image" src="https://github.com/user-attachments/assets/42f6b7c8-0e5c-497d-a486-51dbf62d2ef8" />

### Episode 4: Streamlit Web App

This episode moves the chatbot from the terminal into a web-based interface using Streamlit.
Compared to Episode 3, the chatbot now has a simple UI, but it still does not remember previous conversations.

#### Result
<img width="1027" height="511" alt="image" src="https://github.com/user-attachments/assets/f63efa1b-0a4b-494b-99ad-9762b58fa87d" />
<img width="1017" height="478" alt="image" src="https://github.com/user-attachments/assets/bcb5b672-c8d0-461e-8177-0bd0ff32f79c" />


### Episode 5: Chat History UI

This episode introduces chat-style message rendering with visible conversation history.
Unlike Episode 4, previous messages are now displayed in the UI, but the AI still cannot remember conversational context internally.

#### Note

Chat history is visible, but the AI may still forget context because only the current prompt is sent to Gemini.

#### Result

<img width="1091" height="760" alt="image" src="https://github.com/user-attachments/assets/aa1d1fdd-4144-4159-8495-738190e98370" />

### Episode 6: Conversational Memory

This episode implements true conversational memory by sending the full chat history to Gemini.
Compared to Episode 5, the chatbot can now understand follow-up questions and maintain context throughout the conversation.

#### Result

<img width="982" height="787" alt="image" src="https://github.com/user-attachments/assets/8a07a00c-23a5-49e8-9199-5fce197ecd2c" />


### Episode 7: Professional AI Assistant UI

This episode upgrades the chatbot into a more polished AI assistant with sidebar settings, model selection, and clear chat functionality.
Compared to Episode 6, the focus here is improving user experience and making the chatbot feel more like a real AI product.

#### Result

<img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/b7584543-86e5-4343-aaeb-2fa8f75afa27" />

### Episode 8: Streaming Responses

This episode adds real-time streaming responses for a smoother ChatGPT-like experience.
Unlike Episode 7, responses are now generated progressively in real time instead of appearing all at once.

#### Result

<img width="1738" height="845" alt="image" src="https://github.com/user-attachments/assets/e705bfaa-0d14-4789-b951-ccb7b2c2955c" />

## Key Learnings

- LLM API integration
- Conversational AI architecture
- Stateful chat systems
- Streamlit web applications
- Streaming responses
- Context management
- AI product evolution

## Future Improvements

- PDF Chatbot (RAG)
- Vector Database Integration
- FAISS Embeddings
- Voice Input
- Authentication
- Chat Export
- Dark Mode
- AI Agents


# 👨‍💻 Author

Shellesty Yalla

Building AI applications one episode at a time 🚀
