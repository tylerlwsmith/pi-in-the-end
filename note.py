notes = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
accidentals = {"bb": -2, "b": -1, "": 0, "#": 1, "##": 2}
octave = 12


def to_number(note_string):
    base_note = note_string[0]
    accidental = note_string[1:]

    if base_note not in notes or accidental not in accidentals:
        raise Exception(f'Note "{note_string}" is invalid!')

    note_number = notes[base_note]
    adjustment = accidentals[accidental]

    return (note_number + adjustment) % octave
