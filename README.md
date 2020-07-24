# Chord Story

## Description
Working Prototype development repo for Chord Story

Github: https://github.com/michaelarobertsjr/chord-story.git

## Install Instructions
* Apt-Get modules needed:
  * ffmpeg: sudo apt install ffmpeg
  * tk: sudo apt-get install python3-tk
* Pip install:
 * In directory with setup.py, run "pip3 install ."
 * Note: May need to run sudo with this command
* Executable line to run: "chordstory"

## Gamplay
1. Run command "chordstory"
2. Select a play mode
 * Classic is the only mode currently implemented.
3. Select a difficulty
 * Harder difficulties having more frequent note generation
4. Select the audio file you would like to use for this level
 * .wav or .mp3 files
 * We have included a folder of possible files, but the application should run with any '.wav' file. 
5. The level will begin
 * Move the player object between and along the six rendered strings to avoid the incoming notes. 
 * If you lose 3 lives (by running into 3 of the obstacles generated) you will receive a game over message and be given the option to either restart the level or quit to main menu. The same options are given if you complete the level without losing 3 lives, winning the game.

## Controls
* Up/Down Arrow Keys --> move vertically between strings
* Left/Right Arrow Keys --> move horizontally along the current string
* p Key --> pause the game

## Known Glitches
* Sometimes when the player restarts the game, the player object will move to the right side of the screen. This is resolved by hitting the right arrow key to regain control.

# Other Notes
* This project requires an Ubuntu 20.04 VM to run.