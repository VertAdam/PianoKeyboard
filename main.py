# Jan 16, 2021

# Adam Vert

############## IMPORTS ##############
import mido
from midi_numbers import number_to_note, note_to_number
from keyboard_inputs import PressKey, ReleaseKey
import numpy as np
import time
from note_to_vkkey import win_keys
from binding_gui import binding_gui
import pandas as pd
import os
############# Class ###########

class PianoKeyboard:
    """
    This is the main script. Run this script and you should be good to go.
    """

    def __init__(self):
        df = pd.read_csv(os.path.join("binding_csvs","Empty.csv"))
        self.binding_dict =dict(zip(list(df["Midi #"]), list("Binding")))

    def set_binding(self):
        self.bindings_dict, self.inport_name, self.outport_name = binding_gui()

    def startup(self):
        # Details on dictionaries can be found as note_to_vkkey
        # Current Dicts are:
        #       basic_dict - All keys in alpha numeric order
        #       binding_of_isaac_dict - for the binding of isaac
        #       league_of_legends_dict - for league of legends

        # Play same note inputted, but n notes higher. Default is one octave
        inport = mido.open_input(self.inport_name)
        outport = mido.open_output(self.outport_name)
        prev_10_notes = [0]*10
        with inport as inport:
            for msg in inport:
                try:
                    note = msg.note

                    prev_10_notes.append(note)
                    prev_10_notes.pop(0)
                    if np.sum(prev_10_notes)==96*10:
                        print("Exiting Piano Keyboard...")
                        mid = mido.MidiFile('Windows_OS_-_Windows_Sounds_by_w3sp.mid')
                        for msg in mid.play():
                            outport.send(msg)
                        time.sleep(2)
                        inport.close()
                        outport.close()
                        return


                    binding_dict = self.bindings_dict
                    if note in binding_dict.keys():
                        key = binding_dict[note]

                        if key == None:
                            continue

                        # This means the note is being pressed
                        print(key)
                        if msg.velocity != 0:
                            print("Note:", number_to_note(note)[0], ", Octave:", number_to_note(note)[1],
                                  ", MIDI NOTE #:", note, ", Key Pressed:", key)
                            print("")

                            PressKey(key)

                        # This means the note is being released
                        else:
                            ReleaseKey(key)


                except AttributeError:
                    continue

    def start_keyboard(self):
        self.set_binding()
        self.startup()
if __name__ =="__main__":
    pk = PianoKeyboard()
    pk.start_keyboard()



    x = 1