import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Streamlit page config
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖"
)

# App title
st.title("🤖 Gemini AI Chatbot")

st.write("Your conversational AI assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Type your message here...")

# If user sends message
if user_prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                # Prepare conversation history for Gemini
                gemini_messages = []

                for msg in st.session_state.messages:

                    role = "user" if msg["role"] == "user" else "model"

                    gemini_messages.append(
                        {
                            "role": role,
                            "parts": [
                                {
                                    "text": msg["content"]
                                }
                            ]
                        }
                    )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=gemini_messages
                )

                ai_response = response.text

                st.markdown(ai_response)

                # Store AI response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except Exception as e:
                st.error(f"Error: {e}")