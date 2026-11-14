# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character ("Main character")
define c = Character ("Coach")
define r = Character ("Rebme")
define a = Character ("Anett")
define m = Character ("Meddal")
define cr = Character ("crowd")
    # maybe delted later, useful if the crowd has audio

missed_weak_spot_damage = 10
default damage_cuased_when_weak_spot_is_hit_for_Rebme = 50
default damage_cuased_when_weak_spot_is_hit_for_Anett = 25
default damage_cuased_when_weak_spot_is_hit_for_Meddal = 10 
    # 3 is proably too low

init python:

    import random

    class Fighter:

        def __init__(self, name, health, attack, hitboxes, directions):

            self.name = name
            self.health = health
            self.attack = attack
            self.hitboxes = hitboxes
            self.directions = directions

        def is_alive(self):
            return self.health > 0

        def take_damage(self, damage):
            self.health -= damage
            self.health = max(self.health, 0)

    class Player(Fighter):

        def __init__(self, name, health, attack):

            super().__init__(name, health, attack, 0, [])


    def create_player():

        return Player("Main character", 100, 20)

    def create_rebme():

        return Fighter(
            "Rebme",
            100,
            10,
            3,
            ["Left", "Right"]
        )


    def create_anett():

        return Fighter(
            "Anett",
            100,
            10,
            5,
            ["Left", "Right", "Up", "Down"]
        )


    def create_meddal():

        return Fighter(
            "Meddal",
            100,
            10,
            10,
            ["Left", "Right", "Up", "Down", "Space"]
        )

default missed_weak_spot_damage = 10

default rebme_weak_spot_damage = 50
default anett_weak_spot_damage = 25
default meddal_weak_spot_damage = 10


default player = None
default enemy = None


screen dodge_screen(directions, hitboxes):

    modal True

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "DODGE!"
        text "Choose a direction!"
        text "Hitboxes: [hitboxes]"

        for direction in directions:

            textbutton direction:
                action Return(direction)

label battle(enemy, weak_spot_damage):

    while player.is_alive() and enemy.is_alive():

        show screen battle_status(player, enemy)

        "The enemy prepares to attack!"

        # Randomly select the correct dodge direction
        $ correct_direction = random.choice(enemy.directions)

        # Let the player choose
        call screen dodge_screen(enemy.directions, enemy.hitboxes)

        $ dodge_choice = _return

        # Check whether the player chose correctly

        if dodge_choice == correct_direction:

            "You successfully dodged!"

            $ enemy.take_damage(weak_spot_damage)

            $ renpy.notify("You dealt [weak_spot_damage] damage!")

        else:

            "You failed to dodge!"

            $ player.take_damage(missed_weak_spot_damage)

            $ renpy.notify("You took [missed_weak_spot_damage] damage!")

        # Check if enemy has been defeated

        if not enemy.is_alive():

            hide screen battle_status

            return "win"

        # Check if player has been defeated

        if not player.is_alive():

            hide screen battle_status

            return "lose"

    hide screen battle_status

    return "win"


screen battle_status(player, enemy):

    vbox:
        xalign 0.05
        yalign 0.05
        spacing 10

        text "PLAYER"
        text "Health: [player.health]"

        null height 20

        text "[enemy.name]"
        text "Health: [enemy.health]"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

screen title_screen():

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

            text "THE ELASTIC RING"

        textbutton "Click to Start":
            action Return()

    scene bg outside 
     show mc (F1)
    mc "(this is placeholder) wrong place " 

    scene bg intro 
    show mc (F2)
    c "you are up in x, good luck, you are going to need it" 
   

    scene bg walk through 1
    # maybe delteted later 
    scene bg fight 1
    show mc F3  
    show R F4 
label battel
    "the round begins" 

    while true
        show screen battel status
        menu:
        "attack":
            $ player_turn()
                pause 3.0 
        if not enemy.is_alive(): 
        "you defeated R"
        jump win1 
    
        "Defend":
            $ player.defending = true
    
    
        $ enemy_turn 
             pause 3.0 
            if not player.is_alive(): 
            "lose"
            jump ending1 
        
            "Defend":
                $ player.defending = true

    label win1
    "drtyuio"

    label ending1
    "fadsaghuio"


    

    scene bg walk through 2
    # maybe delteted later 
    

    scene bg fight 2

    show mc F5  
     show a f6  
        label battel
    "the round begins" 

    while true
        show screen battel status
        menu:
        "attack":
            $ player_turn()
                pause 3.0 
        if not enemy.is_alive(): 
        "you defeated R"
        jump win1 
    
        "Defend":
            $ player.defending = true
    
    
        $ enemy_turn 
             pause 3.0 
            if not player.is_alive(): 
            "lose"
            jump ending2
        
            "Defend":
                $ player.defending = true

    label win2
    "drtyuio"

    label ending2
    "fadsaghuio"

     scene bg walk through 3
    # maybe delteted later 





    scene bg fight 3
    
    show mc f7  
    show m f8  
        label battel
    "the round begins" 

    while true
        show screen battel status
        menu:
        "attack":
            $ player_turn()
                pause 3.0 
        if not enemy.is_alive(): 
        "you defeated R"
        jump win1 
    
        "Defend":
            $ player.defending = true
    

        $ enemy_turn 
             pause 3.0 
            if not player.is_alive(): 
            "lose"
            jump ending1 
        
            "Defend":
                $ player.defending = true

    label win3
    "drtyuio"

    label ending3
    "fadsaghuio"


    scene bg end 1 (lose first fight)
    jump start


    scene bg end 2 (lose second fight * reminder health is reflilled at the end of the rounds)
  jump start
   



    scene bg end 3 (loses finnal match)
    
    scene bg end 3

    jump start


    scene bg end 4 (wins all matches, c dialog then turn around and fade to balck + logo/name) 

label ending1:

    scene bg end 1

    "You lost the first match."

    jump start


label ending2:


label ending3:

    return
