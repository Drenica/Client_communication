from socket import *
import math
import socket
import time
import datetime
import random
import string

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Serveri eshte duke pritur per tu lidhur...")

while True:
    message, clientAddress=serverSocket.recvfrom(128)
    pergjigjja=message.decode("ASCII").split(" ")
    

    def IPADRESA():
        serverSocket.sendto(gethostbyname(gethostname()).encode("UTF-8"),clientAddress)
    
    def NUMRIIPORTIT():
        serverSocket.sendto(str(str(clientAddress[1])).encode("UTF-8"),clientAddress)

    def EMRIIKOMPJUTERIT():
        host = gethostname()
        serverSocket.sendto(str("Emri i kompjuterit eshte  " + host).encode('utf-8'), clientAddress)

    def KOHA():
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        serverSocket.sendto(str(date).encode('utf-8'), clientAddress)

    def LOJA():
        loja=[random.randint(1,49) for i in range(7)]
        serverSocket.sendto(str(loja).encode('utf-8'), clientAddress)

    def PRINTIMI(text):
        serverSocket.sendto(str(text).encode('utf-8'), clientAddress)

    def BASHKETINGELLORE(text):
        counter=0
        zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in text:
            if i not in zanoret:
                counter+=1
        serverSocket.sendto(str(str(counter)).encode('utf-8'), clientAddress)
    
    def KONVERTIMI():
        if(fusha=="KilowattToHorsepower"):
              rezultati= 1.341*(int(numer))
              serverSocket.sendto(str(str(numer)+" Kilowatt = "+ str(rezultati)+" Horsepower").encode('utf-8'), clientAddress)
        elif(fusha=="HorsepowerToKilowatt"):
              rezultati = (float(numer))/1.341 
              serverSocket.sendto(str(str(numer)+" Horsepower = "+ str(rezultati)+" Kilowatt").encode('utf-8'), clientAddress)
        elif(fusha=="DegreesToRadians"):
              rezultati = (float(numer)*math.pi)/180  
              serverSocket.sendto(str(str(numer)+" Degrees = "+ str(rezultati)+" Radians").encode('utf-8'), clientAddress)
        elif(fusha=="RadiansToDegrees"):
              rezultati = (float(numer)*180)/math.pi   
              serverSocket.sendto(str(str(numer)+" Radians = "+ str(rezultati)+" Degrees").encode('utf-8'), clientAddress)
        elif(fusha=="GallonsToLiters"):
              rezultati = (float(numer))*3.785  
              serverSocket.sendto(str(str(numer)+" Gallons = "+ str(rezultati)+" Liters").encode('utf-8'), clientAddress)
        elif(fusha=="LitersToGallons"):
              rezultati = (float(numer))/3.785
              serverSocket.sendto(str(str(numer)+" Liters = "+ str(rezultati)+" Gallons").encode('utf-8'), clientAddress)
        else:
             serverSocket.sendto(str("Shkruaj: KONVERTMI llojiikonvertimit numri!").encode('utf-8'), clientAddress)

    def FIBONACCI(text):
        d,b=1,1
        c=int(text)
        for i in range(c-1):
            d,b=b,d+b
        serverSocket.sendto(str(d).encode('utf-8'),clientAddress)

    def SHUMEFISHI(text):
        c=int(text)
        vektori=[]
        for i in range(1,21):
            c=c*i
            vektori.append(c)
            c=int(text)
        serverSocket.sendto(str(vektori).encode("ASCII"),clientAddress)


    def NUMRIIFATIT(text):
        c=int(text)
        x=random.randint(1,100)
        if(c>10 or c>100):
         serverSocket.sendto(str("Numri qe jepni duhet te jet me i madh se 1 e me i vogel se 100").encode("UTF-8"),clientAddress)
        elif(c==x):
         serverSocket.sendto(str("Numri qe keni shenuar paraqet numrin tuaj te fatit").encode("UTF-8"),clientAddress)
        else:
          serverSocket.sendto(str("Numri qe keni shenuar nuk paraqet numrin tuaj me fat sepse numri juaj me fat per sot eshte: "+str(x)).encode("UTF-8"),clientAddress)
         


    if(len(pergjigjja)==1):
        funksioni=pergjigjja[0]
        funksioni=funksioni.upper()

        if(funksioni=="IPADRESA"):
            IPADRESA()

        elif(funksioni=="NUMRIIPORTIT"):
            NUMRIIPORTIT()

        elif(funksioni=="EMRIIKOMPJUTERIT"):
            EMRIIKOMPJUTERIT()

        elif(funksioni=="KOHA"):
            KOHA()

        elif(funksioni=="LOJA"):
            LOJA()

        else:
            serverSocket.sendto(( "Keni shenuar emrin e metodes gabim!").encode('ASCII'),clientAddress)



    elif(len(pergjigjja)==2):
         funksioni=pergjigjja[0]
         funksioni=funksioni.upper()
         text=pergjigjja[1]

         if(funksioni=="PRINTIMI"):
            PRINTIMI(text)

         elif(funksioni=="BASHKETINGELLORE"):
             BASHKETINGELLORE(text)

         elif(funksioni=="FIBONACCI"):
             FIBONACCI(text) 

         elif(funksioni=="SHUMEFISHI"):
            SHUMEFISHI(text)

         elif(funksioni=="NUMRIIFATIT"):
            NUMRIIFATIT(text)



    elif(len(pergjigjja)==3):
        funksioni=pergjigjja[0]
        funksioni=funksioni.upper()
        fusha=pergjigjja[1]
        numer=pergjigjja[2]

        if(funksioni=="KONVERTIMI"):
           KONVERTIMI()
