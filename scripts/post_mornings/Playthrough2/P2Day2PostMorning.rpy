label P2Day2postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror


show y neutral at pos90y with dissolve# former look:left
show t neutral at pos75t with dissolve# former look:left
show a surprised at pos15a with dissolve# former look:right

show v neutral at pos30v with dissolve # former look:left
show s happy at pos60s with dissolve# former look:left
show k flirt at pos45k with dissolve# former ,,-1 # former look:left

k "There you are, [name]!"
show k neutral
k "I've been looking for you. It's time to decide who's your second soulmate candidate!"
show k flirt
"Kat moved in closer to whisper."
show k laugh
k "Not like you really have a choice, though!"
show k flirt
k "So without further ado, [name]... who's the unlucky girl?"

menu:
    m "I'd like to spend some time today with..."

    "Allie" if P1Date1 != "Allie" and P1Date2 != "Allie" and P2Date1 != "Allie":
        jump p2d2pm_Allie
    "Scarlett" if P1Date1 != "Scarlett" and P1Date2 != "Scarlett" and P2Date1 != "Scarlett":
        jump p2d2pm_Scarlett
    "Terra" if P1Date1 != "Terra" and P1Date2 != "Terra" and P2Date1 != "Terra":
        jump p2d2pm_Terra
    "Violet" if P1Date1 != "Violet" and P1Date2 != "Violet" and P2Date1 != "Violet":
        jump p2d2pm_Violet
    "Yui" if P1Date1 != "Yui" and P1Date2 != "Yui" and P2Date1 != "Yui":
        jump p2d2pm_Yui

label p2d2pm_Allie:
show a surprised
m "Allie."
show a happy
$ selectedDate="Allie"
show k neutral
k "We'll make it happen!"
show k neutral
k "Let's get those cameras rolling, people! We're in for a bumpy ride!"
show k flirt
k "Now be a dear and give us a minute to set up the scene, hmm?"
jump DateSelector

label p2d2pm_Scarlett:
show s laugh
m "Scarlett."
$ selectedDate="Scarlett"
show s happy
show k happy
k "Alright! We'll make it happen."
show k neutral
k "Hmmm... let's have [name] start in the mansion... and ooh, I know where to bring Scarlett."
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p2d2pm_Terra:
show t surprised
m "Terra."
show t happy
$ selectedDate="Terra"
show k neutral
k "Alright! Our work's cut out for us."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p2d2pm_Violet:
show v happy
m "Violet."
show v sassy
$ selectedDate="Violet"
show k neutral
k "Alright! We'll make it happen."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p2d2pm_Yui:
show y surprised
m "Yui."
$ selectedDate="Yui"
show k happy
show y blush
k "Yessss! I made a bet with Four you'd choose Yui today."
show k laugh
k "Great choice, [name]! I knew I could count on you!"
m "..."
show k happy
k "Alright, alright. Let's get this show on the road!"
jump DateSelector
