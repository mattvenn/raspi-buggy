import scratch
import buggy
"""
see https://github.com/pilliq/scratchpy for details on scratch module
"""

s = scratch.Scratch()
def listen():
    while True:
        try:
           yield s.receive()
        except scratch.ScratchError:
           raise StopIteration

for msg in listen():
    if msg[0] == 'broadcast':
        pass
        # code to handle broadcasts
    elif msg[0] == 'sensor-update':
        # code to handle sensor updates
        if msg[1].has_key("left"):
            drive(True,1,500)

