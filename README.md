# chord-story
Working Prototype development repo for Chord Story

Github: https://github.com/michaelarobertsjr/chord-story.git

Apt-Get modules needed:
  ffmpeg:
    sudo apt install ffmpeg
  tk:
    sudo apt-get install python3-tk

Pip install: 
  In directory with setup.py, run "pip3 install ."
  
  Executable line to run: "chordstory"

Gameplay:
Running this command will bring up the main menu window, where you may select a play mode (Classic is the only mode currently implemented).  After this you can select a difficulty (with harder difficulties having more frequent note generation) and select the audio file you would like to use for this level (.wav and .mp3 currently implementd, .mp3 takes slightly longer to generate due to file conversion).  After this, the level will begin and you can move the player object between and along the six rendered strings to avoid the incoming notes.  If you lose 3 lives (by running into 3 of the obstacles generated) you will receive a game over message and be given the option to either restart the level or quit to main menu.  The same options are given if you complete the level without losing 3 lives, winning the game.

Controls:
Up/Down Arrow Keys --> moving vertically between strings
Left/Right Arrow Keys --> moving horizontally along the current string
p Key --> pause the game (when paused you may either resume the game or quit the level and return to main menu)
