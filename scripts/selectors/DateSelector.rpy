label DateSelector:
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


#; if xAffection == n...it means they failed the n+1 date
if playthrough == 1:
    jump DateSelectorplaythrough1
if playthrough == 2:
    jump DateSelectorplaythrough2

label DateSelectorplaythrough1:
    # "Okay 1"
    if selectedDate == "Allie":
        jump AllieSelection1
    if selectedDate == "Scarlett":
        jump ScarlettSelection1
    if selectedDate == "Terra":
        jump TerraSelection1
    if selectedDate == "Violet":
        jump VioletSelection1
    if selectedDate == "Yui":
        jump YuiSelection1

label DateSelectorplaythrough2:
    if selectedDate == "Allie":
        jump AllieSelection2
    if selectedDate == "Scarlett":
        jump ScarlettSelection2
    if selectedDate == "Terra":
        jump TerraSelection2
    if selectedDate == "Violet":
        jump VioletSelection2
    if selectedDate == "Yui":
        jump YuiSelection2

label AllieSelection1:
    # "Okay 2"
    if currentDay == 1:
        $ P1Date1="Allie"
    elif currentDay == 2:
        $ P1Date2="Allie"
    elif currentDay == 3:
        $ P1Date3="Allie"
    elif currentDay == 4:
        $ P1Date4="Allie"
    elif currentDay == 5:
        $ P1Date5="Allie"
    elif currentDay == 6:
        $ P1Date6="Allie"

    jump DateSelection

label AllieSelection2:
    if currentDay == 1:
        $ P2Date1="Allie"
    elif currentDay == 2:
        $ P2Date2="Allie"
    elif currentDay == 3:
        $ P2Date3="Allie"
    elif currentDay == 4:
        $ P2Date4="Allie"
    elif currentDay == 5:
        $ P2Date5="Allie"
    elif currentDay == 6:
        $ P2Date6="Allie"
    elif currentDay == 7:
        $ P2Date7="Allie"
    elif currentDay == 8:
        $ P2Date8="Allie"
    elif currentDay == 9:
        $ P2Date9="Allie"

    jump DateSelection

label ScarlettSelection1:
    if currentDay == 1:
        $ P1Date1="Scarlett"
    elif currentDay == 2:
        $ P1Date2="Scarlett"
    elif currentDay == 3:
        $ P1Date3="Scarlett"
    elif currentDay == 4:
        $ P1Date4="Scarlett"
    elif currentDay == 5:
        $ P1Date5="Scarlett"
    elif currentDay == 6:
        $ P1Date6="Scarlett"

    jump DateSelection

label ScarlettSelection2:
    if currentDay == 1:
        $ P2Date1="Scarlett"
    elif currentDay == 2:
        $ P2Date2="Scarlett"
    elif currentDay == 3:
        $ P2Date3="Scarlett"
    elif currentDay == 4:
        $ P2Date4="Scarlett"
    elif currentDay == 5:
        $ P2Date5="Scarlett"
    elif currentDay == 6:
        $ P2Date6="Scarlett"
    elif currentDay == 7:
        $ P2Date7="Scarlett"
    elif currentDay == 8:
        $ P2Date8="Scarlett"
    elif currentDay == 9:
        $ P2Date9="Scarlett"

    jump DateSelection

label TerraSelection1:
    if currentDay == 1:
        $ P1Date1="Terra"
    elif currentDay == 2:
        $ P1Date2="Terra"
    elif currentDay == 3:
        $ P1Date3="Terra"
    elif currentDay == 4:
        $ P1Date4="Terra"
    elif currentDay == 5:
        $ P1Date5="Terra"
    elif currentDay == 6:
        $ P1Date6="Terra"

    jump DateSelection

