import sys, os
import time
import random

def type(text: str):
    """Slowly types a line to the console.

    Args:
        text (str): A line of text.
    """
    # How quickly the text appears in the console.
    typing_speed = 100

    # Slowly prints each character in the text out.
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed )


def display_page_text(lines: list):
    """Displays all the lines of text and prompts the user for input.

    Args:
        lines (list): [description]
    """
    for line in lines:
        # Slowly types the line.
       type(line + os.linesep)

       # Randomly waits for a time between 0s and 1s.
       time.sleep(0.1)
    print()


def get_input(valid_input: list) -> str:
    """Gets input from the user and ensures it is valid.

    Args:
        valid_input (list): A list of all valid inputs.

    Returns:
        str: The user's input.
    """
    while True:    
        user_entered = input()            
        if user_entered not in valid_input:      
            print("Invalid input. Please choose a valid option: ", end="")
            user_entered = None            
        else:
            return user_entered


def get_response(options: list) -> int:
    """
    Displays the current page's possible choices and prompts the user to make a choice.
    Returns the corresponding next page number to the choice that the user made.

    Args:
        options (list): A list of choices that contains the text and the next page number.

    Returns:
        int: The next page number corresponding with the user's choice.
    """
    for index, option in enumerate(options): 
        print(str(index) + f'.) "{option[0]}"') 
    
    print()
    print("Please choose an option: ", end="")

    valid_inputs = [str(num) for num in range(len(options))]
    option_index = int(get_input(valid_inputs))
 
    return options[option_index][1]


def story_flow(story: dict):  
    curr_page = 1   
    while curr_page != None:    
        page = story.get(curr_page, None)
        if page == None:
            curr_page = None
            break
  
        display_page_text(page['Text'])
        
        if len(page['Options']) == 0:      
            curr_page = None      
            break     
        
        curr_page = get_response(page['Options'])
