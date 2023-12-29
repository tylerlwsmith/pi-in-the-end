# "In the End" player for Raspberry Pi (WIP)

This work-in-progress project will run on a Raspberry Pi and will play the chorus from "In the End" by Linkin Park when the song's intro is played on a connected MIDI device. You can see me demoing the script on [my Twitter](https://twitter.com/tylerlwsmith/status/1327802206020464640). The demo prints to the console, but the final project will play the chorus through connected speakers.

## Installation

First, set up a virtual enviornment:

```sh
python3 -m venv .venv
```

Once the environment is created, activate it:

```sh
source .venv/bin/activate
```

Once activated, install the dependencies:

```sh
pip3 install -r requirements.txt
```

Next create a project `.env` file:

```sh
cp .example.env .env
```

## Set the audio file

The audio file is not provided as a part of this repository, so you'll need to provide your own. Save the file into the main project directory, then set its value in `.env` using the `AUDIO_FILE` variable.

## Set the midi interface

The script may pick a different default midi interface than the one which was intended.

If this script does not fire when the correct notes are played, try the following steps to ensure that the the application is listening to the correct midi interface.

Activate the Python virtual environment if it is not already activated in your current terminal session:

```sh
source .venv/bin/activate
```

Once the virtual environment is activated, begin an interactive Python session:

```sh
python
```

In the interactive Python session, run the following commands:

```python
import mido
mido.get_input_names()
```

These commands will return a list of audio interfaces such as the one below:

```python
# Example output:
['Midi Through:Midi Through Port-0 14:0', 'Scarlett 18i8 USB:Scarlett 18i8 USB MIDI 1 20:0']
```

To manually select an audio interface, copy the full name of the audio interface and set the `AUDIO_INTERFACE` value to that string in `.env`:

```sh
# .env file
AUDIO_INTERFACE="Scarlett 18i8 USB:Scarlett 18i8 USB MIDI 1 20:0"
```

## Limitations

- There is no way to specify what audio interface plays the audio clip.
- If the midi device is disconnected while the app is running, the application has no way of reconnecting when the device is plugged back in.
- Multiple midi channels on the same interface will all be collapsed into a single stream of notes.
- The current implementation only supports listening on one device.

## Running tests

After installing the project requirements in a virtual environment, use the following command to run the project's tests:

```sh
pytest
```

## Formatting

This project uses [Black](https://black.readthedocs.io/en/stable/) for formatting.
