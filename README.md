# SIV Project: Extracting Features from Atari games
The repository contains code regarding the project for the course of Signal, Image and Video of the University of Trento.

The goal of the project is to gather information on frames of two games used to test the processing algorithm:
- Breakout
- Skiing.

The processing is composed of the following phases:
- Finding SIFT Keypoints
- Feature matching between frames
- Finding the connected components in the frames
- Classifying the objects we found as stationary or moving
- Track the movement of moving objects.

## Installation guide
To install required modules, create a .venv file and use the command:
```
pip install -r requirements.txt
```

## Acquiring the Images
The folder */acquisition* contains the notebooks that acquires the frames of a given atari game,
saving them in path *../imgs/{game_name}*.
There are two options when it comes to acquiring frames:
- In the notebook *random_acquisition.ipynb* a random agent plays the games allowing for faster acquisition at the cost of low scores. 
- In the file *human_acquisition.py* a human player can play directly the games using the keyboard allowing for higher scores at the cost of lengthier acquisition times. This is just a python file and not a notebook because otherwise there are issues with the ale_py library.

## Episodes Video Visualization
In */processing* folder there is a *frames_to_video.ipynb* notebook to merge the frames into a video in order to better visualize the episode of the desired game.

## Processing
In */processing* folder there is a *processing.ipynb* notebook that processes the frames data to collect features from both the games. Here the explaination for the whole algorithm can be found along with the sperimental results.