label TerraSelection2:
    if currentDay == 1:
        $ P2Date1="Terra"
    elif currentDay == 2:
        $ P2Date2="Terra"
    elif currentDay == 3:
        $ P2Date3="Terra"
    elif currentDay == 4:
        $ P2Date4="Terra"
    elif currentDay == 5:
        $ P2Date5="Terra"
    elif currentDay == 6:
        $ P2Date6="Terra"
    elif currentDay == 7:
        $ P2Date7="Terra"
    elif currentDay == 8:
        $ P2Date8="Terra"
    elif currentDay == 9:
        $ P2Date9="Terra"

    jump DateSelection

label VioletSelection1:
    if currentDay == 1:
        $ P1Date1="Violet"
    elif currentDay == 2:
        $ P1Date2="Violet"
    elif currentDay == 3:
        $ P1Date3="Violet"
    elif currentDay == 4:
        $ P1Date4="Violet"
    elif currentDay == 5:
        $ P1Date5="Violet"
    elif currentDay == 6:
        $ P1Date6="Violet"

    jump DateSelection

label VioletSelection2:
    if currentDay == 1:
        $ P2Date1="Violet"
    elif currentDay == 2:
        $ P2Date2="Violet"
    elif currentDay == 3:
        $ P2Date3="Violet"
    elif currentDay == 4:
        $ P2Date4="Violet"
    elif currentDay == 5:
        $ P2Date5="Violet"
    elif currentDay == 6:
        $ P2Date6="Violet"
    elif currentDay == 7:
        $ P2Date7="Violet"
    elif currentDay == 8:
        $ P2Date8="Violet"
    elif currentDay == 9:
        $ P2Date9="Violet"

    jump DateSelection

label YuiSelection1:
    if currentDay == 1:
        $ P1Date1="Yui"
    elif currentDay == 2:
        $ P1Date2="Yui"
    elif currentDay == 3:
        $ P1Date3="Yui"
    elif currentDay == 4:
        $ P1Date4="Yui"
    elif currentDay == 5:
        $ P1Date5="Yui"
    elif currentDay == 6:
        $ P1Date6="Yui"

    jump DateSelection

label YuiSelection2:
    if currentDay == 1:
        $ P2Date1="Yui"
    elif currentDay == 2:
        $ P2Date2="Yui"
    elif currentDay == 3:
        $ P2Date3="Yui"
    elif currentDay == 4:
        $ P2Date4="Yui"
    elif currentDay == 5:
        $ P2Date5="Yui"
    elif currentDay == 6:
        $ P2Date6="Yui"
    elif currentDay == 7:
        $ P2Date7="Yui"
    elif currentDay == 8:
        $ P2Date8="Yui"
    elif currentDay == 9:
        $ P2Date9="Yui"

    jump DateSelection


label DateSelection:
    window show dissolve

    if selectedDate == "Violet" and violetAffection == 0:
        jump VioletDate1
    if selectedDate == "Violet" and violetAffection == 1:
        jump VioletDate2
    if selectedDate == "Violet" and violetAffection == 2:
        jump VioletDate3
    if selectedDate == "Yui" and yuiAffection == 0:
        jump YuiDate1
    if selectedDate == "Yui" and yuiAffection == 1:
        jump YuiDate2
    if selectedDate == "Yui" and yuiAffection == 2:
        jump YuiDate3
    if selectedDate == "Allie" and allieAffection == 0:
        jump AllieDate1
    if selectedDate == "Allie" and allieAffection == 1:
        jump AllieDate2
    if selectedDate == "Allie" and allieAffection == 2:
        jump AllieDate3
    if selectedDate == "Scarlett" and scarlettAffection == 0:
        jump ScarlettDate1
    if selectedDate == "Scarlett" and scarlettAffection == 1:
        jump ScarlettDate2
    if selectedDate == "Scarlett" and scarlettAffection == 2:
        jump ScarlettDate3
    if selectedDate == "Terra" and terraAffection == 0:
        jump TerraDate1
    if selectedDate == "Terra" and terraAffection == 1:
        jump TerraDate2
    if selectedDate == "Terra" and terraAffection == 2:
        jump TerraDate3
