import librosa
import numpy as np

def detect_pitch(y, sr, t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]

  return pitch

def trim_onsets(onsets, times):
    # Enforce space between onsets used for obstacle generation so player
    # has an appropriate amount of time for movement
    last = 0
    del_array = []
    # Remove onsets from array to generate obstacles that are too close together to be avoided (~<0.5 s)
    for index, current in enumerate(times):
        if current - last < 0.5:
            del_array.append(index)
        else:
            last = current
    onsets = np.delete(onsets, del_array)
    times = np.delete(times, del_array)

    return onsets, times

filename = "../chromatic_scale.wav"

clip, sample = librosa.load(filename)

onset_frames = librosa.onset.onset_detect(y=clip, sr=sample)

# Get frequency levels against frame values
pitches, magnitudes = librosa.core.piptrack(y=clip, sr=sample)

# Get time values against onsets
timestamps = librosa.frames_to_time(onset_frames, sr=sample)

# Trim onset array
trimmed_onset, new_times = trim_onsets(onset_frames, timestamps)

x = 0
while x < len(trimmed_onset):
    pitch_start = detect_pitch(y=clip, sr=sample, t=trimmed_onset[x])
    note = librosa.core.hz_to_note(pitch_start)
    #the string numbers correspond to the strings in
    #Obstacle.py.  Simply replace the print statements
    #with the same number and pass to Obstacle.py

    #string 0 (high) = C7 - infin
    #string 1 = C6 - B6
    #string 2 = C5 - B5
    #string 3 = C4 - B4
    #string 4 = C3 - B3
    #string 5 = A0 - B2
    if(int(note[len(note) - 1]) < 3):
        print('string 5')
    elif(int(note[len(note) - 1]) == 3):
        print('string 4')
    elif(int(note[len(note) - 1]) == 4):
        print('string 3')
    elif(int(note[len(note) - 1]) == 5):
        print('string 2')
    elif(int(note[len(note) - 1]) == 6):
        print('string 1')
    elif(int(note[len(note) - 1]) >= 7):
        print('string 0')
    else:
        print('Error.')
    print('%s %f' % (note, new_times[x]))
    x = x + 1
