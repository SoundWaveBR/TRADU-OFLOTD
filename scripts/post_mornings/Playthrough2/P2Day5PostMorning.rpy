label P2Day5postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k worried at pos50k with dissolve
m "Good morning, Kat! I've been looking for you."
show k sad
k "...Ugh, not so loud, please. My head's killing me from all that wine last night."
show k annoyed
k "I still had to edit our broadcast after that, which didn't help..."
"...Somehow, this scene feels familiar."
m "Something tells me that my chance of surviving goes down for every opened bottle of alcohol on the island."
m "Maybe I should spend today re-enacting Prohibition, instead of going on a date."
show k laugh
k "You do know how Prohibition ended, right?"
show k happy
k "Anyway! Back to the brass tacks."
show k neutral
if P2Date4 == "Allie":
    k "Yesterday's second date with Allie went really well. Let's keep striking the iron while it's hot!"
elif P2Date4 == "Scarlett":
    k "Yesterday's second date with Scarlett went really well. Let's keep striking the iron while it's hot!"
elif P2Date4 == "Terra":
    k "Yesterday's second date with Terra went really well. Let's keep striking the iron while it's hot!"
elif P2Date4 == "Violet":
    k "Yesterday's second date with Violet went really well. Let's keep striking the iron while it's hot!"
elif P2Date4 == "Yui":
    k "Yesterday's second date with Yui went really well. Let's keep striking the iron while it's hot!"

# OLD UNTRANS FORMAT
#k "Yesterday's second date with [#P2Date4] went really well. Let's keep striking the iron while it's hot!"
show k flirt
k "Which soulmate candidate will you be going on a second date with today?"


menu:
    "Allie" if (P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie") and P2Date4 != "Allie":
        jump p2d5pm_Allie
    "Scarlett" if (P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett") and P2Date4 != "Scarlett":
        jump p2d5pm_Scarlett
    "Terra" if (P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra") and P2Date4 != "Terra":
        jump p2d5pm_Terra
    "Violet" if (P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet") and P2Date4 != "Violet":
        jump p2d5pm_Violet
    "Yui" if (P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui") and P2Date4 != "Yui":
        jump p2d5pm_Yui


label p2d5pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k surprised
k "...Really now! I'm surprised, considering how you KO'd yourself last time."
show k laugh
k "But that's none of my business!"
show k happy
k "We'll start filming down at the beach. See you there!"
jump DateSelector

label p2d5pm_Scarlett:
m "Scarlett."
$ selectedDate="Scarlett"
show k surprised
k "...Huh! If making zombies doesn't count as a red flag, I'd love to see what your dating handbook looks like."
show k laugh
k "But that's none of my business!"
show k happy
k "I think Scarlett's somewhere around the mansion. We'll follow you!"
jump DateSelector

label p2d5pm_Terra:
m "Terra."
$ selectedDate="Terra"
show k neutral
k "Alright! Sounds like a plan to me."
show k happy
k "I think she's working on something in the mansion. Lead the way!"
jump DateSelector

label p2d5pm_Violet:
m "Violet."
$ selectedDate="Violet"
show k happy
k "Nice! I kind of had a feeling you would!"
show k neutral
k "I think Violet's somewhere around the mansion. Lead the way!"
jump DateSelector

label p2d5pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "I knew it! Damn, I should've made another bet with Four."
show k neutral
k "Anyway, Yui's somewhere in the fields behind the mansion."
show k flirt
k "I'll be filming as usual. Get a move on!"
jump DateSelector
