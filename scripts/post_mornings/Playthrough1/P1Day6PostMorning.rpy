label P1Day6postMorning:

show bg MansionMorning with dissolve
play music MysteryLoop

#; lowest possible arrangement is 2-1-1-1-1
show k flirt at pos70k with dissolve
show d laugh at pos30d with dissolve
d "Well, look who crawled out of an economy class airplane toilet!"
m "And good morning to you too, Damian."
show k surprised
k "[name]! Don't mind my... err, don't mind him."
show k flirt
k "Damian was just telling me the news - your ratings are doing really well so far!"
show k neutral
k "At this rate, I really think you'll make it out of here."
m "That's great news!"
show d neutral
d "I wouldn't celebrate just yet."
show d happy
d "Just because you've done well till now doesn't mean you won't jump the shark today."
show d neutral
d "Your ratings today need to be higher than they're even been - or you'll get axed."
show d evil_smile
d "Axed literally, if I'm around when your number's up. I guess we'll find that out together, won't we?"
show d neutral
d "'Later."
hide d with dissolve
stop music
play music Morning
show k worried at pos50k with dissolve
k "...Sorry about him, he can be a little mean sometimes."
m "A murder threat is 'a little mean'?"
show k laugh
k "Anyway..."
show k happy

if P1Date6 == "Allie":
    k "You ready for your last date with Allie?"
elif P1Date6 == "Scarlett":
    k "You ready for your last date with Scarlett?"
elif P1Date6 == "Terra":
    k "You ready for your last date with Terra?"
elif P1Date6 == "Violet":
    k "You ready for your last date with Violet?"
elif P1Date6 == "Yui":
    k "You ready for your last date with Yui?"

# OLD UNTRANS FORMAT
#k "You ready for your last date with [#P1Date6]?"
show k flirt
k "It's just this last date, then tomorrow, it'll be the final ceremony!"
m "I'm ready as I'll ever be!"
show k laugh
k "Fantastic! Then we'll start filming right away!"
show k neutral
k "Good luck, [name]. You'll need it."
m "Thanks, Kat. I owe you one."

if P1Date6 == "Allie":
    "It's time for my last date with Allie!"
elif P1Date6 == "Scarlett":
    "It's time for my last date with Scarlett!"
elif P1Date6 == "Terra":
    "It's time for my last date with Terra!"
elif P1Date6 == "Violet":
    "It's time for my last date with Violet!"
elif P1Date6 == "Yui":
    "It's time for my last date with Yui!"

# OLD UNTRANS FORMAT
#"It's time for my last date with [#P1Date6]!"
$ selectedDate=P1Date6
jump DateSelector
