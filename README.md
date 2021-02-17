# PianoKeyboard
Use your digital piano as your computer keyboard!
Simply plug in your digital piano (must have a midi output) to your computer and start typing, or whatever you call it when its on a Piano.

## Setup
This is built on the back off the python package mido which utilizes rtmidi for the port setup.

I am currently using Python 3.9 on windows and have not tested if a different version/Operating systems will cause any problems.

To get this going should be very simple.
1. Plug in your MIDI device
2. Make sure all packages used in main.py are installed
3. run main.py

You should then get an image of the GUI that looks like this:

### insert image of gui *** 

There are a few custom bindings already made, but if you want to create your own simply choose the bindings you want for each note and then press "Save as custom binding". Now this binding will be easily accessible whenever you run the script again.

Once all the bindings you want are selected, press "Use These Bindings". Now the keys you play will perform the binding set to it. Enjoy!


### insert GIF of it being used ***


# TODO's

- ~~add a GUI to customize bindings~~
- make range of keyboard customizable
- ~~Add the ability to use customizable bindings or premade dicts~~
   - ~~Make sure customizable bindings are able to be saved (csv probably)~~
- ~~Fix VK_KEYS arrow keys using the numpad~~
- Add better documentation
    - Update the setup
    - add descriptions to functions
- ~~Add Device MIDI input device to GUI~~

