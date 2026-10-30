
define w = Character(_("Periwinkle"), image="peri", outlines=[(8,"#bedbff",0,0),(4,"#5083c1",0,0)])
define p = Character(_("Pastille"), image="pastille", outlines=[(8,"#FFDAED",0,0),(4,"#b84d75",0,0)])

define a = Character(_("Astragalus"), image="astra", outlines=[(8,"#f3daff",0,0),(4,"#a25898",0,0)])
define c = Character(_("Cassia"), image="cassia", outlines=[(8,"#ffe3da",0,0),(4,"#a26658",0,0)])
define j = Character(_("Jam"), image="jam", outlines=[(8,"#e6daff",0,0),(4,"#6e58a2",0,0)])
define k = Character(_("Kardaemon"), image="kar", outlines=[(8,"#fcdaff",0,0),(4,"#a2589d",0,0)])
define r = Character(_("Amaretti"), image="amaretti", outlines=[(8,"#e0b0d7",0,0),(4,"#a74a7c",0,0)])
define u = Character(_("Nasty Witch"), image="pumpkin", outlines=[(8,"#eda97e",0,0),(4,"#a76e4a",0,0)])
define h = Character(_("Himbo Witch"), image="him", outlines=[(8,"#ed7e8b",0,0),(4,"#a43956",0,0)])
define g = Character(_("Gumdrop"), image="gumdrop", outlines=[(8,"#ffa3d2",0,0),(4,"#ad1b52",0,0)])

define n = Character(None, what_color="#797798")
define narrator = Character(None, kind=nvl)

default acc1 = 0
default acc2 = 0
default acc3 = 0

image title ch1 = Text(_("{size=+8}Chapter 1{/size}\nFirst Date"), size=gui.label_text_size, text_align=.5)
image title ch2 = Text(_("{size=+8}Chapter 2{/size}\nConjured Fragrance"), size=gui.label_text_size, text_align=.5)
image title ch3 = Text(_("{size=+8}Chapter 3{/size}\nMissteps"), size=gui.label_text_size, text_align=.5)
image title ch4 = Text(_("{size=+8}Chapter 4{/size}\nPeach Blossoms"), size=gui.label_text_size, text_align=.5)
image title ch5 = Text(_("{size=+8}Chapter 5{/size}\nStifled Emotion"), size=gui.label_text_size, text_align=.5)
image title ch6 = Text(_("{size=+8}Chapter 6{/size}\nLonging"), size=gui.label_text_size, text_align=.5)
image title ch7 = Text(_("{size=+8}Chapter 7{/size}\nShooting Stars"), size=gui.label_text_size, text_align=.5)

transform chtitle:
    align (.5,.5)
    alpha 0
    easein .2 alpha 1.0

layeredimage side peri:

    always "side_peri_base"

    if acc2 == 0:
        "side_peri_acc2_choker0"
    elif acc2 == 1:
        "side_peri_acc2_choker2"
    elif acc2 == 2:
        "side_peri_acc2_choker3"
    elif acc2== 3:
        "side_peri_acc2_choker1"
    elif acc2== 4:
        "side_peri_acc2_fuwa"
    elif acc2== 5:
        "side_peri_acc2_wings3"
    elif acc2== 6:
        "side_peri_acc2_fuwa3"
    elif acc2== 7:
        "side_peri_acc2_tail1"
    elif acc2== 8:
        "side_peri_acc2_fuwa2"
    elif acc2== 9:
        "side_peri_acc2_wings1"
    elif acc2== 10:
        "side_peri_acc2_wings2"
    elif acc2== 11:
        "side_peri_acc2_ribbon"
    elif acc2== 12:
        "side_peri_acc2_rainbow"
    elif acc2== 13:
        "side_peri_acc2_cloud"

    group outfit auto:
        attribute witch default

    group face auto:
        attribute smile default

    if acc1 == 0:
        "side_peri_acc1_earring0"
    elif acc1 == 1:
        "side_peri_acc1_earring1"
    elif acc1 == 2:
        "side_peri_acc1_earring2"
    elif acc1 == 3:
        "side_peri_acc1_ribbon1"
    elif acc1 == 4:
        "side_peri_acc1_ribbon2"
    elif acc1 == 5:
        "side_peri_acc1_crown1"
    elif acc1 == 6:
        "side_peri_acc1_crown2"
    elif acc1 == 7:
        "side_peri_acc1_ears1"
    elif acc1 == 8:
        "side_peri_acc1_ears2"
    elif acc1 == 9:
        "side_peri_acc1_etc1"
    elif acc1 == 10:
        "side_peri_acc1_etc2"
    elif acc1 == 11:
        "side_peri_acc1_headband1"
    elif acc1 == 12:
        "side_peri_acc1_headband2"
    elif acc1 == 13:
        "side_peri_acc1_bigbow"
    elif acc1 == 14:
        "side_peri_acc1_sweets" 

    if acc3 == 0:
        "side_peri_acc3_glasses0"
    elif acc3 == 1:
        "side_peri_acc3_glasses1"
    elif acc3 == 2:
        "side_peri_acc3_glasses2"
    elif acc3 == 3:
        "side_peri_acc3_glasses3"
    elif acc1 == 4:
        "side_peri_acc3_gloom"
    elif acc1 == 5:
        "side_peri_acc3_sprout"
    elif acc3 == 6:
        "side_peri_acc3_shine"
    elif acc3 == 7:
        "side_peri_acc3_pawgloves"
    elif acc3 == 8:
        "side_peri_acc3_lollipop"
    elif acc3 == 9:
        "side_peri_acc3_thoughts"
    elif acc3 == 10:
        "side_peri_acc3_bodypillow" 


layeredimage pastille:

    always "pastille_base"

    group outfit auto:
        attribute witch default

    group face auto:
        attribute smile default

image petal1:
    "images/petal.png"
    subpixel True
    rotate 0
    linear 5 rotate -360
    repeat

image petal2:
    "images/petal2.png"
    subpixel True
    rotate 0
    linear 3 rotate 360
    repeat

image blossom1 = SnowBlossom("petal1", count=20, start=3)
image blossom2 = SnowBlossom("petal2", count=20, start=3)
image petals:
    contains:
        "blossom1"
    contains:
        "blossom2"

image mm_star:
    "images/titlestar.png"
    alpha .5
    subpixel True
    rotate 0
    linear 5 rotate -360
    repeat

image mm_flower:
    "images/titleflower2.png"
    alpha .5
    subpixel True
    rotate 0
    linear 5 rotate 360
    repeat

image mmblossom1 = SnowBlossom("mm_star", count=20, xspeed=(0,1), start=3)
image mmblossom2 = SnowBlossom("mm_flower", count=20, xspeed=(0,1), start=3)
image mmblossoms:
    contains:
        "mmblossom1"
    contains:
        "mmblossom2"

image firststar:
    alpha 0
    pos (300,160)
    pause .2
    alpha 1.0
    # offset (100,80)
    "shootingstar1"
    pause .08
    "shootingstar2"
    pause .08
    # "shootingstar3"
    # pause .08
    "shootingstar4"
    pause .08
    "shootingstar5"
    pause .08
    alpha 0

image shootingstar:
    alpha 0
    choice:
        pause 6
    choice:
        pause 2
    choice:
        pause 0
    alpha 1.0
    "shootingstar1"
    pause .08
    "shootingstar2"
    pause .08
    # "shootingstar3"
    # pause .08
    "shootingstar4"
    pause .08
    "shootingstar5"
    pause .08
    alpha 0
    pause .08
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 10
    alpha 1.0
    repeat

image shootingstars = SnowBlossom("shootingstar", count=20, border=0, xspeed=(-60,-140), yspeed=(0,0), start=3, horizontal = True)

transform righto:
    xalign .85
    yalign 1.0
    alpha 0
    easein .5 alpha 1.0

transform righta:
    xalign .85
    yalign 1.0

transform rightb:
    xalign .85
    yalign 1.0
    alpha 0 xoffset 30
    easein .5 alpha 1.0 xoffset 0

transform rightc:
    xalign .85
    yalign 1.0
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0

transform lefta:
    xalign 0
    yalign 1.0
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0

transform flip:
    xzoom -1.0
transform unflip:
    xzoom 1.0

transform cgspan:
    yanchor .5 yoffset 280
    yzoom 0 alpha 0
    easein .18 yzoom 1.0 alpha 1.0
    on hide:
        easein .18 yzoom 0 alpha 0

transform cg:
    alpha 0 xalign .5 yalign 1.0 yoffset -40
    parallel:
        easeout .4 alpha 1.0
    parallel:
        easein .3 yalign .12 yoffset -5
        easein .2 yoffset 0

transform slowbounce:
    yoffset 0
    linear .2 yoffset 12
    linear .2 yoffset 0
transform bounce:
    yoffset 0
    linear .1 yoffset 12
    linear .1 yoffset 0
transform bounce2:
    yoffset 0
    linear .07 yoffset 12
    linear .07 yoffset 0
    linear .07 yoffset 8
    linear .07 yoffset 0

transform slowpanup:
    xalign .66 yalign 1.0
    yoffset 0
    alpha 0
    easein .5 alpha 1.0
    linear 2 yoffset 320

transform slowpandown:
    yalign 0
    yoffset 0
    # pause 1
    subpixel True
    ease 12 yoffset -560

transform panup:
    yalign 1.0
    yoffset 0
    subpixel True
    ease 12 yoffset 560

label splashscreen:
    scene black
    if not persistent.setlanguage:
        call screen langset
        $ persistent.setlanguage=True
    show splash with dissolve
    pause 2
    hide splash with fade
    return

# The game starts here.

