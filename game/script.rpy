define character.y = Character("Me")
define y.playerType = 0
define y.playerName = ""

default preferences.text_cps = 30
define gui.text_font = "fonts/Misty Style.ttf"

# variable
default startBattleState = True

# init input
# we will check if we just started the input
init python:
    
    def ashenleaf_bleep(event, **kwargs):
        if event == "show":
            d2 = renpy.random.randint(1,4)
            if d2 == 1:
                renpy.music.play("Dialogue/Ashenleaf 2/DolaVonde_dialogue_ASHENLEAF_2_DS-1.ogg", channel="sound", loop=True)
            elif d2 == 2:
                renpy.music.play("Dialogue/Ashenleaf 2/DolaVonde_dialogue_ASHENLEAF_2_DS-2.ogg", channel="sound", loop=True)
            elif d2 == 3:
                renpy.music.play("Dialogue/Ashenleaf 2/DolaVonde_dialogue_ASHENLEAF_2_DS-3.ogg", channel="sound", loop=True)
            elif d2 == 4:
                renpy.music.play("Dialogue/Ashenleaf 2/DolaVonde_dialogue_ASHENLEAF_2_DS-4.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound" ,fadeout=0.15)
    
    def hapil_bleep(event, **kwargs):
        if event == "show":
            d2 = renpy.random.randint(1,3)
            if d2 == 1:
                renpy.music.play("Dialogue/Hapil/DolaVonde_dialogue_HAPIL DS-1.ogg", channel="sound", loop=True)
            elif d2 == 2:
                renpy.music.play("Dialogue/Hapil/DolaVonde_dialogue_HAPIL DS-2.ogg", channel="sound", loop=True)
            elif d2 == 3:
                renpy.music.play("Dialogue/Hapil/DolaVonde_dialogue_HAPIL DS-3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound" ,fadeout=0.15)

    def pumpell_bleep(event, **kwargs):
        if event == "show":
            d2 = renpy.random.randint(1,3)
            if d2 == 1:
                renpy.music.play("Dialogue/Pumpell/DolaVonde_dialogue_PUMPELL-DS-1.ogg", channel="sound", loop=True)
            elif d2 == 2:
                renpy.music.play("Dialogue/Pumpell/DolaVonde_dialogue_PUMPELL-DS-2.ogg", channel="sound", loop=True)
            elif d2 == 3:
                renpy.music.play("Dialogue/Pumpell/DolaVonde_dialogue_PUMPELL-DS-3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound" ,fadeout=0.15)

    def lowtront_bleep(event, **kwargs):
        if event == "show":
            d2 = renpy.random.randint(1,3)
            if d2 == 1:
                renpy.music.play("Dialogue/Lowtront/DolaVonde_dialogue_LOWTRONT DS-1.ogg", channel="sound", loop=True)
            elif d2 == 2:
                renpy.music.play("Dialogue/Lowtront/DolaVonde_dialogue_LOWTRONT DS-2.ogg", channel="sound", loop=True)
            elif d2 == 3:
                renpy.music.play("Dialogue/Lowtront/DolaVonde_dialogue_LOWTRONT DS-3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound" ,fadeout=0.15)

    # global variable where we store the inputText for the text in the attack/defend menu -> accessible everywhere as long as we do globals()['variable']
    globals()['textNotes'] = "Notes : "

    # append a list to text
    def returnTextByList(list):
        text = "Notes : "
        for x in list: 
            text += x + " "
        #print("dans la def returnTextByList : " +  text)
        return text
        
    # add item to list, not used because I saw that renpy already do this
    def addKeyToList(key, list):
        list.append(key)
        return list

    # debug purposes
    def printList(list):
        text = ""
        for i in list: 
            text += i + " "
        #print(text)

# characters

# i define it but really not sure if we are going to use it
define o = Character("Organizer",callback=lowtront_bleep)
define n = Character("Narrator")
define g = Character("Guardian")
define e = Character("Elder")

define a = Character("Ashenleaf", callback=ashenleaf_bleep)
define p = Character("Pumpell plum", callback=pumpell_bleep)
define h = Character("Hapil", callback=hapil_bleep)
define l = Character("Lowtront glow", callback=lowtront_bleep)

define character.t1 = Character("Trainer 1")
define ht = Character("Hapil Trainer", callback=hapil_bleep)
define pt = Character("Pumpell Plum Trainer")

define l1 = Character("Rivil", callback=pumpell_bleep)
define l2 = Character("Lerea", callback=pumpell_bleep)

define la = Character("Laverie", callback=lowtront_bleep)


# transform for the characters
transform bouncein:
        linear .2 alpha 0.6 xpos 600 ypos -800
        linear .2 alpha 1   xpos 350 ypos -200
        linear .2           xpos 0 ypos 100
        linear .3           xpos 10 ypos 0

transform breath:
    linear 1 xalign 0.4 
    linear 1 xalign 0.6
    repeat 

transform breath2:
    linear 1 ypos -10 
    linear 1
    linear 1 ypos 0   
    repeat 

