from gtts import gTTS
import os


suits = ["hearts", "diamonds", "clubs", "spades"]
values = ["ace", "2","3","4","5","6","7","8","9","10","jack","queen","king"]


def build_deck(suits, values):
    ## Build a list that represents a standard deck of cards
    ## List comprehension buils the list from the lists of suits and values
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    return deck


def build_list_of_prompts(deck, prompt_start="", prompt_end=""):
    ## Generate a list of prompts intended for text-to-speach
    #  Accepts a list of cards as well as a prompt start and end. 
    #  Spaces are accounted for in processing, so arugments are strip()'ed
    list_of_prompts = []
    
    
    ## Loop through the list, formatting the each card between the prompt segments.
    #  Both prompt segments default to "" so the card can be at the beginning, middle, or end. 
    #  As these are intended to be prompts for sound files, capitalization is irrelevent. 
    for card in deck:
        list_of_prompts.append(f"{prompt_start.strip()} {card} {prompt_end.strip()}")

    return list_of_prompts

def convert_to_audio(deck, prompts):
    ##Loops through each prompt and generates an audio file using gTTS
    # The files are then named and saved.
    for card, prompt in zip(deck, prompts):
        tts = gTTS(prompt)
        filename = f"generated_audio/{card}.mp3"
        os.makedirs("generated_audio", exist_ok=True)
        tts.save(filename)
    print("All prompts converted to audio!")

def main():
    ## A deck of cards is built and used to generate a list of prompts.
    deck = build_deck(suits, values)
    prompts = build_list_of_prompts(deck, "thank you for entering your personal security number. You're spectator chose the", "")

    convert_to_audio(deck, prompts)


    
    
main()