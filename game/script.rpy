define e = Character("Eileen")

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

    scene bg room
    jump battlePrototype
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
        call screen battle


# main battle screen
screen battle:

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
            textbutton "attack" action [Hide("battle"), Show("attack")]

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



init python in attention:

    def updateEnnemyLife(damage):
        global attention_ennemy
        attention_ennemy -= damage

    def getEnnemyLife():
        global attention_ennemy 
        return attention_ennemy



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
            print("truc")
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
            textbutton "Return" action [Hide("attack"), Show("battle")]

    if sequFunc.checkSequences(inputList):
        frame:
            xpadding 40 
            ypadding 40
            xalign 0.5
            yalign 0.5
            text "Good Sequence !"
        timer 1.0 action [Hide("attack"), Show("battle")]

    if len(inputList) > 5:
        $ inputList = []