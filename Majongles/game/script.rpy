# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Majongles")

#characters

image s1 = "xd"
image s2 = "majonwaifu"

# The game starts here.

label start:

    play music "silence.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_conceptv2

    "I'm gay lol"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s1

    play music "boss.mp3"

    # These display lines of dialogue.

    e "Pal, who the fuck are you."

    "Huh? Who the fuck is this guy? Is he a mod?"

    e "Are you deaf brainlet? I'm asking who the fuck are you"

    menu:
        "I'm new to this server! Nice to meet you!":
            jump Idk

        "Are you fucking retarded?":
            jump idiot

    label Idk:

        e "Idk but it seems like you can't deal with being retarded"

    return

    label idiot:

    show s2

    e " B-b-baka! Why do you reply if you do not care that much?! You autistic spergmobile!"

    "What? He looks confused!"

    e "Anyways, faggot. What brought you here?"

    menu:
        "ExFalchion's video":
            jump kys

        "You":
            jump faggot

        "Your mom":
            jump baka2

    label kys:

    hide s2

    show s1

    e "Idk but it seems like you can't deal with being retarded"

    return

    label faggot:

    hide s2

    show s1

    e "I ask you, do an IQ test before speaking to me"

    return

    label baka2:

    hide s2

    show s2

    e "Nani??? That's my line!!"

    # This ends the game.

    return
