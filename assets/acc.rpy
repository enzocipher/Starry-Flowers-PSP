
define periacc1 = [ "side_peri_acc1_earring0",
    "side_peri_acc1_earring1", "side_peri_acc1_earring2",
    "side_peri_acc1_ribbon1", "side_peri_acc1_ribbon2",
    "side_peri_acc1_crown1", "side_peri_acc1_crown2",
    "side_peri_acc1_ears1", "side_peri_acc1_ears2",
    "side_peri_acc1_etc1", "side_peri_acc1_etc2",
    "side_peri_acc1_headband1", "side_peri_acc1_headband2",
    "side_peri_acc1_bigbow", "side_peri_acc1_sweets" ]

define periacc2 = [ "side_peri_acc2_choker0",
    "side_peri_acc2_choker2", "side_peri_acc2_choker3",
    "side_peri_acc2_choker1", "side_peri_acc2_fuwa",
    "side_peri_acc2_wings3", "side_peri_acc2_fuwa3",
    "side_peri_acc2_tail1", "side_peri_acc2_fuwa2",
    "side_peri_acc2_wings1", "side_peri_acc2_wings2",
    "side_peri_acc2_ribbon", "side_peri_acc2_rainbow",
    "side_peri_acc2_cloud",]

define periacc3 = [ "side_peri_acc3_glasses0",
    "side_peri_acc3_glasses1", "side_peri_acc3_glasses2",
    "side_peri_acc3_glasses3",
    "side_peri_acc3_gloom",
    "side_peri_acc3_sprout",
    "side_peri_acc3_shine",
    "side_peri_acc3_pawgloves",
    "side_peri_acc3_lollipop",
    "side_peri_acc3_thoughts",
    "side_peri_acc3_bodypillow"]

define periacc1text = [ _("(None)"),
    _("Light Earrings"), _("Dark Earrings"),
    _("White Ribbons"), _("Blue Ribbons"),
    _("Flower Crown"), _("Royal Crown"),
    _("Cat Ears"), _("Bunny Headband"),
    _("Angel Halo"), _("Demon Horns"),
    _("White Headband"), _("Pride Headband"),
    _("Large Bow"), _("Sweets") ]

define periacc2text = [_("(None)"),
    _("Light Choker"), _("Dark Choker"),
    _("Flower Choker"), _("Blue Flowers"),
    _("Fairy Wings"), _("Pretty Sparkles"),
    _("Cat Tail"), _("Lovely Hearts"),
    _("Angel Wings"), _("Demon Wings"),
    _("Large Ribbon"), _("Rainbow"),
    _("Raincloud")]

define periacc3text = [_("(None)"),
    _("Light Glasses"), _("Dark Glasses"),
    _("Stylish Glasses"), _("The Blues"),
    _("Sprout"), _("Shining"),
    _("Paw Gloves"), _("Lollipop"),
    _("Gay Thoughts"),
    _("Body Pillow")]

