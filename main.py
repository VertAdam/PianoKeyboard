# Jan 16, 2021

# Adam Vert

############## IMPORTS ##############
import mido
from midi_numbers import number_to_note, note_to_number
from keyboard_inputs import PressKey, ReleaseKey
import numpy as np
import time
from note_to_vkkey import binding_of_isaac_dict, get_vk_code

############# Class ###########

class PianoKeyboard:
    def __init__(self, input_port_name = None, output_port_name = None):
        if input_port_name == None:
            input_ports = mido.get_input_names()
            for n in range(len(input_ports)):
                print(str(n+1)+": "+ input_ports[n])
            sig_num = input("Which number corresponds to the input you want?")
            self.inport_name = input_ports[int(sig_num) - 1]
        else:
            self.inport_name = input_port_name

        if output_port_name == None:
            output_ports= mido.get_output_names()
            for n in range(len(output_ports)):
                print(str(n+1)+": "+output_ports[n])
            sig_num = input("Which number corresponds to the output you want?")
            self.outport_name = output_ports[int(sig_num)-1]
        else:
            self.outport_name = output_port_name


    def start_keyboard(self, dict):
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
                    # print(msg)
                    # TEMP
                    binding_dict = binding_of_isaac_dict()
                    if note in binding_dict.keys():
                        key = binding_dict[note]


                        # This means the note is being pressed
                        if msg.velocity != 0:
                            print("Note:", number_to_note(note)[0], ", Octave:", number_to_note(note)[1],
                                  ", MIDI NOTE #:", note, ", Key Pressed:", key)
                            print("")
                            PressKey(key)

                        # This means the note is being released
                        else:
                            ReleaseKey(key)

                    prev_10_notes.append(note)
                    prev_10_notes.pop(0)
                    if np.sum(prev_10_notes)==96*10:
                        print("Exiting Piano Keyboard...")
                        inport.close()
                        outport.close()
                        return


                except AttributeError:
                    continue

if __name__ =="__main__":
    pk = PianoKeyboard("Digital Keyboard 0","Digital Keyboard 1")
    pk.start_keyboard(1)



    x = 1