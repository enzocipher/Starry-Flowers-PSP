
label ex_navi:
    window hide
    stop music fadeout 2.0
    $ quick_menu = False
    scene bg chapterbreak with fade

    menu ex_navi1:
        "Art Gallery":
            call gallery from _call_gallery
        "Accessorize!":
            $ faveacc = [0,0,0]
            call screen accessorize("side_peri_outfit_witch")
        "Extra Scenes":
            jump ex_navi2
        "Bonus Chapters":
            jump bonuschapters
        "Main Menu":
            scene black with dissolve
            return

    jump ex_navi

    menu ex_navi2:
        "Busted Lamp" (newevent=persistent.ex1):
            call ex1 from _call_ex1
        "Atelier Sweets" (newevent=persistent.ex2):
            call ex2 from _call_ex2
        "Cuddly Witch" (newevent=persistent.ex3):
            call ex3 from _call_ex3
        "Old Photos" (newevent=persistent.ex4):
            call ex4 from _call_ex4
        "Night on the Town" (newevent=persistent.ex5):
            call ex5 from _call_ex5
        "Return":
            jump ex_navi1
    scene bg chapterbreak with fade
    $ _history_list = []
    jump ex_navi2

    menu bonuschapters:
        "Prologue" (newevent=persistent.ch0):
            call ch0 from _call_ch0
        "Chapter 4.5 - Stay" (newevent=persistent.ch4b):
            call ch4b from _call_ch4b
        "Chapter 7.5 - \"I love you\"" (newevent=persistent.ch7b):
            call ch7b from _call_ch7b
        "Return":
            jump ex_navi1
    scene bg chapterbreak with fade
    $ _history_list = []
    jump bonuschapters

