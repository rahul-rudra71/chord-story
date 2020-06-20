import librosa
import numpy as np

def detect_pitch(magnitudes, pitches, t):
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

def decode(input_wav_file):
    filename = input_wav_file

    clip, sample = librosa.load(filename)

    onset_frames = librosa.onset.onset_detect(y=clip, sr=sample)

    # Get frequency levels against frame values
    ps, mags = librosa.core.piptrack(y=clip, sr=sample)

    # Get time values against onsets
    timestamps = librosa.frames_to_time(onset_frames, sr=sample)

    # Trim onset array
    trimmed_onset, new_times = trim_onsets(onset_frames, timestamps)

    x = 0
    keyout = {}
    while x < len(trimmed_onset):
        pitch_start = detect_pitch(magnitudes=mags, pitches=ps, t=trimmed_onset[x])
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
        if int(note[len(note) - 1]) < 3:
            keyout[round(new_times[x], 2)] = '5'

        elif int(note[len(note) - 1]) == 3:
            keyout[round(new_times[x], 2)] = '4'

        elif int(note[len(note) - 1]) == 4:
            keyout[round(new_times[x], 2)] = '3'

        elif int(note[len(note) - 1]) == 5:
            keyout[round(new_times[x], 2)] = '2'

        elif int(note[len(note) - 1]) == 6:
            keyout[round(new_times[x], 2)] = '1'

        elif int(note[len(note) - 1]) >= 7:
            keyout[round(new_times[x], 2)] = '0'

        else:
            print('Error.')

        x = x + 1
    # Output dictionary of times and string assignments
    return keyout

if __name__ == '__main__':
    keys = decode('BaseAfterBase.wav')
    print(keys)
