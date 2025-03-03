import pyperclip

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


def main():
    ## A deck of cards is built and used to generate a list of prompts.
    deck = build_deck(suits, values)
    prompts = build_list_of_prompts(deck, "bro,", " the shit")

    ## Copy the output to the clipboard to save the user from having to do it manually

    output = "\n".join(prompts)
    pyperclip.copy(output)
    print("Prompts copied to clipboard!")


    
    
main()