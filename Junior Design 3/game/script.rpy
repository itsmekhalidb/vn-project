init python:
    import os
    import chatgpt

#     show obama normal at truecenter

#     show obama mad

#     show obama confused

#     show obama happy

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
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")

    # introduce scenario
    show obama mad at truecenter
    python:
        messages.append(
            {"role": "system", 
            "content": "You are hesitant but ready to reveal what the "
            "threat is. After giving a two sentence synopsis, ask the " +
            "player if they would like to go to a meeting room where " +
            "you can describe the threat in greater detail."}
        )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")


    # end game
    return