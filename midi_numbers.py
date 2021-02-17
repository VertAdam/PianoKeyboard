# Jan 16, 2021

# Adam Vert

############# Functions ###########

def number_to_note(number):
    # Converts MIDI note # to the actual note and octave
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    num_octaves = list(range(11))
    num_notes_octave = 12
    octave = number // num_notes_octave
    note = notes_list[number % num_notes_octave]
    return note, octave

def note_to_number(note, octave):
    # Converts (note, octave) to the corresponding MIDI #
    # Notes must be in the following list: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # Octaves must be from 0 to 10

    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note = notes_list.index(note)
    note += (12 * octave)

    return note