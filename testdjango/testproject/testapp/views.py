# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:45:44 2020

@author: ADARSH
"""

from django.shortcuts import render
import speech_recognition as sr
import smtplib
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import os, time
from playsound import playsound


#global text,ch,ch1,ch2


def button(request):
    #project name
    tts = gTTS("Welcome to project voice,the main aim of the project voice is to assist the visually impaired people",'en')
    ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    tts.save(ttsname)
    playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    os.remove(ttsname)
    #choices
    print ("1. compose a email.")
    tts = gTTS("option 1. compose a email",'en')
    ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    tts.save(ttsname)
    playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    os.remove(ttsname)
    
    print ("2. Check inbox")
    tts = gTTS("option 2. Check inbox",'en')
    ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    tts.save(ttsname)
    playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    os.remove(ttsname)
    
    
    #this is for input choices
    tts = gTTS(text="May I please know your choice", lang='en')
    ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    tts.save(ttsname)
    playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
    os.remove(ttsname)
    
    #voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")
        audio=r.listen(source)
        print ("ok done!!")
    
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        tts1=gTTS("You said")
        #ch=text
        tts=gTTS(text1)
        tts1name=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
        tts.save(ttsname)
        tts1.save(tts1name)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
        os.remove(tts1name)
        os.remove(ttsname)
        
        
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts=gTTS("I could not understand you, Could you say more clearly")
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
         
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        tts=gTTS("I could not fetch results")
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
    
    
    #choices details
    if str(text1) =='compose a mail':
        tts=gTTS("You have chosen compose a mail")
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
        r = sr.Recognizer() #recognize
        with sr.Microphone() as source:
            print ("Your message :")
            tts=gTTS("Your message")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
            audio=r.listen(source)
            print ("ok done!!")
        try:
            text1=r.recognize_google(audio)
            print ("You said : "+text1)
            msg = text1
            message=text1
            tts1=gTTS("You said")
            tts=gTTS(text1)
            tts1name=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
            tts.save(ttsname)
            tts1.save(tts1name)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
            os.remove(tts1name)
            os.remove(ttsname)
                
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            tts=gTTS("I could not understand you, Could you say more clearly")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            tts=gTTS("I could not fetch results")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
            
        #EMAIL_ADDRESS=os.environ.get('EMAIL_USER')
        #EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')
        EMAIL_ADDRESS='vproject007@gmail.com'
        EMAIL_PASSWORD='iloveprogramming'
        
        
        #getting recipients email address
        r = sr.Recognizer() #recognize
        with sr.Microphone() as source:
            print ("Reciever's email address:")
            tts=gTTS("Could you please say the recipient's email address")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
            audio=r.listen(source)
            print ("ok done!!")
        try:
            ID=r.recognize_google(audio)
            print ("You said : "+ID)
            RECIEVERS_ID= ID+'@gmail.com'
            print(RECIEVERS_ID)
            tts1=gTTS("You said")
            tts=gTTS(RECIEVERS_ID)
            tts1name=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
            tts.save(ttsname)
            tts1.save(tts1name)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail1.mp3")
            os.remove(tts1name)
            os.remove(ttsname)
            ID=RECIEVERS_ID
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            tts=gTTS("I could not understand you, Could you say more clearly")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            tts=gTTS("I could not fetch results")
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
    
        
        with smtplib.SMTP('smtp.gmail.com',587)as smtp:#host and port area
            smtp.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
            smtp.starttls() #security connection
            smtp.ehlo
            smtp.login('vproject007@gmail.com','iloveprogramming') #login part
            smtp.sendmail(EMAIL_ADDRESS,'vproject007@gmail.com',msg) #send part
            print ("Congratulations! Your mail has been sent. ")
            tts = gTTS("Congratulations! Your mail has been sent...... Thank You ",'en')
            ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            tts.save(ttsname)
            playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
            os.remove(ttsname)
            sent="congratulations your mail has been sent"
            smtp.close()
    
    #check inbox
    if str(text1) == 'check inbox': 
        mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
        #unm = ('your mail/ victim mail')  #username
        #psw = ('pswrd')  #password
        mail.login('vproject007@gmail.com','iloveprogramming')  #login
        stat, total = mail.select('Inbox')  #total number of mails in inbox
        print("Number of mails in your inbox :"+str(total))
        tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
        
        #search mails
        result, data = mail.uid('search',None, "ALL")
        inbox_item_list = data[0].split()
        new = inbox_item_list[-1]
        old = inbox_item_list[0]
        result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
        raw_email = email_data[0][1].decode("utf-8") #decode
        email_message = email.message_from_string(raw_email)
        print ("From: "+email_message['From'])
        print ("Subject: "+str(email_message['Subject']))
        tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
        #Body part of mails
        stat, total1 = mail.select('Inbox')
        stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
        msg = data1[0][1]
        soup = BeautifulSoup(msg, "html.parser")
        txt = soup.get_text()
        print ("Body :"+txt)
        tts = gTTS(text="Body: "+txt, lang='en')
        ttsname=(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        tts.save(ttsname)
        playsound(r"C:\Users\ADARSH\Desktop\testdjango\testproject\testproject\mail.mp3")
        os.remove(ttsname)
        mail.close()
        mail.logout()
    
    return render(request,'home.html')
    
