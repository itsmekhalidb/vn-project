# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define obama = Character("Obama")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg oval_office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show obama normal at truecenter
    obama "normal"  

    show obama mad
    obama "mad"

    show obama confused
    obama "confused"

    show obama happy
    obama "happy"

    # This ends the game.

    return