transform shake:
    linear .1 xpos 2 
    linear .1 xpos 0 
    linear .1 xpos 4 
    linear .1 xpos 0   
    repeat   

transform shakemore:
    linear .05 xpos -4 
    linear .05 xpos 0   
    linear .05 xpos 4
    linear .05 xpos -4
    #linear .1 xpos 6  
    repeat  


# start of game
label start:

    $ attention_ennemy = 100
    $ attention_player = 100
    $ max_attention = 100
    $ playerName = ""
    $ urTurn = False
    $ begin = True

    # this variable is just so that the program know what battle we are in
    $ battleState = 0

    # type depend on which leafling we are :
    # type = 0 => Ashenleaf
    # type = 1 => PumpellPlum
    # type = 2 => Hapil
    # type = 3 => LowtrontGlow
    $ playerType = 0

    jump intro
    #jump battlePrototype
    return



# ----------------------
# Introduction
# ----------------------
label intro:
    scene black
    centered "Introduction..."
    play music "audio/Music/Main theme/Leaflings theme.ogg" loop

    o "Hmm..."
    o "This won't do"

    # fade image that represents the organizer sitting at the desk

    o "This time next spring the arch will still not have bloomed..."
    o "And Guardian will have to move on. \n\nI have to do something!"

    # fade image that represents the organizer writing at desk
    o "And I'm writing to the sweet villagers of the Hapil, we'd love to invite your fun ways..."
    o "A first of hopefully many events!"
    o "If you can spare one... or two of the Ashenleaf, we can find a way to show their unique skills."
    o "It's about time we get to celebrate some Ashenleaf Voices."
    o "The songs of Pumpell Plums always have a place in our hearts, as they've been the ones to start our tradition."
    o "We hope to hear voices here!"
    o "I can still remember the first time I heard the voice from those on the path of the Lowtront Glow..."
    o "When I was a child the first song I heard haunted me for years... in a good way! Come by!"

    # maybe fade agin on the organizer sitting at the desk
    o "Now then, I just need to get these letters out once-"
    o "Oh ! It's already this late ! \n\nI must hurry !"

    jump sc1_1



# ----------------------
# Scene 1
# ----------------------

# act 1
label sc1_1:
    # fade to the the mc receiving the letter
    # maybe need some more informations on this ?
    # I add the character saying something like "Oh" to make the scene last
    y "Oh..."
    jump sc1_2_1

# act 2.1
label sc1_2_1:
    # need some more information on how we introduce the characters, the ceremony, and the story

    # fade to the day of the opening ceremony, leaflings surround the archway
    
    # leafling 1 = Rivil
    # leafling 2 = Lerea

    # scene change to the arch, without the guaardian.
    scene archway
    play music "audio/Music/Main theme/Leaflings theme.ogg" loop volume 0.1

    show npc_3:
        xalign 0.3
        yalign 1.0
    show npc_4:
        yalign 1.0
        xalign 0.7

    l2 "What's it say?"

    l1 "It's an invitation! To visit the ceremony of the Waving Arch!"
    l1 "..."
    l1 "It's a really bad drawing... is this supposed to be the ceremony?"

    l2 "Aw, well they didn't shine in creative lessons. But you've been, right? You know how mystical the event is."
    l1 "Well, no... It's been years since they've been popular, and I just chose my path, I never had a chance before!"

    l2 "Well, you'll go now right? You have to!"
    l1 "Maybe if the invitation was clearer..."
    l2 "Well it just is! Let's imagine it!"

    scene black 

    "It's a grand, beautiful time. It makes you feel rooted, makes you hear the songs of our ancestors."
    "We carry the tradition of our songs to rouse all the myst we have, and through our voices and songs it's gathered at a specific point."
    
    scene archway

    show npc_3:
        xalign 0.3
        yalign 1.0
    show npc_4:
        yalign 1.0
        xalign 0.7

    l1 "You're telling me that squiggle is an arch?"
    l2 "Imagine."
    l2 "The traditional melody is played, and all the Leaflings know the words."
    l2 "You know how we say we were singing before we could speak? This is the way to go about it."

    l1 "I'm surprised I never saw one, as a kid at the least..."
    l2 "Well that's the thing! You have to be on a path, because they are not supposed to be seen."
    l1 "Who's not?"
    l2 "The Guardian."
    l1 "Who's the guardian?"
    l2 "The Guardian of the Arch!"
    
    l1 "Oooh."
    l2 "Yeah."

    # fade to the leaflings traveling through the forest

    l2 "So anyways, the Guardian of the Arch is not meant to be seen, and well, no one really knows why."
    l2 "To preserve their myst?"
    l2 "To keep their focus on the arch itself and keep it's myst pristine and safe?"
    l2 "To hide that they're immensely shy?"
    l2 "So when the ceremony starts, the guardian does their thing, they sing. It's pretty right?"
    l2 "And then the choir of leaflings sing begin them. The path that started this were the Pumpell Plums. Those leaflings will and perhaps always will be the most skilled at the ceremony."
    l2 "It's a classic to hear them."
    l2 "It took a while, and well, leaflings of the Lowtront Glow path have been allowed to join."
    l2 "It was very, what's the word, unusual to see the Lowtront Glow leaves after it being solely the ugardian and Pumpell Plums before this."
    l2 "It was never the same, but it was better."

    l1 "Wait, they made it better?"
    l1 "The Leaflings on the Lowtront Glow path? Don't they just stay in their caves all day and stare at their glowy gardens at night?"
    l2 "Probably."
    l2 "But I guess the mystical voices of the Pumpell Pluma and Lowtront Glow just... made it better."
    l1 "Well, I see the colors on this figure that must be the Pumpell here... those light pastels... and the Lowtront are all greend and glowy... what are those other figures?"
    l2 "Hm? Oh... The red and spiky, and this other colorful one..."

    l2 "Wait..."
    l1 "It says here..."
    l2 "Oh no... Don't tell me..."
    l1 "Those on the path of the Ashenleaf and Hapil Paths are welcolme to join in at this year's revival ceremony."
    l2 "THis is..."
    l1 "Wonderful, and incluse?"
    l2 "Terrible! Another rift ammong Leaaflings!"
    l1 "Wheren't you just the one saying the better with more Paths?"
    l2 "Well..."
    l1 "Oh look! That must be the guardian!"
    l2 "Oh wow!"
    l2 "Maybe it's time for the big annoucement!"
    jump sc1_2_3

