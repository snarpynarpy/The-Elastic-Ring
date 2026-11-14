# for better location xalign 0-1.0, yalign 0-1.0


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character ("Main character")
define c = Character ("Coach")
define r = Character ("Rebme")
define a = Character ("Anett")
define m = Character ("Meddal")
define cr = Character ("crowd")
    # maybe delted later, useful if the crowd has audio

default missed_weak_spot_damage = 10
default damage_cuased_when_weak_spot_is_hit_for_Rebme = 50
default damage_cuased_when_weak_spot_is_hit_for_Anett = 25
default damage_cuased_when_weak_spot_is_hit_for_Meddal = 10 
    # 3 is proably too low

default player = None
default enemy = None


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

       
        $ correct_direction = random.choice(enemy.directions)


        call screen dodge_screen(enemy.directions, enemy.hitboxes)

        $ dodge_choice = _return

       

        if dodge_choice == correct_direction:

            "You successfully dodged!"

            $ enemy.take_damage(weak_spot_damage)

            $ renpy.notify("You dealt [weak_spot_damage] damage!")

        else:

            "You failed to dodge!"

            $ player.take_damage(missed_weak_spot_damage)

            $ renpy.notify("You took [missed_weak_spot_damage] damage!")



        if not enemy.is_alive():

            hide screen battle_status

            return "win"

        

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


screen title_screen():

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "THE ELASTIC RING"

        textbutton "Click to Start":
            action Start()


label start:
$ player = create_player()

    scene bg outside 
    show mc PLACEHOLDER at left 
   
    mc "Wow… wow.. Wow!!! Today is an amazing day to be almost employed :) " 
    mc "Yup.. This should be the place!!!!"

    scene bg intro 
    show mc PLACEHOLDER at left 
    show c PLACEHOLDER at right 
    c "you are up in x, good luck, you are going to need it" 
   
    scene bg walk through 1
    # maybe delteted later 
   

    scene bg fight 1
    show mc PLACEHOLDER at left 
    show r PLACEHOLDER at right 

    $ enemy = create_rebme()

    "The first round begins!"

    call battle(enemy, damage_cuased_when_weak_spot_is_hit_for_Rebme)
    $ player.health = 100
    $ result = _return

    if result == "lose":

        jump ending1

    "lose"


    scene bg walk through 2
    # maybe delteted later 
    

    scene bg fight 2
    show mc PLACEHOLDER at left 
    show a PLACEHOLDER at right 

    $ enemy = create_anett()

    "The second round begins!"

    call battle(enemy, damage_cuased_when_weak_spot_is_hit_for_Anett)
    $ player.health = 100
    $ result = _return

    if result == "lose":

        jump ending2

    scene bg walk through 3
    # maybe delteted later 



    scene bg fight 3
    show mc PLACEHOLDER at left
    show m PLACEHOLDER at right

    $ enemy = create_meddal()

    "The third round begins!"

    call battle(enemy, damage_cuased_when_weak_spot_is_hit_for_Meddal)
    $ player.health = 100
    $ result = _return

    if result == "lose":

        jump ending3

    "lose"

    scene bg end 3 
    #lose third fight
    jump start


    scene bg end 2 
    #lose second fight * reminder health is reflilled 
    #at the end of the rounds

    jump start
   

    scene bg end 3 
    #loses final match
    
    scene bg end 3

    jump start


    scene bg end 4 
    #wins all matches, c dialog then turn around and fade to balck + logo/name



label ending1:

    scene bg end 1

    "You lost the first match."

    jump start


label ending2:

    scene bg end 2

    "You lost the second match."

    jump start


label ending3:

    scene bg end 3

    "You lost the final match."

    jump start

label ending4:
    scene bg end 4

    c "PLACEHOLDER"
    jump ending4
return 