label start:
    $ save_name = _("Chapter 1 - First Date")
    $ _history=False
    $ quick_menu = False
    window hide
    scene bg chapterbreak with dissolve

    if not persistent.clear:
        $ quick_menu = True
        w happy "Hello, and welcome to the deliciously romantic tale of my first love~! 💙" id start_6178e217
        w calm "There's just one thing before we begin... I can grant you the power to choose my accessories at various points in the story."
        w teehee "I'm being very gracious to offer such a thing, you know 💙 If you use it, you had better make me look as adorable as possible." id start_5aa584c1
        w smile "This little feature has no effect on the story otherwise. It's simply for your entertainment, should you wish for it."

    $ quick_menu = False
    menu:
        n "Would you like to enable the dressup feature?"
        "Yes, let's accessorize!":
            $ faveacc = [0,0,0]
            if not persistent.clear:
                w happy "Then without further ado... let's get ready for my first date with Pastille~! 💙" id start_197230b2
            $ customboy = True
            call screen accessorize("side_peri_outfit_witch")
        "No thanks, I want to read uninterrupted":
            if not persistent.clear:
                w calm "Then without further ado..."
            $ customboy = False

    stop music fadeout 2.0
    scene bg chapterbreak with dissolve
    show title ch1 at chtitle
    centered "{w=3}{nw}"
    $ _history = True

    play music audio.pastille fadein 2.0
    scene bg streetdusk with fade
    window auto
    $ quick_menu = True
    "Today I met a boy at a candy shop."
    "The moment I saw him, I just knew I couldn't leave without flirting a little~"
    "He was so delightfully flustered. Which, of course, only made him that much cuter..."
    "When I told him to meet me here, he could only manage to nod in response."
    nvl clear

    w happy "(So cute... ah, my favorite type to pursue!)"
    w smile "(Ah! There he is now~)"

    scene bg streetdusk

    show cg meetup at slowpanup
    pause 3
    scene bg streetdusk with dissolve

    show pastille manto ehe at rightb
    p ehe "Hey! I hope I didn't keep you waiting too long..."
    w my "Pastille! Look at you~"
    w happy "And here I thought you looked plenty good in that uniform! My heart was unprepared 💙" id start_f197d905
    p ohno "S-sorry, is it too much? I can change..."
    w drool "My, but I haven't even fully seen what's under that cloak of yours! It'd be such a waste to change prematurely..."
    p shy "Ah... r-right! Forget it, then."
    w calm "Besides..."
    w teehee "It'll be my pleasure to unwrap you later on, my sweet 💙" id start_fa697933
    p kyaa "A-AH...!" with vpunch
    w innocent "Now, shall we head to dinner?"
    p omg "O-okay...! Lead the way...."

    scene bg streetdusk with Dissolve(.2)

    "I truly didn't expect it..."
    "He definitely seemed the type to have a more modest sense of style."
    "Thigh highs, with such a short skirt? Or was it a dress...? I only briefly glimpsed it."
    "I'm quite looking forward to seeing more tonight 💙" id start_da91d2ff
    nvl clear

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg restaurant
    show fg table
    with Fade(1,1,1)

    "The restaurant I decided on is one in my usual rotation. Good for a quiet, comfortable evening."
    "For a variety of dates, you must have a variety of locations in mind! Tonight's mood is... ~Romantic Rendezvous~"
    "It's a little high-end, though not overtly so. Just enough to make the night feel special 💙" id start_86384255
    nvl clear

    show pastille manto anxious at rightc behind fg
    n "Pastille slides into the booth, following Periwinkle's lead."
    n "One hand holds his mantle in place, while the other brushes his bangs aside anxiously..."
    w smile "Is this your first time?"
    p wha "Huh...?"
    w happy "Coming here, I mean. What did you think I was asking~?"
    p embarrassed "Ah--! Haha... no, nothing...."
    p neutral "I've never been here before. It seems fancy."
    w calm "I'm a fan of the atmosphere. The food isn't bad, either."

    w smile "Now, let's get a few formalities out of the way, shall we? First and foremost... your pronouns?"
    p oh "Oh, um, I just use he/him. What about you?"
    w calm "The same. Though I don't necessarily mind being called by others... especially considering my presentation."
    p ehe "Aha, understandable..."
    w smile "Next, expectations. I consider clarity in this regard to be a key part of ensuring we both enjoy ourselves to the fullest."
    w "I do this sort of thing often, you see. As such, I have a couple of ground rules to establish."

    p smile "Sure. I'm actually glad you brought it up..."
    w oh "Oh?"
    p ehe "I'm not looking for anything serious. In fact, I kinda prefer when it's just a one-night thing..."
    w innocent "Hmhm, we're on the very same page then!"
    p shy "Um, not that I mind if... y'know. We end up wanting to do this again some other time."
    w drool "(That's quite likely for me, in this case...)"
    w happy "Certainly! I'm open to that as well."
    p um "Did you have... any other ground rules? Sorry, I didn't mean to cut you off..."
    w smile "Are you nervous?"
    p nervous "Y...yes...."
    w calm "You can tell me to stop if you're ever feeling too overwhelmed. That's the other rule."
    p ohno "I, um..."
    w smile "...?"
    p embarrassed "I like... feeling overwhelmed. T-to an extent."
    w love "(I had assumed as much, but to hear you admit it outright...! Ah, Pastille! 💙)" id start_2164c6c3
    w teehee "In that case, I'll do my best to overwhelm you, my sweet~"
    p omg "A-AH...." with vpunch

    scene bg restaurant
    show fg table
    with Dissolve(.2)
    "Yes, this was shaping up to be a wonderful night indeed."
    "The waiter came to take our order. I went first, to give my sweet date a chance to compose himself."
    "With our food ordered, Pastille finally drops his mantle to reveal..."
    nvl clear

    show pastille witch embarrassed at righto behind fg
    w drool "(My, my...! So it was a cute little dress after all!)"

    w happy "Oh~ and here I thought you were saving the surprise for AFTER dinner!"
    p ehe "Sorry, um... I started feeling awkward with the extra layer...."
    w love "Don't apologize~ My only lament is not getting to take it off you myself 💙" id start_6210c123
    p kyaa "A-AH...!" with vpunch
    w teehee "You'll save the last few layers for me, won't you?"
    p dying "M...MHM...!"
    w innocent "That's all that matters, then 💙" id start_a79b9707

    "I'm having the time of my life. And by the looks of it, so is Pastille!"
    "Ahh, I LIVE to tease cute witch boys... how fortunate that I came across the sweetest one today!"
    nvl clear
    show fg table2 with Dissolve(.2)
    "Our food arrives before Pastille is able to recover."
    "He can't even look the waiter in the eye... 💙 How adorable!" id start_e9d06f67
    "No, I mustn't overindulge before we've even eaten our meal..."
    "There will be plenty of time after dessert~"
    nvl clear
    show pastille witch calm
    n "Pastille takes a few bites of his food before speaking up."

    p ehe2 "S-so, Periwinkle... what do you do for a living?"
    w smile "Besides tease you until you're barely able to speak?"
    p flustered "Yes, besides that!"
    w calm "My line of WORK, then... hmhm, I suppose I can tell you."
    show pastille witch neutral
    w smile "I'm an aromagician. I specialize in creating pleasant scents."
    scene bg restaurant
    show pastille witch neutral at righta
    show fg table2
    show cg candle at cgspan
    n "Periwinkle tugs his wand out from his sleeve and lightly taps the candle on the table."
    n "In a small burst, the atmosphere shifts around the pair..."
    n "The candle's original aroma is quickly forgotten as it's replaced by something new and cozier."
    hide cg
    p oh "Oh... that IS nice."
    p smile "What smell is that? I'm no good at pinpointing stuff like this..."
    w oh "Vanilla. I thought it suited you. Although..."
    w shy "I'm starting to think a more lustful scent might've been a better fit."
    p omgstop "Wh-what does that even mean...?!" with vpunch
    w teehee "Just that you've done nothing but exceed my expectations 💙" id start_f5e481ca
    p flustered "I-I'm not... doing anything...."

    n "Pastille retreats behind his glass of water, overwhelmed by embarrassment once again."
    w love "(I did say I'd go a little easier on him, didn't I...? Ah, he's just too irresistible 💙)" id start_0c12172a

    w calm "Anywho... I bottle and sell scents like this one. It's fairly lucrative work, once you build a reputation for yourself."
    p oh "Ah... sounds fulfilling."
    w smile "What about you, Pastille? What kind of magic do you specialize in?"
    p shy "Oh, I... I had mostly been living without magic, until recently."
    w oh "Without magic...? I can't imagine."
    p smile "It's not so bad. I mean, humans do it, so why not?"
    w "I suppose that's true."
    w smile "I very directly make a living off of mine, so I'd find myself in quite a bind if I wasn't able to use it!"
    w teehee "Not that I mind being bound from time to time, you know 💙" id start_a5adf706
    p omgstop "H-how do you keep doing that...?! Every time I think we're talking about something innocent..."
    w love "(Ah, I just can't help myself, can I?)"
    w teehee "Deliberate word choice, my sweet~ would you like me to hold back a little more?"
    p um "N-no, it's okay... I was just..."
    p embarrassed "Kinda impressed...."

    scene bg restaurant
    show fg table3
    with Dissolve(.2)

    "We finish up our meals, and decide on sharing a slice of strawberry cheesecake for dessert."
    "Pastille deliberately leaves the larger bits of strawberries for me..."
    "I wonder, is it because he doesn't like them? Or is he just THAT kind?"
    "Either way, this has quickly become my most favorite date of the past few months 💙" id start_a37124b7
    nvl clear

    show pastille witch neutral at righto behind fg

    w smile "Tell me more about yourself, Pastille. I'm afraid the only thing I know is that you work at the renowned Atelier Sweets..."
    p ehe "Oh, um... there's not much else to know...."
    w happy "Surely there's plenty more than just that! Any hobbies, perhaps?"
    p shy "C...cleaning, maybe?"
    w calm "Any NON work-related hobbies, dear."
    p ehe2 "Sorry, I never know how to answer these types of questions..."
    p smile "My best friend is an alchemist, so I've recently been going on little adventures to help gather ingredients for her craft."
    w my "Now THERE'S something interesting!"
    p shy "Other than that, I honestly don't get out much... I have my hands full running the store."
    w smile "So diligent 💙 Does that mean this is your first night out in a while?" id start_d04e37c7
    p oh "Ah... yeah, I guess it is."
    w innocent "I'm honored you were willing to share it with me, then~"
    p shy "Yeah! I don't think I ever would've tried this place if you hadn't brought me in..."
    p ehe "So... it's been worth it so far. Thanks, Periwinkle."

    scene bg restaurant
    show fg table4
    with Dissolve(.2)

    "The table had long been cleared, and yet our conversation continued through the night."
    "This place is never too busy, which always leaves me free to linger here without the guilt of taking up any much-needed table space."
    "The longer the date, the more satisfying the finale 💙 That's something I live by." id start_b7237054
    "Rushing straight to the climax inevitably gets a bit dull after a while. I want to enjoy this night to its fullest 💙" id start_6ec3835a
    nvl clear

    show pastille witch ehe at righto behind fg
    w love "Hmhmhm... Pastille... do you see the witch at that table over there?"
    p neutral "Hm...?"
    show cg othercouple at smallcg behind pastille
    w happy "Don't be too obvious, now. The one with the tall hat, you see...?"
    p uhoh "Ah... y-yeah, I see them."
    w teehee "I brought them here about two weeks ago. I guess they agreed that it made a nice date spot!"
    p ehe2 "Hahaha... I, um... I actually..."
    p uhoh "Th-the guy sitting across from them... I'm pretty sure I've been with him before."
    hide cg
    w my "NO... surely, you're joking, Pastille!"
    p omgstop "SH-SHHHH!!! Don't say my name so loudly...!"
    w happy "Just keep your head low, I'm sure he won't notice."
    w oh "...Oh, he's just looked this way."
    p scream "AAAAAHH...!!!" with vpunch
    w teehee "Only kidding 💙" id start_f4ea47ed
    p flustered "P-Peri...!!"
    w shy "Ooh, a nickname already? We're moving so fast..."
    p seriously "You're the one who's been calling me \"my sweet\" all night...!"
    w oh "Well, you are, aren't you? Whose fault is it that you share a name with candy?"
    p shout "Not mine!!"
    w smile "Still. Do you think those two make a good couple?"
    p flustered2 "How should I know...?!"
    w happy "Just imagine the kind of person I'd go on a date with, and pair them with the other!"
    p shy "And what kind of person is that...?"
    w innocent "You, for one 💙" id start_33e2c8d5
    p ehe "Pfft--maybe they wouldn't be so good together..."
    w oh "My, am I supposed to take offense to that?"
    p smile "Nah, that guy was just kinda pushy."
    w happy "Hmhm... ahaha, you're too much, Pastille!"

    play music audio.romance fadeout 2.0 fadein 2.0
    scene bg streetnight
    with Fade(1,1,1)

    "We eventually made our way out of the restaurant that night..."
    "It had gotten quite late already. When's the last time I stayed until closing...?"
    "There was never a moment of awkward silence between us. Only Pastille's embarrassed pauses--clear attempts to steer his mind away from debauchery 💙" id start_bc63f4b9
    "As we wander back into the night air, he's the first to speak up again..."
    nvl clear

    show pastille manto um at rightb
    p "You could've at least let me cover the tip..."
    w innocent "Nonsense. I'm the one who asked you out tonight, you don't have to cover a thing."
    p anxious "...."
    w teehee "In fact, I'd prefer if you DIDN'T cover--"
    p omg "Okay, I saw that one coming this time! Y-you don't have to say it..." with vpunch
    w happy "Too easy, hm? Ahaha~"
    w smile "But really, it's a shame to hide such a cute outfit from the world 💙" id start_b2f2809d
    p ehe "I-I don't have the confidence..."
    w shy "Ahh. Reminds me of my youth..."
    w smile "You'll get there, my sweet. One day, you'll be able to toss aside any feelings of inadequacy, and wear all sorts of daring outfits with pride!"
    p neutral "N-no, it's not a matter of self esteem or anything. It's just..."
    p embarrassed "If anyone I knew saw me in this, I would die."

    scene bg streetnight with Dissolve(.2)
    "So that's how it is, hm~?"
    "I'm being treated to a more intimate side of this witch boy right now 💙" id start_7db31c84
    "We walk together under the street lights, until we reach our original meeting place..."
    nvl clear

    show pastille manto neutral at righto

    w oh "Would you like me to escort you home?"
    p wha "N-no, that's okay..."
    w smile "Then, if you don't mind... my place is just down the street."
    w innocent "Perhaps you'd like to accompany me?"
    p embarrassed "Yes--I mean... I wouldn't want you to have to walk alone in the dark."
    w calm "Such a gentleman 💙" id start_de097d15

    scene bg streetnight with Dissolve(.2)
    show cg link at cgspan

    n "Periwinkle expertly slides his hand up and under Pastille's mantle, linking arms as they go along."
    n "They walk in comfortable silence, toward Periwinkle's house..."

    scene bg peristreetnight
    show pastille manto anxious at righto
    with fade

    w calm "Well, this is me..."
    w innocent "I had a most lovely evening. Thank you for accompanying me to dinner tonight 💙" id start_78aeb21b
    p wha "I-I had fun, too... thanks for inviting me out."
    show pastille manto nervous
    n "Pastille fidgets as if he has something to ask, but can't find the words."

    w smile "Pastille."
    show pastille manto wha
    n "Periwinkle takes a step closer."

    p "Y-yes...?"

    scene bg peristreetnight with Dissolve(.2)
    show cg firstkiss at cgspan

    n "He leans in, pausing for any sort of reaction..."
    show cg firstkiss2
    n "...only for Pastille's lips to come clumsily crashing forward."
    hide cg

    w drool "(He's in more of a rush than I thought...!)"
    w shy "(Then again, I DID spend all night winding him up....)"

    show pastille manto wow at rightc
    p "...."
    w love "(So cute...! 💙)" id start_446d0040
    w oh "Ah, Pastille... I just remembered."
    w innocent "Since we're here... would you like to come in and sample some of my magic?"
    p kyaa "I-I'd like that, yes...!"
    w calm "Very well, then 💙" id start_3cf70de4

    scene bg peristreetnight with Dissolve(.2)
    "We both knew from the beginning that he would be staying the night, of course."
    "It's just so much more fun drawing it out like this... 💙" id start_073ddabd
    "Ah, but if that kiss is any indication of things to come... I may have gone a little overboard tonight."
    "If so... we're in for quite a sleepover 💙" id start_3dc4f1af
    nvl clear
    window hide

    scene bg perihousedark
    with fade

    w calm "Sorry about the mess. I just haven't found the time to tidy up~"
    w oh "{nw}"

    n "The door closes loudly behind them. When Pastille doesn't respond, Periwinkle turns back to face him..."
    window auto
    scene bg perihousedark

    show cg firsttime at slowpanup
    pause 3
    n "Pastille's back is against the door as he fumbles to untie his mantle."

    scene bg perihousedark
    with dissolve
    w drool "(He's completely run out of patience, hasn't he...!)"
    w shy "(Then I'm afraid I simply have no choice but to indulge him~)"

    scene bg perihousedark
    show cg firsttime2 at cgspan

    w "Hmhm, I shouldn't keep you waiting a second longer, now should I?"
    p "M-mn...!"
    show cg firsttime3
    w "Ah, but I still need to change into something a little easier to take off..."
    w "Looking this good comes at a price, you see. I promise I won't keep you waiting."
    p "O-okay..."
    hide cg

    n "Periwinkle gives him another peck on the lips, and leads him through the cluttered living room to his bedroom door..."

    stop music fadeout 3.0
    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch2:
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0
    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 2 - Conjured Fragrance")
    show title ch2 at chtitle
    centered "{w=3}{nw}"

    play music audio.peri fadein 2.0

    scene bg bedroom with fade
    $ quick_menu = True
    "It took me ages to get out of bed that morning."
    "After all... I just couldn't stop thinking about how absolutely adorable Pastille was! 💙" id ch2_d9e096c6
    "He scrambled out of here almost as soon as he woke up, saying he couldn't be late for work..."
    "Such a shame. Would've been nice to get one last round in~"
    "...I did get a kiss goodbye, though 💙" id ch2_a69cdafc
    nvl clear
    w bed shy "Ahh, it's nice to feel like a housewife for a moment~"
    w smile "But I should get to work, too..."
    w happy "I have an order to fill, don't I~?"

    scene bg bedroom
    n "Periwinkle finally rolls out of bed and gets ready for the day..."

    scene bg perihouse with fade
    "The order in question is for a nearby apothecary."
    "Did you know? Aromagic like mine is actually quite good for you~"
    "It's got nothing on actual healing magic, but the calming atmosphere it creates does wonders for one's mood."
    nvl clear
    "This particular batch is meant to help with insomnia..."
    "Which is ironic, considering how late I stayed up with Pastille 💙" id ch2_9bdec3ec
    nvl clear

    w pj teehee "Whoops, can't be getting distracted now~ I really need to finish up these last few bottles..."
    w calm "{nw}"
    n "Periwinkle closes his eyes and draws his wand."
    show cg bottles at cgspan
    n "Large drops form at its tip, falling into the empty bottle one by one."
    n "With each drip, the bottle's contents swell, and after only the fifth drop, it's completely filled."
    hide cg

    w innocent "Perfect! Ahh, it's so much easier to finish these with a clear mind..."
    w shy "I can't help it if a refreshing night out is the only way to regain my focus 💙" id ch2_6e325112
    w teehee "Although~ I probably could've gotten one of these done last night if Pastille hadn't been so impatient... 💙" id ch2_afd133a7
    w calm "No, no, mustn't let my mind wander too far from work now."

    n "Periwinkle fills the remaining bottles, screwing the lids on as he goes."

    w smile "There. Hmhm, now my house is going to smell like lavender..."
    w innocent "I'd better head out before I'm lulled to sleep by my own magic~"

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_witch")
        $ quick_menu = True

    play music audio.astra fadeout 2.0 fadein 2.0

    scene bg apothecary
    show fg register
    with Fade(1,1,1)

    "The apothecary is only a short walk away, but I've never managed to walk in its doors on time."
    "Perhaps because it's so close, I always underestimate the time it takes to reach it..."
    "I can hear the owner tapping her foot with impatience as soon as I open the door."
    nvl clear

    show astra neutral at righto behind fg
    w happy "Astragalus~! I have that special order ready for you~"
    a annoyed "You're late again, Periwinkle."
    w innocent "Lost track of time 💙 You'll forgive me, won't you~?" id ch2_1019ebc0
    a "You are literally my only provider who has no respect for appointments."
    w oh "That's simply not true! I never miss a date."
    a lol "There's the problem. You were out getting laid again, weren't you?"
    w pout "How vulgar~ I had a romantic evening with a VERY cute boy..."
    w innocent "Who then ended up sleeping over 💙" id ch2_d7ebcbc7
    a whatever "Well, you had all week to fill the order. Try getting it done in advance next time."
    w calm "Yes, ma'am~"
    a closed "Now let's see what you brought..."

    "I've worked with Astragalus for a few years now."
    "She's COMPLETLY immune to my charms. Shocking, to say the least."
    "But it's meant we've been able to remain good friends all this time~"
    "Or... hm. Let's see..."
    nvl clear

    show astra neutral
    w oh "Astragalus. Would you consider us to be good friends?"
    a whatever "I put up with you."
    w happy "My, but you don't put up with ANYONE! You must really like me 💙" id ch2_373f7314
    a lol "You got a favor to ask or something? Is that what you're getting at?"
    w calm "No, I was just thinking of how to categorize our relationship."
    a "\"Business associate\" works just fine, doesn't it?"
    w happy "Come now, surely you consider us to be closer than that!"
    a sure "I know better than to get involved with you, Periwinkle."
    w my "Why, whatever do you mean?"
    a whatever "You're too dazzling."
    w innocent "I take that as a compliment~"
    a annoyed "Great, now will you stop distracting me? I'm trying to count."

    "Yes, we're definitely good friends."
    "\"Too dazzling\" though... I'm not sure there IS such a thing."
    "And what would be wrong with it if there was? What point is there in not shining as brightly as one can?"
    "Astragalus finishes counting the bottles, sighing in feigned exasperation as she marks them off her checklist..."
    nvl clear

    a sure "You may always be late... but you deliver quality every time. You're consistent, if nothing else."
    w teehee "The waiting is part of the fun. It builds excitement, wouldn't you say?"
    a whatever "Nope, just builds frustration for me. But at least you always come through."

    n "She unlocks a small drawer behind the counter, and takes out an envelope with Periwinkle's name scribbled on it."

    a closed "Here's the rest of your payment. Don't spend it all in one place."
    w calm "Oh, I couldn't if I tried! Really, you're too generous..."

    show astra eyeroll
    n "Astragalus rolls her eyes and begins stocking the shelves with her new inventory."

    "Two or three orders a month... that's all it takes to support myself, entirely through this apothecary."
    "Hard to believe my magic is really worth so much, but who am I to complain?"
    "It's certainly a more favorable balance compared to the kind of work I was doing years ago."
    nvl clear
    "And I do enjoy the freedom, the excessive amounts of time I have for partying, for dates..."
    "Ah, on that note~"
    nvl clear

    w happy "With all that business out of the way... would you like to hear about my date? 💙" id ch2_0b1b7e93
    a sure "Would I LIKE to? Not necessarily."
    w teehee "Please, Astragalus, as someone with no romance in your OWN life, the least you can do is live vicariously through me~"
    a whatever "The no romance thing is by choice. I listen to you gush for your own damn sake."
    w my "For MY sake?"
    a sure "Yeah, I'm afraid you might actually implode if you had no one to talk to about this stuff."
    a lol "I'm actually making a noble sacrifice every day that you come in here with new tales of romantic conquest."
    w pout "Hmph. If you're truly suffering, I shall desist..."
    a smile "That's the thing, though... I DO like seeing you all worked up over something, even if I don't understand it myself."
    w happy "Ahh, so there IS a mutual benefit! You'll listen, then? 💙" id ch2_dfd74c02
    a sure "Yeah, at least until I get all this put away. After that, I'm kicking you out for the day."

    w calm "Fair enough. I'd better be brief, then..."
    show astra happy
    w teehee "He's the absolute cutest thing! I picked him up at a candy shop yesterday 💙" id ch2_c163a19e
    w happy "Fluffy pink hair, with golden eyes, naturally rosy cheeks that make him look as if he's always a little embarrassed by something..."
    w shy "He's shy, but not the type that becomes paralyzed in the bedroom--"
    a augh "Periwinkle, for the last time, I do NOT need to hear about bedroom stuff." with vpunch
    w my "I wasn't giving any details!"
    w shy "Although, the details ARE the best part 💙" id ch2_f28bb905
    a annoyed "This is a \"safe for work\" zone only. Break that rule, and you're outta here."
    w innocent "My apologies~ I'll refrain."
    w love "Anyway, my point is... he's EXTREMELY cute. Adorable, in fact!"
    a eyeroll "Right, so, standard fare for you."
    w my "Absolutely not! If he was just your average cutie, would I be emphasizing his cuteness so much?"
    a sure "I don't meet these people, so it's all the same to me."
    w oh "How can it be~? The intensity is so drastically different... perhaps SO intense that I'm having trouble explaining it properly."
    a closed "I'll say. All you've really told me so far is that he's cute and shy."
    w shy "He's kind, as well! He saved the best part of our dessert for me without even asking!"
    a lol "Wow, I would've led with that one."
    w pout "Ohh, enough of your sarcasm. When all my favorite details are off-limits, what do you suppose I'm LEFT with?"
    a happy "Well, what really matters is that you had a good night. Even if it meant you couldn't get here on time like I asked."
    w love "Ahh~ I'm already hoping to see him again, to be honest..."
    a hm "Oh yeah? Don't hear that from you very often."
    w oh "Really? But I've gone on second dates all the time."
    a lol2 "This guy got a name?"
    w shy "Hmhm, I don't kiss and tell 💙" id ch2_899be6dd
    a sure "No, actually, you tell me about everyone you kiss."
    a lol "C'mon, if he's really the absolute cutest, it's a shame to keep him anonymous, right? Not like I'm gonna tell anyone anyways."
    w calm "Fine... his name is Pastille."
    a annoyed "Hmph. Even his name's cute."
    w happy "Right~?"
    w smile "Oh, that reminds me--he sold me some candies that share his name. Would you like to try?"
    a happy "Sure. How could a witch turn down free candy?"
    n "Periwinkle digs into his bag and pulls out one of the pastilles."
    n "He hands the candy to Astragalus, who promptly unwraps it and pops it into her mouth."
    a hm "Mmf... Oh, these are GOOD. Where'd you say this candy shop was?"
    w happy "Not far from here! I'll give you directions..."

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg streetday
    with Fade(1,1,1)

    "Shortly after telling Astragalus where to find Atelier Sweets, she unceremoniously kicked me out..."
    "She'd long finished putting all those bottles away, after all."
    "With money in my pocket, and no more work to be done for the moment... I'm free to begin pursuing my next date~"
    nvl clear
    "But wherever shall I go? It's a weekday, too early for parties, too early for drinks..."
    "I suppose I could return home and straighten up the place. However..."
    nvl clear

    w calm "(Why would I busy myself with chores when I could be celebrating another order successfully filled?)"
    n "Before Periwinkle can decide on where to go, a familiar witch approaches him."

    show cassia oh at rightb
    c "Periwinkle...?"
    w happy "Ohh, Cassia! So lovely to see you~"
    c happy "Yay, I'm so glad we ran into each other~"

    "How to describe Cassia..."
    "She's exceedingly cuddly. We met at a party one night, during which she latched onto my arm and never let go. Quite endearing!"
    "Since then, we've gone on little dates from time to time..."
    "She really loves my magic, so I tend to spoil her whenever we're together 💙" id ch2_91a4c39c
    nvl clear

    w smile "Did you need something, dear?"
    c aww "Ah, yes! I tried coming over last night, but you didn't seem to be home..."
    w shy "Aww, you came to visit me? I'm flattered 💙" id ch2_693e007a
    w smile "I must've been out to dinner at the time... Sorry that I missed you~"
    c smile "Oh, it's okay~ I was mostly looking to talk..."
    c aww "So, um, if you're available right now... do you wanna go to a café?"
    w innocent "That sounds perfect! I would love to."

    scene bg cafe
    show cassia smile at righta
    show fg cafetable
    with fade
    "We take our seats at the nearby café."
    "It's a pleasant, sunny little place. I've come here often with all sorts of other witches."
    "Cassia orders her usual hot chocolate with extra marshmallows, while I decide on a simple rose tea."
    nvl clear

    c oh "Ooh, Periwinkle, could you make my marshmallows smell like roses, too?"
    w innocent "With pleasure 💙" id ch2_e1d1de4a
    n "Periwinkle's wand drops from his sleeve, and he gives Cassia's cup a quick little tap."
    c happy "Eheh, yay~ It really smells just like roses~!"
    w smile "Just as you asked, dear. It may slightly affect the taste, so let me know if you'd like the spell undone."
    show cassia oh
    n "Cassia dips her spoon in and lifts a marshmallow to her lips, blowing on it lightly before popping it into her mouth."
    c happy "Mmf... no, it's wonderful! Ehehe~ 🤎" id ch2_bb00d05f
    show cassia yay

    "She truly can find the joy in any little moment. Such a delight..."
    "Definitely a contender for the title of absolute cutest witch. Though I would call her... absolutely cute, rather than the absolute cutest."
    "It takes more than cuteness alone to earn the title of absolute cutest witch! That's where the difference lies, of course."
    nvl clear
    "But what am I thinking? How rude it is, to begin ranking my dates in such a way."
    "I must be stuck on the thought from my earlier conversation with Astragalus... trying to put Pastille's cuteness into words."
    "He really is something special... ah, it's all in the contrast! His polite, well-mannered and proper exterior, concealing such intense desire, begging you to make the first move, and then going ahead and taking it on his own as soon as you--"
    nvl clear

    w oops "(...Enough of that! There's someone else in front of me now, isn't there?)" with vpunch
    n "Cassia continues happily sipping her hot chocolate before speaking up again."

    c aw "Ahh, I missed you, Periwinkle~ I've been so busy with packing, I haven't had a chance to see you at all..."
    w my "Packing? And just where are you headed off to?"
    c oh "Oh, that's right! I never had a chance to tell you~"
    c happy "I'm finally moving in with my partners~! In two more days, the three of us will all be sleeping in the same bed~ 🤎" id ch2_28a09411
    w happy "Ooh, that sounds cozy~ Congratulations!"
    c aww "Ehe, thank you~ 🤎 I've looked forward to it for so long..." id ch2_937fc8b0
    w smile "It sounds like you're about to enter a lovely domestic life. You deserve it!"
    c "Aww, hehehe... I'm really happy."
    c oh "But, um... speaking of my partners. You've still never even met them..."
    w calm "True. But I can imagine they're wonderful, just from how you've talked about them."
    c aww "Right~ but, um... what if you didn't have to imagine?"
    c smile "That's what I've been wanting to talk to you about. I was hoping... we might all be able to go on a group date sometime!"
    w oh "Oh~?"
    c aw "Yeah~! Because, like... I just think you're so wonderful, Periwinkle. I want them to know you, too!"
    w sorry "Mm... although it sounds like fun, I'm a bit..."
    c please "W-wait, before you say no...!"
    c "They're both very easygoing, and so loving, and nice...! I can promise it won't be overwhelming..."
    w decline "That unfortunately isn't where the issue lies, my dear..."
    c sad "I-I know you said you didn't want to get involved before... but I just know that we would all get along so well!"
    c "I'd like to reassure you however I can. But I understand if you still turn me down..."

    "Matters of love are so tricky, aren't they?"
    "I still recall the first time something like this was asked of me..."
    "I had been nervous going in, but I had also never entered a group situation before. I attributed my anxiety solely to that."
    "However, it quickly became clear that I just wasn't suited to it at all..."
    nvl clear
    "I do love to spoil each of my partners--but strictly one at a time."
    "Perhaps I was left scarred by the breakdown in communication, the passionate fires of a long-established romance..."
    "Surely Cassia and her partners are magnificent people. It may indeed be fun for a night."
    "But becoming entangled in committed relationships is something I've always avoided from the beginning, isn't it?"
    nvl clear

    w neutral "This is all very sweet of you. But I do have to decline."
    c letdown "Aww... I can't help but feel a little broken-hearted."
    w decline "I apologize... Truly, it's nothing personal."
    c aww "Oh, I know~ I don't take offense or anything..."
    c letdown "It's just sad. Now that I'm going to be living with them... and, knowing you don't want to meet them..."
    c sad "I think it's best we just break things off...."
    w neutral "Yes, I agree. As you said, it's for the best."
    c aww "I hope we can still be friends, though~"
    w smile "Of course~ 💙 I'm sure our paths will cross every now and again." id ch2_a119e9ad
    c happy "Yeah~! Thank you for always treating me so well, Periwinkle."
    w calm "Hmhm, it was my pleasure 💙" id ch2_f9c0bf81

    scene bg streetday with fade
    "Even casual relationships can end in breakups like this."
    "This is largely why I tend to prefer one-night affairs. Things can just become so messy as needs evolve..."
    "As Cassia and I go our separate ways, I can't help feeling a little blue."
    "Perhaps I'll return home for the day after all."
    nvl clear
    window hide

    play music audio.peri fadeout 2.0 fadein 2.0

    scene bg perihouse
    with Fade(1,1,1)

    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    n "Periwinkle quickly changes into something more comfortable, dropping his bag unceremoniously onto the couch."
    w pj neutral "(I could use an afternoon nap...)"
    w calm "(Yes, that's precisely what I need. I'll wake up feeling refreshed, and ready to go back out on the town~)"

    n "He shoves some blankets aside and collapses onto the couch--and when he does, the contents of his bag spills onto the floor."
    w oh "Ah..."
    n "Lazily leaning over to gather it up, he notices the candies from before..."
    w neutral "...."

    scene bg perihouse
    window auto

    "Was I too hasty in saying I'd hoped to see Pastille again?"
    "I suppose I'd forgotten the feeling of not being enough for someone."
    "Usually these things tend to dissipate naturally, without confrontation or notice."
    "So when they don't... it stings."
    nvl clear

    n "Periwinkle scoops up the candies, dropping all but one of them back into his bag."
    n "He settles into place on the couch, nestled in a tangled mess of blankets and cushions... and unwraps his chosen pastille."
    show cg sweet at cgspan

    w pj calm "(...It IS sweet, though.)"
    w shy "(What a shame that would be, if I never got to taste it again!)"

    hide cg
    "That's right. I could never resist the promise of an entertaining night, no matter what may come down the line."
    "I'm a hopeless hedonist after all 💙 Nothing to be done about that!" id ch2_13b346ec
    "Let fate decide, then. If he comes, he comes."
    "And if we never meet again... I can always hold on to the memory of our perfect date 💙" id ch2_191d1d9c
    nvl clear
    window hide

    stop music fadeout 2.0
    scene bg perihousedark with Fade(1,1,1)
    n "Several hours later..."
    n "...there's a knock at the door."

    play music audio.pastille fadein 2.0

    window auto
    scene bg peristreetnight with fade
    n "And right there on his doorstep, Periwinkle is pleasantly surprised to find..."
    show pastille jacket anxious at rightb
    w pj my "Pastille! I wasn't expecting to see you again so soon~"
    w drool "(And treating me to another cute new look, no less! 💙)" id ch2_b15c4708
    p "Sorry, I, um... I couldn't stop thinking about..."
    p ehe2 "I-I mean--I realized, last night I never actually... got to sample your magic? The scents you mentioned..."
    w oh "Oh, that's right..."
    w love "We were quite preoccupied, hm? 💙" id ch2_974aa600
    p seriously "Y-yes... so, th-that's why I'm here!"
    n "He finally manages to make eye contact, but quickly averts his gaze once more."
    p shy "Ah--um, were you in bed? Sorry, I shouldn't have come so late...."
    w calm "Hmhm, these aren't even my sexiest pajamas..."
    p omg "I didn't say anything about that...!" with vpunch
    w innocent "But to answer your question, no, I wasn't."
    w smile "Although I did take a nap earlier this afternoon, I've otherwise been enjoying a relaxing night in."
    w drool "(And I'm so very glad I didn't end up going out! I would've missed out on this flustered mess 💙)" id ch2_7eec0fd7
    p ehe2 "Ah... haha...."
    w innocent "...Would you like to come in?"
    show pastille jacket anxious
    n "Pastille nods vigorously in response."

    scene bg perihousedark
    show pastille jacket neutral at righto
    with fade

    w pj calm "It's still a bit of a mess in here... I hope you don't mind~"
    p oh "There's a path through. I've seen worse."
    w happy "Oh~ maybe I'll let it spiral further into chaos, then! I'm just so competitive, you know? 💙" id ch2_6f4d78ac
    p ehe "I'm not sure that's a competition you'd really want to win..."
    w calm "Hmhm, perhaps not."
    scene bg perihousedark with Dissolve(.2)
    n "Periwinkle carefully steps over some of his clutter to dig through one of the boxes in the far corner of the room."

    w pj smile "Ah, here they are! My personal favorites..."

    show cg share at cgspan
    w calm "This row here contains some of the more potent scents... most of them for relaxation, things to calm the nerves."
    w smile "The rest, I just happen to like. Sweet scents, like strawberry, banana, bubblegum, mango..."
    p "I-is there a reason you're only naming candy flavors...?"
    w innocent "Hm~ must be a coincidence 💙" id ch2_0d95e3c3
    hide cg
    n "Pastille picks out an unlabeled bottle, filled with a pale pink liquid..."

    show pastille jacket oh at rightb
    p "What's this?"
    w teehee "Ahh, watch out~ that one's an aphrodisiac 💙" id ch2_51cf5f4c
    p calm "Hm. We'll see about that."
    show pastille jacket neutral
    n "Pastille locks eyes with Periwinkle as he opens the vial without hesitation."
    w drool "(How bold...!)"

    p ehe "...Oh, it's peach. Hah, I almost expected it to be overpowering..."
    w calm "Yes, well, the aphrodisiac bit was a lie. But I'm glad you like it."
    p smile "You're really good at this type of magic--I've never done anything like it..."
    w smile "Would you like to try it on?"
    p oh "Hm...?"
    p shy "Oh, n-no, I don't do perfume or cologne or anything like that..."
    w oh "You've never tried it? Ohh, so would you say..."
    w shy "You're a perfume virgin, then? 💙" id ch2_cc464b9d
    p seriously "I-I'M NOT...! Who even says things like that?!" with vpunch
    w happy "In my line of work, you'd be surprised~"
    p shy "It's probably just you...."
    w innocent "Hmhm, maybe so."
    w calm "If you're not going to try it, I'll have it back now, please~"
    p anxious "I could.. try...."
    p ehe2 "I just don't know how I'm supposed to apply it."
    w smile "May I?"
    scene bg perihousedark with Dissolve(.2)

    n "Pastille nods, handing over the small vial."
    n "Periwinkle seals the opening with his fingertip and swiftly tilts the bottle over and back."

    show cg share2 at cgspan
    w "Here..."
    n "He lightly rubs a spot on Pastille's neck, engulfing them both in the pleasant scent of his magic."
    show cg share3
    n "Their eyes meet, neither of them daring to be the first to move."
    w "Hmm... maybe the aphrodisiac bit wasn't a lie after all?"
    show cg share4
    n "Pastille breaks the spell, rushing forward with a sudden kiss."
    hide cg
    n "...And then retreats just as quickly."

    show pastille jacket kyaa at rightc
    p "Ah--um, sorry, I just--"
    w pj yay "(He certainly is impulsive... not that I mind at all 💙)" id ch2_99717d55
    w drool "(I'm more than happy to go along with your little game, Pastille...)"
    w shy "Ohh nooo~ my own magic is working too well~!"
    w teehee "I guess there's no choice but to have my way with you, my sweet 💙" id ch2_0bd2374d
    p dying "...O-oh nooo~"

    scene bg perihousedark with dissolve

    n "Pastille's halfhearted protests end there."
    n "Periwinkle's hands were already upon him, and would continue to be for the rest of the night..."

    stop music fadeout 3.0

    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch3:
    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 3 - Missteps")
    show title ch3 at chtitle
    centered "{w=3}{nw}"

    play music audio.peri fadein 2.0

    scene bg bedroom with fade
    $ quick_menu = True

    "Over the next month or so, we fell into quite an enjoyable pattern."
    "Pastille would show up at my doorstep maybe once or twice a week..."
    "Sometimes we'd go out to dinner, but mostly he'd just spend the night 💙" id ch3_89332bf5
    nvl clear
    "It was starting to become almost routine--though each visit was somehow just as exciting as the last~"
    "The details of which... I'll choose to keep private, for Pastille's sake. That boy is insatiable, I WILL say that! 💙" id ch3_e1acc37c
    nvl clear
    "Inevitably, after seeing someone for long enough, one begins to pick up on their habits..."
    "Cute habits. Like the way he kisses me on the cheek before rushing off to work in the early morning."
    "The way he runs his hand through his hair when he's thinking really hard about something."
    nvl clear
    "Even his knock is specific--once, lightly, to test the waters. A pause, as he gathers his courage. Then three, firm and evenly-spaced."
    "I'm not sure which of these habits he's conscious of, but there's one I've decided he MUST be acting knowingly..."
    "Which is, his habit of leaving one of his personal effects behind with each visit."
    nvl clear
    "First, a barrette. Then an earring. His choker, a bracelet..."
    "And then he returns after a few days with an apology, explaining he had just come to pick up whatever he'd left behind."
    nvl clear

    w pj calm "Sure, Pastille. Keep creating your little excuses to come back here... I'll happily go along with them."
    w happy "Hmhm, what fun! I wonder what he'll come looking for THIS time~?"

    n "Periwinkle gathers up the discarded garments that had been left strewn across his bedroom, tossing them into a pile to be dealt with later."

    w oh "He couldn't possibly leave his underwear behind, could he...?"
    w calm "No, that would be impossible to explain. An earring, sure, but there's no way he'd walk out of here like THAT..."

    n "Periwinkle hums to himself as he makes the bed, double-checking between the sheets while he's at it..."

    w pout "...Hm. I'm almost disappointed."
    w oh "It's been so consistent, up until now. I suppose he could just be THAT forgetful..."

    scene bg perihouse with fade
    "Unable to find anything of Pastille's in my bedroom, I decide to spend the rest of the morning cleaning up the place."
    "Now, mind you, I never let my house get DIRTY... only messy."
    "Leaving garbage or food waste about is out of the question."
    "Everything else, though..."
    nvl clear
    "It's simply that many things don't make it back to their proper place. Or rather, I can never decide on a proper place for many of my things..."
    "Toss them into boxes, shuffle the boxes around the room, and suddenly they've become unmanageable piles..."
    "To truly put everything away, these would all have to be emptied and sorted... a daunting task, to be sure!"
    nvl clear
    "But it HAS been a while since my last attempt. I may as well put in some effort..."
    nvl clear

    w pj oops "But where to begin...?"
    w oh "I suppose my work supplies have been a little difficult to navigate as of late."
    w innocent "That's an achievable goal now, isn't it? And practical, as well!"

    n "Periwinkle begins with the box of his favorite perfumes, that had been sitting out since one of Pastille's first visits."
    w drool "Ahh, yes... the \"aphrodisiac\"... hmhm, that was a fun night 💙" id ch3_de62bb1c
    n "He packs the bottles back into their places, then closes the box, sealing them safely inside."

    w oh "This should go... hm, perhaps it'd be better to set it high on the bookshelf?"
    w calm "If I just rearrange things a bit, there should be room for everything...."

    n "As Periwinkle begins setting things aside, a new pile is born, precariously teetering on the back of the couch."
    n "He places the box just where he wants it, and then stacks his various books and knickknacks around it."
    n "Just as he's made his way through half of the pile, a small portion of it topples forward, bouncing safely onto the couch cushions."
    w smile "Ha! Topple all you want. I was prepared..."
    w oh "...Hm?"

    show cg jacket at smallcg
    n "He finally notices Pastille's jacket, which had expertly blended into the blankets and cushions around it."
    w happy "Aha! Just when I'd finally worked up the energy to clean up around here, what do I find?"
    w shy "Yes, this is no mere case of forgetfulness... it was indeed a little game all along!"

    n "Periwinkle giddily laughs to himself, excited to have been proven right."
    hide cg

    w love "You've escalated it too far, Pastille! To leave your jacket behind is just ridiculous 💙" id ch3_4aed7301
    w teehee "He leaves me no choice! I'll just have to return this myself~"
    n "Periwinkle abandons what he was doing, and skips off to his room to get dressed."

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_cute")
        $ quick_menu = True

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg streetday
    with Fade(1,1,1)
    "I hadn't had a chance to return to Atelier Sweets since first meeting Pastille."
    "He was the one always showing up on MY doorstep, after all. There was no need."
    "It's about time I paid him a visit, yes? I could restock on my favorite candies as well 💙" id ch3_928953dd
    nvl clear

    scene bg atelierstreet with fade
    "Upon reaching Atelier Sweets, though, I hesitate."
    "Would it be rude to barge in while he's working? I just know I wouldn't be able to resist teasing him..."
    "Hm. As to not become a nuisance, I shall make my presence known from here!"
    nvl clear

    n "Periwinkle boldly approaches the bench directly in front of the candy shop, and sits down..."
    n "...all while wearing Pastille's \"forgotten\" jacket."

    w jacket calm "(And now, we wait 💙)" id ch3_8cd95367

    "A few minutes pass."
    "I can see Pastille through the shop window... he's currently preoccupied with a customer."
    "Luckily, I brought a lunch 💙 A simple peanut butter and jelly sandwich." id ch3_ae539d34
    "Hmhm, will he notice me before I finish it? The customer is walking out now..."
    nvl clear

    w jacket shy "(...Ah! Our eyes met 💙)" id ch3_e963a0d1

    "Pastille turns away, pacing a bit. I take another bite of my sandwich, still watching intently..."
    "He stops for a moment, in front of the door behind the register... until finally making his way out of the store, broom in hand."
    nvl clear
    "But instead of coming over right away, he turns his back to me, sweeping the sidewalk in front of the entrance."
    "Perhaps he has a strict supervisor?"
    "Ah, he keeps glancing over his shoulder..."
    nvl clear

    w jacket smile "(Just come over here, you silly boy...)"

    "His face is quite red, so I can say with confidence that I've successfully overwhelmed him once again."
    "I've finished my sandwich by the time he approaches. He takes a seat on the opposite end of the bench."
    nvl clear

    show pastille work flustered at rightb
    w jacket happy "Hmhm, I thought you were ignoring me~"
    p omgstop "N-no, I was just trying to decide what to do."
    w calm "Was this a bad time to return your jacket?"
    p shy "Not the WORST time...."
    w smile "Hm~?"

    scene bg atelierstreet
    show pastille work shy at righta
    n "Periwinkle unzips the jacket and shuffles out of it, casually folding it onto his lap."

    w cute smile "I found it whilst I was cleaning up the place."
    w calm "I suppose I could've waited for you to return, but since I was in the area..."
    p ehe2 "R-right... sorry, it's my fault for leaving it behind in the first place."
    scene bg atelierstreet with Dissolve(.2)

    "Pastille can barely look me in the eye."
    "It doesn't stop him from stealing glances at what I'm wearing..."
    "But who could resist that? I wore my cutest dress for this."
    nvl clear
    "Something seems a little off, though..."
    "He's usually a bundle of nerves, yes, but this is a bit much."
    "I'll get right to the point, then..."
    nvl clear

    show cg bench at cgspan

    w cute happy "Oh, Pastille. You know you don't have to plant excuses just to visit me~"
    p "I-I wasn't... planting anything. I just forgot it on my way out."
    w innocent "I find that hard to believe, considering you've forgotten exactly one thing each time you visit 💙 Really, you should be more honest!" id ch3_528b5cc1
    p "...Sorry. Thank you, for returning it."
    w teehee "Oh, it's my pleasure 💙 It gave ME a good excuse to see your flustered little face again!" id ch3_4428d35a

    scene bg atelierstreet with Dissolve(.2)
    n "Periwinkle sets the jacket on the empty space between them, and rises to take his leave..."
    n "But Pastille gently grasps his wrist before he goes."

    show pastille work ohno2 at rightb
    p ohno2 "Peri. I'm, um... Sorry I made you think I was ignoring you."
    w cute guilty "Hmhm, I was only teasing, my sweet..."
    p nervous "Still. I can't, um... I'm not ready to be open about who I see outside of work."
    p flustered2 "I like to keep things VERY discreet--I don't want to have to explain anything to my friends. I'd die of embarrassment."
    w neutral "(So that's why...)"
    w calm "Understood 💙 I'm actually used to being someone's little secret--" id ch3_a218c7e9
    w neutral "...Hm, that didn't sound quite right."
    w guilty "What I'm trying to say is, I don't mind at all! From now on, I'll just continue to let you come to me 💙" id ch3_0c3f8324
    p nervous "Th-thank you... sorry."
    w smile "I don't know what you keep apologizing for, Pastille. I'll see you around, yes?"

    n "Pastille nods... and finally lets go of his wrist."

    scene bg streetday with fade
    "A misstep."
    "A HUGE misstep..."
    "I should've guessed it, from the hints he's given--just a few things he's said here and there."
    "It was enough to put it together, wasn't it?"
    "The most obvious one being that he always comes to me, and not the other way around."
    nvl clear
    "Our comfortable pattern, that I recklessly interrupted..."
    "I should've known, from previous encounters with closeted individuals."
    nvl clear
    "What's supposed to be a fun, surprise appearance can turn so quickly into a desperate rally to cling to normalcy, carefully constructed lies to conceal the piece of yourself that may not be accepted..."
    "...whether it's by the individual themself, or by their loved ones."
    "Certainly an unenviable position to find oneself in."
    nvl clear
    "Pastille and I had been seeing a lot of each other during this past month. Was this the inevitable breaking point, then?"
    "It can only become more complicated from here..."
    "Ah, but it was going so perfectly for so long! Perhaps I'm being overdramatic..."
    "I haven't grown tired of him at all... which is precisely the problem."
    nvl clear
    "Unwilling to return home so soon, I walk in the direction of the apothecary."
    "Astragalus will be able to knock some sense in me. She always does."
    nvl clear
    window hide

    play music audio.astra fadeout 2.0 fadein 2.0

    scene bg apothecary
    show fg register
    with Fade(1,1,1)

    w cute whine "Astragalus~~ Are you busy~~~?"
    show astra augh at righto behind fg
    a "Ugh, I know that whine. You've shifted into dramatic bitch mode."
    w pout "Take pity on me. I'm having a bad day."
    a whatever "Alright, ya baby, tell me what happened. (Things are slow today anyhow...)"
    window auto
    scene bg apothecary
    show astra closed at righta
    show fg register

    "Astragalus listened patiently as I explained the events of the day..."
    "I've learned to come straight to her whenever I find myself unable to make a decision."
    "Although she often puts things far too bluntly, I DO always end up feeling more grounded after her consolation..."
    nvl clear

    a annoyed "So... you're upset, because you overstepped his bounds."
    w cute whine2 "Accidentally!! You always leave out key information..."
    a whatever "And now you think it's over between you two."
    w oops "When you put it like that, I really DO sound dramatic..."
    a think "I mean, you are. But you also have a point."
    a neutral "If you wanna avoid things getting complicated, this is your sign to get out."
    a lol "I gotta say, though... for two guys who AREN'T in a committed relationship, you sure do sound like you're in one."
    w pout "It's purely casual. I've still been seeing a few others in the midst of this!"
    a sure "Buuut all you talk about is Pastille. Every time you come in here--"
    w conflicted "Ugh, I know! I know..."
    w oops "I just wish I hadn't gone to return the jacket. It was supposed to be fun, but now..."
    a whatever "Yeah, honestly, I think he's being unfair. He shows up to your place whenever he wants, right?"
    w sorry "Yes, but I don't have anything else going on! He has a respectable job and all..."
    a think "Mm... Sounds like you just have less self-respect, and this guy isn't treating you right."
    w pout "Now THAT'S unfair. He simply said he wasn't READY--it doesn't mean..."
    a lmao "Hah, making excuses now? You are REALLY hung up on him! This is too hilarious to watch!" with vpunch
    w yell "Enough!! I-I...!"
    w whine "I simply cannot help it if he's just the cutest thing! Of course I don't want to stop seeing him!"

    scene bg apothecary
    show fg register
    with Dissolve(.2)
    "At that moment, a familiar chime sounded, marking a customer's arrival."
    "I turn my head instinctively to see..."
    nvl clear

    show jam gasp at rightb
    j "Periwinkle? Omg, you look so cute today!"
    w cute innocent "Why, thank you! I certainly didn't expect to see you here, Jam!"

    n "Astragalus walks into the back room, still laughing at Periwinkle's expense."

    j ehe "I've been coming here to buy your magic!"
    j wink "Remember when you did a little demo for everyone at that one party? You totally sold me on it back then."
    w calm "Hm, I've done a few, so I can't recall... but I'm happy to hear it regardless!"
    j oh "So what are YOU doing here? On a date, or on the job?"
    w decline "No date today. I ruined my chance at THAT..."
    j whaaat "Aww man, what?! That's such a bummer..."
    j think "Really never thought I'd hear of the day YOU of all people couldn't get a date, though. You date, like, EVERYONE..."
    w smile "It'd be more accurate to say I \"go on dates\" with everyone, rather than ACTUALLY date them."
    j smile "Aww, same diff. You're like, the thirstmaster."
    w neutral "(Mm... she's right. It's not as if Pastille is my only option if I'm looking for a good time.)"
    j ehe "Anyway, are you going to Chirval's party tonight?"
    w oh "No, this is the first I've heard of it! He's throwing yet another soirée?"
    j oh "Yeah, I'm surprised you didn't know!"
    w guilty "I suppose I've been more out of the loop on these things than usual..."
    w oops "(I haven't bothered with as many parties, since...)"
    j smile "Well, you should come! They're good luck. Like, in terms of love~ and romance~!"
    j embarrassed "I mean, I'm finally dating my best friend, thanks to that last one...!"
    w oh "Ah--Marzipan, wasn't it? You weren't together before that?"
    j whaaat "AHHHH, I knew everyone thought we were...! Ugh, so embarrassing..." with vpunch
    j embarrassed2 "I guess what matters is we could finally be totally honest with each other, though... Ahh, I'm really happy...."
    w happy "Well, congratulations! You deserve that happiness."
    j wink "Yeah!! So like, if you ever need relationship advice, I'm your gal!"
    j think "Oh--but I guess you wouldn't, since you don't actually date anyone..."

    n "Periwinkle hears Astragalus snorting with laughter in the back room."

    w insulted "(How dare she! I came here to be comforted, not ridiculed...!)" with vpunch
    w innocent "Jam, dear. What time did you say that party started?"
    j oh "Oh, like... a few hours from now? I think?"
    j embarrassed "Sorry, I can never remember the time difference between here and the Netherworld...."
    w calm "No matter. These things tend to go all night, and I prefer to arrive fashionably late."
    w smile "Now if you'll excuse me, I'm going to return home to freshen up before the soirée."
    j ehe "Sure! See ya there~"

    play music audio.peri fadeout 2.0 fadein 2.0
    scene bg peristreet
    with Fade(1,1,1)

    n "Periwinkle marches home in a huff."
    w cute pout "(Hmph... Astragalus thinks I'm lacking in self-respect.)"
    w "(I'll show her...!)"
    scene bg perihouse with fade
    "I'm going to find someone to spoil me tonight!"
    "Netherworld parties happen to be the perfect venue--always filled with cute faces I haven't yet encountered."
    "Plenty of incubi as well... they LIVE to please their partners."
    "It's been a while since I've slept with a demon... 💙 I'm looking forward to this now~!" id ch3_8e765de2
    nvl clear

    centered "{nw}" #hack to hide nvl txtbox

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_witch")
        $ quick_menu = True

    stop music fadeout 2.0

    n "And so, a few hours later..."

    scene bg party
    with Fade(1,1,.5)
    play music audio.party fadein 2.0

    n "Periwinkle arrives at the soirée."

    show cg partyscene at cgspan
    w drool "(Let's see... who looks available~?)"
    n "Scanning the room, he spots both Jam and Chirval happily chatting with the other guests."
    w shy "(Chirval himself certainly isn't a bad lay... but I couldn't go stealing the host of the party~!)"
    hide cg
    n "Periwinkle begins to gravitate toward the snack table, still scoping out the various party-goers."
    w smile "(Plenty of candidates to choose from... however will I decide? 💙)" id ch3_200cad0c
    n "Before he can make up his mind about who to approach, a taller demon slides into the empty space beside him to start a conversation."

    show kar smile at rightb
    k "Lotsa cute witches at this soirée, huh?"
    w drool "(Oh, so it's been decided FOR me~! I'm ALREADY being spoiled 💙)" id ch3_356d9a00
    w calm "I didn't come here for the witches."
    k happy "Hah! ...I'm Kardaemon."
    w smile "Periwinkle."
    k shy "Periwinkle... So, this is gonna sound weird, but..."
    k ask "Do I... know you from somewhere?"
    w teehee "Your dreams, perhaps?"
    k laugh "Naww, for real! Something about your face is just so familiar..."
    w smile "I frequent these type of events, so it's likely we've crossed paths at some point."
    k shy "Hmmmm... that's not it. I woulda tried hitting on you if we did."
    w happy "Hmhm, well, you're certainly free to do so now 💙" id ch3_9e11e78c
    k happy "I'll give it a shot! With your permission, haha..."
    w smile "(This one isn't bad... I do appreciate how straightforward he's being.)"
    k smile "So! What ARE you here for, if not the witches?"
    w innocent "I had intended to find someone to spoil me... and incubi are rumored to be good for exactly that 💙" id ch3_f5eef97f
    k shy "We are, we are..."
    w my "So the rumors are true~? I'm in luck, then!"
    w teehee "Would you happen to have any friends who would be interested in dancing with a cute little witch like me~?"
    k "Hmmmmmmm... I could ask around."
    k smile "Or! Better idea. You could just settle for me?"
    w calm "Hmhm, I suppose you'll do 💙" id ch3_c9017794
    scene bg party with Dissolve(.2)

    "I present my hand, and Kardaemon gives an exaggerated bow."
    "He pulls me in, albeit a little clumsily, with his gigantic demon hands. Always enjoyable to be swept up in the arms of a larger man 💙" id ch3_084b6170
    "My own hand is almost entirely consumed by his. Unlike with Pastille's, which fit so--"
    nvl clear
    "...Pastille?"
    "Am I STILL comparing everyone to him?"
    "I shake the thought and return to the moment..."
    nvl clear

    show cg partydance at cgspan
    n "The pair twirls around the dance floor, losing themselves in the music."
    n "After a while, Kardaemon suddenly speaks up."
    k "...OH! I think I just realized where I know you from!"
    w love "Really, now?"
    k "Yeah, you were in the magazine I work for!"
    k "I'm an editor. We used your photos for an issue a couple years back."
    w oh "Ah... what a coincidence. I DID used to do some modeling, in the past..."
    w calm "And in the past it shall remain. I'm in a different line of work now."
    k "Aww, really? That's too bad. I always thought you looked amazing."
    w smile "Hmhm, I appreciate that 💙" id ch3_014598d5
    hide cg

    w neutral "(Well this certainly complicates things... I'd much prefer to have been complete strangers.)"
    w decline "(How unfortunate... just when I was beginning to enjoy myself.)"

    show kar laugh at rightc
    k "Haha, wow, I can't believe I ran into you like this. Maybe it's a sign...?"
    w smile "A sign? Of what, dare I ask?"
    k smile "That you should come back to modeling! I can get you in our magazine again--if you're interested, that is."
    w guilty "I appreciate the offer, but I've moved on. It put too much of a strain on my relationship with fashion, among other things..."
    k shy "Ah... well, at least take my card! In case you change your mind."
    w calm "No thank you. I don't see that happening."
    k laugh "Aww, come on... you'd be so great! It feels like such a waste of talent...."
    w neutral "(Hm... I'm quickly growing tired of this.)"
    w smile "Thank you for the dance... but I really should be going now."
    k huh "Huh? Ah, uh... sure."
    w innocent "This was fun. Perhaps we'll meet again sometime 💙" id ch3_b30b1ced
    k sad "Y-yeah...."

    play music audio.peri fadeout 2.0 fadein 2.0

    scene bg partyoutside
    with Fade(1,1,1)

    "I didn't expect to be reminded of my modeling days of all things..."
    "Although his excitement was understandable, the way he went about it certainly ruined the mood."
    "I hate to admit it, but I'd gone into this night far too unstable to begin with. For such a small thing to get to me..."
    nvl clear
    "I'm not even here on my own terms, am I?"
    "This was all to prove a point. That's certainly not in the spirit of a friendly soirée..."
    "It's best I just return home and--"
    nvl clear

    k "Periwinkle, wait!"
    n "He turns his head to find that Kardaemon has chased after him, stumbling into the lonely night air."
    show kar sad at rightb
    k "Hey--I, uh... I'm sorry if I said anything to upset you."
    w oh "...Upset me? Perish the thought!"
    w guilty "It's simply that I'm feeling a little off tonight. I realized I may have come here for the wrong reasons..."
    k pls "Look... I'm sorry that I suddenly started talking about work. That wasn't why I approached you at all."
    k sorry "You came here for a good time, right? Well, a party's definitely the place to find it!"
    k lookoff "Heck, it's what I'M here for, too... so, you're not wrong to come looking for that."
    w neutral "(He's completely misread the situation... Although, it IS starting to look salvageable from here.)"
    k sorry "Anyway, please forget about the magazine stuff--it doesn't matter. We were having fun before that right?"
    w calm "Dancing was nice, yes..."
    k sad "I-I wanna do more than just dance with you."
    w drool "(Oho, there it is~ Now we're getting somewhere.)"
    w shy "More than dance? And what could that mean~?"
    k shy "Hah, well, don't make me spell it out..."
    w smile "A kiss, perhaps?"
    k smile "Sure. And, well, you know... whatever else you'd like to do! As an incubus, I live to please."
    w love "(Since he apologized, I may as well...)"
    w calm "Kissing is a fine start."

    scene bg partyoutside with Dissolve(.2)
    n "Kardaemon holds out his arms, inviting Periwinkle into a soft embrace."
    n "Periwinkle's hands glide up his chest, and he wraps his arms around the demon's neck. Their faces just inches apart, he pauses..."
    k "...?"
    w ah "(...Ah. I expected him to close the gap.)"
    w conflicted "(Pastille would've kissed me. I've grown far too accustomed to that, so I automatically...)"
    w oops "(Shit. This was a mistake...)"
    n "Periwinkle gives him a light peck on the cheek before pulling away."

    show kar huh at rightc
    w decline "...My apologies. I do actually need to get going now."
    k huh "Huh...?"
    w neutral "I shouldn't have led you on. I'm terribly sorry."
    k sorry "Oh--n-no, don't worry about that... If you don't want to, it's fine."
    k sad "I'm, uh... a little confused, though... Did I do something wrong?"
    w decline "It's not you--you're very nice. Very firm muscles."
    k shy "Hah, thanks."
    w neutral "If it were any other night, things would've gone very differently. Please believe me when I say that."
    k lookoff "Seriously... is all this mysterious talk supposed to make me want you less...?"
    w calm "I'm sure you'll have great luck with the witches inside. You're very charming."
    k pls "...Damn. Well, alright..."
    k sorry "Get home safe, Periwinkle. Hope to see you again... on any other night, like you said."
    w innocent "Thank you for keeping me entertained. Farewell~"

    scene bg partyoutside with Dissolve(.2)
    "I shouldn't have come..."
    "What exactly have I proven here tonight? That I'm willing to pursue the first pink-haired boy I come across, out of sheer desperation?"
    "I wanted Astragalus to be wrong for once. To admit that I'm hung up on someone is just...!"
    "I don't feel like myself at all..."
    nvl clear
    window hide

    stop music fadeout 4.0

    scene bg streetnight with fade
    pause 1
    scene bg peristreetnight with fade
    pause 1
    scene bg perihousedark with fade
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    n "Periwinkle arrives home, lazily slipping out of his shoes and dress. He tosses his hat somewhere and collapses onto the couch."
    w lazy oops "(Ugh... I feel even more miserable than before.)"
    w neutral "...."
    n "Periwinkle finds himself staring at the front door, half-expecting to hear a familiar knock..."
    w guilty "(The state Pastille would find me in if he were to show up tonight...)"
    w empty "...."
    w oops "(...I should get in bed.)"
    scene bg perihousedark
    n "But he doesn't. Instead, he buries his face in the cushions and falls asleep..."
    window auto

    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch4:
    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 4 - Peach Blossoms")
    show title ch4 at chtitle
    centered "{w=3}{nw}"

    play music audio.pastille fadeout 2.0 fadein 2.0
    scene bg perihouse with fade
    $ quick_menu = True

    n "Periwinkle bolts awake to the sound of a knock on his door."
    w lazy sleepy "(Ugh, what time is it...?)"
    n "He rises from the couch and lightly treads over to check who might be visiting him so early in the morning..."
    w ah "(Ah...)"

    "At first, I thought my eyes were playing tricks on me."
    "It took several moments to register the fact that Pastille was on my doorstep."
    "The knocking comes again, snapping me out of my stupor."
    nvl clear
    w lazy guilty "*ahem* One moment, please~!"
    n "Periwinkle gathers up the clothes he'd left on the floor and stuffs them out of sight."
    n "Next, he scrambles into the bathroom to check his makeup."
    w oh "(Passable, considering the circumstances...)"
    n "Wrapping a blanket around his shoulders in an attempt to look half-decent, he finally opens the door..."

    scene bg peristreet
    show pastille date ehe at rightb
    with fade

    p "Hi! I took the day off, so I..."
    p ohno2 "Sorry, did I wake you up?"
    w decent my "Yes... yes, I had a late night. Um..."
    w guilty "Come in, come in! I'll be ready in just a moment."

    scene bg perihouse
    with fade
    "Pastille is here."
    "But WHY is he here--a day off...? Not that he HAS the day off, but that he chose to TAKE it... and then came here...?"
    "...Let's just put that aside for now. I need to get dressed."
    nvl clear

    show pastille date think at rightb
    n "Periwinkle scurries back to his bedroom to change, while Pastille waits politely by the door."

    w decent guilty "So, your day off, hm...? And you chose to visit ME? I'm flattered 💙" id ch4_75f30f98
    p ehe "Well, it's not just to visit... I was hoping to, um... take you on a date?"
    w my "Ooh, a date~? Usually we've reserved those for dinnertime, haven't we?"
    p shy "I-I wanted to make up for yesterday."
    p smile "So, if you didn't have any other plans... I was thinking we could just... hang out for a while?"
    w oh "Sure. I don't mind, but..."
    w guilty "What exactly is there to make up for, my sweet?"
    p nervous "Y-you know... how I told you not to come back to the shop, even though you only showed up to do me a favor?"
    w ah "(He... has it completely backwards.)"
    n "Periwinkle pokes his head out from the bedroom to look Pastille in the eye."
    w oh "Au contraire, Pastille, I should be the one to apologize for putting you in such an uncomfortable position!"
    w decline "I shouldn't have shown up unannounced. It wasn't my intention to cause you any ACTUAL discomfort..."
    p ohno2 "N-no, I...! I don't think I clarified my boundaries from the beginning, so..."
    p ehe "That's... not your fault at all."
    w ah "(Then it seems... everything is fine now?)"
    w innocent "Hm~ perhaps I could get to know those boundaries better during our date, then?"
    p uhoh "Wh-why does it sound suggestive when you say it...?"
    n "Periwinkle retreats back to his room with a smile."

    scene bg bedroom
    with fade

    "This boy has truly caught me off guard."
    "I'm almost frustrated that the spiral of guilt and confusion I lost myself in yesterday could be resolved so quickly..."
    nvl clear
    "Ah, that's all it was!"
    "I had merely been fixating on my mistake. It had nothing to do with Pastille, per se..."
    "He just happened to be the one at the center of it, so of course all of my attention was unnecessarily directed toward him."
    nvl clear
    "There's no problem, then!"
    "Which means, as usual, I can enjoy our date to the fullest extent 💙" id ch4_707ce886
    nvl clear
    window hide

    scene bg perihouse
    show pastille date neutral at rightb
    with fade
    w lazy happy "Well, DO tell me where we're headed! I'll need to know if I'm going to pick something to wear."
    p oh "Oh, um..."
    p smile "You haven't had breakfast yet, have you? Let's get something to eat first."
    w calm "Mm...."
    w smile "Actually, could you come in here a moment?"

    window auto
    scene bg bedroom
    with fade

    show cg foldingscreen at cgspan
    p "...Yes?"
    w lazy innocent "I thought it might be fun to have you choose what outfit I wear!"
    p wha "Ah--um... are you sure?"
    w smile "The clean clothes are in that pile, dear."
    p anxious "O-okay... um...."
    hide cg
    scene bg bedroom
    n "Pastille begins to sort through the pile of skirts and dresses, taking extra care to fold the ones he sets aside."
    show pastille date oh at rightb
    p oh "How about... these?"
    n "He approaches the folding screen, and holds the clothes out to the side for Periwinkle to take."
    w lazy oh "(Ooh, these are nice picks... buuut~)"
    w teehee "...No underwear?"
    p seriously "W-weren't you already wearing some?!"
    w shy "So scandalous, Pastille... I didn't know you had it in you~"
    p scream "PLEASE, I'LL FIND YOU A PAIR...!" with vpunch
    w happy "Hahaha 💙 I'm only teasing, my sweet~" id ch4_36731a75

    scene bg bedroom with Dissolve(.2)

    n "Periwinkle finally walks out, fully dressed..."
    show cg readysetdate at slowpanup
    pause 3
    w date happy "Ready to go~ 💙" id ch4_1c98e1e7
    n "Pastille looks him up and down cautiously."
    hide cg with dissolve
    show pastille date uhoh at righto
    p uhoh "Y-you're wearing some, right...?"
    w teehee "Hm~ we'll just have to find out later tonight, won't we?"
    p scream "P-PERI...!" with vpunch

    scene bg bedroom with Dissolve(.2)

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_date")
        $ quick_menu = True

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg streetday
    with Fade(1,1,1)

    "What a lovely day for a date 💙" id ch4_f71e2dad
    "We walk side by side, Pastille with his hands stuffed into oversized pockets. So cute..."
    "He's in the perfect position to be clinged to~ But, I must refrain."
    "I doubt he'd be comfortable with me hanging all over him in broad daylight. Besides, there's no need to jump into such overt affections just yet."
    nvl clear


    scene bg cafe
    show fg cafetable2
    with fade

    "When we reach the café, Pastille orders us some doughnuts to share."
    "I wonder what else he has planned...?"
    "He only mentioned hanging out--who knows what that could entail~?"
    "Munching away at our breakfast, I study his face for clues..."
    nvl clear
    show pastille date think at righta behind fg with dissolve
    "He really is so cute."
    "I remember the choker. He wore it on our first date as well 💙" id ch4_adc44e53
    show pastille date oh
    "And that's the same barrette he left behind after one of our sleepovers~ Such pointed choice in accessories..."
    show pastille date embarrassed
    "Ah, and now all my staring has embarrassed him. You're too easily flustered, my sweet 💙" id ch4_1fd546cf
    nvl clear
    w date "Forgive me for staring; I was trying to intuit what you might have planned for us after this."
    p ehe "Oh, um, nothing in particular... wandering around town is enough for me."
    w calm "I see 💙 Loitering does facilitate conversation quite well." id ch4_0455f80a
    p shy "As long as we're out and about, we won't end up... um...."
    w my "(Oh, is he going to say it~?)"
    p omg "Y-you know...."
    w innocent "(Hmhm, of course not 💙)" id ch4_143046d9
    p wha "I actually like when we get to talk...!"
    p uhoh "I-I mean, not that we DON'T when I sleep over, it's just... a different kind...."
    w calm "True... 💙" id ch4_c6264bf7
    p flustered2 "Sorry... now I feel like I'm talking too much."
    w love "Not at all, my sweet! I have to say, I rather enjoy our chats as well~"
    w teehee "Even if you can't resist cutting them short once we're behind closed doors 💙" id ch4_062a8003
    p omgstop "I-I'm really sorry...!" with vpunch

    "He's simply too much fun..."
    "Ah, but this is no time for my usual teasing~! I can't forget what brought us here..."
    show pastille date calm
    "This is the perfect opportunity to become more deeply acquainted."
    "I'll learn all about Pastille, so that I don't end up crossing the line again..."
    nvl clear

    show pastille date neutral
    w oh "In the interest of defining boundaries... are there any subjects I should avoid bringing up with you?"
    w guilty "On that note, has there ever been anything I've said that's caused you discomfort in the slightest? Please don't hold back."
    p think "Hmm... nothing really comes to mind...."
    p shy "I mean, I've always felt... pretty comfortable around you... so we could probably talk about anything and it'd be okay."
    w love "Anything, really? Surely you must have SOME sensitive topics you'd like to avoid."
    p oh "I guess so... but I wouldn't really be worried talking about them with you."
    p ehe "Actually, you might be the most attentive person I've ever met. Maybe that's why I'm not worried at all."
    w innocent "Hmhm, I'm glad to hear that 💙" id ch4_5e290654
    w smile "But you've certainly piqued my curiosity... what kinds of sensitive topics, if you don't mind me asking?"
    p think "Like... for example. You've never made me feel weird about gender stuff."
    w oh "I'd certainly hope not! That one's a bit sensitive for me as well."
    p happy "See? That's why it feels okay to talk about with you."
    p shy "I'm, well... not very masculine. So I get mistaken for a girl every now and then..."
    p oh "Not that it's something I get mad about or anything. I've always dealt with it, ever since I was little."

    p flustered2 "Still, I think it bothers me in particular, since... well, you know, I'm intersex."
    w decline "Mm, right."
    p ohno2 "I want to be recognized as a boy. But I like wearing feminine clothes, too..."
    w happy "Yes, that's it exactly! I feel the very same!"
    p ehe "Right? Like, I don't wanna be limited to presenting only one way... even if I'm fine with boyish clothes, too."
    w calm "For me, it's simply about looking beautiful. I dress to fit my ideal."
    w oh "It's not a matter of gender, but aesthetic preference. These are the clothes I feel best in."
    p embarrassed "You, um... look really good in them, too...."
    w innocent "Why, thank you! And I must say, YOUR sense of style never fails to impress 💙" id ch4_f6672aa7
    p omg "Ah, haha... I'm glad you like it...."

    n "Pastille sips his drink while Periwinkle continues."

    w calm "When I was young... I didn't have the confidence to dress so beautifully. Hmhm, can you even imagine it?"
    p ehe "You, without confidence? No, I'm not sure that's possible."
    w happy "Right~? I suppose I was a different person back then."
    w neutral "Where I grew up... things were much more black and white. You were either a boy or a girl, and you HAD to dress accordingly."
    p ohno2 "Ah, that sounds harsh..."
    w my "It very much was! I was completely MISERABLE!"
    w oh "Perhaps it's because I come from that sort of environment... that I want it to be known, I look this glamorous as a BOY."
    w pout "Not to say that this is easy for ANY gender--I only wish for my efforts to be acknowledged!"
    p shy "Haha, I think that's just your competitive spirit again."
    w happy "See, you truly understand me~!"
    show pastille date ehe
    n "They laugh together. Periwinkle relaxes into his chair and finishes his drink with a big smile on his face..."

    scene bg streetday
    with fade
    "Pastille and I depart from the café and make our way down the street."
    "With no destination in mind, the details of our surroundings--things I've never really paid any mind to, make themselves known."
    "Aromas from the bakery, the flower shop, the patisserie; each distinct and enticing. I'm left with a peaceful feeling as we pass each of them by."
    nvl clear
    "Now there's a fun idea... a scent that transforms over time, giving you a sense of place--"
    "Ah, but I shouldn't be thinking about work while I'm on a date~!"
    "I turn my attention back to Pastille."
    nvl clear
    show pastille date smile at rightb

    w date smile "With gender thoroughly discussed, the next personal question would have to be..."
    w happy "Ooh, sexuality! Which type of partner gets you THE MOST hot and bothered~?"
    p omgstop "SHH...! You can't just shout those words in the middle of a crowd...!!" with vpunch
    w calm "Ohh, who's even listening? I certainly wasn't shouting."
    p flustered "Please don't talk about that stuff too loudly... people will start giving us weird looks...!"
    w love "Shall I whisper it into your ear, then~?"
    p scream "TH-THAT'S EVEN WORSE...!" with vpunch
    w pout "Hmph, NOW who's shouting."
    show pastille date flustered

    n "Pastille glances around, but despite his outburst, Periwinkle was right--no one had turned their way."

    p ehe2 "Sorry... I-I guess it's okay...."
    w innocent "Feel free to stop me if I'm being too much, yes?"
    p uhoh "There's nothing wrong with being a LITTLE too much...."
    w calm "Hmhm, I imagined you'd say so. Returning to the topic at hand..."
    w happy "I've been with all sorts of partners. I'd say I can appreciate just about anyone 💙" id ch4_cd6834d6
    w shy "But I must admit, I prefer witch boys above all others..."
    p wow "I-I would also... say... witch boys...."
    w drool "OH~~~? Care to elaborate, my sweet?"
    p omg "Nope...! That's... all I have to say on the matter...." with vpunch
    w teehee "Hmhm, I'll have to tease it out of you later, then~ 💙" id ch4_2c430f31
    p dying "(AAAAHH...!!!)"

    scene bg streetday with Dissolve(.2)
    "We follow along the twisting streets of the shopping district, looking in each of the windows as we pass them by."
    "This is my favorite part of town--filled with all the high-end boutiques you could dream of 💙" id ch4_f823e801
    "The mannequins from one of them catch my eye, and I lightly grab Pastille's sleeve to draw his attention."
    nvl clear

    show pastille date neutral at rightb
    show cg mannequins at smallcg
    w date "You'd look so good in that, don't you think?"
    p shy "Really? I don't know if something so extravagant would really suit me..."
    w happy "Nonsense, you could pull it off~! The accents match your eyes 💙" id ch4_16ac6632
    p ehe "Eheh, I guess they do..."
    w oh "Hmm, but you'd look great in that one, too... oh, and THAT one...!"
    p embarrassed "Y-you're pointing to everything...."
    w shy "Yes, well, the alternative would be to say that I'd like to see you in nothing at all 💙" id ch4_9ad57405
    p omg "A-AH...." with vpunch
    hide cg
    w smile "Do you go clothes shopping often? You have such a variety of cute looks."
    p shy "Oh, um, every now and then... but I can't afford the kinds of stuff they sell here."
    w oh "It IS rather pricy... but the brands are worth it."
    p ehe "I really don't know anything about fashion. I just end up picking whatever stands out to me...."
    w smile "As it should be! You're better off not becoming obsessed with these things--it certainly isn't easy on the wallet."
    p smile "I'll leave the brand-name stuff to you, then. Just seeing them is enough for me."
    w teehee "Oh, just seeing them? Not stripping them off of me? 💙" id ch4_1715bc7d
    p dying "AAAAAHH...!!" with vpunch

    scene bg streetday with fade
    "After our little fashion circuit, we end up near the café where we'd started."
    "I've certainly worked him up enough to take home right away, but..."
    "That would mean cutting our date short! And what a shame that would be 💙" id ch4_2c40055e
    "I skip ahead of Pastille and twirl around to face him."
    nvl clear

    show pastille date neutral at righto
    w date innocent "There's somewhere I'd like to take you!"
    p um "Huh? Sure..."
    w smile "I realize I've seen YOUR workplace, but you haven't seen mine. It's a little apothecary I sell my magic to for distribution."
    p oh "An apothecary? I thought you sold perfumes...?"
    w calm "Technically, that's all they are. I don't claim they deliver any lasting health benefits..."
    w smile "They're more for healing the mind. Anxiety, stress, and any other unpleasant feelings can be lifted away with just the right aromas~"
    w oh "It's more effective for some than others. But for those sensitive to such things, it can make quite the difference."
    p think "Huh...."
    w guilty "And now I fear I've bored you with all this uninteresting work chatter..."
    p wha "N-no! That's not it at all--I was just thinking..."
    p shy "It's really admirable, that your magic can be used to help people like that...."
    w ah "(Admirable...?)"
    p ehe "Selling candy... I think, makes people happy too. Maybe that's what's fun about it."
    p shy "Not that I'd ever claim our candy is healthy either. If anything, you might get cavities..."
    w happy "Hmhm, the witch who owns the apothecary really liked the sample I passed along to her."
    w teehee "Perhaps she'll ask to distribute your candies as well~!"
    p flustered2 "Sy--um, my boss would never agree to that."
    p smile "Anyway... I'd be happy to see it. Lead the way!"
    w innocent "Very well 💙 Follow me~" id ch4_573a6eaf

    play music audio.astra fadeout 2.0 fadein 2.0

    scene bg apothecary
    show fg register
    with Fade(1,1,1)

    "When we enter the apothecary, it looks to be completely empty."
    "Astragalus usually sits in the back room, consumed in her work, until she hears the chime of a customer entering."
    "If you ask me, she could really use another helper to liven up the place..."
    "But I suppose the hustle and bustle of an ever-busy shop would have its own setbacks."
    nvl clear

    show pastille date think at rightb
    w date "Feel free to look around. I'm going to go and greet the owner 💙" id ch4_2c0acbc5
    p smile "Sure."
    scene bg apothecary
    show fg register
    with Dissolve(.2)

    n "Periwinkle leans over the counter to peek into the back room."

    w date happy "Astragalus~! You have a customer~~!"

    show astra hm at righto behind fg
    a "Oh, Periwinkle. Didn't expect to see you back so soon."
    w innocent "I brought Pastille! We're on a date 💙" id ch4_8bd3c979
    a annoyed "...Okay."
    n "She looks over at Pastille, who waves when he notices he's being watched. Astragalus turns back to Periwinkle."
    a whatever "I take it you decided NOT to heed my advice."
    w my "Hm? What advice?"
    a augh "Why bother coming to me if you're just gonna do whatever you want..."
    a closed "Well, whatever. Is there a reason you're here?"
    w innocent "I thought I'd drop by to give you a little update! As you can see, everything is fine now."
    a eyeroll "...Sure. Very normal of you to suddenly bring one of your dates here."
    w my "Is it not? I visit you all the time!"
    a lol "Yeah, not for stuff like this."
    w happy "Anyway--I wanted you to meet Pastille!"
    w "Pastille~! Come over here 💙" id ch4_479d8d54
    show astra hm
    n "Startled by suddenly being called upon, Pastille fumbles the bottle he was holding and it crashes onto the floor."
    show cg bottlebroken at smallcg
    w ohdear "Ah--"
    a augh "HEY, you break it, you buy it!" with vpunch
    p "Sorry!! I-I can fix it--"
    show astra annoyed
    n "Pastille sweeps the pieces of the bottle into a pile along with its powdered contents."
    show cg bottlefixed
    n "He holds his hands over the pile, now glowing with magic, and the three of them watch as it reassembles perfectly before them."
    w ah "(Impressive... He's done it so quickly....)"
    hide cg
    show pastille date ehe2 at lefta
    p ehe2 "There... good as new."
    a whatever "...Bring it here."
    p um "Ah--um... sure. S-sorry...."
    w guilty "(I can't help but feel I've put Pastille in yet another uncomfortable situation....)"
    a hm "...Damn, can't even tell it was ever busted up. This kind of magic your specialty?"
    p ehe "Not really... I only learned it because I thought it'd come in handy."
    a closed "Huh."
    scene bg apothecary
    show fg register
    with Dissolve(.2)
    n "Astragalus continues inspecting the bottle, and then takes it into the back room without saying another word."
    w date my "(Wow~ I suppose she was impressed, too!)"

    show pastille date nervous at rightc
    p "Is she mad at me...? I can't really tell...."
    w happy "It looks like you were spared today 💙 That spell really saved you." id ch4_a65c95b5
    p flustered2 "I can't believe I did that... I'm not usually this clumsy, I swear."
    w love "Oh, but wouldn't it be adorable if you were? Pastille the klutz~! 💙" id ch4_ebece81c
    p scream "NO...! I-I'm just gonna go wait outside!!" with vpunch
    w innocent "Hmhm, don't be too hard on yourself~ I promise you made a better impression than you think."
    scene bg apothecary
    show fg register
    with Dissolve(.2)
    "Pastille walks out of the apothecary, and I lean against the counter, waiting for Astragalus to re-emerge from the back room."
    "But when she does, it's with a bag full of... well... I'm not quite sure."
    nvl clear

    show astra hm at rightb behind fg
    a "...Hm? Where'd your boyfriend go?"
    w date "You shouldn't call him that. Might I ask--what is it you're holding?"
    a happy "Busted lamp. I've been meaning to glue it back together myself, until I saw the opportunity to save myself the trouble."
    w pout "How offensive. Take it to a repair shop, like everyone else."
    a lol "Nah, waste of money. You better keep that boy around--he's useful."
    w calm "You've certainly changed your tune...."
    a happy "He's cute. I get a good vibe from him."
    a lol2 "Anyway, bring him back in sometime so I can get this lamp fixed. Got it?"
    w happy "He won't be doing that!!"
    a neutral "Seriously, though. Where I'm from, we were taught that you can tell a lot about a witch from their magic..."
    a closed "And his? Very empathetic. Sincere, compassionate."
    w love "Well, you aren't wrong, but... how can you judge that sort of thing after witnessing one little spell?"
    a lol "Ha, wouldn't YOU like to know?"
    w calm "Hmhm, I don't need your superstitions. I have a date to get back to."
    a smile "Heh, alright. Have fun, Periwinkle...."
    w innocent "Oh, I very much intend to 💙" id ch4_c2b45ec4
    scene bg apothecary
    show fg register
    with Dissolve(.2)
    n "Smiling to himself, Periwinkle strides confidently out the door to where Pastille is waiting."

    play music audio.romance fadeout 2.0 fadein 2.0

    scene bg streetday
    show pastille date um at righta
    with Fade(1,1,1)

    p "Hey--um... do I still need to pay for that bottle?"
    w date calm "She didn't mention it."
    p calm "Phew. I'm glad I could fix it... I was worried it might be expensive."
    w smile "You never told me you were so good with magic. As I recall, you said you had been living without it?"
    p think "Yeah, mostly."
    p ehe "I won't get into the reasons why... but I got back into studying it recently."
    w happy "Astragalus certainly thought you were talented. I'm impressed too, of course."
    p shy "Th-thanks... haha, if only I could use magic to stop myself from being a klutz...."
    w teehee "Oh, are you embracing that nickname now?"
    p scream "N-no!! Please go back to saying \"my sweet\"!!!" with vpunch
    w love "Ah~ if you like that one so much, I suppose I have no choice! 💙" id ch4_e86c0674
    p omgstop "I-I... I just meant...!"
    p flustered "N-Nevermind!! Don't call me anything...!" with vpunch
    w shy "Hmhmhm 💙 Oh, Pastille...." id ch4_58252808

    scene bg streetday with Dissolve(.2)
    "We resume our stroll around town..."
    "This time, it's Pastille who takes the lead. He seems to have someplace in mind, but hasn't said as much."
    "He merely takes my hand and leads me up a labyrinth of stairs..."
    nvl clear

    scene bg lookout with fade
    show petals
    "And once we reach the top..."
    "A gust of wind swoops through the trees overhead, showering us in flower petals."
    nvl clear

    w date ah "Ah. Peach blossoms..."
    show pastille date smile at rightb
    p "It's nice, isn't it?"
    w love "Hmhm, I can't help but think you're trying to tell me something right now~"
    p oh "Huh...?"
    w smile "Don't you remember? My \"aphrodisiac\" was also peach-scented..."
    p wha "Ah..."
    p kyaa "A-AH...! I WASN'T THINKING ABOUT THAT...!!!" with vpunch
    p wow "I-I just, was trying to think of other places we could go, and this one came to mind..."
    w happy "It's lovely. Very romantic 💙" id ch4_eab2cf4c
    w shy "(Straight out of a shoujo manga, honestly... how does he know I'm weak to such things?)"
    p omg "We don't have to stay... I mean, we've already walked around so much--it's okay if you wanna head back now..."
    p omgstop "N-NOT TO... DO THINGS... I just meant...! I-I'm gonna stop talking......" with vpunch
    w love "Pastille."
    p seriously "Y-yes...?"
    w calm "You've presented me quite the conundrum. If I kiss you now, you'll definitely want to return home with me as soon as possible..."
    w happy "But I wasn't done learning all about you. I'm not ready for our date to end 💙" id ch4_80145f9c
    p embarrassed "O-oh... that IS a conundrum...."
    w love "Yes, you see? Both options are equally appealing. However can I decide~?"
    p shy "Haha, um, well... i-it's still light out! Maybe we can hold back until after dinner...."
    w teehee "Or I could have YOU for dinner 💙" id ch4_584de9f1
    p kyaa "A-AH...!" with vpunch
    w calm "On the other hand, you bring up a valid point. Holding back is fun in itself."
    p omgstop "Do you expect me to recover after what you just said...?!"
    w happy "See~? This IS quite fun!"
    w calm "It's decided, then. The date continues."

    hide pastille with Dissolve(.2)

    "I give Pastille a moment to calm himself."
    "We walk up to the railing and look out at the town..."
    nvl clear
    "You can see Atelier Sweets from here. And the train station next to it."
    "My house is... somewhere in a row of similarly built homes. Inconspicuous."
    "Fallen petals litter the bricks at our feet, with every little breeze carrying a few more over the railing to land somewhere unknown."
    "After watching them for a while, I turn back to Pastille."
    nvl clear

    show pastille date think at righto
    w date "Tell me about your magic."
    p um "O-okay... what do you want to know?"
    w innocent "Your specialty, dear!"
    w smile "If you were that good at reconstruction, I imagine it must fall somewhere in that category...?"
    p ehe "Um, not really... I'm actually an astral witch."
    w my "My, how rare! And what exactly does that entail for you?"
    p shy "Ahh, well, I mostly use it for fire spells, like anyone else..."
    w oh "Forgive me, I'm not well-versed in magic theory... but doesn't astral magic have something to do with creation?"
    p ehe2 "It does... but that stuff is pretty advanced. I haven't been able to find any books explaining how to use it."
    p embarrassed "...Which is probably for the best, actually. No one should be allowed to go around creating souls spontaneously...!"
    w neutral "Hm..."

    "Pastille rubs the back of his neck, looking off into the distance."
    "He seems so troubled by the subject..."
    "I suppose because he had been living without magic, it may feel strange to openly discuss it?"
    nvl clear
    "An astral witch, though... I wouldn't have guessed."
    "Putting two and two together, ONE thing makes perfect sense now..."
    nvl clear

    w ah "So the famous Atelier Sweets golem was YOUR creation?"
    p ehe2 "Haha, is she really that famous? I'd expect our sales to be a little better if that were the case..."
    p flustered2 "But... yeah. Just don't go around telling everyone--I didn't know what I was doing when I made her."
    w my "What an amazing feat... and yet you sound almost ashamed of it!"
    p ohno "I-it's not like I regret it or anything... Gumdrop is really great! I just..."
    p nervous "I feel bad that she's stuck in a body with so many limitations. Like, she didn't ask to be made that way..."
    p flustered2 "I didn't know you could even make golems that felt real emotions, so of course I never considered any of that."
    p shy "...Sorry to go off about it. I-I've just been feeling guilty lately--kind of a heavy topic."
    w ah "No, no... thank you for telling me."
    w calm "It's as if I've discovered a whole new side of you today. I'm grateful to know it."
    p ehe "Thanks for listening... I don't get many chances to talk about things like this, so I'm grateful for it, too."
    w love "Hmhm, hearing you speak of her though, I'd love to meet this golem of yours one day."
    p sure "Sure. Maybe one day."
    hide pastille with Dissolve(.2)

    "Pastille is amazing."
    "I've never met anyone who would downplay their talents this much--I could ask a thousand questions and still only scratch the surface..."
    "My, now I'M the insatiable one. How the tables have turned!"
    nvl clear
    "We decide it's time to move on, and descend the stairs from whence we came..."
    "...Still chatting endlessly as we decide where we'll wander to next."
    nvl clear

    scene bg streetdusk with fade
    "Over dinner, Pastille opens up a little more."
    "We trade anecdotes, listening intently to each others' stories no matter how unremarkable the events told within them."
    "I could never tire of it~ I was hooked by his every word."
    nvl clear
    "Alas, the hours flew by, and our day together was quickly approaching its end..."
    "But now we had the whole night to look forward to 💙" id ch4_d04a4349
    "The sun was on its way down as we emerged back onto the street, the atmosphere so different than it had been just a short while ago."
    "Pastille brushes his bangs aside and asks..."
    nvl clear
    show pastille date ehe at rightc
    p "Do you wanna head back? It's starting to get late...."
    w date shy "Hmhm, you've waited so patiently to be able to say that."
    p embarrassed "I-it's not like you aren't thinking of it too..."
    w innocent "Let's go through the park. It's a shorter walk 💙" id ch4_6cca094e
    p ehe "Sure...! A-after you...."
    scene bg streetdusk with Dissolve(.2)
    n "Periwinkle extends his hand, which Pastille takes without hesitation."
    n "Under cover of dusk, they walk toward the park with fingers gently intertwined..."

    scene bg park
    with fade
    "This park, during twilight hours, is nearly always deserted."
    "Tonight was no exception. We had the entire place to ourselves 💙" id ch4_df0cd7c9
    "This way I can cling to Pastille all I want~! And on top of that..."
    nvl clear
    show pastille date smile at rightb
    w date calm "Hmhm... 💙" id ch4_4d0933e5
    p ehe "What are you smiling about?"
    w happy "Finally, no one's around! We can talk about all the inappropriate things we want 💙" id ch4_94a989eb
    p shy "Ahh, haha, I knew there was something dangerous about taking this shortcut...."
    w innocent "It's ok then, right~? No one will overhear your lascivious confessions."
    p flustered "Mnnmmmnnn..."
    p omg "Okay. Wh-what do you want to know...?"
    w my "Oh--I didnt think you'd actually agree! I don't have anything prepared...."
    p wha "Wha--really? How anticlimactic."
    w drool "Unless you're dying to tell me how much you love being dommed~" id ch4_80a4788f
    p scream "I-I'm not gonna say that!!" with vpunch
    w teehee "Any fetishes, then? I have experience with all sorts, you know 💙" id ch4_8613e224
    p omgstop "TH-THIS IS TOO MUCH... I need to sit down...."

    n "Pastille begins his retreat to a nearby bench."

    w love "Ahh, are you perhaps into fooling around outdoors? 💙" id ch4_2eba37f4
    p scream "THAT'S ILLEGAL...!"
    w innocent "Hmhm, only kidding~"

    scene bg park with Dissolve(.2)
    n "Periwinkle follows Pastille to the bench and sits down beside him, leaning his head on his shoulder."

    show cg parkbench at cgspan
    w "Mm~ your sweatshirt is so warm 💙" id ch4_808f58c9
    p "...."
    w "Are you upset with me? For suggesting such a scandalous idea~?"
    p "No... but if you cling to me too much, I'm worried I might change my mind...."
    w "Hmhm, I wouldn't want to compromise your morals. But I'd also hate to let go."
    n "Pastille laughs at that, resigned to his fate."
    hide cg

    n "The pair sits in comfortable silence for a while, listening only to the sound of the fountain before them."
    n "Periwinkle can start to feel himself being lulled to sleep by it, and so, he tries speaking up again..."

    show pastille date think at righto
    w date calm "I don't know what it is about you, Pastille..."
    w shy "We've talked all day, and yet I still don't feel like it's enough."
    p ehe "I, uh... didn't really expect to be out this late either. It just kind of happened."
    w love "Mm... this was all supposed to be foreplay, wasn't it? Forgive me for putting it so bluntly..."
    p omg "Haha, um...! I-I guess it was...."
    w whine "Pastille, we have to get back to my place so I can fuck you..."
    p dying "You really are being so blunt right now...!!" with vpunch
    w shy "We have to... it's the entire purpose of foreplay, isn't it? How could you have let it go on this long..."
    p wow "W-we could head back right now..?"
    w "Yes."
    p wha "...Um, you're gonna have to stand up first...."
    w "In a moment..."

    scene bg park with Dissolve(.2)
    n "...But trapped in their comfortable position on that bench, Periwinkle is unable to stand in the end."
    n "Instead, he falls asleep to the sounds of the fountain and Pastille's beating heart."

    stop music fadeout 3.0

    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch5:
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 5 - Stifled Emotion")
    show title ch5 at chtitle
    centered "{w=3}{nw}"

    play music audio.peri fadein 2.0

    scene bg bedroom with fade
    $ quick_menu = True

    n "Periwinkle wakes up in his bed the next morning... alone."
    w pj sleepy "Hmmn...? Pastille...?"

    "No response."
    "No evidence of him either--none of his clothes laying about, no blankets out of place..."
    "I'm wearing pajamas, though I don't remember changing into them."
    nvl clear

    w "(In fact, I don't remember coming home at all...)"
    w "(Did I.. fall asleep, then...?)"
    w "(Hm... I vaguely remember being carried, but...)"
    scene bg bedroom
    n "He pauses..."
    n "...and then suddenly throws the covers off himself and leaps from bed."

    w pj shock "He truly isn't here?!"
    w conflicted "And he changed my clothes... was I conscious for that...? I-I..."
    w yell "I-I FELL ASLEEP BEFORE WE COULD FUCK?!?!??" with vpunch

    n "Periwinkle paces around his room, desperately running through the events of the previous night."
    w oops "We were on our way here. We stopped to rest. But it was so comfortable that I... I...."

    w insulted "Th-this is unheard of, this is... this is...!"

    "...This is the first time something like this has ever happened."
    "We had such a nice day together. The perfect date, really. It should have ended with a bang."
    "Normally it would have...! We both very much wanted it to!"
    "So how could I have let myself fall asleep like that...?"
    nvl clear
    "No... there's no need to panic. I simply lost track of time."
    "We had been walking around all day! Of course I would be worn out by the end of it."
    "I should've accounted for that. A simple mistake."
    "One that completely nullified all the tension I had so gradually built up..."
    nvl clear
    "Had I gotten lost in the performance, then?"
    "The romantic flourish, meant only to heighten the intensity of the passionate night to come..."
    "It's roleplay. Pretend! The only thing genuine about it is the lust that it masks...!"
    "For me to have reached a point of satisfaction before the intended finale would mean..."
    nvl clear

    w ah "It was just... a legitimate, romantic date...."

    n "Periwinkle stops in his tracks. He turns back toward his bed and crawls under the covers, wrapping himself up in them."

    "Have I ever... had one of those before?"
    "I mean, I certainly don't expect EVERY date to end in a sexual encounter! Sometimes a partner just isn't ready, or something comes up--"
    "It isn't that sex was owed, no... it's that... we never even reached the bedroom."
    "That's...!"
    nvl clear

    w wow "That's never happened..."
    n "The thought sinks in. Periwinkle slowly unwraps himself from his blankets and sits up in bed."

    scene bg bedroom
    "I'm overreacting."
    "Yes, I'm merely embarrassed that I had to be carried home and tucked into bed! To be taken care of like that..."
    "Usually I'M the one who \"takes care of things\". Now I just feel ridiculous."
    "...Something isn't right here. There has to be an explanation."
    nvl clear
    "It's safe to admit, at this point, that I am very sensitive to matters that involve Pastille."
    "But where did that begin? It couldn't have started just the other day."
    "Things were relatively normal--though I WAS seeing him quite often... moreso than other partners in the past...."
    "This has progressed too far beyond casual. What could have caused this...?"
    nvl clear
    n "He thinks for a moment before walking out of his bedroom with purposeful strides."

    scene bg perihouse
    with fade
    n "Going immediately to the bookcase, he tosses a few things aside and pulls down the box of his favorite perfumes."
    n "He then carefully extracts the bottle filled with pale pink liquid..."

    w pj mad "You... you must be the culprit."

    "This aphrodisiac--no, love potion!"
    "I wanted to see Pastille's reaction when I called it that. An inconsequential little joke..."
    "But it's kept coming up! There must be something to it."
    "Could the peach blossoms yesterday have further amplified its effects...?"
    nvl clear
    "Yes, it all makes sense now..."
    "Whether it be by my own magic, or some kind of chain reaction with Pastille's..."
    "I've somehow, unintentionally, created a scent that invokes romantic obsession in witches!"
    nvl clear

    w my "There's research to be done! I have to put an end to these artificially-inspired feelings..."
    w aha "I-I'll create an anti-aphrodisiac, then! Something to cancel out its effects!"
    w innocent "At which point, everything will go back to normal...! There's no problem at all 💙" id ch5_133fd5dc
    scene bg perihouse
    n "Convinced by his new theory, Periwinkle dresses himself and heads out to find a solution..."

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_witch")
        $ quick_menu = True

    # play music audio.date fadeout 2.0 fadein 2.0
    scene bg magicshop
    with Fade(1,1,1)

    "I head directly to the potion supply shop, just a few blocks away."
    "It's brimming with reference materials, though I usually only come to purchase magic containers--the vials to hold my perfumes."
    "Navigating their shelves of spell manuals and encyclopedias, I find myself somewhat overwhelmed..."
    "But soon, the shopkeeper comes to my aid."
    nvl clear

    show amaretti smile at rightb
    r "Good afternoon, Periwinkle! And what might you be looking for today?"
    r wink "New bottles? A book? Or perhaps... ME? 💙" id ch5_c89d618d
    w happy "Amaretti~! It's lovely to see you, but I'm strictly here for business."
    r smirk "Playing the professional today, I see. Your loss~"

    "Few witches have ever come close to my level of flirty energy, but Amaretti is one of them."
    "We may have fooled around at a party once or twice, but who's to say~?"
    "As much as her company would be a welcome distraction, I'm afraid removing my self-inflicted curse takes priority."
    nvl clear

    w calm "There IS actually something you can help me with..."
    w oh "But first, would you happen to know anything about aphrodisiacs?"
    r tell "Ahh, aphrodisiacs! Magic that sways the heart, stimulates the libido..."
    r no "They DO end up being classified as dark magic because of the manipulative aspects, but..."
    r wink "A few popular spellbooks happen to contain instructions for consensual usage. Is that what you'd be looking for?"
    w guilty "Yes--er, rather, assuming those books also contained instructions for CANCELLING the effects..."
    r think "Hmm...."
    r smirk "Did something go wrong in the bedroom? You can tell me! Nothing to get embarrassed about~"
    w oops "No, it's much more complicated than that..."
    w oh "Which spellbooks did you say I could find this information in? I'd like to look through them if possible."
    r think "Hmmmmmm......"
    r smirk "You're lying to me, aren't you? You just wanna learn these spells to spice things up in the bedroom."
    w pout "Not everything is related to sex, Amaretti."
    r think "Love, then...? No, you aren't the type...."
    r wink "Come on, why won't you just tell me? I can't help if you won't give up any details."
    w oops "All I want to know is whether or not aphrodisiac-induced feelings of romantic love can be nullified...! The details aren't important!"
    r tell "So it IS love...! Hmmmm...... hm, hm, hm. Hmm!"
    w insulted "(Why does she insist on wasting my time...?!)"
    scene bg magicshop
    show amaretti uhoh at righta
    n "A large, resounding thud from down the aisle startles both Amaretti and Periwinkle."
    n "The pair turns to see a much shorter witch standing there, fuming..."
    show cg pumpkin at smallcg
    u "UGH...! If I have to listen to you two IGNORAMUSES babble on for another second, I am going to LOSE IT!!" with vpunch
    w ohdear "(There was another customer here...? How long have they been listening?)"
    u "First off--stop conflating aphrodisiacs and love potions! They're ENTIRELY SEPARATE CATEGORIES!!"
    u "A witch who sells POTION SUPPLIES should at least know THAT much! You sell a whole book about it right here!!"
    n "She gestures to the thick tome she had slammed onto the floor at the beginning of her outburst."
    r wink "So THAT'S the one I was thinking of...! You'll find everything you need to know about cancelling your love spell in there, Periwinkle."
    u "NO!! YOU WON'T!!!" with vpunch
    r uhoh "He won't...?"
    u "Because it's not a freakin' ~love spell~ to begin with!"
    u "I find it MAAAAJORLY unlikely someone's been able to pull off a spell like that, when I've been trying for LITERALLY YEARS!!!!"
    w happy "Ah... well, thank you! That certainly answers my question!"
    w my "Since you're familiar with these things, I must ask--if not a love spell, could it have been a side effect of some OTHER type of magic?"
    u "HA...! A side effect... you think it's so easy it could be tacked on, just like that?!"
    u "PLACEBO effect is more like it! In which case, all you'd need to do is stop thinking about it, and it'd go away! (Dumbass...)"
    w happy "Oh, really~? That saves me so much trouble! Thanks for the advice!"
    u "H-HMPH...! If that shopkeeper woulda done her RESEARCH...."
    hide cg
    n "The witch's angry shouts fade into placated mumbles as she storms out of the shop."
    r tell "...You handled that so well! You should work in retail."
    w calm "Oh, so I'M the one in need of a new career now...? After THAT exchange?"
    scene bg magicshop with Dissolve(.2)
    n "Amaretti gives a nervous laugh and steps away to return the spellbook to its proper shelf."
    n "After bidding her farewell, Periwinkle exits the store to begin his short walk home..."

    scene bg streetday
    with fade
    "A placebo... of course it was just a placebo~!"
    "I should've thought of it sooner. There was never any cause for alarm."
    "This is just like before--it has nothing to do with Pastille. He just happens to be the one my mind is fixating on!"
    "It's precisely as that temperamental little witch said: if I stop thinking about him, the problem will resolve on its own 💙" id ch5_acc12d29
    nvl clear
    "And so... I must take a few days to focus on myself!"
    "At least until I can find my way out of this odd state I've ended up in...."
    nvl clear
    window hide

    play music audio.pastille fadeout 2.0 fadein 2.0
    scene bg perihouse
    with Fade(1,1,1)

    n "Operation \"Stop thinking about Pastille\"\nDay 1"
    window auto
    w calm "Let's see... the optimal distracting task would be..."
    w happy "Work, of course! Perhaps I could begin with the transforming aroma I thought of yesterday--"
    w ohdear "Ah, but that idea came about during our date... I should be avoiding any and all memories tied to him at the moment."
    w oops "Hm... this may prove more difficult than I anticipated..."
    w happy "No matter! I'll just warm up with a nice bergamot scent for now 💙" id ch5_fe203ad7

    scene bg perihouse
    show cg cast at cgspan
    n "Periwinkle retrieves a few empty vials from his box of perfume supplies, and readies his wand."
    n "But instead of the bright green drops he expected, what comes out is a familiar pale pink..."
    hide cg

    w ohdear "Peach...? Aha, that isn't right at all...."
    scene bg perihouse
    n "He seals the bottle and moves on to the next..."
    n "...which, much to his dismay, yields the same result."
    w mad "...."
    w oops "Okay. Magic is tied to emotions... I mustn't get frustrated. I have to focus."
    w decline "Deep breaths. It never helps to force it... just imagine the desired scent, and...."
    scene bg perihouse
    show cg cast at cgspan
    n "He tries for a third time..."
    n "...and yet..."
    hide cg

    w yell "Peach again?!" with vpunch
    w pout "This is a waste of supplies. So much for my attempt at diligence...!"
    w oops "If I can't conjure other scents, I'll have to find something else to occupy my time...."
    w innocent "Ahh, housework! I can finally get some chores done around here~!"
    w aha "Nothing could possibly distract me from finishing them today... they ARE the distraction!"
    w oh "Oh, that's right! I still had laundry to put away, didn't I?"
    scene bg bedroom
    with fade
    n "Periwinkle walks into his bedroom to face the pile of clothes he hadn't folded yet."
    w guilty "Whenever I tell myself I'll get to it later, I tend to leave it for days...."
    n "But the single large pile he expected wasn't there. Instead, it was split in two, with one half already neatly folded..."
    w my "Ah... I don't remember making this much progress...."
    w insulted "N-no...! Pastille did this, didn't he?! When he came to pick me up yesterday!!" with vpunch
    w oops "Curses... he's too good! I can't touch this right now...!"
    n "Periwinkle covers the pile of neatly folded clothes with the rest of the unfolded ones in retaliation."
    w aha "There. One less reminder to worry about."
    w decline "Now I'm going to have to think of something else to do...."

    scene bg perihouse
    with fade

    "So far, my attempts at forgetting about Pastille have been completely futile."
    "But that's perfectly fine...! No one said it was going to be easy."
    "Ironically, the more you tell yourself NOT to think of something, the more your mind will be enticed by it...."
    nvl clear
    "I mustn't let this consume me. I have to find a way to relax."
    "A nice bath should help to calm my nerves..."
    nvl clear
    window hide
    scene bg perihousedark with fade
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0
    n "Later that evening..."
    window auto
    w shutin happy "I'm feeling so refreshed, I could do just about anything~!"
    w smile "I should try cooking for myself tonight... Now THERE'S a task that'll require my full attention!"
    n "Periwinkle opens up the fridge for ideas..."
    w oh "A pint of milk. A few cups of yogurt, some eggs, whipped cream..."
    w pout "There isn't much in the way of meals, is there? This is why I never cook..."
    w happy "Ah, but I could try making an omelet! Breakfast for dinner~ oh, what fun~"

    scene bg perihousedark
    n "Periwinkle cheerfully reaches for the eggs, then pauses."
    w shutin oh "...Actually. Can I cook without magic...?"
    n "He turns to face the stove."
    w neutral "This burner... is the kind you'd light with a spell."
    w oops "I'm far too nervous my magic is going to come out smelling of peaches again..."
    w mad "...."
    n "Periwinkle slams the fridge shut."
    w innocent "Forget cooking! What was I thinking~? I'm not cut out to be a chef 💙" id ch5_04db34f2
    w "(Pastille on the other hand...)"
    w oops "No, no, no...! Thinking of him in this delightful domestic context is ESPECIALLY banned!"
    w whine "No matter how much I want to eat his cooking now...! He's obviously the type to be good at it...!"
    w neutral "...."
    w empty "Ahh, this is depressing... I'm already right back to where I started."
    w sleepy "*sigh* I'll just order takeout...."

    scene bg perihousedark
    n "Periwinkle goes to bed that night utterly incapable of forgetting about Pastille."

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg bedroom
    with Fade(1,1,1)
    n "Operation \"SERIOUSLY, do not think about that boy!\" - Day 2"
    "I've tried working... I've tried doing chores... I've even tried to cook! All miserable failures."
    "That's why, today, I'm taking drastic measures: complete escapism!"
    "I'm returning to my roots. I'll reread one of my favorite series! If nothing else, it should make a nice source of inspiration..."
    nvl clear

    n "Periwinkle pulls out volume one of a certain manga from his bookshelf."
    show cg manga at smallcg
    w shutin happy "\"Fabric of our Love\"! How many years has it been~?"
    w love "The dresses were always drawn so beautifully in this series... I still think of them from time to time."
    hide cg
    scene bg bedroom
    "It's the story of a girl who's fallen for a handsome prince 💙 Standard fare for the types of manga I read." id ch5_4ce77425
    "Her mother is a talented seamstress who designs all sorts of dazzling gowns for her to wear... and when the prince sees her in one, he becomes smitten with her!"
    nvl clear
    "At first, she's in heaven! This is the prince of her dreams~!"
    "But she soon wonders if the prince is only attracted to the dresses, the glamour... and not the poor girl underneath."
    "Until the prince reveals... ah, I shouldn't spoil it! 💙 The ending is too sweet~!" id ch5_bbca257f
    nvl clear

    n "After admiring the cover art for a while, Periwinkle finally opens the book and begins to read."
    show cg manga2 at cgspan
    w shutin love "Just as lovely as I remember... such delicate linework...."
    w calm "I wouldn't blame that prince for noticing the dresses before the girl. They really are so beautiful."
    w oh "Come to think of it, the way this prince is drawn..."
    w "His short, fluffy hair, his gentle features... remind me of..."
    hide cg
    scene bg bedroom
    n "Periwinkle closes the book in a panic."

    w shutin mad "That was dangerous. I can't risk even thinking his name...!"
    w whine "Ahh, and there's even a later chapter where he's dressed in servants' clothing! There are too many parallels...!"
    n "Periwinkle rolls across his bed and slides the book back into its place on his shelf."
    w pout "This isn't fair... how can one of my most beloved series be off-limits in my time of need...?"
    n "He scans through the different titles once more, before landing on a 12-volume series..."

    w neutral "I don't remember this one as clearly... but as an all-girls story, it should be safe...."
    scene bg bedroom
    n "Periwinkle pulls the new book from his shelf, and quietly immerses himself in its fictional world..."

    scene bg bedroomdark
    with Fade(1,1,1)
    "Before I knew it, I'd finished reading all 12 volumes. The whole day had flown right by."
    "I couldn't help but keep turning the pages... the story was so much more than I remembered!"
    "The protagonist was nothing to write home about, but her childhood friend? Ah, what a moving character arc...!"
    nvl clear
    "She's very charismatic from the start. The kind of person you'd think has it all figured out... but you couldn't be more wrong!"
    "Over the course of the series, she goes through so many love interests... back in the day, I had assumed it was because the author couldn't make up their mind!"
    nvl clear
    "But reading it all at once, it must've been planned from the beginning... these doomed relationships are merely self-sabotage! A distraction from pursuing her one true love!"
    "She never realizes the obvious answer until the very end...! And what an emotional finale!"
    "When she finally confesses, and the two girls share their first kiss...!"
    nvl clear

    w shutin love "Ah~! The fireworks!! Could anything be more romantic?!" with vpunch
    w happy "Her tears of happiness...! Finally being honest with herself, and with her best friend...! How lovely!"
    w calm "The well of loneliness that is her character was portrayed so flawlessly... she's the most real of them all."
    w love "Ending the story any other way would've been an injustice. She deserves the world...!"
    w oh "Hmm... I own this author's follow-up series as well, don't I...?"
    w happy "Time to get some snacks and start searching for it 💙 I can't resist diving in right away~!" id ch5_7b7b7eff

    scene bg bedroom
    with fade
    n "Operation \"Escape reality\" - Day 3"
    n "Periwinkle continued to read..."

    scene bg perihouse
    with fade
    n "...and read..."

    scene bg perihousedark
    with fade
    n "...and read."
    stop music fadeout 3.0
    n "Until he heard a knock at his door."

    w shutin oh "(Pastille...? No, that isn't his knock.)"
    w oops "(Ah, wait--I was trying to forget about him!)"
    w oh "(Though I suppose it means I was successful for a while... I even forgot that I was avoiding something to begin with....)"

    play music audio.peri fadein 2.0

    scene bg peristreetnight
    with fade
    n "When he opens the door, Periwinkle is greeted by a small crowd of friends and acquaintances."
    show cg friends at cgspan

    h "Periwinkle~! Get dressed, we're hitting the clubs!"
    w shutin happy "Wow~ the whole cavalry's arrived!"
    w love "Unfortunately, I'm going to have to decline... tonight isn't going to work for me."
    h "Whaaat~?! But no one's seen you in AGES! You haven't abandoned us for a new scene, have you?"
    w guilty "Oh, nothing like that... I've just been a little preoccupied. I'm taking some time to myself at the moment."
    h "Nothing wrong with a little self-care, but... are you suuure you don't wanna come out and enjoy the night life?"
    w love "Ahh, I don't know... I've fallen so far behind on my work."
    h "Choosing work over getting laid? Now I KNOW something's up with you!"
    w happy "How offensive~! I have more going on than just going out and flirting with everyone I meet!"
    h "Haahaha! Of course, of course~!"
    w calm "I do appreciate the invitation, though. Thank you for thinking of me."
    h "We just had to come and make sure you were still alive. The clubs are lonely without you~!"
    w happy "I'll have to make my grand return some other time, then. Have a lovely evening~!"
    hide cg
    scene bg peristreetnight
    n "The group waves goodbye and disappears into the night..."

    scene bg perihousedark
    with fade
    w shutin calm "Hmhm... it's been a while since I've had to turn them down...."
    n "Periwinkle leans his back against the door and sighs."

    "I'm definitely not in any state to go clubbing right now."
    "No matter how much it warms my heart to know that I am missed, I won't be making the same mistake as the other night!"
    "I can't go recklessly diving into the comforting arms of another as long as my mind is still hung up on Pastille..."
    nvl clear
    "But how long will I remain in this state?"
    "Shutting myself away, binge-reading comics..."
    "These were emergency measures. I can't avoid the outside world forever."
    nvl clear
    "In any case, shouldn't Pastille be returning here at some point?"
    "From where we left off, I'd have expected him to come knocking as soon as possible!"
    "And yet... it's been three full days now, hasn't it?"
    "How long could he possibly abstain from my touch! Or is something wrong...?"
    nvl clear
    "I shouldn't be thinking about any of this... but I'm beginning to feel..."
    "Annoyed? Confused...?"
    nvl clear

    w shutin conflicted "(If he never comes back, I suppose my problem would go away on its own...)"
    w oops "(But I hate the thought of that. As things are now, I'd only be haunted by thoughts of what I could've possibly done wrong.)"
    w empty "(What IS my plan, then? Continue to ping-pong back and forth between these extreme emotional states?)"
    n "He rubs his eyes in exhaustion."
    w sleepy "...I'll worry about this tomorrow...."
    scene bg perihousedark
    n "Periwinkle steps back into his room and tucks himself into bed with his books..."

    play music audio.romance fadeout 2.0 fadein 2.0

    scene bg perihousedark
    with Fade(1,1,1)
    n "But an hour later... another knock comes."
    n "This time, the pattern is unmistakable."
    w shutin ah "(Pastille is here....)"

    "Well, well, well..."
    "So he's come after all."
    nvl clear
    "Despite all my hard work of trying to forget..."
    "I've actually been waiting for this moment, haven't I?"
    "I don't care what these feelings might mean anymore. I'm tired of fighting them."
    "I... just want Pastille."
    nvl clear
    window hide
    scene bg peristreetnight
    with fade
    n "He opens the door, and sure enough, Pastille is the one he finds standing there."
    show pastille jacket ehe at rightb
    p "Hi!"
    w shutin happy "Why, good evening~ and what could you have possibly come for at this hour?"
    p shy "To, um... pick up where we left off the other night? Maybe?"
    w calm "(It's about time...)"
    w smile "Come in, come in~"
    window auto
    scene bg perihousedark
    with fade
    show pastille jacket ehe at rightb with dissolve
    p "Sorry, I meant to come see you again sooner. I had a few things to sort out before I--"
    w shutin "Hush, now. That's not where we left off at all, was it?"
    p wha "Huh? Y-yeah, I guess not...."
    w calm "I'm more interested in how you got me home that night. You see, the last thing I remember is sitting on that bench..."
    p shy "Oh! Uh, well, I was having a hard time waking you up, so I just ended up carrying you..."
    w love "The whole way, by yourself~?"
    p ehe "I mean, having a broom to ride helped a lot..."
    scene bg perihousedark with Dissolve(.2)
    n "Periwinkle closes in."
    show cg close1 at cgspan
    w "We rode it together, then?"
    p "That was the easiest way, yes..."
    show cg close2
    w "You must've held me close, so I wouldn't fall."
    p "I-I did..."
    w "Putting your hands all over me, hm?"
    show cg close3
    p "I-I didn't feel you up while you were unconscious!!" with vpunch
    show cg close4
    n "He gives him a big kiss."
    w "I was only kidding 💙" id ch5_40d0a112
    hide cg

    scene bg perihousedark
    show pastille jacket flustered at righta
    with Dissolve(.2)

    w shutin oh "But you also changed my clothes..."
    p shout "Because I thought you'd be more comfortable that way! It was an innocent gesture!!"
    w shy "I can't believe you saw my bare chest...!"
    p mou "I've already seen it!!" with vpunch
    w kyaa "Kyaa~!"
    scene bg perihousedark with Dissolve(.2)
    n "Pastille suddenly lifts him by the waist and hoists him over his shoulder."
    show cg close5 at cgspan
    w "PASTILLE--!!!!"
    w "Wah!! Please handle me more delicately~! 💙" id ch5_c919570c

    scene bg bedroomdark
    with fade

    n "When they reach the bed, Pastille falls backwards onto it, taking Periwinkle with him..."
    show cg topple at slowpanup
    pause 3
    n "They pause there a moment, laughs fading to soft breaths."
    w "You forgot to turn the light off...."
    p "W-well... I can't get up now...."
    w "(How can he be so impatient after making me wait for so long...?)"
    show cg topple2
    w "Hmhm... oh well."

    stop music fadeout 3.0

    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch6:
    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 6 - Longing")
    show title ch6 at chtitle
    centered "{w=3}{nw}"

    play music audio.pastille fadeout 2.0 fadein 2.0

    scene bg bedroomclean with fade
    $ quick_menu = True

    "I awake to a rustling sound."
    "My bed is empty again, but when I roll over..."
    "Pastille is there, standing in front of my closet."
    nvl clear
    "I sit up, rubbing the sleep from my eyes."
    "He's holding a box. As he lifts it on to the top shelf, its contents shift, making a clattering noise."
    "Utterly confused as to what he's doing, I finally call out to him."
    nvl clear

    w bed sleepy "Pastille...?"

    show pastille pj ehe at rightc

    p "Sorry! I didn't break anything, I promise."
    w sleepy2 "What are you doing in my closet...?"
    p um "Huh...? You said I could clean up."
    w "Hmm...?"
    w guilty "Oh, haha... is there anything I won't agree to in my sleep...?"
    p embarrassed "Ah--I'm sorry, I thought you were awake when I asked...! I-I'll stop."
    w sleepy3 "It's fine... I just didn't expect to wake up to you rifling through my things."
    p flustered2 "Th-that really wasn't my intention...! I just felt like organizing stuff...."
    p think "What do people normally do on the morning after...? I guess I should've made breakfast."
    w happy "Ohh~ I want to eat pancakes~!"
    p happy "Great! I'll make some!!"
    hide pastille with Dissolve(.2)
    n "Pastille practically bolts from the room to get started on cooking."
    w sleepy3 "Hmhm... oh, Pastille...."

    scene bg bedroomclean
    "Looking around the room, he did much more than organize my closet..."
    "The books I'd been reading were all tucked back into their proper places on the bookshelf."
    "The clothes that had been strewn across the floor, or otherwise left hanging in ridiculous places, now sat in the hamper waiting to be washed."
    nvl clear
    "Even the pile of unfolded laundry I had previously abandoned was now absent--properly folded and placed into the appropriate drawers by Pastille."
    "In a word, I'm in awe."
    "How long had he been at this? And all while I slept?"
    "It shouldn't even be possible."
    nvl clear

    w bed neutral "...."
    w oh2 "(I have so much more floor space than I remembered... how did he manage to do that...?)"

    scene bg bedroomclean
    n "Periwinkle puts on a fresh pair of pajamas and walks out to the kitchen in a daze."

    scene bg perihouse
    with fade

    show pastille pj smile at rightb
    p "Hey! Pancakes are ready."
    show cg pancakes at smallcg
    w pj happy "Oh~! Is it too soon to say I love you?"
    p sure "Haha, please enjoy...."
    n "Periwinkle takes his seat at the table and digs in..."

    scene bg perihouse with Dissolve(.2)
    "They're... delicious."
    "Perfectly light and fluffy... the optimal amount of syrup and whipped cream..."
    "Every bite is so heavenly, I could cry!"
    "I've never felt so emotional over food...! What has this boy done to me?"
    nvl clear
    "I was right about him being the culinary type."
    "I didn't think I would get to try his cooking so soon... this is a surprise attack."
    "He even... ah, but how did those get there? I have to ask--"
    nvl clear

    show pastille pj smile at righto

    w pj oh "Pastille... where did you get these strawberries?"
    p ehe "Oh, I saw you had some jam, so I used a little magic to change its form..."
    p ohno2 "Um, is that okay? Maybe I should've asked first--I just remember you liked strawberries, so..."
    w shy "(Is there any limit to how thoughtful one can be...?!)"
    w love "It's more than okay! This is the best breakfast I've ever had...!"
    p shy "I'm sure you're exaggerating... they're just pancakes."
    w teehee "Careful, my sweet... if you say it like that, I'm going to start asking you to cook my every meal."
    p sure "Fine, you got me. They're special gourmet pancakes I can only whip up every once in a while."
    w happy "Lucky me~! 💙" id ch6_4b7d60e9

    scene bg perihouse with Dissolve(.2)
    n "Periwinkle finishes his pancakes while Pastille begins washing the dishes..."

    "This may just be the most spoiled I've ever felt..."
    "Being with Pastille is like getting caught in an endless whirlwind of positive feelings."
    "No wonder I've become obsessed with him. This boy is dangerously kind."
    "After these past few emotionally tumultuous days, I... how could I possibly turn away from his comfort...?"
    nvl clear

    n "Periwinkle rests his elbows on the table, head tilted into palm as he watches Pastille in his kitchen."
    w pj oh "Out of curiosity..."
    show pastille pj neutral at rightb
    p "Hm?"
    w "Earlier, before I woke up. What made you ask to start cleaning my room?"
    p ehe "Oh, I noticed it was getting harder to walk around..."
    p shy "I think I stepped on some of your clothes when I, um... carried you in there last night. Sorry."
    w calm "That's nothing to apologize for. It was fun."
    p embarrassed "Eheh... a-anyway... I felt a little bad about it."
    p ehe "So I figured, if I'm going to be coming back here so often, I might as well help clean."
    w ah "Ah...!"
    p nervous "I-I'm not getting ahead of myself, am I? Sorry, I didn't mean--"
    w shock "Not at all!" with vpunch
    show pastille woah
    n "Startled by the sudden outburst, Pastille stops what he's doing."
    w shy "Hmhm, silly Pastille..."
    w love "You're always welcome here 💙" id ch6_fa84fa9d
    p doki "Ah...! W-well, thank you...."

    scene bg perihouse with Dissolve(.2)

    "Fine."
    "Okay! Enough... I'll admit it."
    "I'm stupidly, desperately, absolutely ridiculously..."
    "...in love with Pastille."
    nvl clear
    "There! I said it--or at least, I'm saying it to myself."
    "I'll accept this. Pastille is incredible! Who WOULDN'T fall for him?"
    "I don't want anyone else anymore. I've been poisoned by this perfect boy."
    "The problem now is what to DO about it...."
    nvl clear

    show pastille pj flustered2 at righto
    p "Weird question, but..."
    p shy "Would you want to... um..."
    w pj innocent "(Date you? Yes!!)"
    p seriously "...Clean the rest of your house together?" with vpunch
    w ohdear "...Hm?"
    p shy "I-it'll be more fun than it sounds! And if you get bored, we can do something else..."
    w calm "Pastille..."
    p embarrassed "I just thought if we did it together, you'd get a say in where everything goes, so nothing ends up getting lost...!"
    w love "Pastille...!"
    p ehe2 "And it's totally fine if you don't want me going through your stuff anymore. We really don't have to--"
    w happy "Pastille, it's fine! I think it's a lovely idea."
    p wha "R-really...?"
    w innocent "Yes. In fact, I'd appreciate your help."
    w love "One thing or another has always come up when I try to clean on my own. I'm simply useless at it."
    p happy "Then... I'll take the lead! I wanted to start with these boxes by the couch..."

    scene bg perihouse with Dissolve(.2)

    "Pastille already had a plan for everything, it seemed."
    "His energy was contagious. He was right that it would be fun--it was entertaining even just watching him go."
    "To see him dart around the room so energetically, finding the perfect place for every little thing..."
    "He truly has a talent for organization."
    nvl clear
    "Meanwhile, I mostly played the role of assistant."
    "He would ask for my input every now and then, or instruct me to place something he found somewhere across the room."
    "He made little decisions like that so easily. If it were me, I'd get stuck on every one..."
    "But he saw everything through, effortlessly. It was nothing short of amazing."
    nvl clear

    n "And so, in a short few hours..."

    scene bg perihouseclean with fade

    n "...The entire house had become neat and tidy."

    show pastille pj ehe at rightb
    p "Okay... I think I'm satisfied. You?"
    w pj shy "Hmm~ don't you think you deserve to be rewarded for all your hard work? 💙" id ch6_9e685ed1
    p uhoh "Ah--I-I should've seen that one coming...!"
    p shy "But no, not right now! I should actually get going...."
    w smile "You won't stay?"
    p smile "I promised Gumdrop I'd be back for the afternoon shift. She'll start to worry if I don't come back soon."
    w calm "Hmhm... I'll save your reward for next time, then."

    scene bg perihouseclean with Dissolve(.2)
    n "Pastille slips on his jacket and shoes."
    n "Just before he leaves, he turns back to face Periwinkle..."

    show pastille jacket think at righto
    p "By the way, um... I was thinking..."
    w pj "Yes...?"
    p oh "There are some days my friends travel out of town. For alchemy stuff."
    p shy "So if you ever wanted to drop by while I'm working on those days... I think that'd be okay..."
    p ehe "That's, um... the most I can do right now... sorry."
    w happy "I'll gladly take you up on that! I'd love to keep you company 💙" id ch6_41c1209f
    p smile "Great! Okay, then...."
    scene bg perihouseclean with Dissolve(.2)

    show cg goodbyekiss at cgspan
    n "Pastille gives him a quick peck on the cheek..."
    show cg goodbyekiss2
    n "...before saying goodbye, and walking out the door."
    hide cg

    play music audio.peri fadeout 2.0 fadein 2.0

    w pj wow "...."

    "What... WAS all of that?"
    "It was extremely domestic! I can't be imagining things, can I?"
    "He said it was okay... to come and visit him...?"
    "That has to mean something, doesn't it?"
    nvl clear

    w pj nofair "......"
    n "Periwinkle begins pacing around the room."

    "Now, now... let's not get carried away."
    "This is a delicate situation. Dropping these intense feelings onto him out of nowhere may only serve to scare him off."
    "Neither of us was looking for a committed relationship from the beginning--that was made explicitly clear early on!"
    "And yet... and yet...!"
    nvl clear
    w nofair2 "He isn't playing fair...! My heart can't take this!"
    scene bg perihouseclean
    n "Periwinkle throws himself onto the couch dramatically."
    w pj yell "There's no way I'll be able to stop thinking of him now... even being at home has become a reminder in and of itself...!"
    w nofair "Everything is nice because of him! And now I'm suffering...!!"

    "This is simply too much..."
    "There has to be a way for me to safely indulge in these romantic feelings."
    "Things are fine as they are. Progressing, even."
    "If I just let it run its natural course, then maybe we'll end up..."
    nvl clear
    "Ah... what do I want out of this?"
    "To be with him forever? ME?!"
    "I haven't had a single healthy long-term relationship in my entire life! Love isn't in the cards for someone like me..."
    "Ugh, I... I can't even recognize myself right now...!"
    nvl clear
    w decline "*sigh* ...Calm down."
    w neutral "I'm overreacting again. Nothing has effectively changed just yet."

    "I can't keep fighting myself on this..."
    "I'm in love with Pastille--No matter what it entails, that's the reality."
    "He still isn't quite ready for me to meet his friends, which means... there isn't any room to advance further at the moment."
    "I have to be patient."
    nvl clear
    w empty "At the very least, I hope accepting all this lets my magic return to normal..."
    w sleepy "*sigh* ...I need a nap."

    play music audio.date fadeout 2.0 fadein 2.0

    scene bg peristreet with fade
    n "And so, over the next few weeks..."
    scene bg atelierstreet with fade
    n "Periwinkle would come by Atelier Sweets to spend time with Pastille."

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_witch")
        $ quick_menu = True

    scene bg atelierint
    show pastille work smile at rightb
    show fg counter
    with fade
    "He always stood there so sweetly behind the counter."
    "And then I would waltz in, pretending to be just another customer, browsing the aisles before meandering over to him..."
    show pastille happy
    "Others would stop in every now and again, but there was ample time in which I had him completely to myself 💙" id ch6_958370f1
    "That's when I'd take the opportunity to chat..."
    nvl clear
    show pastille smile
    w calm "Hmhm, this place smells just like you, my sweet~"
    p ehe "I think it's the other way around... d-do I smell like candy or something?"
    w happy "Why else do you think I want to eat you up?"
    p omg "A-aaahh...! Please don't say things like that when there are customers here!" with vpunch
    w oh "Customers? I don't see anyone."
    p flustered "I-I know, I mean... just, in general...."
    w love "You don't want to get turned on at work? 💙" id ch6_fde4125f
    p scream "THAT!! THAT'S NOT ALLOWED!!!" with vpunch

    scene bg atelierstreet with dissolve
    "Our exchanges were mostly innocent, unlike other partners I've paid visits to in the past."
    "He was very adamant about not fooling around at work..."
    "Not that it ever stopped me from teasing him about it 💙" id ch6_67128253
    nvl clear
    centered "{nw}" #hack to stop window transition lol

    scene bg atelierint
    show pastille work neutral at rightb
    show fg counter
    with fade
    n "Periwinkle watches as Pastille, armed with a rag and a bottle of cleaner, sprays down the counter in front of him."
    w happy "Hmhm... I think I underestimated your love of cleaning."
    p shy "Are you making fun of me? This is my job, y'know...."
    w love "Oh~ should I have paid you when you cleaned my house?"
    p sure "I'll send you an invoice."
    w happy "Could I pay you in kisses?"
    p omgstop "That's...! Hard to turn down, actually...." with vpunch

    scene bg atelierstreet with dissolve
    "It was fun seeing him hard at work."
    "The only side of him most people would ever be aware of."
    "They'll never know of the lust bubbling beneath the surface. His nervous, vulnerable laughter when I've said something he wanted to hear..."
    nvl clear
    "His gentle touch. The way he can take my hand so casually, and yet becomes a stuttering mess as soon as I lean over him..."
    "His sense of humor. His sincerity. His quirks."
    "His genuine desire to always provide the exact perfect thing to make me smile..."
    "No... the depths of Pastille are reserved for me alone 💙" id ch6_fdebbc43
    nvl clear
    centered "{nw}" #hack to stop window transition lol

    scene bg atelierint
    show fg counter
    with fade
    # $ acc1 = 0
    # $ acc2 = 0

    show cg uniform at cgspan
    w "Welcome to Atelier Sweets~!"
    n "Periwinkle gives a little twirl and winks to Pastille, who's trying his best to stifle his laughter."
    hide cg
    show pastille work smile at righto behind fg
    w uniform smile "How was that? Do you think it suits me?"
    p ehe "Not in the slightest... you're too elegant for a place like this."
    w happy "I can be cute, too, can't I?"
    p sure "You are... but you're gonna need more than that on your résumé if you want the job."
    w love "What, you mean I can't get in through nepotism alone?"
    p smile "It looks like you already have a successful career in another field. You're overqualified, so I'm gonna have to turn you down."
    w calm "Ah~ you're right... besides, if you were my boss, we'd probably have to stop fucking."
    p scream "P-PERI--!!!!!!" with vpunch

    scene bg atelierstreet with dissolve
    "I truly, truly love him."
    "Even the days we'd talk about nothing at all, I wouldn't give up for the world."
    "And the days he would open up to me even moreso."
    nvl clear
    centered "{nw}" #hack to stop window transition lol

    scene bg atelierint
    show pastille work flustered2 at rightb
    show fg counter
    with fade
    p "Sy can be really frustrating sometimes..."
    p calm "But she's my best friend. I still care about her, even when she messes up."
    w calm "Hmhm, she's lucky to have you."
    p seriously "Yeah, she really is! Anyone else would've given up on her by now!"
    p "For YEARS, she would just lock herself in her lab, making all this candy, bragging about how cool her alchemy is compared to magic..."
    p flustered2 "She barely ever talked to anyone else! And when she did, it was to BERATE them over something!"
    p shout "Who treats their own customers like that?! Who do you think pays for the roof over our heads!!" with vpunch
    p calm "*sigh* ...Sorry. I don't wanna give you a bad impression of her. She's gotten much better recently."
    w smile "It sounds complicated. At least your patience is paying off, hm?"
    p ehe "Yeah, seems like it... at one point, it was kinda up to a coin toss on whether I'd stay or go."
    w love "A coin toss? How extreme!"
    p shy "N-not literally... it was more like, whether or not she could prove she actually felt empathy...."
    p sure "Anyway, it turns out she's not a complete monster. So here I am."
    p ohno "...Sorry. I'm still giving you a bad impression of her, aren't I...?"
    p ehe2 "Y-you can just disregard everything I said! Sy is great."
    w calm "I believe you. She must be, if you've put up with so much from her."
    p shy "Haha... yeah...."

    scene bg atelierstreet with dissolve

    "I treasured every moment I got to spend with Pastille."
    "Even without a label on what exactly our relationship was, I could enjoy myself all the same."
    "In truth, I was only biding my time. But it didn't really feel like that at all."
    "Just being near him was enough."
    nvl clear

    play music audio.pastille fadeout 2.0 fadein 2.0

    scene bg peristreet
    with Fade(1,1,1)
    "One day... he finally asked it."
    "The question I'd been waiting to hear."
    nvl clear

    show pastille work anxious at rightb

    p "Do you... wanna meet my friends?"
    w ah "Ah... well, yes, but... are you sure?"
    p nervous "No. But it feels stupid to keep avoiding it..."
    p flustered2 "I started worrying it'd happen on accident one of these days. I-I don't think I would survive that, so...."
    p seriously "We should just go! Before I change my mind!!"
    w ohdear "Ah--right now?"
    p "Yes. C'mon!"
    scene bg peristreet with Dissolve(.2)
    n "Pastille takes Periwinkle by the hand and the pair hastily makes their way to Atelier Sweets."

    scene bg atelierstreet with fade

    n "Slightly out of breath, Pastille stops just before they reach their destination."
    show pastille work calm at rightc
    p "O-okay... gimme a minute...."
    w love "After we rushed all the way here? Don't back down now, my sweet."
    p anxious "I know. I'm preparing, mentally."
    p flustered "I-I've never done this before. I know it'll be fine, I just..."
    w calm "Take your time. We'll go in when you're ready."
    p calm "...."
    p shy "O-okay... I think I'm only getting more nervous standing out here thinking about it. Let's just go in."
    w smile "After you~ 💙" id ch6_0688977c

    scene bg atelierint
    show fg counter
    with fade

    "The meeting itself was nothing memorable."
    show cg them at cgspan
    "Gumdrop was incredibly human, for a golem made out of candy."
    "Syrup was about what I expected. Curt, but also... warm."
    "For all its buildup, the interaction itself was anticlimactic. A quick exchange of pleasantries before the Candy Alchemist called her golem back downstairs."
    nvl clear
    hide cg
    "It didn't feel real."
    "Had I acted normal? Come across as my usual self?"
    "It had only just happened, but it's already a blur."
    "I held Pastille's hand in the end, I remember that. He had been so nervous, I could practically hear his heart beating out of his chest..."
    nvl clear
    scene bg atelierstreet with fade
    "I hadn't understood just how stressful it would be for him."
    "I felt guilty at having put him through it, although the idea was his to begin with."
    "He decided to go through that... for himself? Or for me?"
    "This seemingly mundane interaction that meant so much more for the both of us...."
    nvl clear
    show pastille work anxious at rightc
    p "...."
    w love "Pastille...?"
    p ehe2 "Sorry. I'm okay."
    p embarrassed "I feel stupid having made such a big deal of it... of course it all turned out just fine...."
    w calm "It was important to you. We all get worked up over things we care about, don't we?"
    p shy "A-are you including yourself in that? You seem like you always have it together...."
    w happy "Ohh, am I hiding it THAT well~?"
    p ehe "Haha, anyway... um, we can go...."
    hide pastille with Dissolve(.2)
    w smile "...."
    w ohdear "(How is he going to react when he discovers what a mess I've been...?)"

    scene bg peristreet with fade
    "Pastille walks me home, and promises to return later tonight."
    "Things will move forward from there, won't they? Or is it too soon...?"
    "Maybe it's too much for one day! I don't want to add to his stress...."
    nvl clear
    w oops "(Ugh... why is this so difficult...?)"
    w conflicted "(His perception of me could be completely destroyed! Tarnished!)"
    w sorry "(But that's a risk worth taking... isn't it...?)"

    stop music fadeout 2.0

    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    scene bg perihousecleandark
    with Fade(1,.5,.5)
    n "That night... Periwinkle laid on the floor in the middle of his living room and waited."

    w shutin neutral "...."
    w empty "(I'd expected this night to come eventually, and yet... I still don't feel any more prepared for it.)"
    scene bg perihousecleandark
    n "Periwinkle idly taps his wand to one of the candles on the table."
    w shutin oops "...Still peachy. The curse is not yet lifted."
    scene bg perihousecleandark
    n "Pastille's knock finally comes, and Periwinkle rises to answer."

    play music audio.romance fadein 2.0

    show pastille jacket smile at rightb
    with fade
    p "Oh, it smells nice in here. Is that your magic?"
    w shutin innocent "You like it? It's my latest specialty 💙" id ch6_c6202711
    p happy "Aww, what a treat!"

    p smile "Have you eaten yet? I could make us a special dinner."
    w my "Oh~ what's the occasion?"
    p ehe "Celebrating the fact nothing went horribly wrong today. I brought a few things, if I could just borrow your stove..."
    w innocent "By all means~"

    scene bg perihousecleandark with Dissolve(.2)
    "I once again found myself in the excruciatingly domestic situation of watching Pastille prepare a meal in my kitchen."
    "There's no way he doesn't realize it, right? That we've been acting as a couple for a long time now..."
    "It's just that neither of us have bothered to address it."
    "Shouldn't it be properly acknowledged...?"
    nvl clear
    "Pastille chats with me as he cooks, but I'm admittedly distracted by these thoughts."
    "Perhaps putting a name to it would only cause it to unravel..."
    "Currently, there's no expectation. We're free to see whoever else we like."
    "Though... it doesn't seem either of us are doing that."
    nvl clear

    n "Pastille approaches the table where Periwinkle sits, holding a plate in each hand."
    show cg pasta at smallcg
    show pastille pj happy at rightb

    p "Ta-da~ Pasta's ready."
    w shutin happy "Ooh, bon appétit 💙" id ch6_10cdcc29

    scene bg perihousecleandark with Dissolve(.2)
    "Maybe he's already decided we're a couple, and I'm just obsessing over formalities."
    "What does it matter, so long as the two of us are happy?"
    "And I really AM happy..."
    "His cooking... tastes wonderful...."
    nvl clear

    show pastille pj um at righto
    p "...Peri? You okay?"
    w shutin ah "Hm? Yes...?"
    p ehe "You were being so quiet, I started to worry that I messed up our dinner somehow..."
    w guilty "No, no... it's delicious!"
    w smile "I was just lost in the pasta, is all. Forgive me, I didn't mean to worry you."
    show pastille smile

    "I need to get out of my own head."
    "Pastille is here in front of me! And I'm too distracted to savor it...!"
    "Forget my doubts. We'll just have to see where the night takes us..."
    nvl clear

    n "Periwinkle takes his plate to the sink and begins to wash up."

    p wha "Ah--I can take care of that!"
    w love "Nonsense, you just cooked us dinner! It's your turn to relax, my sweet 💙" id ch6_e738bebe
    p shy "Are you sure I can't help...? I wouldn't mind at all...."
    w calm "You can help by bringing me your plate when you're finished."
    p ehe "Okaaay...."

    scene bg perihousecleandark with Dissolve(.2)
    n "Pastille does as he's told, then wanders over to the couch."

    show cg cozy1 at cgspan
    p "Hey, um..."
    p "If you have anyone you want to introduce me to, I'd be happy to meet them. Return the favor, sort of thing."
    show cg cozy2
    p "I-I know it can be awkward though, so... if not, that's okay too...."
    w "Hm... no, no one comes to mind."
    p "...Huh? Really?"
    w "Sure, I know a lot of people. But I couldn't say I'm particularly close with any of them..."
    show cg cozy3
    w "Except maybe one? But you've already met my business partner."
    p "Oh! At the apothecary, right?"
    show cg cozy4
    w "Precisely."
    p "...."
    show cg cozy4b
    w "Hm~? What's with that look."
    show cg cozy5
    p "N-no, nothing... I just don't know what to say now."
    w "Hmhm, you expected someone as charismatic as me to have all sorts of new people to introduce you to, then?"
    p "I guess so. I'm just surprised..."
    p "I, um, really like... being around you... so I expected that to be true for your other friends, too."
    w "Hmm..."
    show cg cozy6
    w "I'd say you're probably the closest I've ever been with someone."
    w "...Literally speaking."
    hide cg

    scene bg perihousecleandark
    n "They laugh together, then fall into a comfortable silence..."
    n "With their heads leaned together, Periwinkle nuzzles his face into Pastille's shoulder affectionately."
    n "After a few moments, Pastille asks..."

    show pastille pj shy at righto
    p "Do you... wanna get in bed?"
    w shutin teehee "For sleep, or for pleasure?"
    p omg "U-um, that's up to you...!" with vpunch
    scene bg perihousecleandark with Dissolve(.2)
    n "Periwinkle stands, then turns around to take Pastille's hands."
    w shutin "Come, then."

    scene bg bedroomcleandark
    with fade

    n "He leads him into the bedroom, closing the door behind them."
    n "When he does, Pastille speaks up again..."

    show pastille pj ehe at rightb
    p "You know... I'm still finding it hard to believe there's no one else you're close to."
    w shutin "Hm~? Two is a reasonable number."
    w calm "You had two friends as well, did you not? Syrup and Gumdrop."
    p sure "Fair point... but counting YOU makes three."
    w love "Ah, you have me beat. Perhaps I should try harder to catch up."

    scene bg bedroomcleandark with Dissolve(.2)
    n "Periwinkle collapses into bed, while Pastille sits down beside him."

    show cg inbed at cgspan
    w "I think I've preferred it, though. Keeping a healthy distance from others..."
    p "Really? How come?"
    w "The alternative has been disastrous in my experience. I'm far too intense."
    p "Ha, what do you mean by THAT...?"
    w "Goodness, my best example is the worst one..."
    show cg inbed2
    w "In my teenage years... there was a boy I would've done anything for."
    w "I wanted his approval so badly. I wanted to be loved."
    w "...It's funny, I can't even think of what drew me to him."
    show cg inbed3
    w "I suppose he was just a vessel to project onto. An idealized boyfriend, this... shortcut to happiness."
    w "Hmhm... poor guy. He didn't know what to do with the torrent of feelings I'd been forcing onto him. We were young."
    w "A love like that is much too painful. If it can even be called love...."
    show cg inbed4
    w "It took some practice to be able to separate the emotions out."
    w "To be able to indulge in the romantic and sexual energy I craved, while protecting my fragile heart..."
    w "But, ever since I figured it out, I've gotten to experience all sorts of love through these casual flings~"
    w "(What am I saying...?)"
    w "It's perfect for me 💙 The ideal life, really." id ch6_b87e6b7a
    w "(Don't listen to me, Pastille....)"
    # hide cg
    scene bg bedroomcleandark
    with Dissolve(.2)
    show pastille pj think at righto
    p "Hmm..."
    p smile "I don't know if your heart is as fragile as you think."
    w shutin love "You don't believe me? Despite what it seems, I have the heart of an innocent maiden~!"
    p sure "Haha, I don't know about innocent, but..."
    scene bg bedroomcleandark
    with Dissolve(.2)
    show cg inbed5 at cgspan
    n "Pastille leans forward and lays his head on Periwinkle's chest."
    p "...Sounds pretty strong to me."
    w "...!!"
    show cg inbed5b
    p "Ah, it's beating harder now."
    show cg inbed5c
    w "B-because you suddenly embraced me! See, this is what I mean by fragile...!" with vpunch
    hide cg
    scene bg bedroomcleandark
    n "Periwinkle struggles out from under him, and the pair sits facing each other on the bed."

    show pastille pj aw at rightc
    p "You know... at first, I thought romantic stuff was just a formality for you. But you actually love it, huh?"
    w shutin love "Are you only realizing that NOW?"
    p ehe "Haha, I guess not...."

    scene bg bedroomcleandark with Dissolve(.2)

    "What are you trying to say, Pastille?"
    "That it's okay for me to love you...?"
    "That I'll be safe?"
    nvl clear

    show cg inbed6 at cgspan
    w "Then, hurry up and kiss me."
    show cg inbed6b
    p "Okay ❤ Sorry to keep you waiting." id ch6_4a8350ae
    show cg inbed7
    n "Pastille closes the distance between them..."
    "I'm too weak."
    "The words won't come out..."
    nvl clear
    show cg inbed7b
    n "As they kiss, Periwinkle becomes more and more entangled in his thoughts..."
    "Ahh, it hurts...!"
    "I want to be even closer...."
    nvl clear
    show cg inbed7c
    n "He lets himself fall backward, bringing Pastille down with him."
    "This isn't nearly enough to satisfy me..."
    "Just, please, don't stop...."
    nvl clear
    window hide
    scene bg bedroomcleandark with dissolve

    n "Periwinkle's heart cried out..."
    n "His jumbled emotions caught in his throat, manifesting through his hands, clinging desperately to Pastille..."
    n "...who continued to kiss him and hold him through the night."

    stop music fadeout 4.0
    $ quick_menu = False
    scene black with Fade(1.5,1,0)

