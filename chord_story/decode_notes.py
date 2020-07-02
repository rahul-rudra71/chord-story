import librosa
import numpy as np
import random
from tkinter import filedialog
from tkinter import *


def detect_pitch(magnitudes, pitches, t):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]

    return pitch


def trim_onsets(onsets, times, offset):
    # Enforce space between onsets used for obstacle generation so player
    # has an appropriate amount of time for movement
    last = 0
    del_array = []
    # Remove onsets from array to generate obstacles that are too close together to be avoided (~<0.5 s)
    for index, current in enumerate(times):
        if current - last < offset:
            del_array.append(index)
        else:
            last = current
    onsets = np.delete(onsets, del_array)
    times = np.delete(times, del_array)

    return onsets, times


def trim_times(times):
    # Trim onset times to 2 decimal places
    for index, time in enumerate(times):
        times[index] = round(time, 2)

    return times


def assign_string(nt, prev):
    # string 0 = E4 - B5
    # string 1 = B3 - F#5
    # string 2 = G3 - D5
    # string 3 = D3 - A4
    # string 4 = A2 - E4
    # string 5 = E2 - B3
    string0 = ['E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5',
               'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
    string1 = ['B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4',
               'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5']
    string2 = ['G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4',
               'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5']
    string3 = ['D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4',
               'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4']
    string4 = ['A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3',
               'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4']
    string5 = ['E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3',
               'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3']

    out = ''
    possible = []
    if int(nt[len(nt) - 1]) < 2:
        out = 'low'

    if int(nt[len(nt) - 1]) > 5:
        out = 'high'

    if nt in string5:
        possible.append('5')

    if nt in string4:
        possible.append('4')

    if nt in string3:
        possible.append('3')

    if nt in string2:
        possible.append('2')

    if nt in string1:
        possible.append('1')

    if nt in string0:
        possible.append('0')

    # Check possible strings and assign note to one of them while ensuring the previous string
    # is not reused for better playability
    if len(possible) != 0:
        if prev in possible and len(possible) != 1:
            possible.remove(prev)
            out = random.choice(possible)
        else:
            out = random.choice(possible)

    return out


def decode(note_offset):
    # open gui to enable user to select file
    root = Tk()
    root.withdraw()
    root.update()
    filename = filedialog.askopenfilename(filetypes=(("wav files", "*.wav")))
    root.destroy()

    clip, sample = librosa.load(filename)

    onset_frames = librosa.onset.onset_detect(y=clip, sr=sample)

    # Get frequency levels against frame values
    ps, mags = librosa.core.piptrack(y=clip, sr=sample)

    # Get time values against onsets
    timestamps = librosa.frames_to_time(onset_frames, sr=sample)

    # Trim onset array
    trimmed_onset, new_times = trim_onsets(onset_frames, timestamps, note_offset)
    trimmed_times = trim_times(new_times)

    x = 0
    previous = ''
    keyout = {}
    while x < len(trimmed_onset):
        pitch_start = detect_pitch(magnitudes=mags, pitches=ps, t=trimmed_onset[x])

        if pitch_start != 0.0:
            note = librosa.core.hz_to_note(pitch_start)
        # The string numbers correspond to the strings in
        # Obstacle.py.  Iterate through the output dictionary
        # to obtain obstacle string placements and times

        temp_assign = assign_string(note, previous)
        if temp_assign == 'low':
            # Note must be below range, change to 2 to be assigned
            note = note[:-1] + '2'
            temp_assign = assign_string(note, previous)
        elif temp_assign == '':
            # Note must be somewhere from C2 - D#2, change to 3 to be assigned
            note = note[:-1] + '3'
            temp_assign = assign_string(note, previous)
        elif temp_assign == 'high':
            # Note must be above range, change to 5 to be assigned
            note = note[:-1] + '5'
            temp_assign = assign_string(note, previous)

        keyout[trimmed_times[x]] = temp_assign
        previous = temp_assign

        x = x + 1
    # Output dictionary of times and string assignments
    return [keyout, filename]
