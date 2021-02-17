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
from note_to_vkkey import binding_of_isaac_dict, win_keys
import PySimpleGUI as sg

############# Class ###########

# Green & tan color scheme
sg.ChangeLookAndFeel('GreenTan')

sg.SetOptions(text_justification='left')
sg.SetOptions(element_size=(800,800))

min_midi_num = 36
max_midi_num = 96

cols = []
sorted_keys = list(pd.read_excel("Sorted_vkkey_codes.xlsx")["Key"])
for n in range(min_midi_num,max_midi_num+1):
    cols.append([sg.Text(number_to_note(n),size=(18,1), justification='center'), sg.Text("|",size=(6,1), justification='center'),sg.Text(n,size=(18,1), justification='center'),sg.Text("|",size=(6,1), justification='center'), sg.Combo(sorted_keys,size=(25,1), default_value='Empty',key=n)])
    cols.append([sg.Text('-' * 200, size=(800, 1))])

layout = [[sg.Text('Bindings Editor', font=('Helvetica', 25), justification = 'center')],
          [sg.Text('Preset Binding'), sg.Combo(['choice sadasdasdasdsadasdsad1', 'choice 2'],key="Preset Choice")],
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
    if event == "Save as Custom Binding":
        for v in list(values.values()):
            if v in win_keys:print('hi')
        preset_name = sg.popup_get_text('What do you want to name this binding? (do not use any special characters)')
        binding_df = pd.DataFrame({"Midi #":list(values.keys())[1:-1],"Binding":list(values.values())[1:-1]})

        binding_df.to_csv(os.path.join("binding_csvs",preset_name+".csv"))
        x = 1

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()