#аэаээаэаэаэ бляяяя
#Экраны
screen choiceAGE:
    modal True
    imagebutton:
        xalign 0.5
        yalign 0.3
        auto "images/buttons/teen_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceAGE"), Jump("teen")]
        hovered Play("sound", "audio/hovered.mp3")

    imagebutton:
        xalign 0.9
        yalign 0.6
        auto "images/buttons/kid_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceAGE"), Jump("kid")]
        hovered Play("sound", "audio/hovered.mp3")

    imagebutton:
        xalign 0.1
        yalign 0.6
        auto "images/buttons/adult_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceAGE"), Jump("adult")]
        hovered Play("sound", "audio/hovered.mp3")

screen choiceGENDER:
    modal True
    imagebutton:
        xalign 0.5
        yalign 0.3
        auto "images/buttons/person_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceGENDER"), Jump("person")]
        hovered Play("sound", "audio/hovered.mp3")

    imagebutton:
        xalign 0.9
        yalign 0.6
        auto "images/buttons/female_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceGENDER"), Jump("female")]
        hovered Play("sound", "audio/hovered.mp3")

    imagebutton:
        xalign 0.1
        yalign 0.6
        auto "images/buttons/male_%s.png"
        action [Play("sound", "audio/click.mp3"), ToggleScreen("choiceGENDER"), Jump("male")]
        hovered Play("sound", "audio/hovered.mp3")

screen info:
    frame:
        padding (10,10)
        vbox:
            text "Отношения"
            text "Плейер - [player_like]"
            text "Нуби - [nooby_like]"

#звуки и музло
define audio.ooo = "audio/music/ooo.mp3"
define audio.uwa = "audio/music/uwa_so_temperate.mp3"
define audio.quiet_water = "audio/music/quiet_water.mp3"
define audio.home = "audio/music/home.mp3"
define audio.grillbs = "audio/music/grillb's.mp3"
define audio.snowy = "audio/music/snowy.mp3"

define audio.walk = "audio/sounds/walking.mp3"
define audio.run = "audio/sounds/running.mp3"
define audio.dooropen = "audio/sounds/dooropen.mp3"
define audio.doorclose = "audio/sounds/doorclose.mp3"
define audio.i_love_you = "audio/sounds/i_love_you.mp3"
define audio.page_turn = "audio/sounds/page_turn.mp3"
define audio.bookclose = "audio/sounds/bookclose.mp3"
define audio.turn_on_gamepad = "audio/sounds/turn_on_gamepad.mp3"

#картинки (фоны)
define image.choice = "images/BG/choice.png"
define image.beta = "images/beta.png"
define image.beginning_k = "images/BG/beginning.png"
define image.u_room_d = "images/BG/u_room_d.png"
define image.u_room_n = "images/BG/u_room_n.png"

#персонажики там аэаэаэ
define nvl = Character(None, kind = nvl)
define cr = Character("Креатор")
define n = Character("Nooby")
define p = Character("Player")

define title = Character(None,
    what_color = "ffffff",
    what_size = 50,
    what_xpos = 0.15,
    what_ypos = 1.0,
    window_background = None, 
    window_bottom_margin = 880,)

define y = Character("[y]")
define mom = Character("Мама")
define unknown = Character("???")

#остальная херь
define slowdissolve = Dissolve(1.0)

transform nar:
    xalign 0.5
    yalign 0.1

define fastdissolve = Dissolve(0.3)

transform lilright:
    xalign 0.9

transform moveright:
    linear 0.5 xpos 0.85

transform lilleft:
    xalign 0.1

image nightmare:
    "images/BG/dream_k1.png"
    pause (0.6)
    "images/BG/dream_k2.png"
    pause (0.6)
    "images/BG/dream_k3.png"
    pause (0.6)
    repeat

#шейк эффект
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #

#Отношения с разными прекрасными

default maxlove = 10
default minlove = 0

default nooby_like= 0 
default player_like= 0 


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

#лабел

label splashscreen:
    scene beta
    with slowdissolve
    pause (2)
    scene black with fade