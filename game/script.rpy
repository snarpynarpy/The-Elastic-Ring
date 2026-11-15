
define mc = Character("Main character")
define c = Character("Coach")
define r = Character("Rebme")
define a = Character("Anett")
define m = Character("Meddal")
define cr = Character("Crowd")


image bg logo = "logo.png"
image bg outside = "outside.png"
image bg intro = "intro.png"
image bg ring = "inside_the _ring.png"
image bg black = "black_screen.png"
image bg hand_map = "hand-map.png"
image bg end1 = "end1.png"
image bg end2 = "end2.png"


image mc = "mc.png"
image C = "C.PNG"
image R = "r1.png"
image a_test = "a_test.png"
image m = "meddal_stand.png"
image A = "a_stand.png"
image H = "hand_1.png"
image co = "coach.PNG"

image R_defeated = "rebme_defeated.png"
image a_defeated = "anett_defeated.png"
image m_defeated = "meddal_defeated.png"


default missed_weak_spot_damage = 10

default damage_cuased_when_weak_spot_is_hit_for_Rebme = 50
default damage_cuased_when_weak_spot_is_hit_for_Anett = 25
default damage_cuased_when_weak_spot_is_hit_for_Meddal = 10

default player = None
default enemy = None


transform rebme_size:
    zoom 0.65

transform bg_fit:
    xysize (config.screen_width, config.screen_height)

transform anett_size:
    zoom 0.65

transform meddal_size:
    zoom 0.45

transform mc_size:
    zoom 0.65

transform enemy_move_left:
    ease 0.3 xoffset -150
    ease 0.3 xoffset 0

transform enemy_move_right:
    ease 0.3 xoffset 150
    ease 0.3 xoffset 0

transform enemy_move_up:
    ease 0.3 yoffset -100
    ease 0.3 yoffset 0

transform enemy_move_down:
    ease 0.3 yoffset 100
    ease 0.3 yoffset 0


init python:

    import random


    renpy.music.register_channel(
        "clock",
        mixer="sfx",
        loop=True
    )




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

            super().__init__(
                name,
                health,
                attack,
                0,
                []
            )

    def create_player():

        return Player(
            "Main character",
            100,
            20
        )

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

    def opposite_direction(direction):

        opposites = {
            "Left": "Right",
            "Right": "Left",
            "Up": "Down",
            "Down": "Up",
            "Space": "Space"
        }

        return opposites.get(direction, direction)


    def reset_game():

        renpy.music.stop(channel="clock", fadeout=0.1)
        renpy.music.stop(channel="music", fadeout=0.5)

        renpy.hide_screen("countdown")
        renpy.hide_screen("dodge_screen")
        renpy.hide_screen("battle_status")
        renpy.hide_screen("reset_button")

        renpy.jump("start")


label opening_music:

    play music "Featherweight_battle_theme.mp3" fadein 2.0

    $ renpy.music.set_volume(
        1.0,
        delay=1.0,
        channel="music"
    )

    return


label battle_music:

    $ renpy.music.set_volume(
        0.25,
        delay=1.0,
        channel="music"
    )

    return

screen countdown():

    modal True
    zorder 80

    default number = 3

    on "show" action SetScreenVariable("number", 3)

    frame:

        xalign 0.5
        yalign 0.5

        background "#00000099"
        padding (60, 40)

        text "[number]":

            size 110
            color "#ffffff"
            xalign 0.5

    timer 1.0 repeat True action If(
        number > 1,
        SetScreenVariable("number", number - 1),
        Return()
    )


screen dodge_screen(directions, hitboxes):

    modal True

    frame:

        xalign 0.5
        yalign 0.5

        padding (40, 30)

        vbox:

            spacing 20
            align (0.5, 0.5)

            text "DODGE!":

                size 40

            text "Choose a direction!"

            text "Enemy hitboxes: [hitboxes]"

            for direction in directions:

                textbutton direction:

                    action Return(direction)

screen battle_status(player, enemy):

    zorder 10

    frame:

        xalign 0.05
        yalign 0.05

        padding (20, 15)

        vbox:

            spacing 10

            text "PLAYER"

            text "Health: [player.health]/100"

            null height 20

            text "[enemy.name]"

            text "Health: [enemy.health]/100"


screen reset_button():

    zorder 100

    frame:

        xalign 0.98
        yalign 0.02

        background "#000000aa"

        padding (15, 10)

        textbutton "RESTART":

            text_size 20

            action Function(reset_game)

screen main_menu():

    tag menu

    add "bg logo" at bg_fit

    vbox:

        xalign 0.5
        yalign 0.75

        spacing 30

        text "THE ELASTIC RING":

            size 60
            color "#ffffff"
            xalign 0.5

        textbutton "START":

            xalign 0.5

            text_size 35

            action Start()


