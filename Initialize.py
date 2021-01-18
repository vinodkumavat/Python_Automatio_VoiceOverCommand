import datetime
#for speak funtion
import pyttsx3

#takeCommand function
import speech_recognition as sr

#Apnawikipedia function
import wikipedia

#Chrome function
import webbrowser

#for window's function
import os
import  random

#For myMail Function
import smtplib
import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials



#For speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Start with greeting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning, Vinod")
    elif hour<=12 and hour<18:
        speak("Good afternoon, Vinod")
    else:
        speak("Good evening, Vinod")
    speak("I am virtual assistant. How may I help you sir?")



#For listening
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said --> {query}\n")
    except Exception as e:
        print("Try again please....")
        return "None"
    return query



#Wikipedia
def Apnawikipedia(query):
    speak("Searching wikipedia..")
    results = wikipedia.summary(query, sentences=1)
    speak("According to wikipedia")
    print(results)
    speak(results)



#Executes chrome's task
def Chrome(website_name):
    chrome_location = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

    if website_name == "youtube":
        speak("Opening youtube")
        chrome_location.open_new_tab("youtube.com")
    elif website_name == "google":
        speak("Opening google")
        chrome_location.open_new_tab("google.com")
    elif website_name == "email":
        speak("Opening all mails")
        chrome_location.open_new_tab("https://mail.google.com/mail/u/0/")
        chrome_location.open_new_tab("https://mail.google.com/mail/u/1/")
        chrome_location.open_new_tab("https://mail.google.com/mail/u/3/")
    elif website_name == "drive":
        speak("Opening google drive")
        chrome_location.open_new_tab("https://drive.google.com/drive/u/1/my-drive")
    elif website_name == "college":
        speak("Opening College notice")
        chrome_location.open_new_tab("http://www.svnit.ac.in/web/notice_events_tenders.php?tag=notice")
    elif website_name == 'team':
        speak("Opening microsoft team")
        chrome_location.open_new_tab("https://teams.microsoft.com/")
    elif website_name == 'meet':
        speak("Opening Google meet")
        chrome_location.open_new_tab("https://meet.google.com/?authuser=1")
    elif website_name == "mailupdate":
        speak("Opening sheet for update")
        chrome_location.open_new_tab("https://docs.google.com/spreadsheets/d/1scJXUm40Gr5G-1vh2U_lJOJuxqKK-gkGBODb3u1wo5g/edit#gid=0")



#Executes window's basic commands
def WindowsCommands(task):
    if task == "music":
        speak("Playing music")
        music_location = "E:\\Mine\\Music"
        songs_list = os.listdir(music_location)
        i = random.randrange(0, len(songs_list)-1)
        os.startfile(os.path.join(music_location, songs_list[i]))
        return songs_list[i]
    elif task == "code":
        speak("Open Visual Studio Code")
        vscode_location = "C:\\Users\\Vinod\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vscode_location)
    elif task == "chrome":
        speak("Opening Chrome")
        chrome_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        os.startfile(chrome_location)


#mail funtion
def myMail():
    print("\tTo whom??")
    speak("To whom")
    name = takeCommand().lower()
    
    #Take data from google spreadsheet
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Contact_Details").sheet1

    #verifying google spreadsheet data with given data
    count = 0
    for i in range(2, len(sheet.get_all_records())+2):
        row = sheet.row_values(i)
        if name != (row[0].lower()):
            count = count + 1
        else:
            break

    if count == (len(sheet.get_all_records())):
        speak("Not in list want to try again")
        print("\t[ Yes/No ]")
        _command = takeCommand().lower()
        if _command == "yes":
            myMail()
        else:
            return
    else:
        print("\tWhat to send??")
        speak("What to send")
        message_text = takeCommand()
        message = f"From: vinodkumawat9167@gmail.com\r\n" + f"To: {sheet.row_values(count+2)[2]}\r\n" + f"Subject: Python_Automation\r\n" + "\r\n" + f"{message_text}"
        _to = sheet.row_values(count+2)[2]
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        _from = "vinodkumawat9167@gmail.com"
        password = os.environ.get('mail_password')
        server.login(_from, password)
        server.sendmail(_from, _to , message)
        server.quit()
        print(f"\t\tMail has been sended successfully to {name}")
        speak(f"Mail has been sended successfullly to {name}")





''' ******************************* Main Execution began from here ******************************* '''
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            Apnawikipedia(query)
        elif 'open youtube' in query:
            Chrome("youtube")
        elif 'open google' in query:
            Chrome("google")
        elif 'open email' in query:
            Chrome("email")
        elif 'open drive' in query:
            Chrome("drive")
        elif 'college notice' in query:
            Chrome("college")
        elif 'open meet' in query:
            Chrome("meet")
        elif 'open team' in query:
            Chrome('team')
        elif 'play music' in query:
            WindowsCommands("music")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            WindowsCommands("code")
        elif 'open chrome' in query:
            WindowsCommands("chrome")
        elif 'send mail' in query:
            myMail()
        elif 'update mail list' in query:
            Chrome("mailupdate")
        elif 'quit' in query:
            speak("Exiting sir, have a good day")
            exit()
            

            

            