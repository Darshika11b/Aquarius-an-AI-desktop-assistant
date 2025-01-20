import pyttsx3
import speech_recognition  # type: ignore
import requests
import os
import pyautogui
import random



for i in range(3):
    a = input("Enter Password to open Aquarius :- ")
    pw_file = open("password.txt","3")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        
        from INTRO import play_gif
play_gif



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                
                elif "change password" in query:
                 speak("What's the new password")
                 new_pw = input("Enter the new password\n")
                 new_password = open("password.txt","w")
                 new_password.write(new_pw)
                 new_password.close()
                 speak("Done sir")
                 speak(f"Your new password is{new_pw}")
                 
                elif "schedule my day" in query:
                 tasks = [] #Empty list 
                 speak("Do you want to clear old tasks (Plz speak YES or NO)")
                 query = takeCommand().lower()
                 if "yes" in query:
                  file = open("tasks.txt","w")
                  file.write(f"")
                  file.close()
                 no_tasks = int(input("Enter the no. of tasks :- "))
                 i = 0
                 for i in range(no_tasks):
                  tasks.append(input("Enter the task :- "))
                 file = open("tasks.txt","a")
                 file.write(f"{i}. {tasks[i]}\n")
                 file.close()
                elif "no" in query:
                 i = 0
                 no_tasks = int(input("Enter the no. of tasks :- "))
                 for i in range(no_tasks):
                   tasks.append(input("Enter the task :- "))
                   file = open("tasks.txt","a")
                   file.write(f"{i}. {tasks[i]}\n")
                   file.close()
                   
                elif "show my schedule" in query:
                 file = open("tasks.txt","r")
                 content = file.read()
                 file.close()
                 notification.notify(
                  title = "My schedule :-",
                 message = content,
                  timeout = 15
        )
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    
                elif "play a game" in query:
                    from game import game_play
                    game_play()
                    
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")


                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                        exit()

                    
                    else:
                        pass

                elif "show my focus" in query:
                     from FocusGraph import focus_graph
                     focus_graph()
                     
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("Aquarius","")
                    query = query.replace("translate","")
                    translategl(query)



                
#conversation
elif "hello" in query:
    speak("Hello sir, how are you ?")
elif "i am fine" in query:
    speak("that's great, sir")
elif "how are you" in query:
    speak("Perfect, sir")
elif "thank you" in query:
     speak("you are welcome, sir")
            
#web searching
elif "google" in query:
    from SearchNow import searchGoogle
    searchGoogle(query)
elif "youtube" in query:
    from SearchNow import searchYoutube
    searchYoutube(query)
elif "wikipedia" in query:
    from SearchNow import searchWikipedia
    searchWikipedia(query)

#Temperature
elif "temperature" in query:
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")
elif "weather" in query:
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")
    
#Time
elif "the time" in query:
    strTime = datetime.datetime.now().strftime("%H:%M")    
    speak(f"Sir, the time is {strTime}")

#Sleep
elif "finally sleep" in query:
    speak("Going to sleep,sir")
    exit()
    
#Open and Close apps/websites
elif "open" in query:
    from Dictapp import openappweb
    openappweb(query)
elif "close" in query:
    from Dictapp import closeappweb
    closeappweb(query)

#Alarm
elif "set an alarm" in query:
    print("input time example:- 10 and 10 and 10")
    speak("Set the time")
    a = input("Please tell the time :- ")
    alarm(a)
    speak("Done,sir")

#Above (if __name__ = "__main__")  write this function :-
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
  elif "pause" in query:
    pyautogui.press("k")
    speak("video pause")
  elif "play" in query:
    pyautogui.press("k")
    speak("video played")
  elif "mute" in query:
    pyautogui.press("m")
    speak("video muted")

  elif "volume up" in query:
    from keyboard import volumeup
    speak("Turning volume up,sir")
    volumeup()
  elif "volume down" in query:
    from keyboard import volumedown
    speak("Turning volume down, sir")
    volumedown()
    
    elif "tired" in query:
     speak("Playing your favorite songs, sir")
    a = (1,2,3) # You can choose any number of songs (I have only chosen 3)
    b = random.choice(a)
    if b==1:
    webbrowser.open(#Here put the link of your video)

  elif "news" in query:
    from NewsRead import latestnews
    latestnews()

elif "calculate" in query:
    from Calculatenumbers import {% load WolfRamAlpha_tags %}
    from Calculatenumbers import Calc
    query = query.replace("calculate","")
    query = query.replace("Aquarius","")
    Calc(query)

elif "whatsapp" in query:
    from Whatsapp import sendMessage
    sendMessage()

elif "shutdown the system" in query:
    speak("Are You sure you want to shutdown")
    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
    if shutdown == "yes":
        os.system("shutdown /s /t 1")

    elif shutdown == "no":
        break


