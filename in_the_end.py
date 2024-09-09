#!/usr/bin/env python3
import os

import dotenv
import mido
import pygame

from note_util import to_number

dotenv.load_dotenv()
pygame.mixer.init()

# fmt: off
melody_note_names = (
    ("Eb", "Bb", "Bb", "Gb", "F", "F", "F", "F", "Gb") +
    ("Eb", "Bb", "Bb", "Gb", "F"))
# fmt: on

melody = [to_number(note) for note in melody_note_names]
entered_notes = []

audio_file = os.getenv("AUDIO_FILE") or "placeholder.mp3"
project_directory = os.path.dirname(os.path.realpath(__file__))
audio_file_path = os.path.join(project_directory, audio_file)

sound = pygame.mixer.Sound(audio_file_path)
channel = pygame.mixer.Channel(1)

# `None` will select the default audio interface.
audio_interface = os.getenv("AUDIO_INTERFACE") or None
input_port = mido.open_input(audio_interface)
print("Listening for input ...")

try:
    for message in input_port:
        if channel.get_busy():
            continue

        if message.type == "note_on" and message.velocity > 0:
            # Disregarding octaves. C is 0, C# is 1, etc.
            current_note = message.note % 12
            entered_notes.append(current_note)

            # Only keep around enough notes to see if it matches.
            while len(entered_notes) > len(melody):
                entered_notes.pop(0)

            if entered_notes == melody:
                # Reset notes to prevent half matching weirdness.
                entered_notes.clear()
                print("🎶 I tried so hard, and got so far 🎶")

                if os.path.isfile(audio_file_path):
                    channel = sound.play()

except KeyboardInterrupt:
    print("\nShutting down ...")
    input_port.close()
    channel.stop()
    pygame.mixer.quit()
