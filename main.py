import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Create a speech recognition object
recognizer = sr.Recognizer()

# Use a microphone as the audio source
with sr.Microphone() as source:
    print("...listening")
    
    try:
        # Adjust for ambient noise and listen to the user's speech
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")

        # Speak the recognized text
        engine.say(text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    except sr.WaitTimeoutError:
        print("Timeout waiting for the microphone to be ready. Make sure it is connected and functioning.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
