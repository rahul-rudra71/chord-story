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
   * Harder difficulties having more frequent note generation and faster obstacle speed
4. Select the audio file you would like to use for this level
   * .wav or .mp3 files
   * A few sample files are located under folder "music", but the application should run with most '.wav' or '.mp3' files. 
5. The level will begin
   * Move the player object between and along the six rendered strings to avoid the incoming notes. 
   * Running into an obstacle will result in the loss of a player life.
   * If you run out of lives, you will receive a game over message and be given the option to either restart the level or quit to the main menu. 
   * If you reach the end of the level without losing all your lives, you win and will be prompted to either restart the level or return to the main menu.

## Controls
* Up/Down Arrow Keys --> move vertically between strings
* Left/Right Arrow Keys --> move horizontally along the current string
* p Key --> pause the game

## Other Game Features
* Powerups:
  * Extra Life: Grants the player +1 life (max number of lives at a time is 3)
  * Invincibility: Grants the player the ability to phase through obstacles for a short period of time

## Known Glitches
* Sometimes when the player restarts the game, the player object will move to the right side of the screen. This is resolved by hitting the right arrow key to regain control.

## Other Notes
* This project requires an Ubuntu 20.04 VM to run.

## Additional Contributions
* Isabella Bond: Designed all of the pixel art included in the game using https://www.pixilart.com (7/13/2020-7/22/2020)