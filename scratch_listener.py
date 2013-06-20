import scratch
import buggy
import sys
"""
see https://github.com/pilliq/scratchpy for details on scratch module
"""

ip = '10.42.0.1'
port = 42001
if len(sys.argv) == 2:
    ip = sys.argv[1]

print "trying to connect to", ip, ":", port
try:
    s = scratch.Scratch(host=ip, port=port) 
except scratch.scratch.ScratchError, e:
    print "couldn't connect - is scratch running?"
    print e
    exit(1)
print "connected"

def listen():
    while True:
        try:
           yield s.receive()
        except scratch.ScratchError:
           raise StopIteration

for msg in listen():
    # code to handle broadcasts
    if msg[0] == 'broadcast':
        if msg[1] == 'stop':
            print "got stop"
            buggy.stop_all()
        else:
            print "didn't recognise broadcast: ", msg
    # code to handle sensor updates
    elif msg[0] == 'sensor-update':
        if msg[1].has_key("left"):
            buggy.drive(buggy.LEFT,msg[1]["left"])
        elif msg[1].has_key("right"):
            buggy.drive(buggy.RIGHT,msg[1]["right"])
        else:
            print "didn't recognise command: ", msg

