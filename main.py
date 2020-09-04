from story_engine import *

#### HERE IS AN EXAMPLE OF A STORY. ####

example_story = {
    1: {
        'Text': [
            "This text will display before the user can make a choice.",
            "You can have as many lines of text as you want.",
            "Once it is finished typing, the user can then make a choice."
        ],
        'Options': [
            ("This is the first choice. It will take the user to page 2.", 2),
            ("This is the second choice. It will take the user to page 3.", 3),
        ]
    },
    2: {
        'Text': [
            "This is page 2.",
        ],
        'Options': [
            ("Go back to the start of the story.", 1),
            ("Go to the end of the story.", 4),
        ]
    },
    3: {
        'Text': [
            "This is page 3.",
        ],
        'Options': [
            ("Go back to the start of the story.", 1),
            ("Go to the end of the story.", 4),
        ]
    },
    4: {
        'Text': [
            "This is the end of the story.",
        ],
        'Options': [

        ]
    },
}

#### CREATE YOUR OWN STORY HERE! ####

story = {
    1: 
        'Text': [
            "Sample line.",
        ],
        'Options': [
            ("Sample choice", 1)
        ]
}

#### START YOUR CODE BELOW! ####

story_flow(example_story)