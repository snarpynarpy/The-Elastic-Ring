# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character ("Main character")
define c = Character ("Coach")
define r = Chacter ("Rebme")
define a = Charcter ("Anett")
define m = Charcter ("Meddal")
define cr = Charcter ("crowd")
    # maybe delted later, useful if the crowd has audio

missed_weak_spot_damage = 10
damage_cuased_when_weak_spot_is_hit_for_Rebme = 50
damage_cuased_when_weak_spot_is_hit_for_Anett = 25
damage_cuased_when_weak_spot_is_hit_for_Meddal = 10 
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
                    30,
                    3,
                    ["Left", "Right"]
                )
        
            def create_anett():
                return Fighter(
                    "Anett",
                    100,
                    40,
                    5,
                    ["Left", "Right", "Up", "Down"]
                )
        
            def create_meddal():
                return Fighter(
                    "Meddal",
                    150,
                    50,
                    10,
                    ["Left", "Right", "Up", "Down", "Space"]
                )
 modal True
    # modal True makes it interactive

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

        timer 3.0 action Return(None)


def player_turn:
    damage = player.deal_damage(enemy):
        renpy.notify(f"you attack {enemy.name} for {damage} damage!")


def enemy_turn:
    damage = enemy.deal_damage(enemy):
        renpy.notify(f"you attack {player.name} for {damage} damage!")
    if 
    player.defending:
    damage = random.raninit (int(enemy.attck*0.3), int(enemy.attck*0.7))
    play.defending = false
    else 
damage = enemy deal_damage(player)
player.take_damage(damage)
renpy.notify(f"{enemy_name} attacks you for {damage} damage")



screen battel_status():
    vbox: 
        text "player health {player.health}"
        text "enemy health {enemy.health}"
            if not player.isalive
                text "died"
        elif if not enemy.isalive
            text "win" 

defult player = player("Main character", health= 100, attack=20)
defult enemy = enemy("Rebme", health=100, attack=20)
defult enemy = enemy("Anett", health=100, attack=20)
defult enemy = enemy("Meddal", health=100, attack=20)
    #will need to change as "enemy refers to 3 different "
    # check to see if it works, possiabley chnage health


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside 
     show mc (F1- see book)
    mc "(this is placeholder) wrong place " 


    

    scene bg intro 
    show mc (F2)
    c "you are up in x, good luck, you are going to need it" 
   


    scene bg walk through 1
    # maybe delteted later 
    scene bg fight 1
    show mc F3 
    show R F1

    

    scene bg walk through 2
    # maybe delteted later 
    




    scene bg fight 2
     scene bg walk through 3
    # maybe delteted later 





    scene bg fight 3
    





    scene bg end 1 (lose first fight)
    




    scene bg end 2 (lose second fight * reminder health is reflilled at the end of the rounds)
   




    scene bg end 3 (loses finnal match)
    




    scene bg end 4 (wins all matches, c dialog then turn around and fade to balck + logo/name) 


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return





def player_turn:
    damage = player.deal_damage(enemy):
        renpy.notify(f"you attack {enemy.name} for {damage} damage!")


def enemy_turn:
    damage = enemy.deal_damage(enemy):
        renpy.notify(f"you attack {player.name} for {damage} damage!")
    if 
    player.defending:
    damage = random.raninit (int(enemy.attck*0.3), int(enemy.attck*0.7))
    play.defending = false
    else 
damage = enemy deal_damage(player)
player.take_damage(damage)
renpy.notify(f"{enemy_name} attacks you for {damage} damage")



screen battel_status():
    vbox: 
        text "player health {player.health}"
        text "enemy health {enemy.health}"
            if not player.isalive
                text "died"
        elif if not enemy.isalive
            text "win" 

(defult player = player("Main character", health= 100, attack=20)

defult player= 
            
defult enemy = enemy("Rebme", health=100, attack=20)
defult enemy = enemy("Anett", health=100, attack=20)
defult enemy = enemy("Meddal", health=100, attack=20)
    #will need to change as "enemy refers to 3 different "
    # check to see if it works, possiabley chnage health )

    defult player = None
    defult enemy = None


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

        timer 3.0 action Return(None)


            
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside 
     show mc (F1)
    mc "(this is placeholder) wrong place " 


    

    scene bg intro 
    show mc (F2)
    show c (F3)
    c "PLACE HOLDER you are up in x, good luck, you are going to need it" 
   


    scene bg walk through 1
    # maybe delteted later 




    scene bg fight 1
    show mc F4 at right
    mc "sdfghjkl"

    show R F5 at left
    r " "

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
      while true
        show screen battel status
        menu:
        "attack":
            $ player_turn()
                pause 3.0 
        if not enemy.is_alive(): 
        "you defeated R"
        jump win2
    
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
          while true
        show screen battel status
        menu:
        "attack":
            $ player_turn()
                pause 3.0 
        if not enemy.is_alive(): 
        "you defeated R"
        jump win2
    
        "Defend":
            $ player.defending = true
    
    
        $ enemy_turn 
             pause 3.0 
            if not player.is_alive(): 
            "lose"
            jump ending2
        
            "Defend":
                $ player.defending = true











