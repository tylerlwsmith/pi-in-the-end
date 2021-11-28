import mido

notes_to_match = [3, 10, 10, 6, 5, 5, 5, 5, 6, 3, 10, 10, 6, 5]
entered_notes = []

inport = mido.open_input()
print("Listening for input...")

for msg in inport:
    if msg.type == "note_on" and msg.velocity > 0:
        # Append, disregarding octaves. C is 0, C# is 1, etc.
        entered_notes.append(msg.note % 12)

        # Only keep around enough notes to see if it matches.
        entered_notes = entered_notes[-len(notes_to_match):]
        if (entered_notes == notes_to_match):
            # Reset notes to prevent half matching weirdness.
            entered_notes = []
            print("🎶 I tried so hard, and got so far 🎶")

print("I am the end")