label ch7:
    scene bg chapterbreak with dissolve
    $ save_name = _("Chapter 7 - Shooting Stars")
    show title ch7 at chtitle
    centered "{w=3}{nw}"

    scene bg peristreet with fade
    $ quick_menu = True

    n "The next morning, Periwinkle steps out onto his doorstep with a heavy sigh."

    w hood empty "(If I lay around in bed all day, I'll only feel more miserable...)"
    w oops "(I need to stop avoiding my work. I have to talk to Astragalus....)"
    w empty "(She isn't going to be pleased with me though....)"
    scene bg peristreet
    n "Holding his mantle tightly, he makes his way to the apothecary..."

    play music audio.astra fadein 2.0

    scene bg apothecary
    show fg register
    with fade

    n "When he arrives, Astragalus is preoccupied with arranging some of her merchandise."
    n "She turns abruptly at the unexpected sound of the door's chime."

    show astra augh at rightb
    a augh "Hey, we're not open yet--!" with vpunch

    a hm "...Huh? Periwinkle?"
    w hood decline "Good morning, Astragalus."
    a uh "I haven't seen you all month--I barely recognized you under that hood!"
    a augh "I was about to come and knock on your damn door if you didn't show your face here soon. You've got a huge backlog of orders waiting!"
    w empty "...I can't take them. My magic is useless."
    a uh "Whaddaya mean, \"useless\"?"
    n "Periwinkle meekly hands over one of his pale pink vials."
    w ohhh "This is all I can make... it's been this way for ages."
    a whatever "*sigh* Let's see..."
    n "Astragalus unscrews the top, and eyes Periwinkle suspiciously before giving it a whiff..."
    a uh "Whew, that's powerful!!" with vpunch
    a think "Not bad, though... warms me right up. Could stand to be diluted a little, just to make it less overwhelming..."
    a lol "So. What's got you stuck on a scent like this?"
    w ohhh2 "...It's Pastille...."
    w whine2 "He's ruined me! I'll never be able to return to the way I was before...!"
    a closed "I see. So things got complicated, just like I warned you."
    w cwy "Mhm... *sniffle*..."
    w cwy2 "I-I love him so much, I think I might die...."
    a neutral "Come on... Back room. Now."
    scene bg apothecary
    show fg register
    with Dissolve(.2)
    n "Periwinkle nods and obediently follows Astragalus into her private office..."

    scene bg backroom
    with fade

    n "He quietly takes in his surroundings before she suddenly turns to him with a raised finger."
    show astra annoyed at rightb
    a "Don't touch anything."
    w hood ohhh "...?"
    scene bg backroom with Dissolve(.2)
    n "Astragalus drags a bean bag chair out from the corner and plops it in the middle of the room unceremoniously."
    show astra closed at righto
    a "Sit."
    w hood ohhh "...It's dusty...."
    a augh "UGH, you're such a diva..."
    n "She gives it a couple good smacks, beating the dust into the air instead."
    a annoyed "...NOW sit."
    w oops "Very well...."

    scene bg backroom with Dissolve(.2)
    n "He complies, and Astragalus spins her office chair around to face him."

    show cg talkitout at cgspan
    a "Alright, Periwinkle. Here's what's gonna happen."
    a "I'm gonna brew us up some tea, and you're gonna explain everything. From the beginning."
    w hood sorry "Explain what...?"
    a "About Pastille. Even the stuff I already know. Everything, from the top."
    w ohhh "Everything...?"
    a "Skip the bedroom details, obviously. Just walk me through anything important that happened since you met."
    w whine "I-I don't want to! Reliving it all is only going to make things worse...!"
    hide cg
    scene bg backroom with Dissolve(.2)
    n "Astragalus stands and walks over to her kettle to start the tea."
    show astra whatever at rightc
    a "Alright, you lovesick dolt..."
    a annoyed "You wanna know why exactly your magic's been stuck like that? It's because you don't have an outlet for all those emotions."
    a closed "Instead, you keep bottling them up--literally, I guess. It's all that comes out because it's all there is inside you."
    w hood ohhh "...."
    a lol2 "So, let it all out! What, you think I'm gonna judge you?"
    w oops "No... I don't know."
    a lol "Would you rather spill it all to him instead?"
    w cwy "I can't...! It's too much!"
    a sure "Then tell it to me, a neutral third party."
    a uh "Actually, I can't say that I'm neutral... I'd need to find a new supplier if you couldn't fill my orders anymore."
    w oops "I do feel a little more at ease imagining this is all a business matter for you...."
    a smile "Then just think of it like that."
    scene bg backroom with Dissolve(.2)
    n "Astragalus pours their tea and returns to her seat with two mugs in hand."
    n "With a heavy sigh, Periwinkle finally relents and begins his story..."

    play music audio.pastille fadeout 2.0 fadein 2.0

    scene bg backroom
    with Fade(1,1,1)
    "I told her everything I could think of..."
    "My first impressions of him. How he continuously subverted my expectations."
    "My mistakes. Appearing where I shouldn't have, then going into a desperate spiral as I tried to rid myself of the guilt over it."
    "How he was the one to come to apologize afterward..."
    nvl clear
    "Our date that day, which was so, so wonderful... but which also laid bare the feelings I was too afraid to acknowledge."
    "How I latched on to any alternative explanation I could in order to escape them."
    "The moment I could finally admit it to myself. All the ways he'd changed my life for the better."
    "How we grew closer and closer, while I held those feelings tighter to my chest..."
    nvl clear
    "I told her how he had finally worked up the courage to introduce me to his friends."
    "How his hand trembled in mine as we walked out the door together."
    "This point of contention, a far-off goal I had decided would have to be met before advancing..."
    "Everything, up to the state I'm in now. Useless, paralyzed, and sobbing."
    nvl clear
    "Astragalus listened patiently through all of it."
    "She asked questions from time to time. Clarification on the timeframe, certain details..."
    "Her reaffirming comments offered such comfort, such relief to this pain I'd kept confined to my own heart."
    "Until finally, I had nothing left to say."
    nvl clear

    n "Astragalus sits back in her chair and heaves a sigh."
    show astra happy at righto
    a "So? How are you feeling?"
    w hood oh2 "There's a certain clarity in laying it all out at once..."
    w ohhh "But, I still... don't know what I can do to push things forward... could I even handle the rejection...?"
    a eyeroll "He won't reject you."
    w sorry "What makes you so certain...?"
    a lmao "That boy is madly in love with you!! Why else would he devote all that time and energy to making you happy?"
    w pout "Because I'm great in bed! Obviously!!" with vpunch
    a lol2 "Quit deflecting! You know that's not all it is."
    w nofair2 "I don't want to leave any room for doubt... if I were to confess now, and it didn't go well, I'd... I'd be destroyed beyond repair!"
    w nofair "That's why, if I'm going to say it, I want it to be a sure thing."
    a sure "Life ain't about \"sure things\"."
    w oops "Even so. I'm going to wait for the opportune moment before exposing my vulnerable heart...."
    a eyeroll "As long as you've got a plan."

    n "Astragalus leans down to pick up Periwinkle's empty mug, then holds it out in front of him."
    a happy "Try your magic again. Whatever scent you want, just pour it right in the cup."
    w hood ohhh "...."
    scene bg backroom
    with Dissolve(.2)
    # show cg cast at cgspan
    n "Periwinkle nervously draws his wand, holds it out to the cup... then closes his eyes, and taps."
    # hide cg
    show astra closed at righto
    w hood ohhh2 "...Is it...?"
    a "...."
    a hm "Chamomile?"
    w my "It isn't peach...!"
    w happy "I-I'm cured!!" with vpunch
    a lol2 "Yeah, dumbass! Did you forget this is an apothecary?"
    w ohdear "Ah... it is, isn't it...."
    a eyeroll "Next time you've got a problem with your magic, don't sit around crying about it on your own. Come straight to me, and I'll fix you up."
    w love "Thank you... I..."
    w shy "I'm truly glad that we're friends... I would be lost without you."
    a sure "Business associates. Don't forget I've got loads of orders for you now that you're back to normal."
    w happy "I'll go home and fill them right away! But first..."
    w love "May I hug you?"
    a augh "Not a chance!" with vpunch
    w teehee "Hmhm, it was worth a shot. You'll accept my platonic affection one day~!"
    a happy "Yeah, yeah... get outta my office, Periwinkle."

    play music audio.astra fadeout 2.0 fadein 2.0

    scene bg apothecary
    show fg register
    with Fade(1,1,1)
    n "The pair exits the back room, but they only make it a few steps out before Periwinkle turns on his heel."
    w hood oh "Ah, one more thing, before I go..."
    show astra hm at rightb behind fg
    a "Hm? What's up."
    w smile "I've been curious to ask. The last time I was here, you told me that magic can be interpreted as a judge of one's character..."
    a think "Oh, right. When I changed my mind about Pastille."
    w calm "Yes, precisely. It's rather impressive that you could see through to his true nature, despite having only just met..."
    a lol "Sure, but he was pretty easy to read. Don't be too impressed."
    w love "...Well?"
    a lol2 "Well what?"
    w happy "What does my magic say about me~? I'm dying to know 💙" id ch7_665ef7a8
    a sure "YOUR magic... was always lively and carefree. Compassionate, too. Like Pastille's."
    w love "How can you possibly read something like \"carefree\" from perfume?"
    a lol "Hey, I'm just telling you the vibes I've gotten over the years."
    a think "Your aromas prioritize pleasure. But there was definitely a hint of loneliness in them, too..."
    w teehee "Alright, now I KNOW you're making things up. I've always had someone to keep me company 💙" id ch7_d8043053
    a smile "Just because you've always got someone around doesn't mean you can't be lonely."
    w calm "And I suppose someone like you would know a thing or two about loneliness, hm?"
    a hm "I'm not lonely at all. In fact, I PREFER to be alone."
    a closed "YOU on the other hand... can't stand it even for a second. That's why you'd always run off chasing someone to fill the void."
    w ohdear "...Well THAT certainly isn't true."
    a lol "The peach stuff you gave me earlier was PURE loneliness. It was crying out, like \"Please, Pastille, never leave me~!\""
    w pout "This isn't fun anymore. Forget that I asked!"
    a happy "Sorry. Couldn't resist."
    w oops "...."
    w ohhh "I suppose you're right, though... I haven't been able to tell him that in words."
    w nofair2 "I can't keep holding back... he has to know. No matter the outcome."
    a smile "Good luck, okay? I'm sure it'll turn out just fine."
    w ohhh "Yes... yes, it likely will."
    w shy "Thank you again... I'm truly grateful for all that you've done for me."

    scene bg apothecary
    show fg register
    with Dissolve(.2)
    n "Astragalus waves him off, and Periwinkle leaves the apothecary with new resolve..."

    play music audio.peri fadeout 2.0 fadein 2.0

    scene bg streetday with fade
    pause 1
    scene bg peristreet with fade
    pause 1
    scene bg perihouseclean with fade

    "I spent the next several days catching up on my work."
    "Magic truly does come so easily with a clear mind! If only I'd swallowed my pride sooner."
    "I completed batch after batch almost effortlessly, going down the long checklist Astragalus had given me..."
    "I hadn't even felt tired by the end of it. As if all this energy had been stored up inside me all along!"
    nvl clear
    "It was a relief to return to somewhat normalcy."
    "Thinking of Pastille no longer caused my heart to ache... at least, not enough to put me in a state of total despondence."
    "Instead, those thoughts served as motivation. The way forward was clear."
    "I would tell him how I felt... and surely..."
    nvl clear
    w pj calm "Surely things will turn out just fine...."

    scene bg peristreetnight
    with fade
    n "The following night... Pastille shows up on Periwinkle's doorstep."
    show pastille manto smile at rightb
    p "Get dressed. I wanna take you somewhere."
    w pj happy "Oh~ and where exactly am I being whisked away to? 💙" id ch7_89d40548
    p happy "You'll see. Wear comfortable shoes, okay?"
    w calm "How mysterious..."
    w smile "Hmhm, very well. I'll be ready momentarily 💙" id ch7_c60adcac

    scene bg perihousecleandark with fade
    "This is it..."
    "The dramatic confession scene is upon us!"
    "I have to look my best! For good luck, of course."
    "And for confidence...."
    nvl clear

    if customboy:
        $ quick_menu = False
        scene bg chapterbreak with fade
        call screen accessorize("side_peri_outfit_cute")
        $ quick_menu = True

    play music audio.romance fadeout 2.0 fadein 2.0

    scene bg streetnight
    with Fade(1,1,1)
    n "Hand in hand, the pair makes their way to the train station."
    w cute innocent "(Hmhm~ had he been planning something while I was sequestered away with my work?)"
    w love "(Pastille is always so full of surprises... how positively delightful 💙)" id ch7_db582720

    show pastille manto shy at rightb
    p "I hope I didn't interrupt any plans you had for the night...."
    w happy "Oh, not at all~! It was about time I got out of the house again."
    w smile "I've actually had a very productive past several days, you know. Toiling away over my perfumes."
    p ehe "Haha, I thought that might be the case, since you hadn't dropped by in a while."
    w innocent "Did you miss me? 💙" id ch7_fb3a840a
    p embarrassed "W-well...."
    scene bg streetnight with Dissolve(.2)
    n "Periwinkle hugs Pastille's arm tightly as they continue their walk."
    w cute shy "(I missed you, too...)"

    scene bg somewhere with Fade(1,1,1)
    "When Pastille and I step off the train, we're greeted by grassy fields and a sky full of luminous stars."
    "Just where has he taken me...?"
    "A trail of lanterns lights the lone path forward..."
    "Pastille takes the lead."
    nvl clear

    show pastille manto smile at rightb
    p "It's a bit of a walk from here... but I promise it'll be worth it."
    w cute love "A long walk, hm? Couldn't we take a ride on your broom together~?"
    p sure "Nah, it'd defeat the purpose. It'll feel more rewarding getting there on foot."
    w calm "Hmhm... fair enough. Tragic, though, that you'd willingly pass on an opportunity for me to cling to you."
    p ehe "Haha, we can fly on the way back if you want."
    scene bg somewhere with Dissolve(.2)
    n "Pastille offers his hand again, which Periwinkle takes with a smile."

    scene bg somewhere
    show cg walk at cgspan

    w "...Tell me more about your relationship with magic."
    p "Hm? What do you mean?"
    w "It was the same when we cleaned my house together. You insisted on doing things manually..."
    w "Not that I minded at all. Seeing you lift so many heavy things was a treat in itself 💙" id ch7_7c5e0bd7
    p "Hahaha, well..."
    p "Ever since I was young... it was clear I was, um... \"ridiculously talented\", as they'd put it."
    p "My moms wanted me to be a traditional witch. They enrolled me in one of the top schools, so I could learn from the best."
    show cg walk2
    p "I-it was an all-girls school, though... Guess I was young enough that no one realized I was a boy."
    p "I really... didn't belong there. On any level."
    p "But, I kept at it as long as I could. Just enough to keep my parents happy, until I could go out and live on my own."
    show cg walk3
    p "Haha, I still don't understand exactly why... but I always felt uncomfortable using my magic."
    p "It felt like cheating. Like... this kind of power shouldn't come so easily."
    p "Sy thought so, too. I guess that's why I latched onto her when we met..."
    p "She used to really hate magic. Which worked out perfectly for me--it was a good excuse to pretend to be a regular human like her."
    p "So... that's what I did. For the past... seven years?"

    hide cg
    w cute my "Seven years... that's quite a long time!"
    show pastille manto shy at righto
    p "Yeah, but there was a lot to distract me back then... it took a while to get Atelier Sweets up and running."
    p calm "And... Sy did eventually find out. I thought she'd disown me when she did..."
    p ehe "But instead... she told me I shouldn't have hid it. Even though I doubt we would've become friends if I told her from the beginning..."
    w calm "Quite impossible to please, hm?"
    p sure "You have no idea...."
    p smile "But... ever since she said that, I've been able to start embracing magic again. On my own terms."
    w "(I'm beginning to grasp why he values her so highly...)"
    p ohno "Um, sorry that I just keep talking about myself...."
    w happy "Don't apologize~! I'm the one who asked."
    w smile "Besides, I'm content to listen. Say as much as you like."
    p embarrassed "Thanks...."

    scene bg somewhere with Dissolve(.2)
    n "Periwinkle gives Pastille's hand a reassuring squeeze."

    "I love him..."
    "I have to find the right moment to tell him that."
    "Should it be now? During this romantic walk?"
    "Ah, but he still has yet to reveal our destination..."
    "What do you have in store for me, Pastille...?"
    nvl clear

    show pastille manto ehe at righto
    p "I think I might be too used to how Sy is... she's usually so preoccupied with her own stuff."
    p smile "So it's nice... having someone who actually wants to listen to me."
    p flustered2 "Agh, that makes her sound like such a horrible friend...! She's really not!!" with vpunch
    w cute happy "You certainly haven't made a convincing case for her~!"
    p calm "*sigh* I know. But that wasn't the point I was trying to make..."
    w oh "Oh?"
    p ohno2 "I really...!"
    p flustered2 "...."
    w love "Yes...?"
    p seriously "Let me start over."
    scene bg somewhere
    show pastille manto calm at righta
    n "Pastille takes a deep breath before continuing..."
    p wha "Going back to... what we were talking about before. With my magic and everything."
    p think "I think I have trouble accepting myself for what I am... I tend to hide things, even when I don't need to."
    p oh "Being with YOU feels like... it's better not to hide? Like, I'm allowed to just BE."
    p shy "Or, more like... celebrated? For being? I-I don't know, that feels weird to say."
    w cute wow "...."
    p ehe "Y-you can stop me if I'm being too much...."
    w nofair2 "(IT'S BECAUSE I LOVE YOU...! Why can't I just say that...?!)" with vpunch

    p smile "Oh! We're here!"
    w my "W-we are...?"

    play music audio.finale fadeout 2.0 fadein 2.0

    scene black
    show bg starfield at slowpandown
    with Fade(1,1,1)
    pause 1

    "When we came up over the hill..."
    "The vastness of the night sky overwhelmed me."
    "But more than that..."
    "The field of small blue flowers, that stretched as far as the eye could see..."
    "Matched it so perfectly."
    nvl clear

    scene bg starfield
    show fg flowers
    w cute shock "Pastille...!"

    show pastille manto aw at rightb
    p "They're periwinkles. When I looked up where to find some... I found out about this place."
    p doki "A-apparently it's a famous date spot... I thought you'd like to see it, so...."

    w "I... I-I...!"
    w whine2 "I shouldn't have told you I'm weak to romance...!! Pastille!!!" with vpunch

    show firststar

    n "A glint catches Periwinkle's eye,{nw}"
    show shootingstars behind fg
    extend " and he looks up to notice... a meteor shower has begun."

    w my "Ah...!"
    p happy "Oh, good! It started just in time...."
    w shock "You planned this, too?!" with vpunch
    p embarrassed "Well, I knew this was supposed to be happening tonight... so...."

    hide pastille

    show cg hug at cgspan
    w overwhelmed "PASTILLE!!!!!!!"
    show cg hug2
    p "WAH--!!" with vpunch
    scene bg starfield
    show shootingstars
    show fg flowers
    with Dissolve(.2)
    n "Periwinkle tackles Pastille to the ground, landing them in the field of flowers..."

    show cg hug3 at slowpanup
    pause 3
    w "This is perfect..."
    w "I-I don't know what else to say...! I'm speechless...."
    p "Haha, I guess I went a little overboard...."
    w "A little?! This is the most romantic thing anyone's ever done for me!!!" with vpunch
    n "He buries his face in Pastille's chest, holding him close."
    p "Well... there's actually... one more thing I wanted to say."
    show cg hug4
    n "He can feel Pastille's heart pounding."
    p "Ahh, where do I start... um...."
    p "You know how... Sy and Gumdrop are really important to me?"
    p "I always thought that I needed to keep myself available for them. To take care of the store and everything."
    p "But in practice, that just meant... I never really took any time for myself."
    p "Like, my own needs were something I could just bury, and it would be fine... because it's for their sake."
    show cg hug5
    p "I guess that's part of why... I'd go out with random guys in secret. As something just for me, totally detached from everything else."
    p "I tried... having a real relationship once. It didn't work out, obviously. I-I never told Sy about him..."
    p "But that made me think... that I was right to continue on the way I had been. Since I wasn't willing to let my priorities shift."
    n "Periwinkle grips Pastille's cloak a little tighter."
    w "Wh-what are you saying...?"
    p "I guess, um... that, with you... I don't mind it as much."

    hide cg with dissolve
    scene bg starfield
    show shootingstars
    show fg flowers

    "H-he's... he's going to beat me to it at this rate!!"
    "I-I can't let that happen...!"
    nvl clear

    n "Periwinkle suddenly rolls himself on top of Pastille, pinning him down."

    show cg final1 at cgspan
    w "Pastille, I'm in love with you!!!"
    p "Wh-wha--??!?!? S-since when?!" with vpunch
    show cg final2
    w "I-I don't know, maybe this whole time?!"
    w "I only admitted it to myself that morning you made me pancakes...."
    show cg final3
    p "That's what it took..?"
    w "Why? How long have YOU felt this way?"
    show cg final4
    p "Since... having to carry you home, after spending the day together? I think that's when I first realized it..."
    w "Then why didn't you say something?! I've been suffering in silence this entire time...!" with vpunch
    show cg final3
    p "I-I thought you wanted to keep it casual...?"
    w "We saw each other almost every day!! How is that casual?!"
    p "But you never acted any differently...! A-and I was busy sorting through my own feelings anyway...."
    show cg final1
    w "Mmmnnnnnn...!!!!!!! So was I...."
    w "But that's no excuse for how long you kept me waiting...! I-I won't forgive you!"
    show cg final5
    p "...."
    w "Wh-what...? Why are you smiling like that?"
    p "It's cute... seeing you all worked up like this."
    w "--!!"

    hide cg
    n "Periwinkle struggles to his feet and begins stomping away."

    w cute nofair2 "Y-you could've saved me a lot of heartache, you know...!"
    n "Pastille sits up, straightening out his cloak and retrieving his hat."

    show pastille manto aw at rightb
    p "Where are you going...? Come back."
    w nofair "No!! I'm too upset!" with vpunch
    p ehe "Peri...."
    w yell "I was convinced... CONVINCED, that I'd cursed myself with some kind of love potion! My fake aphrodisiac turned real!"
    p "What in the world...?"
    w "Because we didn't fuck that day! Fucking was supposed to be the entire point of it!!" with vpunch
    p dying "P-PERI...!"
    w nofair2 "Everything spiraled out of control since then...! I couldn't stop thinking about you!!"
    w yell "You BROKE my magic! For weeks and weeks, all I could conjure was that stupid peach blossom scent...!"
    p woah "A-ah... really...?"
    w nofair2 "Yes! Until just the other day... which I spent CRYING, in the dusty back room of the apothecary, telling Astragalus all about it...!"
    w nofair "After all that... everything I spent so long preparing my heart for... you have the NERVE to try to confess first...?!"
    p aw "I'm sorry."
    w nofair2 "Don't apologize! I already said I won't forgive you!!" with vpunch
    p ehe "What do you want me to do, then...?"
    w insulted "I don't know, fucking kiss me if you love me so much!!!"

    scene bg starfield
    show shootingstars
    show fg flowers
    with Dissolve(.2)

    show cg finalkiss at cgspan
    n "Pastille approaches, gently raising a hand to Periwinkle's cheek..."
    show cg finalkiss2
    n "...and does exactly as he's told."
    show cg finalkiss3
    p "I love you."
    n "Periwinkle's heart skips a beat."
    show cg finalkiss4
    w "I love you, too...!"
    n "He hugs Pastille tightly, careful not to knock him over this time."

    scene black
    show bg starfield at top
    # show shootingstars
    with fade

    "It takes everything I've got to keep myself from bursting into tears."
    "I won't ruin my makeup on this perfect date...!"
    "This beautiful place, that Pastille chose just for us..."
    "I can't have my memory of this perfect night obscured by tears...."
    nvl clear

    scene bg starfield
    show pastille manto think at righta
    with fade

    p "It looks like the meteor shower's over...."
    w cute pout "...Take me home...."
    p ehe "A-are you still mad at me...?"
    w oops "I'm not mad at you...."
    p aw "I've never seen you like this. I don't know how else I should interpret it."
    w conflicted "I'm overwhelmed. Elated... relieved... and frustrated...."
    w ohhh "I-I want to get in bed... so that you can hold me close all night..."
    w ohhh2 "I don't think I'll be convinced that this was real unless you do that. So... please...?"
    p doki "That sounds... really nice...."
    p happy "Okay ❤ If it's to convince you, I guess I have no choice...." id ch7_23f5322d
    w shy "... 💙" id ch7_cb290d59

    stop music fadeout 3
    $ quick_menu = False
    $ _game_menu_screen = None
    jump credits
