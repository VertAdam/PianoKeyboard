Adam Vert

# PianoKeyboard
Use your digital piano as your computer keyboard!
Simply plug in your digital piano (must have a midi output) to your computer and start typing! 

...or whatever you call it when its on a Piano.

Enjoy!


### insert GIF of it being used ***

## Setup
This is built on the back off the python package mido which utilizes rtmidi for the port setup.

I am currently using Python 3.9 on windows and have not tested if a different version/Operating systems will cause any problems.

To get this going should be very simple.
1. Plug in your MIDI device
2. Make sure all packages used in main.py are installed
3. run `main.py`

You should then get an image of the GUI that looks like this:

![Binding Editor Screenshot](assets\GUI screenshot.png)


There are a few custom bindings already made (Discussed Below), but if you want to create your own simply choose the bindings you want for each note and then press "Save as custom binding". Now this binding will be easily accessible whenever you run the script again.

Once all the bindings you want are selected, press "Use These Bindings". Now the keys you play will perform the binding set to it. Enjoy!


# Premade Bindings
There are three premade bindings as the moment

#### 1. Empty
This is the default binding setting. This has no binds meaning all keys will do nothing.

### 2. RACECAR
This can be used to test that everythings working. If you play the major scale with these bindings it should spell out

`RACECAR RACECAR` 

| Midi # |  Binding |
|:------:|:--------:|
|   60   |     R    |
|   62   |     A    |
|   64   |     C    |
|   65   |     E    |
|   67   |     C    |
|   69   |     A    |
|   71   |     R    |
| 72     | SPACEBAR |
** Add gif of it being used **

### 3. league_of_legends
This is used for playing League of Legends, the bindings are:

| Midi # |  Binding |
|:------:|:--------:|
|   60   |     R    |
|   62   |     A    |
|   64   |     C    |
|   65   |     E    |
|   67   |     C    |
|   69   |     A    |
|   71   |     R    |
| 72     | SPACEBAR |

*** Add picture of keyboard with bindings overlaid ***

### 4. Binding of Isaac
This is used for playing the steam game Binding of Isaac, the bindings are:

| Midi # |  Binding |
|:------:|:--------:|
|   60   |     R    |
|   62   |     A    |
|   64   |     C    |
|   65   |     E    |
|   67   |     C    |
|   69   |     A    |
|   71   |     R    |
| 72     | SPACEBAR |

*** Add picture of keyboard with bindings overlaid ***



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

