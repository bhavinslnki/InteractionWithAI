import os
from gtts import gTTS
import json
import requests
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I didn't understand that!")
    text = "I didn't understand that."


url = "https://api.openai.com/v1/chat/completions"

payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": text
        }
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR API KEY'
}

try:
    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    if 'choices' in data:
        generated_text = data['choices'][0]['message']['content']
        print("Generated response:", generated_text)
    else:
        print("Error in API response:", data)
        generated_text = "Sorry, something went wrong with the AI response."
    
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    generated_text = "Sorry, I couldn't connect to the AI service."

# Text-to-Speech (gTTS)
tts = gTTS(generated_text, lang="en")
tts.save("chatGpt.mp3")


if os.name == 'nt':  # Windows
    os.system("start chatGpt.mp3")
elif os.name == 'posix':  # macOS or Linux
    os.system("open chatGpt.mp3" if 'darwin' in os.sys.platform else "xdg-open chatGpt.mp3")