label sc1_2_3:

    scene archway
    show guardian arch at center
    g "..."

    "Someone bumps into you"
    
    show laverie woah at center

    la "Oh! I'm so sorry! Are you okay?"

    show laverie smile at breath
    la "I'm Laverie, I'm a bit rushed today, aha!"
    la "You must be one of the Leaflings preparing to sing, what was your name?"

    show laverie hmm at center

    call screen characterSelection

# images related to the button, it's ugly for the moment, we need to take time to make correct buttons
# also I do this to resize the image, thoses weird numbers is just the width and height of each image times 0.8
image ashenleafButtonIdle = im.Scale("ashenleaf default.png", 343.2, 778.4)
image PumpellPlumButtonIdle = im.Scale("PumpellPlum default.png", 375.2, 698.4)
image hapilButtonIdle = im.Scale("hapil default.png", 348, 752)
image lowtrontGlowButtonIdle = im.Scale("LowtrontGlow default.png", 267.2, 734.4)

# character Selection screen
screen characterSelection:
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 40

        # ashenleaf button
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "ashenleafButtonIdle" action [SetVariable("playerType", 0), SetVariable("playerName", "Ahele"), Jump("nameAshenleafChoices")]

        # pumpell plum
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "PumpellPlumButtonIdle" action [SetVariable("playerType", 1), SetVariable("playerName", "Melulu"), Jump("namePumpellPlumChoices")]

        # hapil
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "hapilButtonIdle" action [SetVariable("playerType", 2), SetVariable("playerName", "Pali"), Jump("nameHapilChoices")]

        # lowtront glow
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "lowtrontGlowButtonIdle" action [SetVariable("playerType", 3), SetVariable("playerName", "Wotto"), Jump("nameLowtrontGlowChoices")]

# important to remove and replace !!!!!!!!!!!!

# choices for name
# for ashenleaf
menu nameAshenleafChoices:
    "Your name is Ahele and you choose the Ashenleaf Path. Are you sure?"

    "Yes":
        jump sc1_2_4
    "No":
        call screen characterSelection
# for Pumpell Plum
menu namePumpellPlumChoices:
    "Your name is Melulu and you choose the Pumpell Plum Path. Are you sure?"

    "Yes":
        jump sc1_2_4
    "No":
        call screen characterSelection
# for Hapil
menu nameHapilChoices:
    "Your name is Pali and you choose the Hapil Path. Are you sure?"

    "Yes":
        jump sc1_2_4
    "No":
        call screen characterSelection
# for Lowtront Glow
menu nameLowtrontGlowChoices:
    "Your name is Wotto and you choose the Lowtront Glow Path. Are you sure?"

    "Yes":
        jump sc1_2_4
    "No":
        call screen characterSelection


