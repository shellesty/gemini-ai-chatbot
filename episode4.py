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

# Streamlit UI
st.title("🤖 My First Gen AI App")

st.write("Ask anything to Gemini!")

# User input
user_prompt = st.text_input("Enter your prompt:")

# Generate response
if st.button("Generate Response"):

    if user_prompt:

        with st.spinner("Generating response..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=user_prompt
                )

                st.subheader("AI Response:")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")