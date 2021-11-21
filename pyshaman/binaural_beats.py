import numpy as np

from .sound_utilities import generate_sound, write_wav


def binaural_beat(left=400, right=440, duration=10, filename=None):
    """
    A binaural beat is an auditory illusion perceived when two different pure-tone waves with less than a 40 Hz difference between them, are presented to a listener dichotically (one through each ear). For example, listening to 520 and 530 Hz (presented respectively in the left and the right ear) will result in the illusory perception of a third tone, called a **binaural beat**, with a pitch correlating to a frequency of 10 Hz (the difference between the two tones). This effect was discovered in 1839 by Heinrich Wilhelm Dove.

    Parameters
    ----------
    left : int
        The frequency of the left ear.
    right : int
        The frequency of the right ear.
    duration : float
        The duration of the sound in seconds.
    filename : str
        The name of the file to save, e.g., ``"my_binaural_beat.wav"``.

    Examples
    --------
    >>> import pyshaman
    >>> pyshaman.binaural_beat(left=400, right=440, duration=10, filename="my_binaural_beat.wav")

    """
    stero = np.column_stack(
        (
            generate_sound(frequency=left),
            generate_sound(frequency=right),
        )
    )
    if filename is not None:
        write_wav(stero, filename=filename)
    return stero
