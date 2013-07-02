import buggy
import time
import sys

"""
little demo to show buggy control via python
"""

buggy.stop_all()
max_speed = 60 
if len(sys.argv)==2:
    max_speed = int(sys.argv[1])
    print "maxspeed:", max_speed

pause_time = 1 #second
drive_time = 1 #second

while True:

    #straight line
    print "straight"
    buggy.drive(buggy.LEFT,max_speed)
    buggy.drive(buggy.RIGHT,max_speed)
    time.sleep(drive_time)
    buggy.stop_all()

    print "pause"
    time.sleep(pause_time)
