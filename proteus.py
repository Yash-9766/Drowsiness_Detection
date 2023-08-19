import RPi.GPIO as GPIO
from time import sleep
import pio
import Ports

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pio.uart=Ports.UART () # Define serial port

buzzer = 7
motor1 = 11
motor2 = 12
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)

while(1):
    Data=pio.uart.recv()
    if(Data=="s"):
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(3)
        GPIO.output(buzzer,GPIO.LOW)
    