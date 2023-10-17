import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import random
import openai
from config import apikey
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice' , voices[1].id) #0 for Male , 1 for Female
#print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Wishing you a pleasant start at morning!")
        print("Yennefer : Wishing you a pleasant start to your morning!")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon!")
        print("Yennefer : Good Afternoon!")
    else:
        speak("Wishing you a pleasant evening!")
        print("Yennefer : Wishing you a pleasant evening!")
        
    speak("My name is Yennefer, and I'm here to assist you.")
    print("Yennefer : My name is Yennefer, and I'm here to assist you.")
        

def takeCommand():
    # It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....just hold on for a moment....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....just hold on for a moment....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User : {query}\n")
        
    except Exception as e:
       # print(e)
        
        print("I am Sorry ! Could you please repeat that?")
        return "Nothing"
    return query
        
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('supriti.kole.56@gmail.com','eepiti@123??')
    server.sendmail('supriti.kole.56@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        
        sites = [["wikipedia","https://www.wikipedia.com"],["youtube","youtube.com"],["google","google.com"],["stack overflow","stackoverflow.com"],["amazon", "amazon.com"],["w3schools","w3schools.com"],["tutorials point","tutorialspoint.com"],["flipkart","flipkart.com"]]
        
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} for you")
                webbrowser.open(site[1])
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia....just hold on for a moment....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            print("Yennefer : According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # elif 'open google' in query:
        #     speak("Opening Google")
        #     webbrowser.open("google.com")
        # elif 'open stack overflow' in query:
        #     speak("Opening Stack Overflow")
        #     webbrowser.open("stackoverflow.com")
        # elif 'open amazon' in query:
        #     speak("Opening Amazon")
        #     webbrowser.open("amazon.com")
        # elif 'open w3schools' in query:
        #     speak("Opening W3Schools")
        #     webbrowser.open("w3schools.com")
        # elif 'open tutorials point' in query:
        #     speak("Opening Tutorials Point")
        #     webbrowser.open("tutorialspoint.com")
        # elif 'open meet' in query:
        #     speak("Opening Google Meet")
        #     webbrowser.open("https://apps.google.com/meet/?hs=197")
        # elif 'open flipkart' in query:
        #     speak("Opening Flipkart")
        #     webbrowser.open("flipkart.com")
        # elif 'open drive' in query:
        #     speak("Opening Google Drive")
        #     webbrowser.open("drive.google.com")
        # elif 'open classroom' in query:
        #     speak("Opening Google Classroom")
        #     webbrowser.open("classroom.google.com")
        if 'play music' in query:
            speak("playing Music for you")
            music_dir = 'D:\Personal\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            random_number = random.randint(0,9)
            os.startfile(os.path.join(music_dir,songs[random_number]))
            
        if "time" in query:
           strfTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(f"Yennefer : The time is {strfTime}")
           speak(f"The time is {strfTime}")
           
        if 'email to neha' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "supriti.kole.56@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                speak("Sorry...I am not able to send the email")
                print("Yennefer : Sorry...I am not able to send the email")
                
        # if "openai".lower() in query.lower():
            
           
            
        