label sc1_2_4:

    show laverie hmm:
        xalign 0.7
        yalign 1.0

    if playerType == 0:
        show pc3 grr: 
            xalign 0.3 
            yalign 1.0
        a "Woah! You trying to knock me away?"
    elif playerType == 1:
        show pc4 grr: 
            xalign 0.3 
            yalign 1.0
        p "My, you're just trying to flow through this crowd, aren't you?"
    elif playerType == 2:
        show pc1 aw: 
            xalign 0.3 
            yalign 1.0
        h "Oh no, I'm sorry! Are you okay? I hope you're okay!"
    elif playerType == 3:
        show pc2 gr: 
            xalign 0.3 
            yalign 1.0
        l "Ah. It's... okay."

    la "Oh, [playerName]? I recognize that name. And now I know your face! I'm not the best at remembering some things, but I never forget a face!"

    show npc_3:
        xalign 0.1
        yalign 1.0
    show npc_4:
        yalign 1.0
        xalign 0.2

    l1 "Hey, why isn't the Guardian saying anything?"
    l1 "Isn't there supposed to be something happening?"

    hide npc_3
    hide npc_4

    la "Oh! I'm sorry [playerName], I have to go. Did I mention I'm the Organizer of this event? I have to talk to everyone, please excuse me!"

    if playerType == 0:
        hide pc3
    elif playerType == 1:
        hide pc4
    elif playerType == 2:
        hide pc1
    elif playerType == 3:
        hide pc2

    show laverie woo:
        xalign 0.3
        yalign 1.0
    show guardian center:
        yalign 1.0
        xalign 0.7

    # make her wiggle through the crowd and make it jiggle on the stage
    la "Welcome everyone! Thank you all so much for coming to the first annual ceremony for the Waving Arch!"
    la "This is the Guardian of the Arch! We thank you for welcoming us here Guardian!"

    la "My name is Laverie, and I'm the organizer of this event as a whole, so don't be afraid to come to me with questions!"
    la "But, uh, hopefully I'll answer a lot of you questions right now, before you have them. Ahem!"

    la "Thank you all for being here!"
    la "I love seeing all your little leafy and petal-y faces, I'm excited for what we have planned."
    la "Me and the Guardian of the Arch are very excited."

    show guardian close:
        yalign 1.0
        xalign 0.7
    g "..."

    la "That was a nod!"
    la "Now!\n\nI do wonder who's been to a ceremony like this before?"
    la "Our newest Guardian here as been working hard to maintain this arch and it's pearls."

    show guardian left
    g "..."

    la "With all their hard work, we as a community need to come back together to aid our Guardian!"
    la "This ceremony we will hold will be for the pearls of..."
    la "Um, the pearls of... \n\nWe want to..."

    show guardian right

    la "I'm sorry Guardian, what were these pearls holding?"

    show guardian center
    la "..."
    la "Violet seeds..."

    la "Oh yes! Right!"
    la "Help us hold and revive the violet seeds!"

    show guardian close
    la "A rather mysterious pearl we've come across holding the violet seeds, we know so little about them, and we need your help to make them bloom."
    la  "But yes, whose ready to help these bloom!"

    l1 "Wait, how do we help them bloom?"
    l2 "Yeah I don't really know how it works, do you?"
    l1 "Nope."
    l1 "Honestly, it looks like no one else around us does either!"

    la "Er, well..."
    la "That was were you all were supposed to cheer and sing a little bit..."
    la "But that's okay! \n\nI guess I should have explained things a bit..."

    la "Our voices are what will be the mystical force that will be collected into this pearl."
    la "Our guardian will place it in the arch, way up high in one of those spots up here."
    la "Collectively, our voices, with the songs, that for centuries, has given arches like these all around the mystical power make seeds like this, bloom to us leaflings!"
    la "It will grow and diversify our forest, and make us all the happier!"

    la "Though participation in this ceremony is ultimately not a competition, I thoguht it would be fun to add a little layer of sport to the whole thing!"
    la "So, at the end of it all, when the — if, hopefully, but, when the arch blooms, the best singers will be given a fantastic prize!"

    la "Oh I forgot to — I'll announce it in a second, nevermind. You'll learn four songs, each chosen by those of different paths, symbolizing unity and growth!"
    la "To that end, there will be song trainers in each village to help you learn the song of their path."
    la "They've each bee ngiven a red banner, so make sure to look for them!"
    la "And um— please don't put up a red banner if you're not a trainer"
    la "I didn't tell anyone not to, so it might confuse the participants if you do."

    la "If you're here, thank you! Thank you so much again for being here!"
    la "Those who wish to watch, please feel free to stay and enjoy the hospitality of the Hapil!"
    la "I can't wait to meet you all! Best of luck!"

    jump sc4_1

# ----------------------
# Scene 2
# ----------------------



# ----------------------
# Scene 3
# 
# New day, and this is where we are going to do the tutorial with the first trainer, more of a tutorial than anything else
# ----------------------
label sc3_1:
    scene black
    centered "End of the intro"
    centered "Day 1"

    # will change just for debug purpose
    t1 "Hey I will train you"
    jump first_battle

label first_battle:

    $ battleState = 1
    jump battles_hub

label first_battle_Hub_Player:
    $ urTurn = False
    jump first_battle

label firstBattleLose:
    t1 "Maybe next time!!"
    jump sc4_1

label firstBattleWin:
    t1 "Good job!!"
    jump sc4_1



