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
    $ urTurn = false
    $ begin = true

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
# New day, and this is where we are going to do the tutorial with the first trainer
# ----------------------



# ----------------------
# Scene 4
#
# 
# ----------------------




# ----------------------
# All related to the battles
# ----------------------
label battles_hub:

    # here we choose randomly whose turn gonna be
    # actually, I will do one chance out of three, so the player will have more chance to begin, it will be more fun
    # 0 = ennemy turn
    # 1 and 2 = our turn
    $ d3 = renpy.random.randint(0, 2)

    if begin == true :

        # screen that show the attention bars on right and left
        show screen attentionBars
        
        if d2 == 0:
            $ urTurn = false
            $ begin = false
        else
            $ urTurn = true
            $ begin = false

    if urTurn == true:
        # all related to our turn !
        call screen battleMenu
    else: 
        # all related to the opponent turn !

        if attention_player <= 66:
            
            if d3 == 0:

            elif d3 == 1:

            elif d3 == 2:

        elif 33 <= attention_player < 66:

            if d3 == 0:

            elif d3 == 1:

            elif d3 == 2:

        elif attention_player < 33:  

            if d3 == 0:

            elif d3 == 1:

            elif d3 == 2:

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
        timer 1.0 action [Hide("attack"), Show("battleMenu")]

    if len(inputList) > 5:
        $ inputList = []