label ch0:
    play music audio.peri fadein 3.0

    scene bg atelierstreet
    with fade
    $ quick_menu = True

    n "Periwinkle is strolling through town when he comes across a certain candy store..."
    w oh "(Atelier Sweets...?)"
    w happy "(Ahh, so this is where it is! The place with the cute golem mascot everyone is talking about.)"
    w oh "(I wonder if she's there...?)"
    n "Periwinkle takes a peek through the window..."
    w drool "(...Ah! I don't see her, but I DO see something I like...!)"

    scene bg atelierint
    show pastille work neutral at righta
    show fg counter
    with fade

    n "Periwinkle walks in, and promptly approaches the sweet pink-haired boy at the counter..."
    w drool "(My, he's even cuter up close...!)"
    w innocent "Why, hello there! This is the shop famous for the Candy Golem, is it not?"
    p ehe "Oh! Um, yes, it is!"
    p smile "If you wanted to meet Gumdrop, you unfortunately just missed her."
    w calm "Mm... bad luck on my part. I'll have to come back another time, I suppose."
    p "Sorry about that. Have a nice day!"
    w smile "Oh, I wasn't planning on leaving just yet. After all, I came all this way..."
    p ehe "Right... in that case, I'll leave you to browse our selection!"
    w innocent "Ohhh no, you're not getting away that easily. Keep me company, won't you?"
    p wha "H-huh?"
    w shy "I'm absolutely useless at making decisions, you see..."
    p shy "Oh! Certainly...!"
    scene bg atelierint
    show fg counter
    with Dissolve(.2)
    n "Visibly flustered by Periwinkle's words, the pink-haired boy comes out from behind the counter to assist his customer..."
    show pastille work oh at rightc
    p "Do you have a favorite type of candy? Or maybe flavor? Anything to narrow it down...?"
    w smile "Mm... I'm a little fickle. What would you recommend?"
    p think "Well, these ones have been pretty popular lately..."
    n "He gestures to the shelf in front of them. Periwinkle takes a step closer..."
    w oh "I'm not asking what's popular, I'm asking what you'd recommend, Mister...?"
    p wha "Pastille."
    w happy "Pastille... hmhm, is that why you decided to work at a candy shop? Because of your name?"
    p ehe2 "N-no, I just ended up here..."
    w drool "I don't think I've ever tried pastilles before... how would you say they compare to other candies?"
    p embarrassed "Ah-haha, um, I-I'm not sure how to answer that!"
    n "Periwinkle leans in a little closer..."
    w innocent "Suppose I'll have to taste for myself, hm?"
    p omg "O-okay! I'll ring you up!!" with vpunch
    scene bg atelierint
    show fg counter
    with Dissolve(.2)
    n "Pastille retreats behind the counter once more. Periwinkle can hardly keep himself from giggling with delight."
    w drool "(Oh, THIS one is going to be fun...)"
    stop music fadeout 3.0

    $ persistent.ch0 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ch4b:
    play music audio.romance fadein 3.0
    scene bg peristreetnight
    with fade
    $ quick_menu = True

    n "Pastille dismounts his broom, careful not to let the sleeping Periwinkle slip from his shoulders."

    show pastille date oh at rightb
    p "Time to wake up, Peri... I need your housekey."
    w date calm "...Zzz...."
    p ehe2 "...Okay. Well. I can't just leave you on your doorstep...."
    p think "So... pardon me...."
    scene bg peristreetnight with Dissolve(.2)
    n "Pastille searches Periwinkle's pockets until his fingers brush against what might be a keychain."
    n "And when he pulls it out..."
    show pastille date smile at rightc
    p "...Oh! What a cute character."
    p aw "Wanna tell me what it's from? Or are you still sound asleep?"
    w date calm "...Mmnm...."
    n "Periwinkle's hands slip under Pastille's jacket as he snuggles into him, rubbing his chest before settling once more."
    p omg "Wahhh...! A-are you awake or not?!" with vpunch
    w "......"
    p flustered "...Okay. I found your key, so... let's get you in bed...."

    scene bg perihousedark
    with fade

    n "Pastille unlocks the door and carries Periwinkle inside."

    scene bg bedroomdark
    with fade

    n "When they reach the bedroom, Pastille gently lays him in bed..."

    show pastille date ehe at rightc

    p "Now's your last chance to wake up...."
    n "Despite his prodding, Periwinkle is unresponsive."
    p flustered2 "...Ahh, I have to change you myself, don't I? Where are your pajamas...."

    scene bg bedroomdark with Dissolve(.2)
    n "Pastille opens and closes each dresser drawer until he finally comes across Periwinkle's sleepwear."

    show pastille date neutral at rightb
    p "Here we go... umm... this one looks easy to slip on...."

    scene bg bedroomdark with Dissolve(.2)
    n "He returns to Periwinkle on the bed and gets to work undressing him...."
    $ faveacc = [acc1,acc2,acc3]
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0
    show pastille date smile at righta
    with fade

    p "There. You're all tucked in."
    p ehe "So... I guess I'll head out now. Goodnight, Peri."

    n "As Pastille shifts himself off the edge of the bed to leave, Periwinkle sleepily grabs onto his sleeve, stopping him in his tracks."
    show pastille date woah
    w pj shy "...Stay...."
    p "...?"
    p shy "...Peri...?"
    w "......"
    p flustered "...Nnnn......"
    p omgstop "(It's really tempting... it's really, REALLY tempting...!)"
    p nervous "(So tempting that... it scares me a little....)"
    p ohno2 "...."
    show pastille date calm
    n "Pastille takes Periwinkle's hand and tucks it back under the blanket."
    p ehe "Sleep well, okay...?"

    scene bg perihousedark
    with fade
    show pastille date nervous at rightc

    p "...."
    p shy "(I have to head back... Sy's already gonna ask all sorts of questions....)"
    p nervous "(It was only supposed to be a few hours...! But I was having too much fun, I couldn't just....)"
    p flustered2 "......"
    p nervous "(Ahhh... this is serious, isn't it...?)"

    scene bg perihousedark with Dissolve(.2)
    n "Pastille hurriedly makes his way out the door, a hand over his mouth to hide his troubled expression...."

    stop music fadeout 3.0

    $ acc1 = faveacc[0]
    $ acc2 = faveacc[1]
    $ acc3 = faveacc[2]

    $ persistent.ch4b = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ex1:
    play music audio.astra fadein 3.0

    scene bg apothecary
    show fg register
    with fade
    $ quick_menu = True

    n "Today, Astragalus has asked Pastille to work his magic on her busted lamp."
    n "He happily agrees. Meanwhile, Periwinkle looks on, arms folded and pouting..."

    show astra neutral at righto behind fg
    show pastille manto smile at lefta
    p "...There! How's it look?"
    a think "Hm... it's not EXACTLY like it was before... but, beggars can't be choosers."
    p ehe2 "A-ah... it'd help if I knew the original shape... I had to guess from looking at the pieces."
    a sure "Nah, better this than a pile of glass. Thanks, kiddo."
    w witch pout "...."
    a eyeroll "Ha, you should probably do something to fix your boyfriend's face next."
    w "My face doesn't need fixing. I'm looking flawless as ever."
    p aw "Peri...."
    w innocent "If you're finished being used, however, I'd like to have you back now, please~!"
    p ehe "It was just a small favor. I really don't mind... in fact, I'm happy to help."
    a sure "See? He's more than willing."
    w oops "Stop exploiting his kindness...!"
    p smile "Let me know if there's anything else I can fix for you, ma'am."
    a lol2 "Now that you mention it... I'm sure there were a few other things... I'll be right back!"
    scene bg apothecary
    show fg register
    with Dissolve(.2)
    n "Astragalus takes her repaired lamp and heads into her office to retrieve the next broken object."
    show pastille manto smile at rightc
    w pout "...."
    p ehe "Peri... it's really nothing to get upset over. This is just an excuse for us to get to know each other better."
    w decline "I would rather you not be categorized as a tool in her mind... but, if you insist...."
    p smile "I'll let her know if she starts asking too much of me. So, no more pouting, okay?"
    w shy "...Hmhm, how could I refuse such a gentle command? 💙" id ex1_9b1bf24b
    p doki "A-as long as you're in a better mood now...."
    w love "I am. Besides... it was quite hilarious to hear you call her \"ma'am\" in earnest."
    p oh "Huh...? She's older than us, isn't she? We should respect our elders."
    w happy "Ahaha, Pastille...! If you call her an elder to her face, she'll go absolutely ballistic~!"

    scene bg apothecary
    show astra sure at rightb
    show fg register
    show pastille manto ehe at left
    with fade

    a "Turns out there WERE a few things! I've got 'em right here--"
    a lmao "Hm? Oh, look at that, you really DID fix his face! Damn, nice work!"
    w happy "Listen, Astragalus~! You'll never guess what Pastille just said! 💙" id ex1_1d9f3a18
    p kyaa "W-wait, you're telling her?! Didn't you just say she'll get mad...?!" with vpunch
    a annoyed "What am I about to get mad at? Were you saying something behind my back?"
    p scream "PERI!!! P-please, I'm innocent!!" with vpunch

    stop music fadeout 3.0

    $ persistent.ex1 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ex2:
    play music audio.pastille fadein 3.0

    scene bg atelierint
    show fg counter
    with fade
    $ quick_menu = True
    n "Periwinkle walks into Atelier Sweets to pick up Pastille for a date. But instead, he's greeted by an enthusiastic golem..."
    show gumdrop yay at righto behind fg
    g "Periwinkle is here! Welcome!!"
    w happy "Gumdrop~ How lovely to see you. I've come to retrieve my boyfriend 💙" id ex2_790fa654
    g smile "Master Pastille is downstairs with Syrup right now! He will return soon if you do not mind waiting."
    w innocent "Certainly~ I'm in no rush."
    g "...."
    w smile "......"
    g "........"
    w calm "You aren't one for small talk, are you, Gumdrop?"
    g oh "Small talk...? Yes, I think talking at a normal volume is best."
    w happy "How funny! Pastille's given you quite the sense of humor."
    g yay "Master Pastille is wonderful! I love him very much."
    w calm "Hmhm, I feel the same 💙" id ex2_53d7b708
    g happy "He is always so happy when he comes back from visiting you. Thank you for always taking care of him!"
    w drool "Ohh, it's my pleasure~! I was hoping to \"take care of him\" tonight as well...."
    g yay "Please do! It is fun to watch his face turn pink, like mine!"
    show pastille work scream at lefta
    p "Gumdrop?! What are you telling him...?!" with vpunch
    g "Yes, pink! Just like that!"
    w innocent "Ahh, there you are, my sweet! Are you ready to spend a lovely evening with me? 💙" id ex2_c3c7c8cb
    p flustered "I can't believe I let this happen... you two should never be allowed to speak to each other unsupervised."
    g oh "Oh! If it is not allowed, I will refrain from greeting him next time."
    w pout "Don't listen to him, Gumdrop. He just doesn't want us trading information."
    w teehee "Please, tell me more about how Pastille acts on the mornings after he's slept over~!"
    p scream "PERI, NO! W-WE'RE LEAVING, RIGHT NOW!!" with vpunch

    stop music fadeout 3.0

    $ persistent.ex2 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ex3:
    play music audio.date fadein 3.0

    scene bg streetday
    with fade
    $ quick_menu = True

    n "Periwinkle and Pastille are out on a date when they run into a familiar face...."

    show cassia oh at rightb
    c "Oh! It's Periwinkle!"
    w date happy "Cassia~! It's been a while, how have you been?"
    c happy "I've been just perfect! Moving in with my partners went really well~!"
    c "Every single night I get to fall asleep while snuggling the both of them 🤎 Ahh~ life really couldn't be better..." id ex3_7a1f6722
    c smile "Anyway, I hope things have been going just as well for you, Periwinkle!"
    w calm "Hmhm, they have indeed! But first, introductions..."
    show pastille date neutral at lefta
    w smile "Pastille, this is Cassia! She's a very sweet and cuddly witch, as you've probably gathered."
    p smile "Nice to meet you."
    w shy "And Cassia, this is my boyfriend, Pastille! Can you believe I've finally settled down~? 💙" id ex3_6f8559b4
    c oh "*gasp* Really...?! I never would've guessed!"
    c happy "But, wow...! I'm so happy for you~! You look so cute together~! 🤎" id ex3_a5ce115b
    w happy "I know, right~? We're a perfect match 💙" id ex3_b75f7932
    c yay "Hehehe~ I'm so glad I don't have to worry about you anymore, Periwinkle~!"
    c letdown "You always used to be so closed off... it made me want to cuddle you lots and lots, so that you didn't feel lonely."
    w ohdear "A-ah, is that how it was...?"
    w oops "(To think her affections were only given out of pity...! Is that why she attempted to pull me into her relationship back then...?)"
    c happy "I'm glad there was someone out there who could open your heart! Good job, Pastille~!"
    p ehe "Haha, it sounds like you tried your best to take care of him. I appreciate it."
    c aww "I really did! But he wouldn't let me in at all~! I had to give up in the end."
    c smile "At least we can be friends now, right Periwinkle~?"
    w guilty "Yes, of course. I apologize for having worried you so."
    c yay "That's okay~! As long as you promise to come over for dinner sometime..."
    c happy "You can bring Pastille, and it'll be like a double date~! Doesn't that sound fun~?"
    w my "A double date...? That certainly does sound like an entertaining night~!"
    w innocent "What do you think, Pastille? Will you accompany me to dinner with Cassia and her partners~?"
    p aw "Yeah, that sounds really nice! I'd love to."
    c "Then it's settled~! I have to get back to my errands, but I'll contact you the next time I'm free, okay~?"
    w happy "Lovely~ 💙 It was nice seeing you again~!" id ex3_f0f464d6

    scene bg streetday
    with fade
    show pastille date think at rightb

    p "...Pink hair...."
    w date oh "Hm~?"
    p shy "Oh, nothing. I just noticed... you kinda have a type, don't you?"
    w love "And what type would that be, exactly?"
    p ehe "Cute and pink."
    w happy "Please, I would say that her hair is closer to white than it is pink!"
    p sure "Sure, sure... still pink, though."
    w shy "Oh, hush... you know you're the only one for me, my sweet."
    p shy "I know ❤ It's just funny." id ex3_54e6cefa
    w pout "Ohh, I see. You only brought it up to make fun of me."
    w whine2 "Honestly, I'M the one who's supposed to tease YOU! How could you turn the tables on me like this, Pastille?"
    p aw "Eheh, sorry. Do you want a kiss?"
    w wow "...!" with vpunch
    w love "Yes, always...!"

    scene bg streetday
    with Dissolve(.2)
    n "Periwinkle cheerfully accepts his apology kiss, and they continue on their way..."

    stop music fadeout 3.0

    $ persistent.ex3 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ex4:
    play music audio.peri fadein 3.0

    $ faveacc = [acc1,acc2,acc3]
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    scene bg bedroomclean
    with fade
    $ quick_menu = True

    n "Pastille is happily organizing Periwinkle's closet... with conscious permission this time."
    show pastille pj neutral at rightc
    p "...Hm? What's in this box?"
    w bed teehee "Ah~ did you find my hidden collection of sex toys? 💙" id ex4_cb20464f
    p sure "No, I'm pretty sure that's not what's in here."
    w pout "Hmph... what a boring reaction. How can you be so sure?"
    p shy "Because if it was, I probably would've known about it by now...."
    w happy "Touché! You would indeed."
    p smile "Can I open it?"
    w neutral "Let's see...."
    scene bg bedroomclean
    show pastille pj smile at righta
    n "Periwinkle rolls out of bed to kneel next to Pastille."
    w decent oh "Ahh, some of my old modeling photos are in here. Along with a few other keepsakes...."
    p oh "Modeling...?"
    w decline "Yes, a rather short-lived career... it wasn't quite what I'd hoped. Being made to look the way someone else wants..."
    w neutral "I'm much happier dressing myself, thank you. I am not some doll."
    w guilty "Er... nothing against other models, of course. It just wasn't for me."
    p neutral "Hm...."
    w smile "You can look through them if you'd like. I only kept the ones I looked best in."
    p anxious "...."
    w love "You've gotten so quiet~ What kinds of naughty photos are you imagining?"
    p omgstop "I-I wasn't! I just didn't want to intrude on your past...!"
    w happy "Intrude all you like! My past, present, and future are all yours for the taking, my sweet 💙" id ex4_231d2a3c
    p seriously "O-okay! I'm looking!!" with vpunch
    scene bg bedroomclean with Dissolve(.2)
    n "Pastille opens the box, and picks up the small stack of photos contained within."
    n "Periwinkle watches over his shoulder as he goes through them..."
    w decent oh2 "(It's been a while since I've seen these... goodness, I look so unhappy in some of them.)"
    show pastille pj neutral at righto
    p "...."
    p shy "C-could I... keep one?"
    w ah "Hm?"
    p embarrassed "Sorry--um, I hope that's not weird to ask! Y-you just look really nice in this one in particular...."
    w oh2 "(Ah... he chose one of the only ones where I actually like what I'm wearing...)"
    w shy "(How did you guess, Pastille...? )"
    w smile "Take it. The rest can be thrown away... I don't need them anymore."
    p wha "Ah... okay."
    p anxious "M-maybe I should take more than one, then...."
    w teehee "If it's more photos you want, I can take sexier ones for you 💙" id ex4_f3c9b293
    p dying "A-AAAAHH!! Nevermind!!!" with vpunch
    p flustered "I'm gonna be too embarrassed to even look at these on my own anyway...! I-it's fine...."
    w love "Ah~ in that case... could I take sexy photos of YOU instead~? 💙" id ex4_3eec19bf
    p scream "N-NOOOOOO....!!!!!" with vpunch

    stop music fadeout 3.0

    $ acc1 = faveacc[0]
    $ acc2 = faveacc[1]
    $ acc3 = faveacc[2]

    $ persistent.ex4 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ex5:
    play music audio.date fadein 3.0

    scene bg streetnight
    with fade
    $ quick_menu = True

    n "Periwinkle takes Pastille out for a night on the town..."
    show pastille witch ehe at rightb
    p "It's been so long since I've been out to any clubs... I hope I won't stand out too much...."
    w date calm "Don't worry, my sweet 💙 If anyone starts hitting on you, I'll come to your rescue." id ex5_e04f40bd
    p ehe2 "A-ah... you're expecting me to need to be rescued...?"
    show cg him at smallcg behind pastille
    show pastille witch oh
    h "Periwinkle~! Glad to see you finally return to the night life!"
    h "Ohh, and you've already picked someone up before even walking into the club? You work faster than ever!"
    w happy "Hmhm, I picked this one up a LONG time ago~ Allow me to introduce you..."
    w love "This is my boyfriend, Pastille! 💙" id ex5_96bcb186
    p woah "H-hello! Nice to meet you...."
    h "Did I hear that right...? Does this mean Periwinkle's taken himself off the market?!"
    w happy "That's correct! I wanted all you gossips to see us together tonight. Start spreading the word 💙" id ex5_aead228f
    p ohno "W-wait, is that really why you invited me out...?"
    w calm "A secondary gain, my sweet. You should've known I'd want to show you off."
    p flustered "P-Peri...!"
    h "What a cute pick... any chance you'd consider an open relationship? 💙" id ex5_e459db29
    w pout "Absolutely not! I refuse to share."
    p wow "...."
    h "You sure~? He looks like he might want to."
    w my "Pastille...?"
    p dying "N-no! It's not that... I'm just...." with vpunch
    p ehe2 "Flattered... I guess?"
    p seriously "B-but still--no thank you...!"
    w teehee "See~? We aren't the polyamorous type at all. You never stood a chance."
    h "Hahaha, well congrats to the happy couple! I'm headed inside, so see you around~!"
    w innocent "Farewell~! 💙" id ex5_3196ae5f
    scene bg streetnight
    show pastille witch neutral at righta
    with fade
    p "...."
    w date decline "...Perhaps that single interaction was enough to accomplish my goal. We can return home if you'd like."
    p shy "Are you sure? You're not just saying that cuz you got a little jealous...?"
    w pout "Nonsense, I have nothing to feel jealous over."
    p ehe "You're pouting, though...."
    w innocent "I'm not! Why bother with the clubs, hm? Too many prowling singles. I shouldn't taunt them with my perfect catch."
    w drool "Let's return home after all... I want you aaall to myself tonight 💙" id ex5_ccbc56bc
    p omgstop "See, you DID get jealous...! You're being extra possessive...!!"
    w happy "Nooo~ I just figured, why tire ourselves out on a dance floor when we could go straight to tiring ourselves out in bed? 💙" id ex5_2dc4b778
    p scream "P-PERI...!!!" with vpunch

    stop music fadeout 3.0

    $ persistent.ex5 = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return

