import librosa
import os

def detect_pitch(y, sr, t):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]

    return pitch

filename = input("Please enter file name: ")
y, sr = librosa.load(filename)
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

x = 0
while x < 8:
    pitch_start = detect_pitch(y=y, sr=sr, t=onset_frames[x])
    note = librosa.core.hz_to_note(pitch_start)
    print(note)
    x = x + 1
print(librosa.frames_to_time(onset_frames, sr=sr))     
              
