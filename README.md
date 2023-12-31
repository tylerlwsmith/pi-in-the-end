# "In the End" player for Raspberry Pi

This project will run on a Raspberry Pi and will play the chorus from "In the End" by Linkin Park (mp3 not included) when the song's intro is played on a connected MIDI device. You can see me demoing an early version of the script on [my Twitter](https://twitter.com/tylerlwsmith/status/1327802206020464640). The demo prints to the console, but this completed project plays the chorus through connected speakers.

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

## Set the audio file

The audio file is not provided as a part of this repository, so you'll need to provide your own. Save the file into the main project directory, then set its value in `.env` using the `AUDIO_FILE` variable.

## Deploy to Pi

On the Pi, install the system-level dependencies for the [PyGObject](https://pygobject.readthedocs.io/en/latest/index.html) package:

```sh
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0
```

Then install the dependencies for [GStreamer](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c).

```sh
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

Next, install Git:

```sh
sudo apt install git
```

After that, run the following commands to clone the repo into the home directory:

```sh
cd ~
git clone git@github.com:tylerlwsmith/pi-in-the-end.git
```

**If you are not using the default audio driver for output, follow [Jeff Geerling's instructions to set a different audio device](https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi).**

To adjust the ouptut volume, grab the name of the device you'd like to change the volume of with the following command:

```sh
amixer scontrols
```

It may return something like `Simple mixer control 'PCM',0`. You can target the device name in single quotes to change the volume of the output with the following command (more info on [Stack Overflow](https://askubuntu.com/a/380764)):

```sh
amixer set PCM 100% # 100% means full volume.
```

Next create, a `systemd` unit file by running the following command:

```sh
sudo vi /etc/systemd/system/linkinpark.service
```

Paste the following into the new `linkinpark.service` file, **replace `<username>` with the desired user**, and save and quit with `wq!`:

```ini
[Unit]
Description=Linkin Park MIDI Playback Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/<username>/pi-in-the-end
User=<username>
Restart=always
ExecStart=/home/<username>/pi-in-the-end/.venv/bin/python /home/<username>/pi-in-the-end/in_the_end.py

[Install]
WantedBy=multi-user.target

```

Once created, run the following commands to activate the service:

```sh
sudo systemctl daemon-reload
sudo systemctl enable linkinpark.service
sudo systemctl start linkinpark.service
sudo systemctl status linkinpark.service

```

## Limitations

This is a proof-of-concept implementation is not intented be put into production, so it has several potential issues that are not addressed:

- There is no way to specify what audio interface plays the audio clip within the code: that happens at the operating system level.
- Linux may change the ID of desired output audio interface.
- If the midi device is disconnected while the app is running, the application has no way of reconnecting when the device is plugged back in.
- The MIDI device name that the `mido` library sees may change between system boots.
- If the midi device is disconnected when `systemd` starts the app, the service will go into a rapid boot loop.
- Multiple midi channels on the same interface will all be collapsed into a single stream of notes.
- The current implementation only supports listening on one device.
- The Python `playsound` library requires an enormous number of dependencies on a headless Pi. It may be worth replacing with `pygame` as outlined in [Jeff Geerling's article](https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi).
- Even though the main thread is blocked while the audio is playing, the midi device is continuing to collect input that will execute immediately after the audio stops. If the melody is played during the audio playback, the audio playback will start again immediately after the playing audio stops.

All of these issues are fixable, but are not worth expanding this demo project's scope to mitigate.

## Running tests

After installing the project requirements in a virtual environment, use the following command to run the project's tests:

```sh
pytest
```

## Formatting

This project uses [Black](https://black.readthedocs.io/en/stable/) for formatting.
