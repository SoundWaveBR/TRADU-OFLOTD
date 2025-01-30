label MorningSelector:
    stop music
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
    jump MorningSelectorplaythrough1
if playthrough == 2:
    jump MorningSelectorplaythrough2



label MorningSelectorplaythrough1:
    if currentDay == 2:
        jump Episode2
    if currentDay == 3:
        jump Episode3
    if currentDay == 4:
        jump Episode4
    if currentDay == 5:
        jump Episode5
    if currentDay == 6:
        jump Episode6
    if currentDay == 7:
        jump Episode7

label Episode2:
    play sound MysteryPiano
    show bg Episode2 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label Episode3:
    play sound MysteryHarp #loop:false
    show bg Episode3 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label Episode4:
    play sound MysteryPiano #loop:false
    show bg Episode4 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label Episode5:
    play sound MysteryPiano #loop:false
    show bg Episode5 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label Episode6:
    play sound MysteryHarp #loop:false
    show bg Episode6 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label Episode7:
    play sound MysteryPiano #loop:false
    show bg Episode7 with dissolve
    $ renpy.pause(delay = 2.0, hard = True)
    jump MorningChoice

label MorningSelectorplaythrough2:
    #; ADD PICTURES HERE
    jump MorningChoice

label MorningChoice:
    window show dissolve
    if selectedDate == "Violet" and violetAffection == 1:
        jump VioletMorning1
    if selectedDate == "Violet" and violetAffection == 2:
        jump VioletMorning2
    if selectedDate == "Violet" and violetAffection == 3:
        jump VioletMorning3
    if selectedDate == "Yui" and yuiAffection == 1:
        jump YuiMorning1
    if selectedDate == "Yui" and yuiAffection == 2:
        jump YuiMorning2
    if selectedDate == "Yui" and yuiAffection == 3:
        jump YuiMorning3
    if selectedDate == "Allie" and allieAffection == 1:
        jump AllieMorning1
    if selectedDate == "Allie" and allieAffection == 2:
        jump AllieMorning2
    if selectedDate == "Allie" and allieAffection == 3:
        jump AllieMorning3
    if selectedDate == "Scarlett" and scarlettAffection == 1:
        jump ScarlettMorning1
    if selectedDate == "Scarlett" and scarlettAffection == 2:
        jump ScarlettMorning2
    if selectedDate == "Scarlett" and scarlettAffection == 3:
        jump ScarlettMorning3
    if selectedDate == "Terra" and terraAffection == 1:
        jump TerraMorning1
    if selectedDate == "Terra" and terraAffection == 2:
        jump TerraMorning2
    if selectedDate == "Terra" and terraAffection == 3:
        jump TerraMorning3
    "morningChoice Afters"
