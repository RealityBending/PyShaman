import wave

import numpy as np


def generate_sound(frequency=440, duration=5.0, volume=1.0, rate=44100) -> np.ndarray:
    """[summary]

    Parameters
    ----------
    frequency : int, optional
        [description], by default 440
    duration : float, optional
        [description], by default 5.0
    volume : float, optional
        [description], by default 1.0
    rate : int, optional
        [description], by default 44100

    Returns
    -------
    np.ndarray
        [description]
    """
    time_points = np.linspace(0, duration, int(duration * rate))
    data = np.sin(2 * np.pi * frequency * time_points)
    # Normalize by the maximum value of a two-byte integer is 2^15−1, which is the maximum volume.
    data = data * volume * (2 ** 15 - 1)
    return data


def write_wav(data, filename="mysound.wav", rate=44100):
    """
    Writes the array data to the specified filename.
    The array data type can be arbitrary as it will be
    converted to numpy.int16 in this function.
    """
    soundfile = wave.open(filename, "w")
    try:
        _, n = np.shape(data)
    except ValueError:
        n = 1
    soundfile.setnchannels(n)
    soundfile.setsampwidth(2)
    soundfile.setframerate(rate)
    newdata = data.flatten()
    soundfile.writeframesraw(newdata.astype(np.int16).tostring())
    soundfile.close()

