label P2Day4postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k flirt at pos50k with dissolve
k "'Morning, [name]!"
show k happy
k "Congrats, you've made it to the fourth day!"
show k laugh
k "...And you've become the first person to have not one, not two, but three soulmate candidates! Who'd have thought!"
show k sassy
k "Granted, soulmate candidates don't really exist, but hey, we'll edit that part out!"
show k happy
k "You should be really, really proud of yourself."
m "...I can't tell if you're being serious or not."
show k laugh
k "I'll leave that for you to guess!"
show k flirt

menu:
    # OLD UNTRANS VERSION
    #k "Anyway, between your three *cough* lucky romantic interests... [#P2Date1], [#P2Date2], and [#P2Date3]... who do you want to spend today with?"
    k "Anyway, between your three *cough* lucky romantic interests... who do you want to spend today with?"

    "Allie" if P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie":
        jump p2d4pm_Allie
    "Scarlett" if P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett":
        jump p2d4pm_Scarlett
    "Terra" if P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra":
        jump p2d4pm_Terra
    "Violet" if P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet":
        jump p2d4pm_Violet
    "Yui" if P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui":
        jump p2d4pm_Yui

label p2d4pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k surprised
k "...Really now! I'm surprised, considering how you KO'd yourself last time."
show k laugh
k "But that's none of my business!"
show k happy
k "We'll start filming down at the beach. See you there!"
jump DateSelector

label p2d4pm_Scarlett:
m "Scarlett."
$ selectedDate="Scarlett"
show k surprised
k "...Huh! If making zombies doesn't count as a red flag, I'd love to see what your dating handbook looks like."
show k laugh
k "But that's none of my business!"
show k happy
k "I think Scarlett's somewhere around the mansion. We'll follow you!"
jump DateSelector

label p2d4pm_Terra:
m "Terra."
$ selectedDate="Terra"
show k neutral
k "Alright! Sounds like a plan to me."
show k happy
k "I think she's working on something in the mansion. Lead the way!"
jump DateSelector

label p2d4pm_Violet:
m "Violet."
$ selectedDate="Violet"
show k happy
k "Nice! I kind of had a feeling you would!"
show k neutral
k "I think Violet's somewhere around the mansion. Lead the way!"
jump DateSelector

label p2d4pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "I knew it! Damn, I should've made another bet with Four."
show k neutral
k "Anyway, Yui's somewhere in the fields behind the mansion."
show k flirt
k "I'll be filming as usual. Get a move on!"
jump DateSelector
