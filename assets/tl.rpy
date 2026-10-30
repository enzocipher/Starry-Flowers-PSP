#this screen lets you select your language before the game starts

define all_translations = [ (None, None, "{font=tl/None/Nunito-Bold.ttf}{size=32}English{/size}{/font}"),
    ("es", "rinphonny", "{font=tl/None/Nunito-Bold.ttf}{size=32}Español{/size}{/font}"),
    # ("ess", "Gabriel Fiallegas Medina\n(Basajaun Games)", "{font=tl/None/Nunito-Bold.ttf}{size=32}español (ES){/size}{/font}"),
    ("fr", "Yuri Akuto", "{font=tl/None/Nunito-Bold.ttf}{size=32}Français{/size}{/font}"),
    ("ger", "Antonio Moss", "{font=tl/None/Nunito-Bold.ttf}{size=32}Deutsch{/size}{/font}"),
    ("ita", "Rypher", "{font=tl/None/Nunito-Bold.ttf}{size=32}Italiano{/size}{/font}"),
    ("pl", "Nika Klag", "{font=tl/None/Nunito-Bold.ttf}{size=32}Polski{/size}{/font}"),
    ("ptbr", "Fah Braccini", "{font=tl/None/Nunito-Bold.ttf}{size=32}Português{/size}{/font}"),
    ("ru", "Zweelee", "{font=tl/ru/VDS_New.ttf}{size=36}Pусский{/size}{/font}"),
    ("ukr", "storyteller613", "{font=tl/ru/VDS_New.ttf}{size=36}Українська{/size}{/font}"),
    ("tur", "Naamk", "{font=tl/None/Nunito-Bold.ttf}{size=32}Türkçe{/size}{/font}"),
    ("zh", "Gu Lyencha", "{font=tl/zh/ResourceHanRoundedCN-Bold.ttf}{size=30}简体中文{/size}{/font}"),
    ("kor", "KyleHeren", "{font=tl/kor/Goyang.ttf}{size=32}한국어{/size}{/font}"),
    # ("jp", " ", "{font=tl/jp/ .ttf}{size=28}日本語{/size}{/font}"),
    ("vi", "Bánh", "{font=tl/None/Nunito-Bold.ttf}{size=32}Tiếng Việt{/size}{/font}"),
    ("thai", "Whateverzone", "{font=tl/thai/BoonJot-Regular.ttf}{size=32}ภาษาไทย{/size}{/font}"),
    # ("baq", "Gabriel Fiallegas Medina\n(Basajaun Games)", "{font=tl/None/Fiery_Turk.ttf}{size=24}basque{/size}{/font}"),
    # ("", "", "")
    ]

init python:
    def get_translatorname():
        for i in all_translations:
            if preferences.language==i[0]:
                return i[1]
        return ""

screen language():

    tag menu

    use game_menu(_("Language"), scroll="viewport"):
        null height 20

        vbox:
            spacing 14
            style_prefix "radio"
            xsize 800
            hbox:
                spacing 20
                box_wrap True
                box_wrap_spacing 20
                for i in all_translations:
                    textbutton i[2] action Language(i[0])

            null height 20
            textbutton _("Back") action ShowMenu("preferences") activate_sound audio.back

init -2:
    style langset_frame:
        xsize 700
        ypadding 30
        xalign .5
        yalign .5
        background None
    style langset_button:
        idle_background Frame("gui/button/gal2b_idle.png",20,20)
        hover_background Frame("gui/button/gal2b_hover2.png",20,20)
        selected_background Frame("gui/button/gal2b_hover.png",20,20)
        selected_hover_background Frame("gui/button/gal2b_selected_hover.png",20,20)
        padding (20,16)
        size_group "langset"
        xpadding 30
    style langset_button_text:
        xalign .5

    style langset_label:
        xalign .5

    style langset_vbox:
        xalign .5
        yalign .35

screen langset():
    modal True
    add "bg chapterbreak"

    default lang = None

    frame:
        style_group "langset"
        has vbox
        label "Language" style "game_menu_label" align (.5,.5)
        vbox:
            xsize 820
            hbox:
                spacing 20
                box_wrap True
                xalign .5
                for i in all_translations:
                    textbutton i[2] action SetScreenVariable("lang", i[0])

        null height 40
        textbutton "OK" xalign .5:
            action [ Language(lang), Return() ]
            keysym "game_menu" style "language_confirm_button"

style language_confirm_button:
    background Frame("gui/button/b_idle.png",20,20)
    padding (20,16)
    xsize 240
    activate_sound audio.choice
style language_confirm_button_text:
    font "tl/None/Nunito-Bold.ttf"
    size 40

##below doesn't show up in game, it's just for translation convenience
screen mobilestorepage():
    text _("two witch boys fall in love")
    text _("STARRY FLOWERS is a visual novel about two witch boys falling in love.")
    text _("it's a sequel to Syrup and the Ultimate Sweet and First Kiss at a Spooky Soiree, though you can still enjoy this game without playing the others first!")
    text _("FEATURES")
    text _("extremely sweet slow burn romance")
    text _("27k word count, estimated 2 hours to complete")
    text _("dress up game! choose from 20 accessories to make periwinkle look extra cute for his dates!")
    text _("bonus gallery including extra scenes")
    text _("CREDITS")
screen charaprofiles():
    text _("Pronouns: he/him")
    text _("Age: 26")
    text _("A flirty witch whose favorite things are beautiful dresses and cute witch boys.")
    text _("A kind and gentle boy who works at a candy shop. Used to hide the fact that he's a powerful witch.")
    text _("First Appearance:")
    text _("Syrup and the Ultimate Sweet")
    text _("First Kiss at a Spooky Soirée")
