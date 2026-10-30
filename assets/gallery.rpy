
init offset = -1

label gallery:
    call screen cggallery
    return

screen cggallery():

    default currentsong = 0

    frame:
        style_prefix "cggal"
        background Frame("gui/button/b_idle.png",20,20)
        padding (20,14)
        align (.5,.4)
        has vbox
        textbutton _("CG Gallery 1") action ShowTransient("viewcg") activate_sound audio.choice
        textbutton _("CG Gallery 2") action ShowTransient("viewcgsmall") activate_sound audio.choice
        textbutton _("CG Gallery 3") action ShowTransient("viewcgtall") activate_sound audio.choice
        textbutton _("Concept Art") action ShowTransient("viewconcept") activate_sound audio.choice

    frame:
        style_prefix "cggal"
        background Frame("gui/button/b_idle.png",20,20)
        ysize 78
        xpadding 20
        align (.5,.7)
        has hbox
        yalign .5
        label _("Music:") yalign .5
        null width 10
        textbutton "1" action [ Play("music", audio.date, selected=False, loop=True), SetScreenVariable("currentsong",1) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "2" action [ Play("music", audio.pastille, selected=False, loop=True), SetScreenVariable("currentsong",2) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "3" action [ Play("music", audio.peri, selected=False, loop=True), SetScreenVariable("currentsong",3) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "4" action [ Play("music", audio.astra, selected=False, loop=True), SetScreenVariable("currentsong",4) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "5" action [ Play("music", audio.party, selected=False, loop=True), SetScreenVariable("currentsong",5) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "6" action [ Play("music", audio.romance, selected=False, loop=True), SetScreenVariable("currentsong",6) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "7" action [ Play("music", audio.finale, selected=False, loop=True), SetScreenVariable("currentsong",7) ]
        add "gui/button/check_selected_foreground.png"
        textbutton "8" action [ Play("music", audio.credits, selected=False, loop=True), SetScreenVariable("currentsong",8) ]
        add "gui/button/check_selected_foreground.png"
        textbutton _("OFF") action [ Stop("music", fadeout=1), SetScreenVariable("currentsong",0) ]

    if currentsong>0:
        frame:
            background Frame("gui/button/b_idle.png",20,20)
            align (0,.1)
            padding (40,10)
            xoffset -20
            at smallcg
            has hbox
            null width 40
            add "gui/songnote.png"

            if currentsong==1:
                text _("#1 - Lovely Date")
            elif currentsong==2:
                text _("#2 - Pastille")
            elif currentsong==3:
                text _("#3 - Periwinkle")
            elif currentsong==4:
                text _("#4 - Astragalus")
            elif currentsong==5:
                text _("#5 - Spooky Soirée")
            elif currentsong==6:
                text _("#6 - Romantic Evening")
            elif currentsong==7:
                text _("#7 - Starry Flowers")
            elif currentsong==8:
                text _("#8 - Pretty in Pink")

    textbutton _("Return") action Return() align (.5,.9) style "galreturn_button"


screen viewcg():
    modal True
    add "bg chapterbreak"
    default whichcg = 0

    label _("CG Gallery 1") style "game_menu_label" at galname

    add cglist[whichcg] at cgspan

    hbox:
        xalign .5
        yalign .7
        imagebutton auto "gui/button/b_prev_%s.png":
            if whichcg==0:
                action SetScreenVariable("whichcg", len(cglist)-1)
            else:
                action SetScreenVariable("whichcg", whichcg-1)

        frame:
            style_prefix "cggal"
            background Frame("gui/button/b_idle.png",20,20)
            ysize 78
            xpadding 20
            has hbox
            yalign .5
            textbutton "1" action SetScreenVariable("whichcg", 0) selected whichcg<6 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "2" action SetScreenVariable("whichcg", 6) selected 5<whichcg<12 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "3" action SetScreenVariable("whichcg", 12) selected 11<whichcg<15 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "4" action SetScreenVariable("whichcg", 15) selected 14<whichcg<17 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "5" action SetScreenVariable("whichcg", 17) selected 16<whichcg<25 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "6" action SetScreenVariable("whichcg", 25) selected 24<whichcg<48 activate_sound audio.choice
            add "gui/button/check_selected_foreground.png"
            textbutton "7" action SetScreenVariable("whichcg", 48) selected 47<whichcg activate_sound audio.choice

        imagebutton auto "gui/button/b_next_%s.png":
            if whichcg==len(cglist)-1:
                action SetScreenVariable("whichcg", 0)
            else:
                action SetScreenVariable("whichcg", whichcg+1)

    if whichcg<6:
        text _("Chapter 1 - First Date") at viewcgtitlepos
    elif whichcg<12:
        text _("Chapter 2 - Conjured Fragrance") at viewcgtitlepos
    elif whichcg<15:
        text _("Chapter 3 - Missteps") at viewcgtitlepos
    elif whichcg<17:
        text _("Chapter 4 - Peach Blossoms") at viewcgtitlepos
    elif whichcg<25:
        text _("Chapter 5 - Stifled Emotion") at viewcgtitlepos
    elif whichcg<48:
        text _("Chapter 6 - Longing") at viewcgtitlepos
    else:
        text _("Chapter 7 - Shooting Stars") at viewcgtitlepos

    text "#{}" .format(whichcg+1) pos (960,80)


    textbutton _("Return") action Hide("viewcg") align (.5, .9) style "galreturn_button"

style cggal_button:
    activate_sound None

transform viewcgtitlepos:
    pos (240,80)
    alpha 0 xoffset 30
    easein .5 alpha 1.0 xoffset 0

screen viewcgsmall():
    modal True
    add "bg chapterbreak"
    default whichcg = 0

    label _("CG Gallery 2") style "game_menu_label" at galname

    add smallcglist[whichcg] at smallcggalpos

    grid 3 3:
        xalign .82
        yalign .45
        # spacing 6
        for c, i in enumerate(smallcgbuttonlist,0):
            button:
                idle_background Frame("gui/button/gal2b_idle.png",20,20)
                hover_background Frame("gui/button/gal2b_hover.png",20,20)
                add i align (.5,.5) xoffset -2
                xysize (172,132)
                action SetScreenVariable("whichcg",c)
                focus_mask None

    textbutton _("Return") action Hide("viewcgsmall") align (.5,.9) style "galreturn_button"

transform smallcggalpos:
    yoffset 88
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0
    on hide:
        easein .5 alpha 0 xoffset -30

transform smallcg:
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0
    on hide:
        easein .5 alpha 0 xoffset -30

transform galname:
    align (.09,.89)
    # alpha 0
    # easein .5 alpha 1.0
    # on hide:
    #     easein .5 alpha 0

screen viewcgtall():
    modal True
    add "bg chapterbreak"
    default whichcg = 0

    label _("CG Gallery 3") style "game_menu_label" at galname

    if whichcg<8:
        viewport:
            # yinitial yinitial
            xalign gui.galvp_xalign
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            xsize 612
            # side_yfill True
            add tallcglist[whichcg]
            at tallcggalpos
    else:
        add tallcglist[whichcg] at tallcggalpos

    hbox:
        xalign .1
        yalign .46
        spacing 10
        imagebutton auto "gui/button/b_prev_%s.png":
            if whichcg==0:
                action SetScreenVariable("whichcg", len(tallcglist)-1)
            else:
                action SetScreenVariable("whichcg", whichcg-1)
        imagebutton auto "gui/button/b_next_%s.png":
            if whichcg==len(tallcglist)-1:
                action SetScreenVariable("whichcg", 0)
            else:
                action SetScreenVariable("whichcg", whichcg+1)
    textbutton _("Return") action Hide("viewcgtall") align (.11,.6) style "galreturn_button"

style galreturn_button:
    background Frame("gui/button/b_idle.png",20,20)
    padding (20,16)
    activate_sound audio.back
style galreturn_button_text is gui_button_text

transform tallcggalpos:
    # yalign 1.0
    alpha 0
    easein .5 alpha 1.0
    on hide:
        easein .5 alpha 0

screen viewconcept():
    modal True
    add "bg chapterbreak"
    default whichcg = 0


    frame xysize(520,560):
        style_prefix "cggal"
        background Frame("gui/button/b_idle.png",20,20)
        padding (20,20)
        align (.6,.5)
        add conceptlist[whichcg] at tallcggalpos

    text "#{}" .format(whichcg+1) pos (980,560)#align (.8,.8)

    hbox:
        xalign .1
        yalign .46
        spacing 10
        imagebutton auto "gui/button/b_prev_%s.png":
            if whichcg==0:
                action SetScreenVariable("whichcg", len(conceptlist)-1)
            else:
                action SetScreenVariable("whichcg", whichcg-1)
        imagebutton auto "gui/button/b_next_%s.png":
            if whichcg==len(conceptlist)-1:
                action SetScreenVariable("whichcg", 0)
            else:
                action SetScreenVariable("whichcg", whichcg+1)
    textbutton _("Return") action Hide("viewconcept") align (.11,.6) style "galreturn_button"
    label _("Concept Art") style "game_menu_label" at galname

define cglist = [
    "cg candle",
    "cg link",
    "cg firstkiss",
    "cg firstkiss2",
    "cg firsttime2",
    "cg firsttime3",
    "cg bottles",
    "cg sweet",
    "cg share",
    "cg share2",
    "cg share3",
    "cg share4",
    "cg bench",
    "cg partyscene",
    "cg partydance",
    "cg foldingscreen",
    "cg parkbench",
    "cg cast",
    "cg manga2",
    "cg friends",
    "cg close1",
    "cg close2",
    "cg close3",
    "cg close4",
    "cg close5",
    "cg goodbyekiss",
    "cg goodbyekiss2",
    "cg uniform",
    "cg them",
    "cg cozy1",
    "cg cozy2",
    "cg cozy3",
    "cg cozy4",
    "cg cozy4b",
    "cg cozy5",
    "cg cozy6",
    "cg inbed",
    "cg inbed2",
    "cg inbed3",
    "cg inbed4",
    "cg inbed5",
    "cg inbed5b",
    "cg inbed5c",
    "cg inbed6",
    "cg inbed6b",
    "cg inbed7",
    "cg inbed7b",
    "cg inbed7c",
    "cg talkitout",
    "cg walk",
    "cg walk2",
    "cg walk3",
    "cg hug",
    "cg hug2",
    "cg final1",
    "cg final2",
    "cg final3",
    "cg final4",
    "cg final5",
    "cg finalkiss",
    "cg finalkiss2",
    "cg finalkiss3",
    "cg finalkiss4"
    ]
define tallcglist = [
    "cg meetup",
    "cg firsttime",
    "cg readysetdate",
    "cg topple",
    "cg topple2",
    "cg hug3",
    "cg hug4",
    "cg hug5",
    "cg ending",
    "cg ending2"
    ]

define smallcglist = [
    "cg othercouple",
    "cg jacket",
    "cg mannequins",
    "cg bottlebroken",
    "cg bottlefixed",
    "cg pumpkin",
    "cg manga",
    "cg pancakes",
    "cg pasta"
    ]
define smallcgbuttonlist = [
    "cg2_couple",
    "cg2_jacket",
    "cg2_mannequins",
    "cg2_bottlebroken",
    "cg2_bottlefixed",
    "cg2_pumpkin",
    "cg2_manga",
    "cg2_pancakes",
    "cg2_pasta"
    ]

define conceptlist = [
    "ex_peri2",
    "ex_pastille2",
    "ex_astra",
    "ex_witch2",
    "ex_witch1",
    "ex_witch3",
    "ex_witch4",
    "ex_ui",
    "ex_ui2"
]
