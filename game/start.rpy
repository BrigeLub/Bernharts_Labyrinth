define hasShears = False
define goodJokes = ["poop", "fart", "shit"]
define riddleAnswer = ["echo", "ECHO", "Echo"]
define n = Character("Narrator", who_color="#a12e2e")

label start:
    jump corn_maze_1

label entrance:
    $ hasShears = False
    jump fountain_room

label shackles_den:
    if hasShears:
        menu:
            "Cut a large hole -> Shackle Escape":
                jump cut_a_large_holeshackle_escape
            "Cut a small hole -> Player Escape":
                jump cut_a_small_holeplayer_escape
    else:
        menu:
            "Take the deal -> Crow Ending":
                jump take_the_dealcrow_ending
            "Refuse -> Eaten Ending":
                jump refuseeaten_ending
label cut_a_large_holeshackle_escape:
    n "You cut a large hole, Shackle Ransacks the world."
    return
label cut_a_small_holeplayer_escape:
    n "You cut a large hole, Shackle is pissed."
    return
label take_the_dealcrow_ending:
    n "You are a crow!"
    return
label refuseeaten_ending:
    n "You got eaten"
    return

label fountain_room:
    menu:
        "Go Right -> Maim's Nest":
            jump maims_nest
        "Peer into the Water -> Basin":
            jump basin

label maims_nest:
    n "There's a giant boar! Maybe you should run!" 

    $ jokeInput = renpy.input("Tell a joke:")
    
    if "knock" in jokeInput:
        jump knock_knock
    elif any(word in jokeInput for word in goodJokes):
        jump good_joke
    else:
        jump bad_joke

label dank_hallway:
    menu:
        "Keep Going? -> Deep Hallway":
            jump deep_hallway
        "Follow path back -> Maim's Nest":
            jump maims_nest

label deep_hallway:
    jump shackles_den

label basin:
    menu:
        "Follow axolotyl -> Garden Sewer 1":
            jump garden_sewer_1
        "No thanks -> Fountain Room":
            jump fountain_room

label garden_sewer_1:
    menu:
        "Follow axolotyl -> Garden Sewer 2":
            jump garden_sewer_2
        "Break through the grate -> Dank Hallway":
            jump dank_hallway
        "Go right -> Garden":
            jump garden

label garden_sewer_2:
    menu:
        "Enter the Pit -> Garbage Pit":
            jump garbage_pit
        "Go Back -> Garden Sewer 1":
            jump garden_sewer_1

label garbage_pit:
    $ hasShears = True
    jump deep_hallway

label corn_maze_1:
    menu:
        "Try Right -> Cmaze 2":
            jump cmaze_2
        "Try Left -> Cmaze 3":
            jump cmaze_3

label good_joke:
    jump garden

label bad_joke:
    jump fountain_room

label knock_knock:
    # You can randomize the reaction here
    jump good_joke

label garden:
    jump riddle

label riddle:
    $ answer = renpy.input("What am I?")

    if any(ans in answer for ans in riddleAnswer):
        "You have passed the riddle."
        menu:
            "Enter the pit -> Garbage Pit":
                jump garbage_pit
    else:
        menu:
            "Retry -> Riddle":
                jump riddle
            "Give Up -> Fountain Room":
                jump fountain_room

label cmaze_2:
    jump cmaze_5

label cmaze_3:
    menu:
        "Try Right -> Cmaze 5":
            jump cmaze_5
        "Try Left":
            jump mouse_dinner

label cmaze_4:
    menu:
        "Try Right":
            jump cmaze_2
        "Try the stone clearing":
            jump entrance

label cmaze_5:
    menu:
        "Try Right":
            jump cmaze_4
        "Try Left":
            jump cmaze_6

label cmaze_6:
    jump entrance

label mouse_dinner:
    jump cmaze_3

