import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (use 0 for male)

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def wish_user():
    """Greet user based on time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your personal assistant. How can I help you today?")

def take_command():
    """Listen to user command and recognize speech"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except Exception:
        print("Sorry, I didn't catch that. Please say again.")
        return "None"
    return command.lower()

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date}")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_folder = r"C:\Users\REETHA K T\Music"  # Update if needed

            if os.path.exists(music_folder):
                songs = [song for song in os.listdir(music_folder) if song.endswith(('.mp3', '.wav'))]

                if songs:
                    speak("Playing music")
                    os.startfile(os.path.join(music_folder, songs[0]))
                else:
                    speak("No music files found in the folder.")
            else:
                speak("Music folder does not exist.")

        elif 'open notepad' in query:
            os.system('notepad')

        elif 'open calculator' in query:
            os.system('calc')

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I can search that on Google for you.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

# Run the assistant
if __name__ == "__main__":
    run_assistant()
