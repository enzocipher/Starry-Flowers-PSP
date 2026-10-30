##
image cred1 = Text(_("Story + Art + Music\n\nby NomnomNami"), text_align=0.5, xalign=.2, yalign=0.25, color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred2 = Text(_("Ending Theme\n\"Pretty in Pink\"\nby Marlene Bellissimo"), text_align=0.5, xalign=.2, yalign=0.25, color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred3 = Text(_("Testing and Feedback"), color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred4 = Text(_("Special Thanks"), color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred5 = Text(_("Supported by Patrons"), color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred6 = Text(_("Made with\nRen'Py"), text_align=0.5, xalign=.2, yalign=0.25, color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
image cred7 = Text(_("Thanks for playing!"), xalign=.2, yalign=.8, color="#fff", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])

image cred comp = Composite(
    (480, 2280),
    (0, 0), "cred3",
    (0, 20), "names1",
    (0, 740), "cred4",
    (0, 760), "names2",
    (0, 1500), "cred5",
    (0, 1560), "names3")

image credscroll:
    subpixel True
    xoffset -200
    yanchor 0 yoffset -30
    "cred comp"
    linear 66.8 yanchor 1.0 yoffset -720

image flower1:
    "images/flower1.png"
    subpixel True
    rotate 0
    linear 5 rotate -360
    repeat

image flower2:
    "images/flower2.png"
    subpixel True
    rotate 0
    linear 3 rotate 360
    repeat

image pinkflowers1 = SnowBlossom("flower1", count=20, start=3)
image pinkflowers2 = SnowBlossom("flower2", count=20, start=3)
image credflowers:
    contains:
        "pinkflowers1"
    contains:
        "pinkflowers2"

image cinebar = Solid("#000", xsize=1280, ysize=60)
image cinebars:
    contains:
        "cinebar"
        yalign 0
    contains:
        "cinebar"
        yalign 1.0

image lyric tl1a = Text(_("You look so pretty in pink "), color="#58a3ff")
image lyric tl1b = Text(_("Against the starry night sky "), color="#58a3ff")
image lyric tl1c = Text(_("Without you my heart would sink "), color="#58a3ff")
image lyric tl1d = Text(_("So I am telling you why "), color="#58a3ff")

image lyric tl2a = Text(_("The world has to move "), color="#58a3ff")
image lyric tl2b = Text(_("And with that we have to make do "), color="#58a3ff")
image lyric tl2c = Text(_("But I don't want "), color="#58a3ff")
image lyric tl2d = Text(_("to do anything without you "), color="#58a3ff")

image lyric tl3a = Text(_("So now you know "), color="#58a3ff")
image lyric tl3b = Text(_("What I think "), color="#58a3ff")
image lyric tl3c = Text(_("You look so pretty in pink "), color="#58a3ff")

image lyric tl4a = Text(_("And here we go "), color="#58a3ff")
image lyric tl4b = Text(_("My love "), color="#58a3ff")
image lyric tl4c = Text(_("My dear "), color="#58a3ff")
image lyric tl4d = Text(_("My sweet "), color="#58a3ff")

#####
image lyric 1a = Text("You look so pretty in pink", color="#fff")
image lyric 1b = Text("Against the starry night sky", color="#fff")
image lyric 1c = Text("Without you my heart would sink", color="#fff")
image lyric 1d = Text("So I am telling you why", color="#fff")

image lyric 2a = Text("The world has to move", color="#fff")
image lyric 2b = Text("And with that we have to make do", color="#fff")
image lyric 2c = Text("But I don't want", color="#fff")
image lyric 2d = Text("to do anything without you", color="#fff")

image lyric 3a = Text("So now you know", color="#fff")
image lyric 3b = Text("What I think", color="#fff")
image lyric 3c = Text("You look so pretty in pink", color="#fff")

image lyric 4a = Text("And here we go", color="#fff")
image lyric 4b = Text("My love", color="#fff")
image lyric 4c = Text("My dear", color="#fff")
image lyric 4d = Text("My sweet", color="#fff")

image lyrics:
    align (.5,.99)
    alpha 0
    pause .7
    "lyric 1a" #.7
    alpha 1.0
    pause 4.5
    "lyric 1b" #5.2
    pause 3.8
    "lyric 1c" #9
    pause 3.8
    "lyric 1d" #12.8
    pause 4.9
    "lyric 2a" #17.7
    pause 3.8
    "lyric 2b" #21.5
    pause 4.9
    "lyric 2c" #26.4
    pause 2
    "lyric 2d" #28.4
    pause 4.8
    "lyric 3a" #33.2
    pause 4.3
    "lyric 3b" #37.5
    pause 3.4
    "lyric 3c" #40.9
    pause 4.1
    alpha 0 #45
    pause 32.3
    "lyric 3a" #77.3
    alpha 1
    pause 3.9
    "lyric 4a" #81.2
    pause 2.7
    "lyric 4b" #83.9
    pause 1.1
    "lyric 4c" #85
    pause 1
    "lyric 4d" #86
    pause 1
    "lyric 3c" #87
    pause 4.2
    # alpha 1.0 #91.2
    # linear 3 alpha 0

image tld lyrics:
    align (.5,.02)
    alpha 0
    pause .7
    "lyric tl1a" #.7
    alpha 1.0
    pause 4.5
    "lyric tl1b" #5.2
    pause 3.8
    "lyric tl1c" #9
    pause 3.8
    "lyric tl1d" #12.8
    pause 4.9
    "lyric tl2a" #17.7
    pause 3.8
    "lyric tl2b" #21.5
    pause 4.9
    "lyric tl2c" #26.4
    pause 2
    "lyric tl2d" #28.4
    pause 4.8
    "lyric tl3a" #33.2
    pause 4.3
    "lyric tl3b" #37.5
    pause 3.4
    "lyric tl3c" #40.9
    pause 4.1
    alpha 0 #45
    pause 32.3
    "lyric tl3a" #77.3
    alpha 1
    pause 3.9
    "lyric tl4a" #81.2
    pause 2.7
    "lyric tl4b" #83.9
    pause 1.1
    "lyric tl4c" #85
    pause 1
    "lyric tl4d" #86
    pause 1
    "lyric tl3c" #87
    pause 4.2
    # alpha 1.0 #91.2
    # linear 3 alpha 0

transform witchfly:
    on show:
        subpixel True
        yoffset 0
        easein 1.25 yoffset 20
        easein 1.25 yoffset 0
        repeat

    on hide:
        subpixel True
        parallel:
            easein 1.0 yoffset 20
            easein 1.25 yoffset 0
        parallel:
            xoffset 0
            easeout 3.0 xoffset -1000
        parallel:
            pause 1
            alpha 1.0
            linear 1.0 alpha 0

label credits:

    scene black
    show bg starfield at top
    show cinebars
    with Fade(2,1,1)

    play music credits
    show lyrics
    show tld lyrics

    show cg ending at witchfly with dissolve #.5
    pause 1
    show cred1 with dissolve #2
    pause 3.5
    hide cred1 with dissolve #6
    show cred2 with dissolve
    pause 3.5
    hide cred2 with dissolve #10.5

    show credscroll behind cinebars
    pause 33.8
    show credflowers behind credscroll
    pause 33
    hide credscroll

    show cred6 with dissolve #77.3
    pause 3.5
    hide cred6
    with dissolve #81.3

    hide cg
    pause 3#6

    hide credflowers
    with Dissolve(1.5)
    pause 2
    #91.2

    hide cinebars
    show cg ending2
    with Dissolve(1.5)

    show cred7 with dissolve
    pause 4

    stop music fadeout 4.0
    hide cred7 with dissolve

    scene black with Fade(2,1,1)

    if persistent.clear:
        pause 1
        jump returntotitle

label epilogue:
    $ acc1 = 0
    $ acc2 = 0
    play music audio.peri fadein 2.0
    scene bg chapterbreak with dissolve
    w happy "Thank you for reading \"Starry Flowers\"! A beautiful memoir detailing my first experience with true love 💙" id epilogue_0a503317
    w teehee "As a reward for finishing the story, you may now access the extra scenes and bonus chapters, along with a lovely image gallery~!"
    show pastille work ohno at rightb
    p "M-memoir...? Peri?? How detailed is this...?"
    w innocent "Don't worry, my sweet 💙 I've kindly skipped over all the sex scenes, so you have nothing to be embarrassed about." id epilogue_d85fbe55
    p kyaa "Th-the stuff leading up to those is still embarrassing...! How much did you leave in?!" with vpunch
    w smile "Ohh, it doesn't matter. This isn't canon! Merely an excuse to speak directly to the reader."
    w love "I would never reveal such private details about you (such as your fetishes) without your explicit consent 💙" id epilogue_16909bf1
    p scream "AAAAH!! AAAAHHHH, THAT'S ENOUGH, END THE SCENE!!!!" with vpunch
    w teehee "Please enjoy the bonus material! Thanks again~! 💙" id epilogue_809ccbf4

    $ persistent.clear = True
    if renpy.variant("pc"):
        $ mp.starryflowers = True
        $ mp.save()

    stop music fadeout 2.0
    scene black with Fade(1,1,.5)

label returntotitle:
    #pan up from the flowers to show the logo
    scene black
    show bg starfield
    with Fade(.5,.5,1)
    return
