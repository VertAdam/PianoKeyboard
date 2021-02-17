# Jan 16, 2021

# Adam Vert

############## IMPORTS ##############
import mido
import os
import pandas as pd
from midi_numbers import number_to_note, note_to_number
from keyboard_inputs import PressKey, ReleaseKey
import numpy as np
import time
from note_to_vkkey import win_keys
import PySimpleGUI as sg

############# Class ###########
def binding_gui():


    input_ports = mido.get_input_names()
    output_ports = mido.get_output_names()
    # Green & tan color scheme
    sg.ChangeLookAndFeel('GreenTan')

    sg.SetOptions(text_justification='left')
    sg.SetOptions(element_size=(800,800))

    min_midi_num = 36
    max_midi_num = 96

    preset_bindings_list = os.listdir("binding_csvs")
    preset_bindings_list = [x[:-4] for x in preset_bindings_list]

    cols = []
    sorted_keys = list(pd.read_excel("Sorted_vkkey_codes.xlsx")["Key"])
    for n in range(min_midi_num,max_midi_num+1):
        cols.append([sg.Text(number_to_note(n),size=(18,1), justification='center'), sg.Text("|",size=(6,1), justification='center'),sg.Text(n,size=(18,1), justification='center'),sg.Text("|",size=(6,1), justification='center'), sg.Combo(sorted_keys,size=(25,1), default_value='Empty',key=n)])
        cols.append([sg.Text('-' * 200, size=(800, 1))])

    layout = [[sg.Text('Bindings Editor', font=('Helvetica', 25), justification = 'center')],
              [sg.Text('Preset Binding'), sg.Combo(preset_bindings_list,default_value="Empty",key="Preset Choice"), sg.Text("     ",size = (10,1)),sg.Text("MIDI Input Device   "), sg.Combo(input_ports, default_value=input_ports[0], key = "Device Input", size = (20,1))],
              [sg.Button('Apply'), sg.Text("     ",size = (36,1)), sg.Text("MIDI Output Device", justification='right'), sg.Combo(output_ports, default_value=output_ports[0], key = "Device Output", size = (20,1))],
              [sg.Text('_' * 100, size=(800, 1))],
              [sg.Text('Bindings', font=('Helvetica', 15), justification='left')],
              [sg.Text('(Key1, Octave1)', font=('Helvetica', 15), size = (15,1), justification='center'),sg.Text("|", font=('Helvetica', 15),size = (5,1),justification='center'),sg.Text('Midi#', font=('Helvetica', 15), size = (15,1), justification='center'),sg.Text("|", font=('Helvetica', 15),size = (5,1),justification='center'), sg.Text("Binding", font=('Helvetica', 15),size = (20,1),justification = 'center')],
              [sg.Text('-' * 200, size=(800, 1))],
              [sg.Column(cols, scrollable=True, vertical_scroll_only= True,size= (800,450))],
              [sg.Text('_' * 100, size=(800, 1))],
              [sg.Button('Save as Custom Binding')],
              [sg.Submit(button_text="Use These Bindings"), sg.Cancel()]]

    col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
           [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],
           [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]
    window = sg.Window('Machine Learning Front End', layout, font=("Helvetica", 12),size=(800,800))


    while True:  # Event Loop
        event, values = window.read()

        if event == 'Apply':
            preset_bin = list(values.values())[0]
            preset_df = pd.read_csv(os.path.join("binding_csvs", preset_bin+".csv"))
            for n in range(min_midi_num, max_midi_num + 1):
                window[n].update(preset_df["Binding"].loc[preset_df["Midi #"] == n].values[0])

        if event == "Save as Custom Binding":
            preset_name = sg.popup_get_text('What do you want to name this binding? (do not use any special characters)')
            if preset_name == None:
                continue
            binding_df = pd.DataFrame({"Midi #":list(values.keys())[2:],"Binding":list(values.values())[2:]})

            binding_df.to_csv(os.path.join("binding_csvs",preset_name+".csv"))
            x = 1

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            raise ConnectionAbortedError

        if event == "Use These Bindings":
            window.close()
            device = values["Device"]
            del values['Preset Choice']
            return values, device

    window.close()

if __name__ =="__main__":
    binding_gui()