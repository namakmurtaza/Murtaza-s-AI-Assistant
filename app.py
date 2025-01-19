from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Set API key for Generative AI
genai_api_key = "AIzaSyCY9L7bXQ0UlJI9xRfQU_zVW7L91NekxSQ"
genai.configure(api_key=genai_api_key)

# Function to get a response from the Gemini model
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Murtaza's AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom styling and background
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fc;
        font-family: Arial, sans-serif;
    }
    .header {
        color: #2c3e50;
        font-size: 2.5em;
        text-align: center;
        margin-top: 10px;
    }
    .sub-header {
        color: #34495e;
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    .feature-title {
        font-size: 1.4em;
        font-weight: bold;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.9em;
        color: #7f8c8d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="header">🤖 Murtaza\'s AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your versatile AI-powered companion</div>', unsafe_allow_html=True)

# Sidebar for feature selection
st.sidebar.title("🪄 Features")
features = st.sidebar.radio(
    "Choose a feature:",
    ["Q&A Chat", "Explain a Concept", "Summarize a Text", "Generate Images", "LinkedIn Post Writer"]
)

# Dynamic instructions based on feature
instructions = {
    "Q&A Chat": "Ask any question, and I will respond intelligently.",
    "Explain a Concept": "Enter a topic, and I'll provide an easy-to-understand explanation.",
    "Summarize a Text": "Paste a long text, and I'll summarize it for you.",
    "Generate Images": "Enter a description, and I'll generate an image based on it.",
    "LinkedIn Post Writer": "Provide a brief description of your achievement or update, and I'll craft a professional LinkedIn post."
}

st.markdown(f"### {features} 🚀")
st.write(instructions[features])

# Input field
input_placeholder = {
    "Q&A Chat": "Ask me a question...",
    "Explain a Concept": "Enter a concept (e.g., Quantum Computing)...",
    "Summarize a Text": "Paste a long text here...",
    "Generate Images": "Describe the image you want (e.g., a sunset over the mountains)...",
    "LinkedIn Post Writer": "Describe your achievement or update briefly..."
}
user_input = st.text_area("Input:", placeholder=input_placeholder[features], height=150)

# Submit button
submit = st.button("🔍 Submit")

# Response section
if submit:
    if user_input.strip():
        if features == "Q&A Chat":
            with st.spinner("Processing your question..."):
                response = get_gemini_response(user_input)
            st.subheader("💬 AI Response:")
            st.write(response)

        elif features == "Explain a Concept":
            with st.spinner("Explaining the concept..."):
                response = get_gemini_response(f"Explain {user_input} in simple terms.")
            st.subheader("📘 Explanation:")
            st.write(response)

        elif features == "Summarize a Text":
            with st.spinner("Summarizing the text..."):
                response = get_gemini_response(f"Summarize this: {user_input}")
            st.subheader("📝 Summary:")
            st.write(response)

        elif features == "Generate Images":
            with st.spinner("Generating your image..."):
                st.image("https://via.placeholder.com/800x400?text=Generated+Image")  # Placeholder
                st.write("Image generation can be integrated with tools like DALL·E for real images.")

        elif features == "LinkedIn Post Writer":
            with st.spinner("Writing your LinkedIn post..."):
                response = get_gemini_response(f"Write a LinkedIn post for this: {user_input}")
            st.subheader("🔗 LinkedIn Post:")
            st.write(response)
    else:
        st.warning("⚠️ Please provide valid input!")

# Footer
st.markdown('<div class="footer">Made with ❤️ by Murtaza Namak | Powered by Generative AI</div>', unsafe_allow_html=True)

