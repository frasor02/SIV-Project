# Acquisition of Image Samples with Human Agent

# Introduction
#Using the Arcade Learning Environment ALE, we acquire frames of Atari games of choice to be further processed.
#This project will study two environments:
#- Breakout: a simpler game used for simple testing of the processing algortihm
#- Skiing: a game with more objects in order to test the processing in more complex use cases.
#This notebook in order to have a faster acquisition plays the games with a human agent. Meaning that the recording of framers will take longer with the advantage of better quality gameplay.

# Libraries
#Now we import the necessary libraries. Let's have a rundown of each one and their purpose in this notebook:
#- keyboard: used to get input in order to play the game.
#- os: used for saving the frames in a directory.
#- shutil: used for cleaning up previous frames for the chosen games.
#- ale_py: main library that allows to play and record frames of lots of different Atari games.


import keyboard
import os
import shutil
from ale_py import ALEInterface, roms

# Utility Functions

#Now we define a function where, given the game and directory where to put the frames, the enviroment is configured, the frames are recorded and the human agents gives an input for every action until the game ends.

#The keybinds  for each actions are:
#- W: NOOP action, used to stay still and move the game forward.
#- S: FIRE action, used in breakout to start the game after each ball is lost.
#- A: LEFT action, used to move left.
#- D: RIGT action, used to move right.


def save_frames(game, recording_dir):
    """Function to let ALE play the game and save the frames of the match in a given recording dir."""
    ale = ALEInterface()
    ale.setInt('random_seed', 123)
    ale.setBool('display_screen', True) # We display the screen in order for the human player to act.
    ale.setBool('sound', False)

    ale.setString("record_screen_dir", recording_dir)
    ale.loadROM(roms.get_rom_path(game))

    # Each action has an assigned number:
    # NOOP: 0, FIRE: 1, RIGHT: 3, LEFT: 4
    actionDict = {'w': 0, 's': 1, 'd': 3, 'a':4}

    while not ale.game_over():
        event = keyboard.read_event()
        if actionDict.get(event.name, -1) != -1:
            action = actionDict.get(event.name, -1)
            ale.act(action)
    
    
    print(f"Finished episode. Frames can be found in {recording_dir}.")

#After defining the previous function we create another one to handle the presence or abscence of the directory where to put the frames in. 

def choose_and_save(game):
    """Function to do the whole process of saving frames given a game"""
    # Get all games available
    path_to_dir = f'../imgs/{game}/'

    if os.path.exists(path_to_dir):
        shutil.rmtree(path_to_dir)
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

    save_frames(game, path_to_dir)

## Breakout Acquisition
#What remains to be done is simply to execute the functions and save the frames for the Breakout game.

choose_and_save('breakout')

## Skiing game acquisition
#What remains to be done is simply to execute the functions and save the frames for the Skiing game.

choose_and_save('skiing')