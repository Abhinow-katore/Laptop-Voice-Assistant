import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5') # nsss, espeak
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good moring")
    elif hour>=12 and hour<18:
        speak("good after noon")
    else:
        speak("good evening")
    speak("woof ! hello abhinav what can i do for you")

def takeCommand():
    #it takse microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source) #,timeout=1,phrase_time_limit=10
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # for voice recognition.
        print(f"User said: {query}\n")  #our query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


'''email sending part commented, ue to risk of less secure app'''
"""def sendEmail(to, content):
    server smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login('shicnhan@gmail.com', 'himawari')
    server.sendEmail('shicnhan@gmail.com', to, content)
    server.close()"""

    

if __name__ == "__main__":
        speak("woof, hello abhinav, how may i help you")
        if 1 :
            query = takeCommand().lower()
            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)     
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")  
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open github' in query:
                webbrowser.open("github.com")    
            elif 'play music' in query:
                music_dir = 'C:\\Users\\91957\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'open visual code' in query:
                codepath = "C:\\Users\\91957\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                
           




