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
        # temp = chatgpt.completion(messages, apikey)
        # messages = temp[0]
        # text = temp[1]
        # for r in text:
        #     obama("[r]")

    # introduce scenario
    show obama mad at truecenter
    python:
        messages.append(
            {"role": "system", 
            "content": "You are hesitant but ready to reveal what the "
            "threat is. After giving a two sentence synopsis, ask the " +
            "player if they would like to move from the oval office to a " +
            "meeting room where you can describe the threat in greater detail."}
        )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")


    # either go to conference room or leave
    python:
        user_input = renpy.input("Will you go?", length=1000)
        messages.append(
            {"role": "user", "content": user_input}
        )
        messages.append(
            {"role": "system", 
            "content": "If the player's response seems to want to leave, " +
            "use the word goodbye. If they seem to want to go to the " +
            "conference room, do not use the word goodbye. Only include one " +
            "response; do not send both. Do not include about going " +
            "to the conference room."}
        )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")
        gb = 0
        if "goodbye" in messages[-1]["content"].lower():
            gb = 1
    if gb == 1:
        return
    
    # go to conference room
    hide obama with moveoutright
    pause(0.5)
    
    scene bg meeting_room
    show obama mad at truecenter with moveinleft

    # explain threat in detail
    python:
        messages.append(
            {"role": "system", 
            "content": "Explain the previously mentioned threat in " +
            "detail but do not provide a solution for it. Keep it relatively" +
            "short but be detailed and do not use the word done."}
        )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")

    show obama normal at truecenter
    # loop asking player if they have questions
    python:
        while "done" not in messages[-1]["content"].lower():
            user_input = renpy.input("Any questions?", length=1000)
            messages.append({"role": "assistant", "content": "Any questions?"})
            messages.append({"role": "user", "content": user_input})
            messages.append(
                {"role": "system", "content": "You must use the phrase \"now " +
                "that we're done with questions\" in your response if the " +
                "user has no more questions, otherwise do not use the " +
                "phrase. If they seem done, also ask them how they would " +
                "solve the crisis. Please limit responses to less than " +
                "6 sentences. Do not use the phrase if the user asked a " +
                "question."}
            )
            temp = chatgpt.completion(messages, apikey)
            messages = temp[0]
            text = temp[1]
            for r in text:
                obama("[r]")

    # ask how they would solve the crisis and determine if it's good or bad
    python:
        user_input = renpy.input("What is your solution?", length=1000)
        messages.append({"role": "user", "content": user_input})
        messages.append(
            {"role": "system", "content": "Evaluate whether this would be " +
            "a good or bad solution to the crisis. If it would be good " +
            "then use the word happy somewhere in your response, but do " +
            "not use it if it is a bad suggestion. If it would be a bad " +
            "solution then use the word mad, but do not use it if it is " +
            "a good solution. Be critical based on the information from " +
            "earlier questions asked by the player."}
        )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        emotion = ""
        if "mad" in messages[-1]["content"].lower():
            emotion = "mad"
        elif "happy" in messages[-1]["content"].lower():
            emotion = "happy"
        else:
            emotion = "normal"

    # set face and read text
    if emotion == "mad":
        show obama mad at truecenter
    elif emotion == "happy":
        show obama happy at truecenter
    elif emotion == "normal":
        show obama normal at truecenter
    else:
        show obama confused at truecenter
    python:
        for r in text:
            obama("[r]")

    # thank them for their time and exit
    python:
        messages.append(
                {"role": "system", "content": "Thank them for their time."}
            )
        temp = chatgpt.completion(messages, apikey)
        messages = temp[0]
        text = temp[1]
        for r in text:
            obama("[r]")
    hide obama with moveoutright
    pause(1.0)
    # end game
    return