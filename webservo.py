#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')
print('<form action="" method="post">')
print('<input type="number" name="degree">')
print('<input type="submit" value="submit">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
value = form.getvalue("degree")

def setservo(kakudo):
	nanika = (1.9*(kakudo+90)/180+0.5)/20*100
	servo.ChangeDutyCycle(nanika)
	time.sleep(1.0)

setservo(int(value))

