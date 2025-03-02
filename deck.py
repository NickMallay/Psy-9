suits = ["hearts", "diamonds", "clubs", "spades"]
values = ["ace", "2","3","4","5","6","7","8","9","10","jack","queen","king"]


def build_deck(suits, values):
    ## Build a list that represents a standard deck of cards
    ## List comprehension buils the list from the lists of suits and values
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    return deck


def build_list_of_prompts(deck):
    ## Generate a list of prompts intended for text-to-speach from a hardcoded prefix and a list representing a deck of cards
    
    
    ## This is currently a hard coded prompt, but this function will be reworked 
    ## to accept a string as an arugment reperesenting the desired prompt
    prompt = "Your spectator's chosen card was "
    
    list_of_prompts = []
    
    
    # loop through the list, joining each card to the end of the given prompt and adding it to a new list of prompts
    for card in deck:
        list_of_prompts.append(f"{prompt}{card}")
    return list_of_prompts


def main():
    ## A deck of cards is built and used to generate a list of prompts.
    deck = build_deck(suits, values)
    prompts = build_list_of_prompts(deck)

    ## this list of prompts is printed to the console for debugging purposes.
    for prompt in prompts:
        print(prompt)

    
    
main()