# ----------------------
# Scene 4
#
# first real battle
# ----------------------
label sc4_1:
    scene black
    centered "End of the intro"
    centered "Day 1"

    scene hapil village2

    # fade to the meeting room

    show laverie hmm at center
    la "Oh, OH, I forgot!!"
    show laverie close at center
    la "So everyone, you will be paired with someone!"
    show laverie woah at center
    "Everyone" "WHAT?!"
    hide laverie

    # fade to hapil village
    if playerType == 0:
        show pc1 smile:
            xalign 0.7
            yalign 1.0
        show pc3 grr:
            yalign 1.0
            xalign 0.3
        a "(Argh, of course I got paired with a hapil...)"
        a "(She seems like way, wayyyyy too much of a morning person.)"
        a "(But there could be worse people to pair up with.)"
        h "Hello !!"
        a "...Sup."

    if playerType == 2:        
        
        show pc1 aw:
            xalign 0.3
            yalign 1.0
        show pc3 grr:
            yalign 1.0
            xalign 0.7
        h "(Oh boy, he looks... angry)"
        h "(Are we sure this is right leaf to pair me with...?)"
        h "(Well. Well ! Nothing to do about it but make a good first impression!)"
        show pc1 smile
        h "Hello !!"
        a "...Sup."

    # ashenleaf and hapil
    if playerType == 0 or playerType == 2: 
        # we need to show both characters here I think
        h "So we're partners, I guess!!"

        # need information on his name + the daredevil thing
        h "Good to meet you ! My name's Pali and I like branch diving and bracelet-making and singing, and I'm super excited to join chorus!"
        show pc3 uh
        a "Yeah, I heard-, wait, you like the branch diving?!"
        show pc1 hehe
        h "For sure!!"
        show pc3 yeah
        a "Have you been to the red leaf sea? They have, like, the most extreme dives, it's my favorite place to go."
        h "Ooh, not yet. All the places I travel to are local."
        a "You gotta go out there. I did a half-branchslide down a chip into a ghost flip -- impossible to do without the speed you get from the locale."
        show pc1 oh
        h "A... What flip now?"
        a "Y'know, a-- OH wait right we have to go learn whatever song they want us to learn. I'm Ahele, also."
        h "Okay! Cool!!"
        show pc3 what
        a "If you ask me, it's stupid, not cool. They invited us, they should let us do our own thing!!"
        show pc3 yeah
        a "But hey fine, whatever, we gotta do the doo-doo-doo song."
        show pc1 smile
        a "Aw but it's a lovely doo doo doo. C'mon!"
        jump second_battle_trainer

    # pumpell plum and lowtront glow
    elif playerType == 1 or playerType == 3:

        show pc2 gr:
            xalign 0.3
            yalign 1.0
        show pc4 smile:
            yalign 1.0
            xalign 0.7

        p "Come on now, we will be partners."
        l "Oh, but I didn't... okay?"
        p "Your name Wotto, right?"
        show pc2 heh
        l "Yes that's me."
        p "Perfect. My name is Melulu. I've heard through the grapevine you have a beautiful voice, which is a blessing blessing for us traditional singers."
        p "Once they hear us hitting the notes ever-so flawlessly, they'll be be so impressed by our radiance they'll just give up on the spot!"
        l "O-oh! Um, thank you! But, maybe we should... learn how to sing, first..."
        p "Absolutely right. Though, I'm sure it won't be much of a feat. To the trainer, then."
        jump second_battle_trainer

# for this part I will need way more informations on how to setup it
label second_battle_trainer:
    # all related to the trainer battle
    if playerType == 0 or playerType == 2:
        show pc1 smile:
            xalign 0.1
            yalign 1.0
        show pc3 yeah:
            yalign 1.0
            xalign 0.3

    if playerType == 1 or playerType == 3:
        show pc2 gr:
            xalign 0.1
            yalign 1.0
        show pc4 smile:
            yalign 1.0
            xalign 0.3

    show hapiltrain close:
        yalign 1.0
        xalign 0.8

    ht "Goooooooood morning everyone!!"
    ht "It's the first battle and I know that working with someone that is not necessary in your path can be complicated."
    ht "And I will try my best to teach you everything so that you can perform the best in front of the organizer."
    ht "Let's start right now !"

    "You will start the tutorial, the four inputs of the game are the keys : Q, W, E, and R."
    "When you will attack for the first time, try to do the sequence QWER"

    $ battleState = 2
    play music "audio/Music/Battle themes/Modern/Hapil/Modern - Hapil battle.ogg" loop
    jump battles_hub

label after_trainer:
    play music "audio/Music/Main theme/Leaflings theme.ogg" loop
    ht "Good job both! I think you're ready."
    
    if playerType == 0 or playerType == 2:
        ht "Your first opponent will be a duo of Pumpell Plum and Lowtront Glow."
        ht "Good luck!"
        jump third_battle
    else:
        ht "Your first opponent will be a duo of Ashenleaf and Hapil."
        ht "Good luck!"
        jump third_battle

label third_battle:
    # all related to the first big battle
    hide hapiltrain

    if playerType == 0 or playerType == 2:
        show pc2 gr:
            xalign 0.7
            yalign 1.0
        show pc4 smile:
            yalign 1.0
            xalign 0.9


    if playerType == 1 or playerType == 3:
        show pc1 smile:
            xalign 0.7
            yalign 1.0
        show pc3 yeah:
            yalign 1.0
            xalign 0.9

    $ battleState = 3
    $ attention_ennemy = 100
    $ attention_player = 100
    $ begin = True
    play music "audio/Music/Battle themes/Modern/Hapil/Modern - Hapil battle.ogg" loop
    jump battles_hub

