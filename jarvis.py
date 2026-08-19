import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5' if os.name == 'nt' else 'espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male voice, 1 for female voice
engine.setProperty('rate', 175)             # Speed of the voice

def speak(audio):
    """Makes JARVIS speak the given text string."""
    print(f"JARVIS: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the current time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS, sir. How may I help you today?")

def take_command():
    """Listens to the microphone and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        # Logic for executing tasks based on commands
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("I couldn't find any relevant results, sir.")

        elif 'open youtube' in query:
            speak("Opening YouTube, sir.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google, sir.")
            webbrowser.open("google.com")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'open code' in query:
            # Update this path to match your local installation if needed
            code_path = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(code_path):
                speak("Opening Visual Studio Code, sir.")
                os.startfile(code_path)
            else:
                speak("Visual Studio Code path not found, sir.")

        elif 'shutdown' in query or 'goodbye' in query:
            speak("Goodbye sir. Have a productive day!")
            break
