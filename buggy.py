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
#i2c pins can be enabled high at boot - see http://www.raspberrypi.org/phpBB3/viewtopic.php?f=44&t=35321
l_enable_pin = 4
l_forward_pin = 3
l_backward_pin = 2
r_enable_pin = 17
r_forward_pin = 27
r_backward_pin = 22

#constants
LEFT = 1
RIGHT = 2

#setup the pins
RPIO.setup(l_forward_pin, RPIO.OUT)
RPIO.setup(r_forward_pin, RPIO.OUT)
RPIO.setup(l_backward_pin, RPIO.OUT)
RPIO.setup(r_backward_pin, RPIO.OUT)

#pwm setup
dma_l = 0
dma_r = 1
PWM.init_channel(dma_l)
PWM.init_channel(dma_r)
#this is silly, but otherwise pwm will complain if we try and clear a channel that hasn't been already used
PWM.add_channel_pulse(dma_l,l_enable_pin,0,0)
PWM.add_channel_pulse(dma_r,r_enable_pin,0,0)

def stop_all():
    print "stop"
    PWM.clear_channel_gpio(dma_l, l_enable_pin)
    PWM.clear_channel_gpio(dma_r, r_enable_pin)

#direction, how long to drive for, how fast to drive
def drive(wheel,speed):
    if wheel == LEFT:
        print "left",
        dma = dma_l
        enable_pin = l_enable_pin
        forward_pin = l_forward_pin
        backward_pin = l_backward_pin
    elif wheel == RIGHT:
        print "right",
        dma = dma_r
        enable_pin = r_enable_pin
        forward_pin = r_forward_pin
        backward_pin = r_backward_pin
    else:
        error_msg( "unknown wheel")
        return


    if speed > 100 or speed < -100:
        error_msg("speed should be > -100 and < 100")
        return

    if speed > 0:
        RPIO.output(forward_pin, True)
        RPIO.output(backward_pin, False)
        print "forward",
    elif speed < 0:
        RPIO.output(forward_pin, False)
        RPIO.output(backward_pin, True)
        print "backward",
    else:
        print "stop",

    pwm_amount = int(abs(speed * (1999/100)))

    print "pwm:", pwm_amount
    PWM.add_channel_pulse(dma,enable_pin,0,pwm_amount)

def end():
    PWM.cleanup()

def error_msg(msg):
    sys.stderr.write(msg + "\n")
