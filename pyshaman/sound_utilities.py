import wave

import numpy as np


def generate_sound(
    frequency=440, duration=5.0, amplitude=1.0, volume=1.0, rate=44100
) -> np.ndarray:
    """Generate sound of the given frequency and duration

    Parameters
    ----------
    frequency : int, optional
        Sound frequency, by default 440.
    duration : float, optional
        Sound duration, by default 5.0.
    amplitude : float, optional
        Amplitude of each frequency, by default 1.0.
    volume : float, optional
        Volume of the sound, by default 1.0.
    rate : int, optional
        Signal rate, by default 44100.

    Returns
    -------
    np.ndarray
        Sound data.
    """
    time_points = np.linspace(0, duration, int(duration * rate))
    # Sanitize input
    if isinstance(frequency, (int, float)):
        frequency = [frequency]
    if isinstance(amplitude, (int, float)):
        amplitude = np.repeat(amplitude, len(frequency))
    if isinstance(volume, (int, float)):
        volume = np.repeat(volume, len(time_points))

    data = np.zeros(len(time_points))
    for i, freq in enumerate(frequency):
        signal = np.sin(2 * np.pi * freq * time_points)
        signal *= amplitude[i]
        data += signal
    # Normalize data
    data -= np.min(data)
    data /= np.max(data)
    # Normalize by the maximum value of a two-byte integer is 2^15−1, which is the maximum volume.
    data *= 2 ** 15 - 1
    # Volume modulation
    data *= volume

    return data


def write_wav(left=None, filename="mysound.wav", right=None, rate=44100):
    """
    Writes the array data to the specified filename.
    The array data type can be arbitrary as it will be
    converted to numpy.int16 in this function.
    """
    # Number of channels
    try:
        _, n = np.shape(left)
    except ValueError:
        n = 1
        left = np.array(left)

    # Add right channel if available
    if n == 1 and right is not None:
        n = 2
        left = np.column_stack((left, right))

    soundfile = wave.open(filename, "w")
    soundfile.setnchannels(n)
    soundfile.setsampwidth(2)
    soundfile.setframerate(rate)
    newdata = left.flatten()
    soundfile.writeframesraw(newdata.astype(np.int16).tostring())
    soundfile.close()
