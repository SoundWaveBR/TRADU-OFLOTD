label postMorningSelector:
    # stop music
    stop sound
    show bg Black
    hide a
    hide s
    hide t
    hide v
    hide y
    hide k
    hide d
    hide b1
    hide b2
    hide b3
    hide b4
    hide b5
    with dissolve
    window hide dissolve
    $ renpy.pause(delay = 2.0, hard = True)

    if playthrough == 1:
        jump postMorningSelectorplaythrough1
    if playthrough == 2:
        jump postMorningSelectorplaythrough2

label postMorningSelectorplaythrough1:
    window show dissolve
    if currentDay == 2:
        jump P1Day2postMorning
    if currentDay == 3:
        jump P1Day3postMorning
    if currentDay == 4:
        jump P1Day4postMorning
    if currentDay == 5:
        jump P1Day5postMorning
    if currentDay == 6:
        jump P1Day6postMorning
    #; 1(NA)-1-2-2-3-3(END)


label postMorningSelectorplaythrough2:
    window show dissolve
    if currentDay == 2:
        jump P2Day2postMorning
    if currentDay == 3:
        jump P2Day3postMorning
    if currentDay == 4:
        jump P2Day4postMorning
    if currentDay == 5:
        jump P2Day5postMorning
    if currentDay == 6:
        jump P2Day6postMorning
    if currentDay == 7:
        jump P2Day7postMorning
    if currentDay == 8:
        jump P2Day8postMorning
    if currentDay == 9:
        jump P2Day9postMorning

#; 1(NA)-1-1-2-2-2-3-3-3(END)