screen accessorize(outfit):

    default face = "side_peri_face_smile"

    add "bg chapterbreak"

    label _("Accessorize!") align (.2,.1) style "game_menu_label"

    frame xysize (420,420):
        background Frame("gui/button/b_idle.png",20,20)
        padding (10,10)
        align (.25,.5)
        add "side_peri_base"
        add periacc2[acc2]
        add outfit
        add face
        add periacc1[acc1]
        add periacc3[acc3]

    frame xysize (300,200):
        style_prefix "acc"
        background None
        xalign .7 ypos 180
        has vbox
        hbox:
            xalign .5
            textbutton _("Load Favorite"):
                align (.5,.5) padding (40,16) ysize None
                sensitive faveacc!=[0,0,0] selected False
                action [ SetVariable("acc1", faveacc[0]), SetVariable("acc2", faveacc[1]), SetVariable("acc3", faveacc[2]), Show("mynotif", msg=_("Looking fabulous~!")), SetScreenVariable("face", "side_peri_face_happy") ]
                activate_sound audio.acc_load

            imagebutton auto "gui/button/b_fave_%s.png":
                action [ SetVariable("faveacc", [acc1, acc2, acc3]), Show("mynotif", msg=_("Ooh, my favorite 💙")), SetScreenVariable("face", "side_peri_face_shy")]
                sensitive faveacc!=[acc1,acc2,acc3]
                activate_sound audio.acc_fave


        hbox:
            imagebutton auto "gui/button/b_prev_%s.png" action SetVariable("acc1", acc1-1) sensitive acc1>0

            textbutton periacc1text[acc1] action ShowTransient("acc_grid", group=1)
            # frame xysize gui.acc_button_xysize:
            #     background Frame("gui/button/b_idle.png",20,16)
            #     text periacc1text[acc1] align (.5,.5)

            imagebutton auto "gui/button/b_next_%s.png" action SetVariable("acc1", acc1+1) sensitive acc1<len(periacc1text)-1 xalign 1.0
        hbox:
            imagebutton auto "gui/button/b_prev_%s.png" action SetVariable("acc2", acc2-1) sensitive acc2>0

            textbutton periacc2text[acc2] action ShowTransient("acc_grid", group=2)
            # frame xysize gui.acc_button_xysize:
            #     background Frame("gui/button/b_idle.png",20,16)
            #     text periacc2text[acc2] align (.5,.5)
            imagebutton auto "gui/button/b_next_%s.png" action SetVariable("acc2", acc2+1) sensitive acc2<len(periacc2text)-1 xalign 1.0
        hbox:
            imagebutton auto "gui/button/b_prev_%s.png" action SetVariable("acc3", acc3-1) sensitive acc3>0

            textbutton periacc3text[acc3] action ShowTransient("acc_grid", group=3)
            # frame xysize gui.acc_button_xysize:
            #     background Frame("gui/button/b_idle.png",20,16)
            #     text periacc3text[acc3] align (.5,.5)
            imagebutton auto "gui/button/b_next_%s.png" action SetVariable("acc3", acc3+1) sensitive acc3<len(periacc3text)-1 xalign 1.0

        null height 20
        textbutton _("OK!") action [ Hide("mynotif"), Return() ]:
            background Frame("gui/button/b_idle.png",20,16) padding (120,20) xalign .5
            text_idle_color gui.hover_color
            text_hover_color gui.hover_muted_color
            activate_sound audio.acc_ok
            text_layout "nobreak"

        if face!="side_peri_face_smile":
            timer 2.0 action SetScreenVariable("face", "side_peri_face_smile")

style acc_button:
    background Frame("gui/button/b_idle.png",20,16)
    padding (0,16)
    xysize gui.acc_button_xysize

style acc_button_text:
    idle_color gui.hover_color
    hover_color gui.hover_muted_color
    xalign .5
    text_align .5

style acc_grid_image_button:
    xysize (120,120)
    idle_background Frame("gui/button/gal2b_idle.png",20,20)
    hover_background Frame("gui/button/gal2b_hover.png",20,20)
    selected_idle_background Frame("gui/button/gal2b_hover2.png",20,20)
    selected_hover_background Frame("gui/button/gal2b_selected_hover.png",20,20)

    selected_foreground "gui/button/acc_check.png"
    activate_sound audio.acc_load

screen acc_grid(group):

    default acc_group = periacc1
    if group==2:
        $ acc_group = periacc2
    elif group==3:
        $ acc_group = periacc3

    frame background Frame("gui/frame2.png",20,20):
        modal True
        align (1.0,.5) xoffset -60
        padding (40,40)
        style_group "acc_grid"
        grid 4 4:
            for c, i in enumerate(acc_group):
                if c:
                    imagebutton:
                        idle "thumb_" + i
                        if group==2:
                            action [SetVariable("acc2", c), Hide()]
                        elif group==3:
                            action [SetVariable("acc3", c), Hide()]
                        else:
                            action [SetVariable("acc1", c), Hide()]
            imagebutton:
                idle Null()
                if group==2:
                    action [SetVariable("acc2", 0), Hide()]
                elif group==3:
                    action [SetVariable("acc3", 0), Hide()]
                else:
                    action [SetVariable("acc1", 0), Hide()]

screen mynotif(msg):
    timer 2.0 action Hide("mynotif")

    text msg at mynotiftext

transform mynotiftext:
    align (.75,.2)
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0
    on hide:
        easein .5 alpha 0 xoffset 30
