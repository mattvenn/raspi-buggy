# Raspberry pi scratch controlled drawing buggy

Simple buggy to control with scratch. A python listener is run on the raspberry pi which uses scratch's mesh networking capability to turn commands from scratch into motor controls.

Scratch itself is run on another computer to avoid the large overhead of sending graphics over the network

Scratch will need to be setup meshed: http://wiki.scratch.mit.edu/wiki/Mesh

Start scratch, turn on the mesh network, and load the example buggy.sb
Then start the scratch_listener on the raspberry pi (see section below)

# installation on the raspberry

scratchpi: https://github.com/pilliq/scratchpy

sudo easy_install scratchpy

RPIO: https://pypi.python.org/pypi/RPIO

sudo easy_install RPIO

# scratch_listener.py

runs on the raspberry pi. You provide the IP_ADDRESS of the scratch computer.

sudo python scratch_listener.py IP_ADDRESS

# buggy.py

the lower level software for driving the motors, used by scratch_listener.py

# bill of materials for building the buggy

* raspberry pi
* l293d dual h bridge
* hook up wires
* 3-5v battery pack
* robot base http://www.mindsetsonline.co.uk/product_info.php?cPath=17_134_685&products_id=1034

# photos

http://www.flickr.com/photos/matthewvenn/sets/72157633441674047/with/9027093148/
