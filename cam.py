import subprocess
import RPi.GPIO as GPIO
import time

#Connect GPIO Pin 18 to Button stop the camera
#Connect GPIO Pin 23 to Laser input

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        input_laser = GPIO.input(23)
	input_button = GPIO.input(18)
	if input_laser == 0:                                      ## If there is intrusion detected on the camera 
	    subprocess.call('service motion start',shell=True) 
	    subprocess.call('service motion restart',shell=True)
	    print('START')
	    time.sleep(0.2)
	if input_button == 0:                                     ## If the button is clicked stop the camera 
	    subprocess.call('service motion stop',shell=True)
            print('STOP')
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
