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

# Page configuration
st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Sidebar
st.sidebar.title("⚙️ Settings")

# Model selection
selected_model = st.sidebar.selectbox(
    "Choose Gemini Model",
    [
        "gemini-2.5-flash",
        "gemini-2.5-pro"
    ]
)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()

# Main title
st.title("🤖 Gemini AI Assistant")

st.write("Conversational AI chatbot with memory")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Type your message here...")

# If user enters prompt
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

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # Prepare Gemini conversation history
                gemini_messages = []

                for msg in st.session_state.messages:

                    role = (
                        "user"
                        if msg["role"] == "user"
                        else "model"
                    )

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

                # Generate response
                response = client.models.generate_content(
                    model=selected_model,
                    contents=gemini_messages
                )

                ai_response = response.text

                # Display AI response
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