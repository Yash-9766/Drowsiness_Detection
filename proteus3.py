import RPi.GPIO as GPIO
import time 

trigg = 37
echo = 40
GPIO.setmode(GPIO.BOARD)
while True:
    print("Distance measuring : ")
    GPIO.setup(trigg,GPIO.OUT)
    GPIO.setup(echo,GPIO.OUT)
    GPIO.output(trigg,True)
    time.sleep(0.00001)
    GPIO.output(trigg,False)
    while GPIO.input(echo)==0:
        start = time.time()
    while GPIO.input(echo)==1:
        end = time.time()
    duration = end - start
    distance = duration*17150
    distance = round(distance,2)
    print("distance : ",distance," cm")
    time.sleep(2)
