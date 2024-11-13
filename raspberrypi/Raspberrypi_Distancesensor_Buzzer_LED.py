from gpiozero import DistanceSensor, Buzzer
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

sensor = DistanceSensor(23,24)
buzzer = Buzzer(17)


while True:
	cm_distance = sensor.distance * 100
	print(“Distance to nearest object:”, cm_distance, ‘cm’)
	sleep(0.5)
	If cm_distance < 5:
		buzzer.on()
		GPIO.output(21, True)
	elif 5 < cm_distance < 15:
		GPIO.output(20, True)
		GPIO.output(21, False)
		buzzer.off()
	elif cm_distance > 15:
		GPIO.output(16, True)
		GPIO.output(20, True)
		GPIO.output(21, True)
                buzzer.off()




