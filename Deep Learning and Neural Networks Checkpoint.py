# What You're Aiming For

# In this exercise, we will combine the speech recognition and chatbot algorithms to create a speech-enabled chatbot. The chatbot will take voice input from the user, transcribe it into text using the speech recognition algorithm, and then use the chatbot algorithm to generate a response.

# Note: Before attempting this exercise, make sure you have installed the necessary packages, including nltk, streamlit, and speech_recognition.


# Instructions

# First, import the necessary packages in your code. This includes nltk, streamlit, and speech_recognition.
# Load the text file and preprocess the data using the chatbot algorithm.
# Define a function to transcribe speech into text using the speech recognition algorithm.
# Modify the chatbot function to take both text and speech input from the user. If the user provides text input, the chatbot should function as before. If the user provides speech input, the speech recognition algorithm should transcribe the speech into text, which is then passed to the chatbot.
# Create a Streamlit app that allows the user to provide either text or speech input to the chatbot. If the user provides text input, the chatbot should function as before. If the user provides speech input, the speech recognition algorithm should transcribe the speech into text, which is then passed to the chatbot. The chatbot's response should be displayed to the user.
# Test the chatbot with both text and speech input to ensure that it functions correctly.
# Note: In order to use the speech recognition algorithm, the user will need to have a microphone connected to their device.
    
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
