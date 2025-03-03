import os

# Define suits and values
suits = ["hearts", "diamonds", "clubs", "spades"]
values = ["ace", "2","3","4","5","6","7","8","9","10","jack","queen","king"]


## create a lookup of filepaths to be use to determine what audio file to play
def load_audio_lookup():

    audio_lookup = {}
    for suit in suits:
        for value in values:
            filename = f"generated_audio/{value}_of_{suit}.mp3"
            audio_lookup[f"{value} of {suit}"] = filename
    return audio_lookup

