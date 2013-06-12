import scratch
import buggy
"""
see https://github.com/pilliq/scratchpy for details on scratch module
"""

#s = scratch.Scratch()
s = scratch.Scratch(host='10.42.0.1', port=42001) 
def listen():
    while True:
        try:
           yield s.receive()
        except scratch.ScratchError:
           raise StopIteration

while True:
    for msg in listen():
        if msg[0] == 'broadcast':
            print msg
            pass
            # code to handle broadcasts
        elif msg[0] == 'sensor-update':
            # code to handle sensor updates
            if msg[1].has_key("left"):
                buggy.drive(buggy.LEFT,msg[1]["left"])
            elif msg[1].has_key("right"):
                buggy.drive(buggy.RIGHT,msg[1]["right"])
            elif msg[1].has_key("stop"):
                print "got stop"
                buggy.stop_all()
            else:
                print "didn't recognise command: ", msg

