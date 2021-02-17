# Used https://github.com/andohuman/pyKey for the general code structure

import ctypes
import time
from note_to_vkkey import win_keys as key_dict

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


#Presses a key and holds it until explicitly called the releaseKey function.
def PressKey(key=None):
    if key == 'Empty':
        return
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()

    #These keys use the extendedkey prefix 0xE0, directly simulating the actual key rather than the redundant ones in numpad
    if key in ['INS', 'HOME', 'PGUP', 'PGDN', 'END', 'DEL', 'UP', 'DOWN', 'LEFT', 'RIGHT']:
        ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0001, 0, ctypes.pointer(extra) )
    #Else normal use
    else: ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008, 0, ctypes.pointer(extra) )

    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#Releases a key that was pressed using pressKey. NEVER FORGET TO USE THIS AFTER USING pressKey()
def ReleaseKey(key=None):
    if key == 'Empty':
        return
    assert key in key_dict, "The key({}) you're trying to release does not exists! Please check for any spelling errors.".format(key)

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()

    if key in ['INS', 'HOME', 'PGUP', 'PGDN', 'END', 'DEL', 'UP', 'DOWN', 'LEFT', 'RIGHT']:
        ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0002 | 0x0001, 0, ctypes.pointer(extra) )
    else: ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0002, 0, ctypes.pointer(extra) )

    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# if __name__ =="__main__":
#     time.sleep(2)
#     key_name = "D"
#     PressKey()
#     time.sleep(2)
#     ReleaseKey()