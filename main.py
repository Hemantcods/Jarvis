import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import client
from gtts import gTTS
from playsound import playsound
import os


name="friday"
status=False
engine=pyttsx3.init()
def oldspeak(sentence):   #for google text to speech
    language = 'en'  # English, change to 'hi' for Hindi
    tts = gTTS(text=sentence, lang=language, slow=False)

    # Save the speech to a file with absolute path
    file_path = os.path.abspath("output.mp3")
    tts.save(file_path)

    # Play the audio using the absolute path
    playsound(file_path)
    os.remove(file_path)

def speak(sentence): 
     # Set properties (Speed, Volume, and Voice)
    rate = engine.getProperty('rate')  # Get the current speech rate
    engine.setProperty('rate', rate - 10000)  # Decrease the rate (speed)

    volume = engine.getProperty('volume')  # Get the current volume
    engine.setProperty('volume', 1)  # Set volume to max (1.0)

    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[1].id)  # Change to the second voice (usually a female voice)

    # Speak the sentence
    engine.say(sentence)
    engine.runAndWait()

def recognise():
         # obtain audio from the microphone
            with sr.Microphone() as source:
                    r = sr.Recognizer()
                    print("Listening...")
                    audio=r.listen(source)
                    print("recognising.....")
            word=r.recognize_google(audio)
            return word
 
def processcommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com/")
        speak("Opening google,sir")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com/")
        speak("Opening Youtube,sir")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://www.linkedin.com/feed/?doFeedRefresh=true&nis=true&lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3B5vMP3V0DQl20fabn%2BIZn7g%3D%3D")
        speak("Opening Linkedin,sir")
    elif(c.lower().startswith("play")):
        song=c.lower().split(" ")[1] 
        link=musiclibrary.music[song] 
        webbrowser.open(link)
        speak("playing"+song)  
    # elif("news" in c.lower() ):
    #     response=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    #     if response.status_code == 200:
    #             data = response.json()
    #             headlines = [article['title'] for article in data['articles']]
    #             try:
    #                 for i, headline in enumerate(headlines, 1):
    #                      H=f"{i}. {headline}"
    #                      speak(H)
    #             except Exception as e:
    #                  H="No news avilable sir.."
    #     else:
    #          print(f"Error: {response.status_code}")  
    elif("search" in c.lower() and "on youtube" in c.lower()):
        search=((c.lower().replace("search","")).replace("on youtube",""))
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
    else:
         #let open ai handle the request
        a=client.ai(c)
        print(a)
        speak(a)                        
if __name__=="__main__":
    speak(f"Initialising {name}...")
    #listen for the wake word "jarvis"
    while True:
        r = sr.Recognizer()
           # recognize speech using Sphinx
        
        try:
            word=recognise()
            if(word.lower()==name):
                    speak("yes sir, how can i help you!!")
                #listen for command
                    print(f"{name} Active...")
            command=recognise()
            print(command)
            processcommand(command)
            
        

            
        
                        

        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))