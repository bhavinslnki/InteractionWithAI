# AI Interaction Project

This project demonstrates a simple interaction between speech recognition, OpenAI's GPT model, and text-to-speech using Python. The program listens to your voice input, transcribes it to text, sends the transcribed text to the GPT-3.5 model, and then converts the AI's response back to speech.

# Key Features:
Speech Recognition: Converts your speech to text using SpeechRecognition and Google Web Speech API.
AI Interaction: Sends the recognized text to OpenAI's GPT-3.5 model for processing via an API request.
Text-to-Speech: The AI's response is converted to speech using the gTTS (Google Text-to-Speech) library.
Cross-Platform Audio Playback: The AI-generated speech is played back using system commands (os.system) to ensure compatibility on both Windows and Unix-like systems.


# Tech Stack:
Python: The main programming language.
SpeechRecognition: Used to capture and transcribe speech input.
OpenAI GPT-3.5 API: Provides intelligent responses based on the user's voice input.
gTTS: Converts text responses into speech.
Requests: To handle HTTP API requests.
PyAudio: Required for capturing microphone input.


# How it Works:
The user speaks into the microphone.
The speech is converted to text using the Google Web Speech API.
The recognized text is sent to the OpenAI GPT-3.5 API.
The AI generates a response based on the input text.
The AI’s response is converted back into speech using gTTS.
The response is played back as an audio file.

# Requirements:
Python 3.6+
PyAudio (for speech recognition)
gTTS
OpenAI API Key


# Installation:

Clone the repository.

Install the required libraries:
 pip install -r requirements.txt

Run the program:
 python InteractionWithAi.py