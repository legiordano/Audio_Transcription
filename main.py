import speech_recognition as sr

r = sr.Recognizer()

def transcribe_audio():
    with sr.Microphone() as source:
        print("Listening... Say something!")
        audio = r.listen(source)
    
    try:
        print("Transcribing...")
        text = r.recognize_google(audio)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

transcribe_audio()