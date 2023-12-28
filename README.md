# "In the End" player for Raspberry Pi (WIP)

This work-in-progress project will run on a Raspberry Pi and will play the chorus from "In the End" by Linkin Park when the song's intro is played on a connected MIDI device. You can see me demoing the script on [my Twitter](https://twitter.com/tylerlwsmith/status/1327802206020464640). The demo prints to the console, but the final project will play the chorus through connected speakers.

## Installation

First, set up a virtual enviornment:

```sh
python3 -m venv .venv
```

Once the environment is created, activate it:

```sh
source ./venv/bin/activate
```

Once activated, install the dependencies:

```sh
pip3 install -r requirements.txt
```

## Running tests

After installing the project requirements in a virtual environment, use the following command to run the project's tests:

```sh
pytest
```