label sc4_3_Win:
    ht "Wonderful, wonderful job !!"

    if playerType == 0 or playerType == 2:
        show pc1 boo
        h "Yyyes! That was so fun!!"
        # ?????? dont understand leafling stand in for cake
        a "YEAH!! See, what'd I tell ya ! Piece of hapil! I mearn... uh."
        show pc3 uh
        show pc1 smile
        h "Ah, don't worry about it. I hear that all the time."

        show pc3 yeah
        a "Aright. Cool"
        show pc1 hehe
        h "So, where to next? Lead the way, partner."
        a "Laverie! If we finished first, we can totally brag about it."
        jump sc4_4
    
    if playerType == 1 or playerType == 3:

        show pc4 heh
        p "There! Nothing less than perfection. Just like I knew it would be."

        # lowtront blushing
        show pc2 ha
        l "Yeah... yeah."
        show pc2 heh
        show pc4 smile
        p "Let's go then. Onto learning the next song!!"
        jump sc4_4

label sc4_3_Lose:
    if playerType == 0 or playerType == 2:
        show pc1 boo
        h "Whoa! Haha, that went well!"
        show pc3 no
        a "Aaagh, no it didn't! What did I tell you? This whole thing is stupid."
        show pc1 uh
        h "Aw, I guess it didn't. Could we try again?"
        show pc3 grr
        a "No way. Let's keep this one to ourselves."
        jump sc4_4
    
    if playerType == 1 or playerType == 3:
        show pc4 no
        p "Oh, dear. That needs some... work."
        show pc2 umm
        l "Mmm..."
        jump sc4_4
    
label sc4_4: 

    # we fade to the pumpell village, with the organizer that sends here

    scene black
    centered "End day 1 (and demo !)"
    jump endGame

