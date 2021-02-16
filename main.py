# Jan 16, 2021

# Adam Vert

############## IMPORTS ##############
import mido

############# Class ###########
class PianoFun:
    def __init__(self, input_port_name = None, output_port_name = None):
        if input_port_name == None:
            input_ports = mido.get_input_names()
            for n in range(len(input_ports)):
                print(str(n+1)+": "+ input_ports[n])
            sig_num = input("Which number corresponds to the input you want?")
            self.inport = mido.open_input(input_ports[int(sig_num) - 1])
        else:
            self.inport = mido.open_input(input_port_name)

        if output_port_name == None:
            output_ports= mido.get_output_names()
            for n in range(len(output_ports)):
                print(str(n+1)+": "+output_ports[n])
            sig_num = input("Which number corresponds to the output you want?")
            self.outport = mido.open_output(output_ports[int(sig_num) - 1])


    def play_note_n_higher(self, n = 12):
        # Play same note inputted, but n notes higher. Default is one octave
        with self.inport as inport:
            for msg in inport:
                try:
                    x = msg.note
                    print(msg)
                    self.outport.send(mido.Message('note_on', note=msg.note + 12, velocity=msg.velocity))
                except:
                    continue

pf = PianoFun("Digital Keyboard 0","Digital Keyboard 1")


x = 1
