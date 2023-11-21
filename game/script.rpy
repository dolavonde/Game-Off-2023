# characters
define character.y = Character("Me")
define y.playerType = 0
define y.playerName = ""

# i define it but really not sure if we are going to use it
define n = Character("Narrator")
define o = Character("Organizer")
define g = Character("Guardian")
define e = Character("Elder")

define a = Character("Ashenleaf")
define p = Character("Pumpell plum")
define h = Character("Hapil")
define l = Character("Lowtront glow")

define character.t1 = Character("Trainer 1")
define ht = Character("Hapil Trainer")
define pt = Character("Pumpell Plum Trainer")

default preferences.text_cps = 30

# variable
default startBattleState = True

# init input
# we will check if we just started the input
init python:
    
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

    jump sc3_1
    #jump battlePrototype
    return



# ----------------------
# Introduction
# ----------------------
label intro:
    scene black
    centered "Introduction..."

    o "Hmm..."
    o "This won't do"

    # fade image that represents the organizer sitting at the desk

    o "This time next spring the arch will still not have bloomed..."
    o "And Guardian will have to move on. \n\nI have to do something !"

    # fade image that represents the organizer writing at desk
    o "And I'm writing to the sweet villagers of the Hapil, we'd love to invite your fun ways..."
    o "A first of hopefully many events !"
    o "If you can spare one... or two of the Ashenleaf, we can find a way to show their unique skills"
    o "It's about time we get to celebrate some Ashenleaf Voices."
    o "The songs of Pumpell Plums always have a place in our hearts, as they've been the ones to start our tradition."
    o "We hope to hear voices here !"
    o "I can still remember the first time I heard the voice from those on the path of the Lowtront Glow..."
    o "When I was a child the first song I heard haunted me for years... in a good way ! Come by !"

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
    "?" "Oh ! Excuse me !"
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
            imagebutton idle "ashenleafButtonIdle" action [SetVariable("y.playerType", 0), Jump("nameAshenleafChoices")]

        # pumpell plum
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "PumpellPlumButtonIdle" action [SetVariable("y.playerType", 1), Jump("namePumpellPlumChoices")]

        # hapil
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "hapilButtonIdle" action [SetVariable("y.playerType", 2), Jump("nameHapilChoices")]

        # lowtront glow
        frame:
            xpadding 30
            ypadding 30
            xalign 0.5
            yalign 0.5
            imagebutton idle "lowtrontGlowButtonIdle" action [SetVariable("y.playerType", 3), Jump("nameLowtrontGlowChoices")]

# important to remove and replace !!!!!!!!!!!!

# choices for name
# for ashenleaf
menu nameAshenleafChoices:
    "What's your name ?"

    "Sahen":
        $ y.playerName = "Sahen"
        jump sc1_2_2
    "Aheleh":
        $ y.playerName = "Aheleh"
        jump sc1_2_2
    "Enel Ehales":
        $ y.playerName = "Enel"
        jump sc1_2_2
# for Pumpell Plum
menu namePumpellPlumChoices:
    "What's your name ?"

    "Melulu":
        $ y.playerName = "Melulu"
        jump sc1_2_2
    "Ume":
        $ y.playerName = "Ume"
        jump sc1_2_2
    "Lemu":
        $ y.playerName = "Lemu"
        jump sc1_2_2
# for Hapil
menu nameHapilChoices:
    "What's your name ?"

    "Pilla":
        $ y.playerName = "Pilla"
        jump sc1_2_2
    "Hali":
        $ y.playerName = "Hali"
        jump sc1_2_2
    "Ala":
        $ y.playerName = "Ala"
        jump sc1_2_2
# for Lowtront Glow
menu nameLowtrontGlowChoices:
    "What's your name ?"

    "Itlin":
        $ y.playerName = "Itlin"
        jump sc1_2_2
    "Otorn":
        $ y.playerName = "Otorn"
        jump sc1_2_2
    "Wotto":
        $ y.playerName = "Wotto"
        jump sc1_2_2