label battle(enemy, weak_spot_damage, enemy_image, defeated_image):

    while player.is_alive() and enemy.is_alive():

        show screen battle_status(player, enemy)

        "The enemy prepares to attack!"

        

        $ correct_direction = random.choice(enemy.directions)


        $ renpy.music.play(
            "clock_ticking.mp3",
            channel="clock",
            loop=True
        )

        $ renpy.music.set_volume(
            0.8,
            delay=0.2,
            channel="clock"
        )


    

        call screen countdown

        hide screen countdown


        $ renpy.music.stop(
            channel="clock",
            fadeout=0.3
        )



        call screen dodge_screen(enemy.directions, enemy.hitboxes)

        $ dodge_choice = _return


        $ enemy_direction = correct_direction


        if enemy_direction == "Left":

            show expression enemy_image as current_enemy at enemy_move_left

        elif enemy_direction == "Right":

            show expression enemy_image as current_enemy at enemy_move_right

        elif enemy_direction == "Up":

            show expression enemy_image as current_enemy at enemy_move_up

        elif enemy_direction == "Down":

            show expression enemy_image as current_enemy at enemy_move_down

        else:

            pause 0.3


        pause 0.3


        if dodge_choice == correct_direction:

            "You successfully dodged!"

            $ enemy.take_damage(weak_spot_damage)

            $ renpy.notify(
                "Weak spot hit! {} damage!".format(weak_spot_damage)
            )

        else:

            "You failed to dodge!"

            $ player.take_damage(missed_weak_spot_damage)

            # Normal counterattack.

            $ enemy.take_damage(player.attack)

            $ renpy.notify(
                "You took {} damage!".format(missed_weak_spot_damage)
            )


        if not enemy.is_alive():

            if enemy.name == "Rebme":

                show expression defeated_image as current_enemy at center, rebme_size

            elif enemy.name == "Anett":

                show expression defeated_image as current_enemy at center, anett_size

            elif enemy.name == "Meddal":

                show expression defeated_image as current_enemy at center, meddal_size


            "Your opponent has been defeated!"

            hide screen battle_status

            return "win"

        if not player.is_alive():

            $ renpy.music.stop(channel="clock", fadeout=0.2)

            hide screen countdown
            hide screen dodge_screen
            hide screen battle_status

            return "lose"


    hide screen battle_status

    return "win"

label death_screen:

    $ renpy.music.stop(channel="clock", fadeout=0.2)

    scene bg black at bg_fit

    centered "YOU DIED"

    pause 1.0

    jump start


label start:

    $ player = create_player()

    show screen reset_button

    call opening_music

    scene bg logo at bg_fit

    pause 2.0

    scene bg outside at bg_fit

    show H at right, mc_size

    mc "Wow… wow.. Wow!!! Today is an amazing day to be almost employed :)"

    scene bg hand_map at bg_fit

    mc "Yup.. This should be the place!!!!"

    scene bg intro at bg_fit

    show co at center

    pause 0.5

    show C at left
    with move

    c "Hey uhh.. You. The featherweight, right?"
    mc "Weird way to refer to me at an interview but yeah sure!!!"
    c "It's about time you came. Everyone's been waiting to see the new fighter, I have a lot of people betting on you. I can't wait to rake in the cash when.. You win… Definitely win. Oh and I'm your coach. You'll be lucky to even survive this place, featherweight. It's a fight to the death out here. Take this to fight, as a gift from me to you,"
    mc "To fight ^o^?? Wow what a fun interview ^_^"

    scene bg ring at bg_fit

    call battle_music

    show R as current_enemy at center, rebme_size

    $ enemy = create_rebme()
    c “How you fight is simple, featherweight. Just hit them with that ball (and get hit). Or dodge as well… but maybe don't do that. I've got some… plans for that.”
 
    r “You really think you can defeat the great speed demon Rembe? Prepare for this attack!!”

    mc "Oohh ok!!! (^v^)"

    "The first round begins!"

    call battle(
        enemy,
        damage_cuased_when_weak_spot_is_hit_for_Rebme,
        "R",
        "R_defeated"
    )

    $ result = _return

    if result == "lose":

        jump death_screen

    $ player.health = 100





label round_two:
    
    # Restore player health.
    $ player.health = 100


    scene bg ring at bg_fit

    show A as current_enemy at center, anett_size

    $ enemy = create_anett()







    c “You lived..?? I mean good job featherweight…i guess… but now you need to do the same here. And remember! Throw the fight!”

    mc “Throw… hmmmm… Of course I’ll throw the ball!!”

    c “no I meant.. Nevermind.”

    a “I’m Anett, the cutest magical girl in the world. I’ll defeat you with my magical charm ray!”

    mc “... THAT’S A GUN?!! ToT”

    a “Prepare to dodge this! I can shoot in all directions”

    "The second round begins!"

    call battle(
        enemy,
        damage_cuased_when_weak_spot_is_hit_for_Anett,
        "A",
        "a_defeated"
    )

    $ result = _return

    if result == "lose":

        jump death_screen

    # Restore player health.
    $ player.health = 100

    scene bg ring at bg_fit

    show m as current_enemy at center, meddal_size

    $ enemy = create_meddal()


   $ enemy = create_meddal()

c "HOW ARE YOU STILL ALIVE?? Featherweight, you can't possibly survive the next one!?"

m "Please don't hurt me..."

mc "Your snakes are so cool!!! What do you feed them?? :DDD"

m "Huh... I swear that kind of venom would knock out a person... I've even tested it on myself! That's why my legs don't feel so well..."

c "Featherweight! If you don't finish the job, they'll bounce back!!"

mc "Oh wow"

"The final round begins!"

call battle(
    enemy,
    damage_cuased_when_weak_spot_is_hit_for_Meddal,
    "m",
    "m_defeated"
)

$ result = _return

if result == "lose":

    jump death_screen

jump ending4

    $ renpy.music.stop(channel="clock", fadeout=0.3)

    scene bg ring at bg_fit
    c “KID, YOU SURVIVED??!!! Welp, my loss on money, but you’ll be my new star fighter! Bring me even more cash!! Congratulations! You survived all three rounds!"

    "You have won the tournament!"

    c “Wait…YOU DIDN’T FINISH THEM?”
    
    mc “what do you mean..?”
    r “YOU’RE DEAD FEATHER WEIGHT!”
    a “YOU’RE DEAD FEATHER WEIGHT!”
    m “YOU’RE DEAD FEATHER WEIGHT!”


    scene bg end1 at bg_fit
    pause 2.0

    scene bg end2 at bg_fit
    pause 2.0

    return
