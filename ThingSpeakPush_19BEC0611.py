import os
import time
import sys
import random
import urllib
import urllib.request
n=72
while (n!=0):
    	senva1= random.randrange(0,50)
    	senva2= random.randrange(0,100)
    	senva3= random.randrange(0,100)
    	senva4= random.randrange(0,100)
    	senva5= random.randrange(0,100)
    	print(senva1)
    	print(senva2)
    	print(senva3)
    	print(senva4)
    	print(senva5)
    	b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=8BHAVW82IGR00XAV&field1=' + str(senva1)+ '&field2=' + str(senva2)+ '&field3=' + str(senva3)+ '&field4=' + str(senva4)+ '&field5=' + str(senva5))
    	time.sleep(5)
    	print(b.read())
    	n=n-1
print('end')
