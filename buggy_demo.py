import buggy
import time

"""
little demo to show buggy control via python
"""

buggy.stop_all()
loops = 10
max_speed = 30 
pause_time = 1 #second
drive_time = 1 #second

for repeat in range(loops):
    print repeat, "of", loops

    #straight line
    print "straight"
    buggy.drive(buggy.LEFT,max_speed)
    buggy.drive(buggy.RIGHT,max_speed)
    time.sleep(drive_time)
    buggy.stop_all()

    print "pause"
    time.sleep(pause_time)

    print "turn on spot"
    #turn on the spot
    buggy.drive(buggy.LEFT,max_speed)
    buggy.drive(buggy.RIGHT,-max_speed)
    time.sleep(drive_time)
    buggy.stop_all()

    print "pause"
    time.sleep(pause_time)

    print "arc"
    #turn on the spot
    buggy.drive(buggy.LEFT,max_speed)
    buggy.drive(buggy.RIGHT,max_speed * 0.7)
    time.sleep(drive_time)
    buggy.stop_all()

    print "pause"
    time.sleep(pause_time)
