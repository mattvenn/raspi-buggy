# Buggy build instructions

# Get the parts

You will need:

*  some [male to male wires](http://oomlout.co.uk/products/jumper-wires-70-piece)
*  some [female to male wires](http://oomlout.co.uk/products/premium-female-to-female-jumper-wires-x21)
*  [l293d motor driver](http://oomlout.co.uk/products/motor-controller-l293d)
*  [400 point breadboard](http://oomlout.co.uk/collections/prototyping/products/breadboard-400-point)
*  4 AA battery holder and 4 *rechargable batteries*
*  [buggy unit](http://www.mindsetsonline.co.uk/product_info.php?cPath=17_134_685&products_id=1034)
*  pen and bluetack

# Build the circuit

follow this diagram to build the circuit, but don't insert the batteries yet.

![circuit](./buggy_bb.png)

# Log in to the raspberry pi

You will need to power up the raspberry pi and connect to it over the network.

# Download the buggy software

On the raspberry pi, start a terminal. Then run these commands to download the software:

    wget https://github.com/mattvenn/raspi-buggy/archive/master.zip
    unzip master.zip

Then we need to install some extra software for the buggy software to work.

## easy_install

easy_install makes it easier to install python libraries.

    sudo apt-get -y install python-setuptools

## RPIO

RPIO is the library that lets a python program control the raspberry pi GPIO pins - which we'll use to drive the motor chip.

    sudo easy_install RPIO

## scratchpy

scratchpy is the library we'll use to talk to scratch

    sudo easy_install scratchpy

# Test the motors

Change into the buggy directory:

    cd buggy-master

Then start the test running by running this command:

    sudo python buggy_demo.py

If all is well, the program will start printing lines like this:

    Using hardware: PWM
    PW increments:  10us
    stop
    0 of 10
    straight
    left forward pwm: 570
    right forward pwm: 570
    stop
    pause

You can then connect the batteries, and providing your circuit is correct the buggy should start moving its motors!

The test will run 10 times, to stop the test early, you can press control-C

You can look at what the test does by using an editor:

    nano buggy_demo.py

It drives the motors in different directions to perform a sequence of moves: a straight line, a turn and then an arc. This is done 10 times. 

# buggy.py

buggy.py is a little library that sets up the GPIO pins and defines 2 functions that allow easy control of the motors. The first is called:

    buggy.drive(wheel,speed)

It takes 2 arguments, the wheel to control, and the speed to move the wheel at. The wheel is chosen by passing either buggy.LEFT or buggy.RIGHT. The speed can be set to -100 to +100. A speed of 0 will stop the motor. 

The second is used to stop both motors:

    buggy.stop_all()

# Scratch

To use scratch to control the buggy, we run scratch on a different computer, and then send commands from scratch to the raspberry pi. To do that we need to use scratch's mesh function, which allows scratch to talk over the network to the raspberry pi.

## Configure scratch

Follow the [instructions here](http://wiki.scratch.mit.edu/wiki/Mesh) to enable mesh on scratch. 

Download the [scratch demo](https://github.com/mattvenn/raspi-buggy/blob/master/buggy.sb?raw=true).

Then start scratch, and turn on the mesh network (using the above instructions). 
Load the example buggy.sb you just downloaded. Before we can run it, we need to start the raspberry pi listening to scratch.

# Start Raspberry pi listening to scratch

We run the scratch_listener.py program on the raspberry pi to listen to the command from scratch. To do that, we need the IP address of the computer running scratch. [Follow these instructions to find your IP address.](http://computer.howstuffworks.com/internet/basics/how-to-find-ip-address.htm)

Then start the scratch_listener program like this (change IP_ADDRESS to your IP address)

    sudo python scratch_listener.py IP_ADDRESS

If you see this:

    couldn't connect - is scratch running?
    [Errno 111] Connection refused

Then either scratch isn't setup for mesh networking, the mesh network isn't enabled, or you have the wrong IP address.


# photos

Some [photos of the buggy and the pictures that it has drawn.](http://www.flickr.com/photos/matthewvenn/sets/72157633441674047/with/9027093148/)
