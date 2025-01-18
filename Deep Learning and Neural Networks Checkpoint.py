import nltk
import speech_recognition as sr
import streamlit as st
import random
import time

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Chatbot logic
def preprocess(text):
    # Simple preprocessing - convert to lowercase and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def chatbot_response(text):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a chatbot, but I'm doing well, thank you!",
        "bye": "Goodbye! Have a great day!",
    }
    # Preprocess the input text
    processed_text = preprocess(text)
    # Simple chatbot response based on keyword matching
    for keyword in responses:
        if keyword in processed_text:
            return responses[keyword]
    return "Sorry, I don't understand that. Can you ask something else?"

# Speech recognition function
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please speak into your microphone.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        st.write("Transcribing...")
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your speech. Please try again."
        except sr.RequestError:
            return "There was an issue with the speech recognition service. Please try again later."

# Streamlit interface
def main():
    st.title("Speech-Enabled Chatbot")
    st.write("""
        This chatbot can take both text and speech input. You can type your question or speak into the microphone.
        Try asking it questions like "Hello", "How are you", or "Bye".
    """)

    # User input section
    input_type = st.radio("Select input type", ("Text Input", "Speech Input"))

    if input_type == "Text Input":
        user_input = st.text_input("Type your message:")
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"Chatbot: {response}")

    elif input_type == "Speech Input":
        if st.button("Start Listening"):
            response = transcribe_speech()
            if response:
                chatbot_reply = chatbot_response(response)
                st.write(f"Chatbot: {chatbot_reply}")

if __name__ == "__main__":
    main()
