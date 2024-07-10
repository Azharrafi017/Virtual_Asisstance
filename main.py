import speech_recognition as sr
import webbrowser
import pyttsx3
import musicDictionary
recognizer=sr.Recognizer()
listen=pyttsx3.init()

def speak(text):
    listen.say(text)
    listen.runAndWait()

def processCommand(c):
    print(c)
    if "open google"in c.lower():
        webbrowser.open("https://www.google.com/")
    if "open youtube"in c.lower():
        webbrowser.open("https://www.youtube.com/")
    if "open instagram"in c.lower():
        webbrowser.open("https://www.instagram.com/")
    if "open linkedin"in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "play" in c.lower():
        song=c.lower()[5:len(c)]
        if song in musicDictionary.music.keys():
            webbrowser.open(musicDictionary.music[song])
            return
        command=song.split(" ")[0]
        print("/ncommand ", command)
        for key, value in musicDictionary.music.items():
            if command in key:
                webbrowser.open(value)
                return
    

if(__name__=="__main__"):
    speak(" Initializing Jarvis... ")

    #obtain audio from the microphone
    while True :
    
            try:
             # using google speech recognition
                with sr.Microphone() as source:  
                    print("Listening...")
                    audio_text = recognizer.listen(source,timeout=2,phrase_time_limit=2)
                    
                word=recognizer.recognize_google(audio_text)
                print(word)
                if(word.lower()=="jarvis"):
                    speak("ya")
                    with sr.Microphone() as source:  
                        print("Jarvis Active...")
                        audio = recognizer.listen(source,timeout=3,phrase_time_limit=3)
                        command=recognizer.recognize_google(audio)
                        processCommand(command)
                    
            
            except Exception as e:
                print("Error; {0}".format(e))
