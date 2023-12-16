init python:
    import os
    import chatgpt

# define obama = Character("Obama")

# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg oval_office

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show obama normal at truecenter
#     obama "normal"

#     show obama mad
#     obama "mad"

#     show obama confused
#     obama "confused"

#     show obama happy
#     obama "happy"

#     # This ends the game.
#     return

label start:
    python:
        # get openai key
        apikey = renpy.input("What is your OPENAI API Key?", length=64)

        # add context for chatgpt
        # system is added context
        # assistant is me directly controlling what the AI says
        # I will avoid this as much as possible
        messages = [
            {"role": "system", 
            "content": "You are President Obama, slightly worried about a silly " +
            "but potentially devastating threat to the United States. " + 
            "You are not ready to reveal this information yet."},
            {"role": "assistant", 
            "content": "Hello, this is President Barack Obama, what is your name?"}
        ]

    scene bg oval_office
    show obama normal at truecenter
    define obama = Character("Obama")

    # get player's name
    python:
        obama("Hello, this is President Barack Obama, what is your name?")

        user_input = renpy.input("What is your name?", length=1000)
        messages.append(
            {"role": "user", "content": user_input}
        )
        messages = chatgpt.completion(messages, apikey)
        response = messages[-1]["content"]
        obama("[response]")

    # introduce scenario
    show obama mad at truecenter
    python:
        messages.append(
            {"role": "system", 
            "content": "You are hesitant but ready to reveal what the "
            "threat is. After giving a short synopsis, ask the player if " +
            "they would like to go to a meeting room where you can describe " +
            "the threat in greater detail."}
        )
        messages = chatgpt.completion(messages, apikey)
        response = messages[-1]["content"]
        obama("[response]")

    # end game
    return