import json

import IPython.display
import numpy as np

import pyshaman

# Binaural
pyshaman.binaural_beat(left=400, right=420, duration=10)

# Mono
sr = 44100
volume = nk.rescale(nk.signal_simulate(duration=5, sampling_rate=sr, frequency=10))
sound = pyshaman.generate_sound(frequency=[400, 800], duration=5, volume=volume, rate=sr)

volume = nk.rescale(nk.signal_simulate(duration=5, sampling_rate=sr, frequency=5))
sound += pyshaman.generate_sound(frequency=[200], duration=5, volume=volume, rate=sr)

nk.signal_plot(sound)

# IPython.display.Audio(sound, rate=44000)  # https://github.com/microsoft/vscode-jupyter/issues/1012
pyshaman.write_wav(sound, filename="test2.wav")


# Stereo
sr = 44100
volume = nk.rescale(nk.signal_simulate(duration=5, sampling_rate=sr, frequency=10))
left = pyshaman.generate_sound(frequency=[1600], duration=5, volume=volume, rate=sr)

volume = nk.rescale(nk.signal_simulate(duration=5, sampling_rate=sr, frequency=2.5))
right = pyshaman.generate_sound(frequency=[200], duration=5, volume=volume, rate=sr)

# nk.signal_plot([left, right])
pyshaman.write_wav(left=left, right=right, filename="test2.wav")
