from socket import *
from _thread import *
import socket
import math
import random
import sys
import datetime
import time




print("<><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("\t\t\t\t\tFIEK-TCP SERVERI")
print("<><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("")
print("Serveri eshte aktivizuar.")
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)


def clientthread(msg):
    message=msg.recv(128)
    modifiedMessage=message.decode().split(" ")
    

    def IPADRESA():
        msg.send(str("IP adresa juaj eshte: ").encode("ASCII")+(gethostbyname(gethostname()).encode('ASCII')))
    

    def NUMRIIPORTIT():
        msg.send(str("Porti juaj eshte: ").encode("ASCII")+str(str(clientAddress[1])).encode('ASCII'))
    

    def BASHKETINGELLORE(text):
        counter=0
        zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in text:
            if i not in zanoret:
                counter+=1
        msg.send(str("Numri i bashketingelloreve ne tekstin tuaj eshte: ").encode("ASCII")+str(counter).encode('ASCII'))
        msg.close()
    

    def PRINTIMI(text):
         msg.send(("Teksti qe keni shkruar eshte: ").encode("ascii")+str(text).encode('ASCII'))
         msg.close()


    def EMRIIKOMPJUTERIT():
     try:
        host = gethostname()
        msg.send(("Emri i kompjuterit eshte: ").encode("ASCII")+str(host).encode("ASCII"))
     except socket.error:
         msg.send(("Emri i kompjuterit nuk dihet.").encode("ASCII"))
     msg.close()



    def KOHA():
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        msg.send(("Data e sotme dhe koha per momentin eshte: ").encode("ascii")+str(str(date)).encode("ASCII"))
        msg.close()



    def LOJA():
            loja=[random.randint(1,49) for i in range(7)]
            msg.send(("7 numra te rastesishem nga 1-49 jane: ").encode("ascii")+str(str(loja)).encode("ASCII"))
            msg.close()
    

    def KONVERTIMI():
          if(text=="KilowattToHorsepower"):
                conversion = 1.341*(int(numri))
                msg.send(str(str(numri)+" Kilowatt = "+ str(conversion)+" Horsepower").encode("ASCII"))
       
          elif(text=="HorsepowerToKilowatt"):
                conversion = (float(numri))/1.341
                msg.send(str(str(numri)+" Horsepower = "+ str(conversion)+" Kilowatt").encode("ASCII"))

          elif(text=="DegreesToRadians"):
                conversion = (float(numri)*math.pi)/180
                msg.send(str(str(numri)+" Degrees = "+ str(conversion)+" Radians").encode("ASCII"))
     
          elif(text=="RadiansToDegrees"):
                conversion = (float(numri)*180)/math.pi
                msg.send(str(str(numri)+" Radians = "+ str(conversion)+" Degrees").encode("ASCII"))
           
          elif(text=="GallonsToLiters"):
                conversion = (float(numri))*3.785
                msg.send(str(str(numri)+" Gallons = "+ str(conversion)+" Liters").encode("ASCII"))
               
          elif(text=="LitersToGallons"):
                conversion = (float(numri))/3.785
                msg.send(str(str(numri)+" Liters = "+ str(conversion)+" Gallons").encode("ASCII"))
               
          else:
                msg.send("Shkruaj: KONVERTMI llojiikonvertimit numri ".encode('ASCII'))
                msg.close()


    def FIBONACCI(text):
        d,b=1,1
        c=int(text)
        for i in range(c-1):
            d,b=b,d+b
        msg.send(str("Numri fibonacci eshte : ").encode("ASCII")+str(d).encode('utf-8'))
        


    def SHUMEFISHI(teksti):
        c=int(teksti)
        vektori=[]
        for i in range(1,21):
            c=c*i
            vektori.append(c)
            c=int(teksti)
        msg.send(str("Shumefishat per numrin e dhene ").encode("ASCII")+str(c).encode("ASCII")+str(" jane: ").encode("ASCII")+str(vektori).encode("ASCII"))
        msg.close()



    def NUMRIIFATIT(teksti):
        c=int(teksti)
        x=random.randint(1,100)
        if(c<1 or c>100):
         msg.send(str("Numri qe jepni duhet te jet me i madh se 1 e me i vogel se 100").encode("ASCII"))
        elif(c==x):
         msg.send(str("Numri qe keni shenuar paraqet numrin tuaj te fatit").encode("ASCIS"))
        else:
         msg.send(str("Numri qe keni shenuar nuk paraqet numrin tuaj me fat sepse numri juaj me fat per sot eshte: ").encode("ASCII")+str(x).encode("ASCII"))


    array=["KilowattToHorsepower","HorsepowertoKilowatt","DegreesToRadians","RadiansToDegrees","GallonsToLiters","LitersToGallons"]
    array1=["IPADRESA","NUMRIIPORTIT","EMRIIKOMPJUTERIT","KOHA","LOJA","BASHKETINGELLORE","PRINTIMI","FIBONACCI","SHUMEFISHI","NUMRIIFATIT","KONVERTIMI"]

    if(len(modifiedMessage)==1):
      funksioni = modifiedMessage[0]
      funksioni=funksioni.upper()
      if(funksioni in array1): 

        if (funksioni=="IPADRESA"):
            IPADRESA()

        elif (funksioni=="NUMRIIPORTIT"):
            NUMRIIPORTIT()

        elif (funksioni=="EMRIIKOMPJUTERIT"):
            EMRIIKOMPJUTERIT()

        elif (funksioni=="KOHA"):
            KOHA()

        elif (funksioni=="LOJA"):
           LOJA()

      else:
         msg.send(("Keni bere gabim gjate shkrimit te emrit te metodes ose nuk keni shenuar parametrat e metodes.").encode('ASCII'))

    elif(len(modifiedMessage)==2):
       funksioni = modifiedMessage[0]
       funksioni=funksioni.upper()
       text=modifiedMessage[1]
       if(funksioni in array1): 

        if(funksioni=="BASHKETINGELLORE"):
             BASHKETINGELLORE(text)

        elif(funksioni=="PRINTIMI"):
             PRINTIMI(text)

        elif(funksioni=="FIBONACCI"):
            if((text>='a' and text<='z') or (text>='A' and text<='Z')):
                msg.send(("Ju lutem shtypni nje numer!").encode("ASCII"))
            else: 
                FIBONACCI(text)


        elif(funksioni=="SHUMEFISHI"):
            if((text>='a' and text<='z') or (text>='A' and text<='Z')):
                msg.send(("Ju duhet te shenoni numer!").encode("ASCII"))
            else: 
                SHUMEFISHI(text)


        elif(funksioni=="NUMRIIFATIT"):
            if((text>='a' and text<='z') or (text>='A' and text<='Z')):
                msg.send(("Ju duhet te shenoni nje numer me te madh se 1 e me te vogel se 100!").encode("ASCII"))
            else: 
                NUMRIIFATIT(text)

       else:
           msg.send(("Keni bere gabim gjate shkrimit te emrit te metodes ose nuk keni shenuar parametrat e metodes.").encode("ASCII"))


    elif(len(modifiedMessage)==3):
       funksioni=modifiedMessage[0]
       funksioni=funksioni.upper()
       text=modifiedMessage[1]
       numri=modifiedMessage[2]
       if(funksioni in array1): 

        if(funksioni=="KONVERTIMI"):
            if(text in array and numri ==""):
                msg.send(("Ju duhet te shtoni parametrat per konvertim!").encode("ASCII"))
            elif(text in array): 
                if((numri>='a' and numri<='z') or (numri>='A' and numri<='Z')):
                 msg.send(("Per konvertim ju duhet te jepni numer e jo shkronje!").encode("ASCII"))
                else:
                 KONVERTIMI()
            else:
                msg.send(("Keni shkruar gabim llojin per konvertim!").encode("ASCII"))
       else:
          msg.send(("Keni bere gabim gjate shkrimit te emrit te metodes!").encode("ASCII"))

while 1:
    msg,clientAddress=serverSocket.accept()
    print("Serveri eshte i lidhur me: "+ gethostbyname(gethostname())+"   "+str(clientAddress[1]))
    start_new_thread(clientthread,(msg,))
serverSocket.close()