# ----------------------
# All related to the battles
# ----------------------
label battles_hub:

    # here we choose randomly whose turn gonna be
    # actually, I will do one chance out of three, so the player will have more chance to begin, it will be more fun
    # 1 = ennemy turn
    # 3 and 2 = our turn
    $ d3 = renpy.random.randint(1, 3)

    if battleState == 1:

        if begin == True :

            # screen that show the attention bars on right and left
            show screen attentionBars

            if d3 == 1:
                $ urTurn = False
                $ begin = False
            else:
                $ urTurn = True
                $ begin = False

        # all related to our turn !
        if urTurn == True:
            centered "Our turn !"

            if attention_ennemy <= 0:
                hide screen attentionBars
                jump firstBattleWin
            else:
                call screen battleMenu
        else: 
            # all related to the opponent turn !
            centered "Trainer turn !"

            if attention_player >= 66:

                if d3 == 1:
                    t1 "Haha"
                    $ attention_player -= 15
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    t1 "Try some new sequences like Q W E R"
                    $ attention_player -= 23
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    t1 "A little bit more !!"
                    $ attention_player -= 15
                    $ urTurn = True
                    jump battles_hub

            elif 33 <= attention_player < 66:

                if d3 == 1:
                    t1 "You're making some progress !!"
                    $ attention_player -= 12
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    t1 "Continue like that !!"
                    $ attention_player -= 23
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    t1 "Try the sequence E W Q W E"
                    $ attention_player -= 17
                    $ urTurn = True
                    jump battles_hub

            elif 0 < attention_player < 33:

                if d3 == 1:
                    t1 "Almost there !!"
                    $ attention_player -= 9
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 2:
                    t1 "In sync !"
                    $ attention_player -= 14
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 3:
                    t1 "Try the sequence R Q Q R E E !"
                    $ attention_player -= 16
                    $ urTurn = True
                    jump battles_hub

            elif attention_player <= 0:
                hide screen attentionBars
                jump firstBattleLose

    if battleState == 2:

        if begin == True :

            # screen that show the attention bars on right and left
            show screen attentionBars

            if d3 == 1:
                $ urTurn = False
                $ begin = False
            else:
                $ urTurn = True
                $ begin = False

        # all related to our turn !
        if urTurn == True:
            centered "Our turn !"

            if attention_ennemy <= 0:
                hide screen attentionBars
                jump after_trainer
            else:
                call screen battleMenu
        else: 
            # all related to the opponent turn !
            centered "Trainer turn !"

            if attention_player >= 66:

                if d3 == 1:
                    $ attention_player -= 15
                    ht "This song is very special, try the sequence QWER."
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    $ attention_player -= 23
                    if playerType == 0 or playerType == 2:
                        show pc3 grr
                        a "Urgh, where'd this song come from, the ancients?"
                        show hapiltrain open
                        ht "Yes them!"
                        show hapiltrain close
                    if playerType == 1 or playerType == 3:
                        show pc4 heh
                        l "Mmm... I've heard this song before, but never this in two parts..."
                        show hapiltrain close
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    $ attention_player -= 15
                    ht "A little bit more!!"
                    $ urTurn = True
                    jump battles_hub

            elif 33 <= attention_player < 66:

                if d3 == 1:
                    $ attention_player -= 12
                    ht "You're making some progress!! Maybe try the sequence RQQREE"
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    $ attention_player -= 23
                    if playerType == 0 or playerType == 2:
                        show pc3 grr
                        a "We could make it better by doing... Literally anything else."
                    if playerType == 1 or playerType == 3:
                        show pc2 gr
                        p "It doesn't sound too difficult, just remember that you must breathe in between the low C and high A."
                        p "Or your voice may slide, and minor difference as it is, that's not how it's supposed to sound."
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    $ attention_player -= 17
                    ht "You need to reajust, that's not quite it!"
                    $ urTurn = True
                    jump battles_hub

            elif 0 < attention_player < 33:

                if d3 == 1:
                    $ attention_player -= 9
                    ht "Almost there!!"
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 2:
                    $ attention_player -= 14
                    if playerType == 0 or playerType == 2:
                        show pc1 uh
                        h "It seems important to them..."
                        show pc3 yeah
                        a "Whatever. I'm gonna freestyle it."
                        show pc1 smile
                        h "O-okay. I'll try to hhelp, but we have to stay on the melody"
                    if playerType == 1 or playerType == 3:
                        show pc4 grr
                        p "And remember this note here is a G flat, not an F sharp. And this measure has two rests, unlike the typical one."
                        p "Have tou gotten all that?"                        
                        show pc2 umm
                        l "...Uh. I dont know if I can..."
                        p "Good! Let us perform!"
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 3:
                    $ attention_player -= 16
                    ht "You can try the last sequence EWQWE!"
                    $ urTurn = True
                    jump battles_hub

            elif attention_player <= 0:
                hide screen attentionBars
                jump after_trainer

    if battleState == 3:

        if begin == True :

            # screen that show the attention bars on right and left
            show screen attentionBars

            if d3 == 1:
                $ urTurn = False
                $ begin = False
            else:
                $ urTurn = True
                $ begin = False

        # all related to our turn !
        if urTurn == True:
            centered "Our turn !"

            if attention_ennemy <= 0:
                hide screen attentionBars
                jump sc4_3_Win
            else:
                call screen battleMenu
        else: 
            # all related to the opponent turn !
            centered "Opponent turn !"

            if attention_player >= 66:

                if d3 == 1:
                    $ attention_player -= 15                    
                    if playerType == 0 or playerType == 2:
                        show pc3 grr
                        a "Let's continue!!"
                    if playerType == 1 or playerType == 3:
                        show pc4 heh
                        l "Like this!"
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    $ attention_player -= 23
                    if playerType == 0 or playerType == 2:
                        show pc1 hehe
                        h "We're doing right!!"
                    if playerType == 1 or playerType == 3:
                        show pc4 heh
                        p "Not like this..."
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    $ attention_player -= 15                    
                    if playerType == 0 or playerType == 2:
                        show pc1 hehe
                        h "It's just the beginning"
                    if playerType == 1 or playerType == 3:
                        show pc4 heh
                        p "They're not serious at all..."
                    $ urTurn = True
                    jump battles_hub

            elif 33 <= attention_player < 66:

                if d3 == 1:
                    $ attention_player -= 12                    
                    if playerType == 0 or playerType == 2:
                        show pc1 aw
                        h "We're doing good!"
                    if playerType == 1 or playerType == 3:
                        show pc4 heh
                        l "Like in the training!"
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 2:
                    $ attention_player -= 23
                    if playerType == 0 or playerType == 2:
                        a "Even if this is stupid, let's do everything them!"
                    if playerType == 1 or playerType == 3:
                        p "Don't forget breathe between the low C and the high A."
                    $ urTurn = True
                    jump battles_hub

                elif d3 == 3:
                    $ attention_player -= 17
                    if playerType == 0 or playerType == 2:
                        show pc3 grr
                        h "Don't forget the sequence EQQERR"
                    if playerType == 1 or playerType == 3:
                        show pc2 gr
                        p "Don't forget the sequence EQQERR."
                    $ urTurn = True
                    jump battles_hub

            elif 0 < attention_player < 33:

                if d3 == 1:
                    $ attention_player -= 9
                    if playerType == 0 or playerType == 2:
                        h "It's the complicated part, but we have to stay in the melody!"
                    if playerType == 1 or playerType == 3:
                        l "I don't know if-"
                        p "It's not the moment!"
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 2:
                    $ attention_player -= 14
                    if playerType == 0 or playerType == 2:
                        h "You're in a complete freestyle!"
                        a "Yeah I know, but we will destroy them."
                    if playerType == 1 or playerType == 3:
                        p "We're almost finished!"
                    $ urTurn = True
                    jump battles_hub
                
                elif d3 == 3:
                    $ attention_player -= 16
                    if playerType == 0 or playerType == 2:
                        show pc3 grr
                        h "Don't forget the sequence EWQWE"
                    if playerType == 1 or playerType == 3:
                        show pc2 gr
                        p "Don't forget the sequence EWQWE."
                    $ urTurn = True
                    jump battles_hub

            elif attention_player <= 0:
                hide screen attentionBars
                jump sc4_3_Lose

label player_hub:
    $ urTurn = False
    jump battles_hub

