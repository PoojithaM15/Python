import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import os.path
import pywhatkit as kit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
import time
import cv2
import pyjokes
import PyPDF2
import pyautogui
import pygeoip
import operator
import requests
from newsapi import NewsApiClient


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wishme
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    
    speak("I am Jarvis . Please tell me how may I help you")  

    
#for news updates
def news():
        main_url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=7abb6ff6ea514689a23f6c7b096633b4'

        main_page = requests.get(main_url).json()
        #print(main_page)
        article = main_page["articles"]
        #print(articles)
        head = []
        day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
        for ar in article:
            head.append(ar["title"])
        for i in range (len(day)):
            #print(f"today's {day[i]} news is: ", head[i])
            speak(f"today's {day[i]} news is: {head[i]}")     


#To read pdf  
def pdf_reader():
        book = open('Dcn chapter1.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"Total numbers of pages in this book {pages} ")
        speak("please enter the page number i have to read")
        pg = int(input("please enter the page number:"))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)
        #jarvis speaking speed should be controlled by user   
           

#To covert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(soruce)
        # audio = r.listen(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        #speak("Say that again please...")  
        return "None"
    query = query.lower()    
    return query

    
def TaskExecution():
    wishMe() 
    while True:
        query = takeCommand()
     
       # Logic building for tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\poojitha M\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")    

        elif "send whatsapp message" in query:
            pywhatkit.sendwhatmsg('+91.......', 'Hi Bro', 15, 27)
            time.sleep(120)
            speak("message has been sent")   

        elif "play song on youtube" in query:
            kit.playonyt("Baby Shark")    
               
        elif "open google" in query:
            speak("what should i search on google") 
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")   
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Poojitha, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\poojitha m\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            #you should enter your path here

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")  

#to close any application
        elif "close notepad" in query:
            speak("okay, closing notepad")
            os.system("taskkill /f /im notepad.exe") 

        elif "close command prompt" in query:
            speak("okay, closing command prompt")
            os.system("taskkill /f /im command prompt.exe")                

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("restart /r /t 5") 

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")                        

#To open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            count = 0
            while True:
                ret, img = cap.read()
                cv2.imshow("WebCam", img)
                if not ret:
                    break;

                k=cv2.waitKey(1)

                if k%256==27:
                    #For Esc key
                    print("Close")
                    quit('q')
                    break;
                elif k%256==32:
                    #For Space key

                    print("Image "+str(count)+"saved")
                    file='C:\\Users\\poojitha M\\Desktop\\Image'+str(count)+'.jpg'
                    cv2.imwrite(file, img)
                    count +=1

            cap.release()
            cv2.destroyAllWindows     




        elif 'email to poojitha' in query:
                speak("What should I send?")
                query = takeCommand().lower()
                if "send a file" in query:
                    email = 'your mail ID@gmail.com' #your email
                    password = 'your mail ID password' #your email account password
                    send_to_email = 'sender mail ID@gmail.com' #whom you are sending the message to
                    speak("okay, what is the subject for this email")
                    query = takeCommand().lower()
                    subject = query #The Subject in the email
                    speak("and, what is the message for this email")
                    query2 = takeCommand().lower()
                    message = query2 #The Message in the email
                    speak("please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here") #The File attachment in the email

                    speak("please wait, i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.emcode_base64(part)
                    part.add_header('content.Disposition', "attachment; filename= %s" % filename)

                    #Attach the attachment to the MEMEMultipart object
                    msg.attach(part)

                    server = smtlib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to poojitha")
                else:
                    email = 'your mail ID@gmail.com' #your email
                    password = 'your mail ID password' #your password
                    send_to_email = 'sender mail ID@gmail.com' #whom you are sending the message to
                    message = query #The message in the email  

                    server = smtlib.SMTP('smtp.gmail.com', 587) #connect to the server
                    server.starttls() #use TLS
                    server.login(email, password) #Login to the email server
                    server.sendmail(email, send_to_email, message) #send the email
                    server.quit() #Logout of the email server
                    speak("email has been sent to poojitha")      

#To find my location using IP Address
        elif "where we are" in query:
            speak("wait, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://www.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry, due to network issue i am not able to find where we are.")
                pass            

#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        
#To read PDF file
        elif "read pdf" in query:
            pdf_reader()  
              
        elif "tell me news" in query:
            speak("please wait, feteching the latest news")
            news()  

#To take screenshot
        elif "take screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done, the screenshot is saved in our main folder. now i am ready for next command")  

#To calcualate
        elif "do some calculations" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                print("Listening....") 
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiplied by
                    'divided' : operator.__truediv__,  #divided
                    }[op]
            def eval_binary_expr(op1, oper, op2): #5 plus 8
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is:")
            speak(eval_binary_expr(*(my_string.split())))   


        elif "hello" in query:
            speak("hello, may i help you with something.")

        elif "how are you" in query:
            speak("i am fine, what about you.")

        elif "fine" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query:
            speak("it's my pleasure.")

        elif "you can sleep" in query:
            speak("okay, i am going to sleep you can call me anytime,")
            break                                           
       

         
if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("thanks for using me, have a good day")
            sys.exit()    

               
