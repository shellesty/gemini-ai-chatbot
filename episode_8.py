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
        "gemini-2.5-pro",
        "gemini-3-flash-preview"
    ]
)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()

# Main title
st.title("🤖 Gemini AI Assistant")

st.write("Now with streaming responses!")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
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

        try:

            # Prepare conversation history
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

            # Placeholder for streaming text
            response_placeholder = st.empty()

            full_response = ""

            # Stream response
            response_stream = client.models.generate_content_stream(
                model=selected_model,
                contents=gemini_messages
            )

            for chunk in response_stream:

                if chunk.text:

                    full_response += chunk.text

                    response_placeholder.markdown(full_response)

            # Store AI response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:
            st.error(f"Error: {e}")