# all labels about camera
label attack:
    camera:
        ease 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-333.0, 288.0, 612.0)*RotateMatrix(0.0, 0.0, -4.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        easeout 5.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    return


screen attentionBars:
    zorder 100
    vbar value AnimatedValue(attention_player, max_attention, delay=1.0):
        xalign 0.05
        yalign 0.2
        xmaximum 100
        ymaximum 600
    vbar value AnimatedValue(attention_ennemy, max_attention, delay=1.0):
        xalign 0.95
        yalign 0.2
        xmaximum 100
        ymaximum 600



# choices for menu prototype
menu battlePrototype:
    "Start battle":
        show screen attentionBars
        call screen battleMenu
        
# main battle screen
screen battleMenu:

    $ startBattleState = True
    
    hbox: 
        xalign 0.5
        yalign 0.9
        spacing 20

        # attack button
        frame:
            xpadding 40
            ypadding 20
            xalign 0.1
            yalign 0.5
            textbutton "attack" action [Hide("battleMenu"), Show("attack")]

        # defend button
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "defend" 

        # defend button
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "inventory"

        # talk button but still not sure about this 
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "talk" 



# getter and setter for globals()['textNotes']
init python in variables:

    def changeText(text):
        globals()['textNotes'] = text
        #print("new text : " + globals()['textNotes'])

    def getText():
        #print("bonjour je suis appelé une fois : " + globals()['textNotes'])
        return globals()['textNotes']



# sequFunc for sequences Function, at the very first i wanted to call it sequences, but renpy has this weird thing of already taking big functions with 
# names like variables, sequences, text etc...
init python in sequFunc:

    # sequences
    globals()['sequences'] = [
        ["q", "w", "e", "r"],
        ["r", "q", "q", "r", "e", "e"],
        ["e", "w", "q", "w", "e"]
    ]

    def checkSequences(inputSequence):

        #print("appelé")

        # the boolean that will keep state of if it a good ssequence or not
        matches = []

        # for each sequence
        for j in range(0, len(globals()['sequences'])):

            # debug purpose
            #print(globals()['sequences'][j])

            matches = []

            # for each element of each sequence
            for i in range(0, len(globals()['sequences'][j])):

                # if the length of our input is superior of the sequence it is automaticaly a bad inputSequence
                if i < len(inputSequence) :
                    #print(globals()['sequences'][j][i])
                    #print(inputSequence[i])
                    matches.append(inputSequence[i])

            if matches == globals()['sequences'][j]:                
                print('good sequence')
                return True

        print('bad sequence')
        return False

    def jumpGoodSequence():
        renpy.hide("attack")
        renpy.hide("battle")
        renpy.jump("goodSequNotes")


# when we have input to do
screen attack:

    python:
        if startBattleState == True:
            #print ("--")
            print(globals()['attention_ennemy'])
            variables.changeText("Notes : ")
            inputList = []
            startBattleState = False
        if sequFunc.checkSequences(inputList):
            globals()['attention_ennemy'] -= 20
        #else:
            #print("state of list : ")
            #printList(inputList)

    # Note: i need to change the renpy navigation method, i cant use right, down and left arrows keys because they are already used by renpy

    # key up
    key "K_q" action [
        # we add "up" -> "q" un our inputList
        AddToSet(inputList, "q"), 
        # set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        Play("sound", "Music/Battle themes/Modern/Hapil/5 notes seq/Hapil voice - note 1.ogg"),
        # refresh
        renpy.restart_interaction
    ]

    # key down
    key "K_w" action [
        # we add "up" -> "w" un our inputList
        AddToSet(inputList, "w"), 
        # set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        Play("sound", "Music/Battle themes/Modern/Hapil/5 notes seq/Hapil voice - note 2.ogg"),
        # refresh
        renpy.restart_interaction
    ]

    # key right
    key "K_e" action [
        # we add "up" -> "e" un our inputList
        AddToSet(inputList, "e"), 
        # set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        Play("sound", "Music/Battle themes/Modern/Hapil/5 notes seq/Hapil voice - note 3.ogg"),
        # refresh
        renpy.restart_interaction
    ]

    # key left
    key "K_r" action [
        # we add "up" -> "r" un our inputList
        AddToSet(inputList, "r"), 
        # set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        Play("sound", "Music/Battle themes/Modern/Hapil/5 notes seq/Hapil voice - note 4.ogg"),
        # refresh
        renpy.restart_interaction
    ]


    $ variables.changeText(returnTextByList(inputList))
    $ textToShow = variables.getText()
    #$ print("dans la fonction principale : " + textToShow)

    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        # where we see our game inputs
        frame:
            xpadding 40 
            ypadding 40
            xalign 0.5
            yalign 0.5
            text "[textToShow]"
        
        # return button
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "Return" action [Hide("attack"), Show("battleMenu")]

    if sequFunc.checkSequences(inputList):
        frame:
            xpadding 40 
            ypadding 40
            xalign 0.5
            yalign 0.5
            text "Good Sequence !"
        timer 1.0 action [Hide("attack"), Jump("player_hub")]

    if len(inputList) > 5:
        $ inputList = []

label endGame:
    return