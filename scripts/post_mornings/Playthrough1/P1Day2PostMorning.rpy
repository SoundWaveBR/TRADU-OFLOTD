label P1Day2postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show a surprised at pos15a with dissolve# former look:right
show y neutral at pos90y with dissolve# former look:left
show v neutral at pos30v with dissolve# former look:left
show t neutral at pos75t with dissolve# former look:left
show s happy at pos60s with dissolve# former look:left
show k neutral at pos45k with dissolve# former ,,-1 # former look:left
with dissolve

#; some discussion between the girls over who's gonna be the 2nd Soulmate Candidate
k "Oh, there you are, [name]!"
show k neutral
k "I've been looking for you. It's time to decide who's your other soulmate candidate!"
show k serious
k "You remember what we discussed yesterday, right?"
m "How could I forget?"
show k neutral
m "It's not like I've ever forgotten anything important before, except for, well... everything."
show k flirt
k "Save the snark for whichever poor girl you end up seeing today."
m "Ow, that stings."
show k sassy
k "It'll be just between your two soulmate candidates from here on out, so choose wisely!"

if P1Date1 != "Yui":
    jump p1d2pm_YuiNotFirstDate
if P1Date1 != "Violet":
    jump p1d2pm_VioletNotFirstDate


label p1d2pm_YuiNotFirstDate:
show y surprised
y "W-Wait, really? So if we don't get chosen... what are we supposed to do?"
show k flirt
k "Well, for starters... we're in a tropical paradise! Think of it as a vacation."
show k bored
k "Soulmates aren't real anyway, so it's not a big deal."
with vpunch
show y surprised
y "They're not real!?"
show k bored
k "Oh boy... [name], you might want to pick your second soulmate candidate quick."
jump p1d2pm_TerraJoke

label p1d2pm_VioletNotFirstDate:
show v neutral
v "If we are not chosen within these first two days, what are we to do instead?"
show k flirt
k "Well, we are in a tropical paradise. Think of the rest of the show as a vacation!"
show k bored
k "It's not like you're losing anything. Soulmates aren't real anyway."
show v laugh
v "Not much for romance, are you, Kat?"
show k laugh
k "How could you tell?"
jump p1d2pm_TerraJoke

label p1d2pm_TerraJoke:
show t worried
t "Wait a minute, Kat! Will we be splitting up the group after today?"
show k happy
k "Nope! Don't worry, you'll still be able to hang out together... and who knows where that will go!"
show t happy
t "Whew! Good to know my battle plans will still come in handy."
show t surprised
t "*Cough* I mean... friendship plans. Good to know I still get to see my new friends, yes sir!"
show k flirt
k "So without further ado, [name]... who's the unlucky girl?"

jump p1d2pm_DateSelection


label p1d2pm_DateSelection:

menu:
    m "I'd like to spend some time today with..."

    "Allie" if P1Date1 != "Allie":
        jump p1d2pm_Allie
    "Scarlett" if P1Date1 != "Scarlett":
        jump p1d2pm_Scarlett
    "Terra" if P1Date1 != "Terra":
        jump p1d2pm_Terra
    "Violet" if P1Date1 != "Violet":
        jump p1d2pm_Violet
    "Yui" if P1Date1 != "Yui":
        jump p1d2pm_Yui


label p1d2pm_Allie:
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

label p1d2pm_Scarlett:
show s laugh
m "Scarlett."
$ selectedDate="Scarlett"
show s happy
show k happy
k "Alright! We'll make it happen."
show k neutral
k "Hmmm... let's have [name] start in the mansion, and ooh, I know where to bring Scarlett."
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p1d2pm_Terra:
show t surprised
m "Terra."
show t happy
$ selectedDate="Terra"
show k neutral
k "Alright! Our work's cut out for us."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p1d2pm_Violet:
show v happy
m "Violet."
show v sassy
$ selectedDate="Violet"
show k neutral
k "Alright! We'll make it happen."
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label p1d2pm_Yui:
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
