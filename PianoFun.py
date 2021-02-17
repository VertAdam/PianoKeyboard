# Jan 16, 2021

# Adam Vert

############## IMPORTS ##############
import mido
from midi_numbers import number_to_note, note_to_number

import numpy as np
import time
############# Class ###########
class PianoFun:
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


    def play_note_n_higher(self, n = 12):
        # Play same note inputted, but n notes higher. Default is one octave
        inport = mido.open_input(self.inport_name)
        outport = mido.open_output(self.outport_name)
        prev_10_notes = [0]*10
        with inport as inport:
            for msg in inport:
                try:
                    note = msg.note
                    print(msg)
                    outport.send(mido.Message('note_on', note=note + n, velocity=msg.velocity))

                    prev_10_notes.append(note)
                    prev_10_notes.pop(0)
                    if np.sum(prev_10_notes)==96*10:
                        print("Exiting play notes " + str(n)+" higher...")
                        mid = mido.MidiFile('Windows_OS_-_Windows_Sounds_by_w3sp.mid')
                        for msg in mid.play():
                            outport.send(msg)
                        time.sleep(2)
                        inport.close()
                        outport.close()
                        return


                except AttributeError:
                    continue

    def print_note(self):
        # Print note being played on input device
        inport = mido.open_input(self.inport_name)
        outport = mido.open_output(self.outport_name)
        prev_10_notes = [0]*10
        with self.inport as inport:
            for msg in inport:
                try:
                    note_number = msg.note
                    n2n = number_to_note(note_number)
                    if msg.velocity != 0:
                        print("Note:",n2n[0],"\nOctave",n2n[1],"\n")

                    prev_10_notes.append(note_number)
                    prev_10_notes.pop(0)
                    if np.sum(prev_10_notes)==96*10:
                        print("Exiting print_note...")
                        mid = mido.MidiFile('Windows_OS_-_Windows_Sounds_by_w3sp.mid')
                        for msg in mid.play():
                            outport.send(msg)
                        time.sleep(2)
                        inport.close()
                        outport.close()
                        return
                except AttributeError:
                    continue

    def play_note(self,note,octave,velocity = 100, duration = 5):
        # Play a single note to your output device
        # Notes must be in the following list: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        # Octaves must be from 0 to 10
        #Duration in seconds

        outport = mido.open_output(self.outport_name)
        outport.send(mido.Message('note_on', note=note_to_number(note,octave), velocity=velocity))
        time.sleep(duration)
        outport.close()
        return

if __name__ =="__main__":
    pf = PianoFun("Digital Keyboard 0","Digital Keyboard 1")
    # pf.play_note_n_higher(2)
    pf.play_note('C',1)


x = 1
