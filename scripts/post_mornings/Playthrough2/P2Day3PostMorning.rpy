label P2Day3postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show a surprised at pos15a with dissolve # former look:right
show y neutral at pos90y with dissolve # former look:left
show v neutral at pos30v with dissolve # former look:left


show t neutral at pos75t with dissolve # former look:left
show s happy at pos60s with dissolve # former look:left
show k neutral at pos45k with dissolve # former ,,-1 # former look:left

"I found Kat in the same place she found me yesterday."
show k neutral
k "'Morning, [name]! It's time to decide who's your last soulmate candidate!"
show k sassy
k "Oh man, I'm gonna make a killing from today's bet with Four."
m "The poor guy! He doesn't know you've been rigging the show?"
show k laugh
k "What he doesn't know can't hurt him!"
show k flirt
k "Anyway, after you make your choice, it'll be just between the three soulmate candidates from here on out."
show y surprised
y "W-wait just a second, what does-"
show k flirt
k "I thought somebody would ask, so let me explain."
show k happy
k "If you don't get chosen, we'll make the rest of this show a tropical getaway for you!"
show k laugh
k "You'll still be able to see the other girls, and live in the mansion, so really, it's no big deal."
show t happy
"Terra did a little fist bump."
show k flirt
k "So without further ado, [name]... who's the last unlucky girl?"

menu:
    m "I'd like to spend some time today with..."

    "Allie" if P1Date1 != "Allie" and P1Date2 != "Allie" and P2Date1 != "Allie" and P2Date2 != "Allie":
        jump p2d3pm_Allie
    "Scarlett" if P1Date1 != "Scarlett" and P1Date2 != "Scarlett" and P2Date1 != "Scarlett" and P2Date2 != "Scarlett":
        jump p2d3pm_Scarlett
    "Terra" if P1Date1 != "Terra" and P1Date2 != "Terra" and P2Date1 != "Terra" and P2Date2 != "Terra":
        jump p2d3pm_Terra
    "Violet" if P1Date1 != "Violet" and P1Date2 != "Violet" and P2Date1 != "Violet" and P2Date2 != "Violet":
        jump p2d3pm_Violet
    "Yui" if P1Date1 != "Yui" and P1Date2 != "Yui" and P2Date1 != "Yui" and P2Date2 != "Yui":
        jump p2d3pm_Yui



label p2d3pm_Allie:
show a surprised
m "Allie."
show a happy
$ selectedDate="Allie"
show k happy
k "We'll make it happen!"
show k angry
k "Let's get the cameras rolling, people! We're in for a bumpy ride!"
show k flirt
k "Now be a dear and give us a minute to set up the scene, hmm?"
jump DateSelector

label p2d3pm_Scarlett:
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

label p2d3pm_Terra:
show t surprised
m "Terra."
show t happy
$ selectedDate="Terra"
show k neutral
k "Alright! Our work's cut out for us."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p2d3pm_Violet:
show v happy
m "Violet."
show v sassy
$ selectedDate="Violet"
show k neutral
k "Alright! We'll make it happen."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p2d3pm_Yui:
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
