import socket
serverName='localhost'
serverPort=12000

print("<><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("\t\t\t\t\t\tFIEK-UDP KLIENTI")
print("<><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("")
print("Serveri eshte duke pritur per kerkesen tuaj...")
print("")
print("\tMetodat : ")
print("")
print("IPADRESA -----> Kjo metode do te kthej IP adresen tuaj.")
print("")
print("NUMRIIPORTIT -----> Kjo metode do te kthej numrin e portit tuaj.")
print("")
print("BASHKETINGELLORE -----> Kjo metode do te kthej numrin e shkronjave qe jane bashketingellore ne fjaline tuaj.")
print("")
print("PRINTIMI -----> Kjo metode do te kthej kthen fjaline e shtypur ne tekst.")
print("")
print("EMRIIKOMPJUTERIT -----> Kjo metode do te kthej emrin e kompjuterit.")
print("")
print("KOHA -----> Kjo metode do te kthej daten dhe oren aktuale.")
print("")
print("LOJA -----> Kjo metode do te kthej 7 numra nga rangu [1,49].")
print("")
print("FIBONACCI -----> Kjo metode do te kthej gjen numrin Fibonacci ne baze ne parametrit qe ju do te jepni.")
print("")
print("KONVERTIMI -----> Kjo metode do te kthej si rezultat konvertimet varesisht opsioneve te zgjedhura nga ana juaj: \n\t\tKilowattToHorsepower\n\t\tHorsepowertoKilowatt\n\t\tDegreesToRadians\n\t\tRadiansToDegrees\n\t\tGallonsToLiters\n\t\tLitersToGallons")
print("")
print("")
print("\tNdersa metodat shtese : ")
print("")
print("SHUMEFISHI -----> Kjo metode do te kthej 20 shumefishat e pare per numrin qe shtypet. ")
print("")
print("NUMRIIFATIT -----> Kjo metode do te kthej numrin tuaj me fat per sot.")
print("")
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    sentence=input("\nJu lutem shkruani emrin e metodes qe doni te implementoni: ")
    if sentence=="":
     print("Ju lutem shkruani emrin e metodes!")
    else:
     clientSocket.sendto(sentence.encode("ASCII"),(serverName,serverPort))
     ReturnedText = clientSocket.recv(128).decode("UTF-8")
     print("\nRezultati nga implementimi i metodes eshte : "+ReturnedText)
     print("<><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    
