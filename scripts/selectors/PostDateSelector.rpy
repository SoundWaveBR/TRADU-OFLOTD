label postDateSelector:
    # stop music
    #stop music
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
        jump postDateSelectorplaythrough1
    if playthrough == 2:
        jump postDateSelectorplaythrough2

label postDateSelectorplaythrough1:
    window show dissolve
    if currentDay == 1:
        jump P1Day1postDate
    if currentDay == 2:
        jump P1Day2postDate
    if currentDay == 3:
        jump P1Day3postDate
    if currentDay == 4:
        jump P1Day4postDate
    if currentDay == 5:
        jump P1Day5postDate

#; 1-1-2-2-3-3(END)

label postDateSelectorplaythrough2:
    window show dissolve
    if currentDay == 1:
        jump P2Day1postDate
    if currentDay == 2:
        jump P2Day2postDate
    if currentDay == 3:
        jump P2Day3postDate
    if currentDay == 4:
        jump P2Day4postDate
    if currentDay == 5:
        jump P2Day5postDate
    if currentDay == 6:
        jump P2Day6postDate
    if currentDay == 7:
        jump P2Day7postDate
    if currentDay == 8:
        jump P2Day8postDate

#; 1-1-1-2-2-2-3-3-3(END)

#; DOCUMENTATION!"
#; postDate controls the currentDay
#; It takes 4 dates to max a girl, there are 8 dates in total
#; no real game over screens
