import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import smtplib
import os.path
import instaloader
import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)
#engine.setProperty('rate',180-200)   #speech rate


#text to speech 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
#voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=8)
        
    try:
        print("Recognizing..........")
        query=r.recognize_google(audio,language='en-in')
        print("user said : {}".format(query))
    
    except Exception as e:
        speak("say that again please .....")
        return "none"
    query=query.lower()
    return query 


#to wish 
def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M:%p")
    
    if(hour>=0 and hour<=12):
        speak(f"good morning, its {tt}")
    elif(hour>=12 and hour <=18):
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good good evening, its {tt}")
    speak("i am jarvis . please tell me how may i help you")
    
#to send mail 
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) #verify the server
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ID','YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ID',to,content)
    
#pdf reader   
def pdf_reader():
    book = open('book.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("please enter the page number to read")
    pg=int(input("enter the page number: "))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak(text)
    
    
def taskexecution():
    speak("verification successfull")
    speak("welcome back vishnu")
    wish()
    while True:
        query  = takecommand().lower()
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("what should i do next")
        elif "close notepad" in query:
            speak("okay closing notepad")
            os.system("taskkill /f /im notepad.exe")
            speak("what should i do next")
            
        elif "open ms word" in query:
            speak("okay opening microsoft word")
            npath = "C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(npath)
            speak("what should i do next")
        elif "close ms word" in query:
            speak("okay closing microsoft word")
            os.system("taskkill /f /im WINWORD.EXE")
            speak("what should i do next")  
        
        elif "open ppt" in query:
            speak("okay opening microsoft power point")
            npath = "C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(npath)
            speak("what should i do next")
        elif "close ppt" in query:
            speak("okay closing microsoft powerpoint")
            os.system("taskkill /f /im POWERPNT.EXE")
            speak("what should i do next")
        
        elif "open excel" in query:
            speak("okay opening excel")
            npath = "C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(npath)
            speak("what should i do next")
        elif "close excel" in query:
            speak("okay closing microsoft excel")
            os.system("taskkill /f /im EXCEL.EXE")
            speak("what should i do next")
               
        elif "open command prompt" in query:
            os.system("start cmd")
            speak("what should i do next")
            
        elif "open camera" in query:
            vid = cv2.VideoCapture(0)
            k=0
            while(k<20):
                ret, frame = vid.read()
                cv2.imshow('frame', frame)
                k+=1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            vid.release()
            cv2.destroyAllWindows()
            speak("camera opened successfully")
            speak("what should i do next")

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")
            
       
        elif "play music" in query:
            speak(f'No music available')
        
        elif "ip address" in query:
            
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            speak("what should i do next")
            
        elif "wikipedia" in query:
            speak("searching in wikipedia.........")
            query = query.replace("wikipedia","")
            try:
                results = wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
            except:
                speak("No page found")
                
            speak("what should i do next")
                
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
            speak("what shoulf i play on youtube")
            cm = takecommand().lower()
            kit.playonyt(cm)
            
            speak("what should i do next")
            
            
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            speak("enter the username to search")
            name=input("Enter the user name: ")
            webbrowser.open(f"www.instagram.com/{name}")
            #speak("Here is user profile of the user",name)
            time.sleep(5)
            speak("Would you like to download profile picture of this account")
            condition =  takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("image downloaded and it is saved in main folder")
            else:
                pass
            
            speak("what should i do next")
        
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please hod the screen for few seconds, i am taking the screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done and image is saved in folder")
            speak("what should i do next")
                
        
        elif "open google" in query:
            speak("what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("what should i do next")
            
        elif "send whatsapp message" in query:
            #taking more time
            kit.sendwhatmsg("+91XXXXXXX","hello",2,36)#hr and min should be checked
            #time.sleep(10)
            speak("message has been sent")
            speak("what should i do next")
        
        #login not working
        elif "send email" in query:
            speak("what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email='your gmail'
                password='your password'
                send_to_email='reciver mail id'
                speak("okay, what is the subject for this email")
                query = takecommand().lower()
                subject=query
                speak("and, what is message for this email")
                query2=takecommand().lower()
                message=query2
                speak("please enter the correct path of the file into shell")
                file_loc=input("enter the path here")
                speak("the email is sending now")
                
                msg=MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['Subject']=subject
                msg.attach(MIMEText(message,'plain'))
                
                #Setup attchment
                filename=os.path.basename(file_loc)
                attachment=open(file_loc,"rb")
                part=MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment;filename=%s"%filename)
                msg.attach(part) 
                
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                text=msg.as_string()
                server.sendmail(email,send_to_email,text)
                server.quit()
                speak("email has been sent")
            else:
                email='your mail'
                password='your password'
                send_to_email='reciver mail'
                message=query
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                text=msg.as_string()
                server.sendmail(email,send_to_email,text)
                server.quit()
                speak("email has been sent")
            speak("what should i do next")
                
        
            
        
        
        elif "set alarm" in query:
           speak("please tell me the time to set alarm. for example set alarm to 5:50 a.m")
           tt=takecommand()
           tt.replace("set alarm to ","")#5:30 a.m.
           tt.replace(".","") #5:30 am
           tt.upper() #5:30 AM
           import MyAlarm
           MyAlarm.alarm(tt)
           
           speak("what should i do next")
               
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            speak("what should i do next")
            
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
        
        elif 'switch the windown' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")   
            speak("what should i do next")
            
        elif "hello" in query or "hey" in query:
            speak("hello, may i help you with something")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
        elif "how are you" in query:
            speak("i am fine, what about you")
        
        elif "fine" in query or "good" in query:
            speak("that's great to here from you")
        elif "not fine" in query or "sad" in query:
            speak("that's not good take some rest")
        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure")
        elif "you can sleep" in query or "sleep now" in query:
            speak("okay, i am going to sleep call me anytime")
            break 
        
       
        elif "temperature" in query:
            speak("Tell me which city temp you want to know")
            search = takecommand()
            if "temperature in " in search:
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")# a Python library for pulling data out of HTML and XML file
                temp=data.find("div",class_="BNeawe").text
                speak(f"The current {search} is {temp}")
                
            else:
                speak("Sorry, command not recognized") 
            speak("what should i do next")
                
        
        elif "activate how to do mod" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how=takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay, how to do mode closed")
                    else:
                        max_results=1
                        how_to=search_wikihow(how,max_results)
                        assert len(how_to) == 1 
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry, i am unable to find this")
            speak("what should i do next")
        
        
        elif 'battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage=battery.percent
            speak(f"the system have {percentage} percent battery")    
        
        elif "internet speed" in query or "network speed" in query:
            import speedtest
            
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("No internet connection")
            speak("what should i do next")
                        
        elif "send sms" in query:
            from twilio.rest import Client
            speak("what should i say")
            account_sid = ''
            auth_token=''
            client = Client(account_sid,auth_token)
            message = client.messages \
                .create(
                    
                    body=takecommand(),
                    from_='+1XXXXXX', #should be verified
                    to = '+91XXXXXXX'
                )
            print(message.sid)
            speak("message sent successfully")
            
        elif "make a call" in query:
            from twilio.rest import Client
            account_sid = ''
            auth_token=''
            client = Client(account_sid,auth_token)
            call = client.calls.create(
                    twiml='<Response><Say>hello this a bot call</Say></Response>',
                    from_='+18XXXXXX', #should be verified
                    to = '+91XXXXXXX'
                )
            print(call.sid)
            speak("what should i do next")
        
        
        elif "open mobile camera" in query:
            import urllib.request
            import numpy as np
            import time
            url= "https://25.145.60.171.8080/sample.jpg"
            while True:
                img_arr=np.array(bytearray(urllib.request.urlopen(url).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q=cv2.waitKey(1)
                if q==ord("q"):
                    break
             
if __name__=="__main__":
    
    recognizer=cv2.face.LBPHFaceRecognizer_create()#local binary patterns histograms
    recognizer.read('trainer/trainer.yml')
    casecadepath="haarcascade_frontalface_default.xml"
    faceCascade=cv2.CascadeClassifier(casecadepath)

    font=cv2.FONT_HERSHEY_SIMPLEX
    id=2
    names=['','vishnu'] #frist empty bcoz starts with 0

    cam =cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(3,640)#width
    cam.set(4,480)#height
    #defining min window size to be recognized
    minW =0.1*cam.get(3)
    minH=0.1*cam.get(4)

    while True:
        ret,img=cam.read()
        converted_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(
            converted_img,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW),int(minH)),
            )
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,accuracy=recognizer.predict(converted_img[y:y+h,x:x+h])
            print(id,"          ",accuracy)#used to predict
            if(accuracy<100):
                id=names[id]
                accuracy=" {0}%".format(round(100-accuracy))
                taskexecution()
            else:
                id="unknown"
                accuracy=" {0}%".format(round(100-accuracy))
                speak("verification failed please try again")
            cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
            cv2.putText(img,str(accuracy),(x+5,y-5),font,1,(255,255,0),1)
        cv2.imshow('camera',img)
        k=cv2.waitKey(10)&0xff #press esc for exit
        if k==27:
            break
        
    speak("thanks for using")
    cam.release()
    cv2.destroyAllWindows()
        
            
                
            
                
                    
                    