label sc1_2_2:

    # I don't know how to do the transition but it's okay
    y "Hello ? My name is [y.playerName] !"

    # I thought it would be fun to make the character react weird if you choose enel ehales
    if y.playerName == "Enel Ehales":
        "?" "It will be just [y.playerName]..."
    else:
        "?" "Hello [y.playerName] ! I'm ?, it's great to meet you !"

    # I read the script it's hard to understand who is this person, what does he want us 
    # or even what are all of the dialogues that appears on the script...



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
    t1 "Maybe next time !!"
    jump sc4_1

label firstBattleWin:
    t1 "Good job !!!"
    jump sc4_1



# ----------------------
# Scene 4
#
# first real battle
# ----------------------
label sc4_1:
    t1 "Oh I think the organizer is calling a meeting, let's see what does he want..."
    # fade to the meeting room

    o "So everyone, you will be paired with someone !"
    scene black

    # fade to hapil village

    # ashenleaf and hapil
    if y.playerType == 0 or y.playerType == 2: 
        # we need to show both characters here I think

        h "So we're partners, I guess !!"

        # need information on his name + the daredevil thing
        h "Good to meet you ! My name's ____ and I like something daredevil and bracelet-making and singing, and I'm super excited to join chorus"
        a "Yeah, I heard-, wait, you like the daredevil thing ?!"

        # still need some informations on how to setup
        # I imagine that we skip the part where the ashenleaf is talking about, and we just show them vibing

        a "But- OH wait right we have to go learn whatever song they want us to learn."
        h "Okay ! Cool !"
        a "If you ask me, it's stupid, not cool. They invited us, they should let us do our own thing !!"
        a "But hey fine, whatever, we gotta do the doo-doo-doo song."
        a "Aw but it's a lovely doo doo doo. C'mon !"
        jump second_battle_trainer

    # pumpell plum and lowtront glow
    elif y.playerType == 1 or y.playerType == 3:

        p "Come on now, we will be partners."
        l "Oh, but I didn't... okay ?"

        # still need the name
        p "Your name ____, right ?"
        l "Yes that's me."
        p "Perfect. I've heard through the grapevine you have a beautiful voice, which is a blessing blessing for us traditional singers."
        p "Once they hear us hitting the notes ever-so flawlessly, they'll be enraptured by our grace...!"
        l "O-oh ! Um, thank you ! But, maybe we should... learn how to sing, first..."
        p "Exactly"
        jump second_battle_trainer

# for this part I will need way more informations on how to setup it
label second_battle_trainer:
    # all related to the trainer battle
    ht "Goooooooood morning everyone !!"

label third_battle:
    # all related to the first big battle


label sc4_3_Win:
    ht "Wonderful, wonderful job !!"

    if y.playerType == 1 or y.playerType == 3:
        h "Yyyes ! That was so fun !!"
        # ?????? dont understand leafling stand in for cake
        a "YEAH !! See, what'd I tell ya ! Piece of (leaflinf stand-in for cake ??)"
        h "So, where to next ? Lead the way, partner."
        a "To the (organizer) ! If we finished first, we can totally brag about it."
        jump sc4_4
    
    if y.playerType == 0 or y.playerType == 2:
        p "There ! Nothing less than perfection. Just like I knew it would be."

        # lowtront blushing
        l "Yeah... yeah."
        p "Let's go then. Onto learning the next song !!"
        jump sc4_4

label sc4_3_Lose:
    if y.playerType == 1 or y.playerType == 3:
        h "Whoa ! Haha, that went well!"
        a "Aaagh, no it didn't ! What did I tell you ? This whole thing is stupid"
        h "Aw, I guess it didn't. Could we try again ?"
        a "No way. Let's keep this one to ourselves."
        jump sc4_4
    
    if y.playerType == 0 or y.playerType == 2:
        p "Oh, dear. That needs some... work."
        l "Mmm..."
        jump sc4_4
    
label sc4_4: 

    # we fade to the pumpell village, with the organizer that sends here

    show black
    centered "End day 1"
    jump sc5_1



# ----------------------
# Scene 5
# ----------------------
label sc5_1: 

    centered "Day 2"
    
    # fade to pumpell plum village
    pt "You're late ! Come here, come here, stand in your spots. Quickly ! Thank you, dears."


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