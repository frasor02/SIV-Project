# SIV Project: Extracting Features from Atari games
The repository contains code regarding the project for the course of Signal, Image and Video of the University of Trento.
The goal of the project is to gather information on frames of a given game (i.e. Breakout).
The processing is composed of the following phases:
- Finding SIFT Keypoints
- Feature matching between frames
- Finding the connected components in the frames
- Classifying the objects we found as stationary or moving
- Track the movement of moving objects.

## Installation guide
To run the code, create a .venv file and use the command:
```
pip install -r requirements.txt
```

## Acquiring the images
The folders acquisition contains the notebook that acquires the frames of a given atari game,
saving them in path *../imgs/{game_name}*.

## Video visualization
In processing folder there is a notebook to merge the frames into a video in order to better visualize the episode of agent that played the game.

## Processing
In processing folder there is a notebook that processes the frames data to collect features from the game.