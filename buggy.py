#import the library to control the GPIO pins
import RPIO
from RPIO import PWM
RPIO.setwarnings(False)

PWM.setup()

#get rid of debug output
PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)

#import the time library
import time

#pins
enable_pin = 2
forward_pin = 3
backward_pin = 4

#setup the pins
RPIO.setup(forward_pin, RPIO.OUT)
RPIO.setup(backward_pin, RPIO.OUT)

#pwm setup
dma = 0
PWM.init_channel(dma)
#direction, how long to drive for, how fast to drive
def drive(dir,drive_time,pwm_amount):
	if pwm_amount > 1999:
		pwm_amount = 1999
		print "limiting pwm to 1999"
	PWM.add_channel_pulse(dma,enable_pin,0,pwm_amount)
	if dir:
		RPIO.output(forward_pin, True)
		RPIO.output(backward_pin, False)
	else:
		RPIO.output(backward_pin, True)
		RPIO.output(forward_pin, False)
	time.sleep(drive_time)
	PWM.clear_channel_gpio(dma, enable_pin)

def end():
    PWM.cleanup()

