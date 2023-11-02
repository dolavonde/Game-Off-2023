define e = Character("Eileen")

default startBattleState = True

#init input
#we will check if we just started the input
init python:
    
    globals()['textNotes'] = "Notes : "

    def returnTextByList(list):
        text = "Notes : "
        for x in list: 
            text += x + " "
        print("dans la def returnTextByList : " +  text)
        return text
        
    def addKeyToList(key, list):
        list.append(key)
        return list

    def printList(list):
        text = ""
        for i in list: 
            text += i + " "
        print(text)

label start:
    scene bg room
    jump battlePrototype
    return

menu battlePrototype:
    "Start battle":
        call screen battle

#main battle screen
screen battle:
    $ startBattleState = True
    
    hbox: 
        xalign 0.5
        yalign 0.9
        spacing 20
        frame:
            xpadding 40
            ypadding 20
            xalign 0.1
            yalign 0.5
            textbutton "attack" action [Hide("battle"), Show("attack")]
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "defend" 
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "inventory" 
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "talk" 

init python in variables:

    def changeText(text):
        globals()['textNotes'] = text
        print("new text : " + globals()['textNotes'])

    def getText():
        print("bonjour je suis appelé une fois : " + globals()['textNotes'])
        return globals()['textNotes']

#when we have input to do
screen attack:

    python:
        if startBattleState == True:
            print ("--")
            variables.changeText("Notes : ")
            inputList = []
            startBattleState = False
        else:
            print("state of list : ")
            printList(inputList)

    #key up
    key "K_q" action [
        #we add "up" -> "u" un our inputList
        AddToSet(inputList, "q"), 
        #set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        #refresh
        renpy.restart_interaction
    ]

    #key down
    key "K_w" action [
        #we add "up" -> "u" un our inputList
        AddToSet(inputList, "w"), 
        #set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        #refresh
        renpy.restart_interaction
    ]

    #key right
    key "K_e" action [
        #we add "up" -> "u" un our inputList
        AddToSet(inputList, "e"), 
        #set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        #refresh
        renpy.restart_interaction
    ]

    #key left
    key "K_r" action [
        #we add "up" -> "u" un our inputList
        AddToSet(inputList, "r"), 
        #set variable of input by appending to it out inputList
        Function(variables.changeText, returnTextByList(inputList)), 
        Function(printList, inputList),
        #refresh
        renpy.restart_interaction
    ]

    $ variables.changeText(returnTextByList(inputList))
    $ textToShow = variables.getText()
    $ print("dans la fonction principale : " + textToShow)

    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        #where we see our game inputs
        frame:
            xpadding 40 
            ypadding 40
            xalign 0.5
            yalign 0.5
            text "[textToShow]"
        
        #return button
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "Return" action [Hide("attack"), Show("battle")]