label ch7b:
    play music audio.finale fadein 3.0

    $ faveacc = [acc1,acc2,acc3]
    $ acc1 = 0
    $ acc2 = 0
    $ acc3 = 0

    scene bg bedroomcleandark
    with fade
    $ quick_menu = True

    n "That night, the two of them lay in bed together, wrapped comfortably in each other's arms..."

    show cg ending3 at cgspan
    w bed "...Say it again."
    p "I love you."
    w shy "Nn~~! 💙" with vpunch id ch7b_bd152a55
    n "Periwinkle hugs him tighter each time, before pulling back to ask for more."
    w love "Again!"
    p "I love you ❤" id ch7b_b69db97b
    w kyaa2 "Mnmmnnnn~~~~~!! 💙" with vpunch id ch7b_4972286e
    n "He snuggles up to him as close as he possibly can."
    w yay "...Once more?"
    n "Pastille whispers it in his ear this time."
    p "I love you."
    w kyaa "AHHH~~~~~~~~~~~~~~~!!!!! 💙 💙 💙" with vpunch id ch7b_0bc9a5df
    p "Haha, you can't get enough, can you?"
    w love "How can I? This is my ultimate fantasy...!"
    n "Pastille kisses his forehead."
    p "You're so cute...."
    w shy "Hmhmhmhm~! I love you, Pastille 💙" id ch7b_1429fa32
    p "I love you, too!"
    w kyaa "Ahhhh~~~! 💙 Again, again~!" with vpunch id ch7b_5c209a50

    scene bg bedroomcleandark with Dissolve(.2)
    n "This embarrassing display continued through the night, only stopping once Periwinkle fell asleep in Pastille's arms...."

    stop music fadeout 3.0

    $ acc1 = faveacc[0]
    $ acc2 = faveacc[1]
    $ acc3 = faveacc[2]

    $ persistent.ch7b = True
    $ quick_menu = False
    scene black with Fade(1,.5,0)
    return
