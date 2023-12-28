import os
import pathlib

import mido
from playsound import playsound

from note import to_number

current_script_directory = os.path.dirname(os.path.realpath(__file__))
audio_file_path = current_script_directory + "/audio.mp3"

# fmt: off
melody_note_names = (
    ("Eb", "Bb", "Bb", "Gb", "F", "F", "F", "F", "Gb") +
    ("Eb", "Bb", "Bb", "Gb", "F"))
# fmt: on

melody = [to_number(note) for note in melody_note_names]

entered_notes = []

input_port = mido.open_input()
print("Listening for input ...")

try:
    for msg in input_port:
        if msg.type == "note_on" and msg.velocity > 0:
            # Append, disregarding octaves. C is 0, C# is 1, etc.
            entered_notes.append(msg.note % 12)

            # Only keep around enough notes to see if it matches.
            while len(entered_notes) > len(melody):
                entered_notes.pop(0)

            if entered_notes == melody:
                # Reset notes to prevent half matching weirdness.
                entered_notes.clear()
                print("🎶 I tried so hard, and got so far 🎶")

                if os.path.isfile(audio_file_path):
                    playsound(audio_file_path, block=True)

except KeyboardInterrupt:
    print("\nShutting down ...")
