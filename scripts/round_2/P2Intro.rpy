label P2Intro:

show bg MansionMorning with dissolve
play music Morning

$ scarlettAffection=0
$ yuiAffection=0
$ violetAffection=0
$ terraAffection=0
$ allieAffection=0
$ currentDay=1
$ playthrough=2

show a surprised at pos15a with dissolve
show y neutral at pos90y with dissolve
show t neutral at pos75t with dissolve
show s happy at pos60s with dissolve
show v neutral at pos30v with dissolve
show k neutral at pos45k with dissolve
"How on earth did I get into this mess?"
"I'm somehow stuck on an island in the middle of nowhere, in an insane dating show from hell."
"From what Kat said, I'm dead meat if I can't finish this show with a fiancée, or if the ratings aren't high enough."
"None of the girls on the show know the truth, and if they found out... they'd kill all of us."
"Why couldn't I wake up with no memories in a regular hospital, like a regular drama protagonist?"
"At least the girls seemed nice."
"Allie's quite something. Something tells me she'll be hard to keep up with, and that's not just from losing a race to her in the field."
"Scarlett's... interesting. I've still got no idea if she was trying to read the magazine, or the book hiding it."
"...I'll figure that out later."
"Terra marches to the beat of her own drum. I like that."
"Violet's cool, but intimidating as hell. I'm pretty sure she was about to cook one of the brothers for dinner."
"...Then there's Yui. She seems like a really sweet girl. Something about her is so familiar..."
"She said she knew me from before. I'll have to ask her about what I was like before as soon as I can."
"But for now... the show must go on."
show k neutral
k "...And that's why [name] is the perfect soulmate for each of you."
show s surprised
s "I'm sorry, you just drew a bunch of numbers and symbols that don't mean anything."
show t surprised
t "It's like the bullshit math they show on-screen in a movie!"
show k happy
k "Ah, you're late to the party, [name]!"
show k flirt
k "Now that we're all together, it's time to explain the rules of this show!"
show k neutral
k "[name]... one of the five lovely women here is your soulmate."
stop music
play sound MysteryHarp
show k flirt
play music Smile
k "You'll get to know three of the girls over the next nine days, over three dates with each of them."
show k neutral
k "Then, on the tenth day... you'll have to ask one of them to marry you!"
"So I've got... ten days to save my life."
show k neutral
k "So without further ado... who do you want to spend time with?"
m "Wait, I have to choose already?"
m "I haven't even had the chance to really talk with any of them yet."
show k flirt
k "Don't think of it that way, think of it as who do you want to talk to the most right now."
m "Uh, alright..."
m "Well, I guess I'd like to spend today's alone time with..."
show k surprised
k "Hold on just a second! I forgot to tell you something pretty important."
"She pulled me aside."
hide a with dissolve
hide s with dissolve
hide t with dissolve
hide v with dissolve
hide y with dissolve
show k neutral at pos50k with dissolve
k "...This should be far enough."
show k flirt
k "So the girls think you'll be asking any of the five of them for a date."
show k sassy

if P1Date1 == "Allie" and P1Date2 == "Scarlett":
    k "But really, I only want you to be asking three of them. Basically, everybody but Allie and Scarlett."
elif P1Date1 == "Allie" and P1Date2 == "Terra":
    k "But really, I only want you to be asking three of them. Basically, everybody but Allie and Terra."
elif P1Date1 == "Allie" and P1Date2 == "Violet":
    k "But really, I only want you to be asking three of them. Basically, everybody but Allie and Violet."
elif P1Date1 == "Allie" and P1Date2 == "Yui":
    k "But really, I only want you to be asking three of them. Basically, everybody but Allie and Yui."
elif P1Date1 == "Scarlett" and P1Date2 == "Allie":
    k "But really, I only want you to be asking three of them. Basically, everybody but Scarlett and Allie."
elif P1Date1 == "Scarlett" and P1Date2 == "Terra":
    k "But really, I only want you to be asking three of them. Basically, everybody but Scarlett and Terra."
elif P1Date1 == "Scarlett" and P1Date2 == "Violet":
    k "But really, I only want you to be asking three of them. Basically, everybody but Scarlett and Violet."
elif P1Date1 == "Scarlett" and P1Date2 == "Yui":
    k "But really, I only want you to be asking three of them. Basically, everybody but Scarlett and Yui."
elif P1Date1 == "Terra" and P1Date2 == "Allie":
    k "But really, I only want you to be asking three of them. Basically, everybody but Terra and Allie."
elif P1Date1 == "Terra" and P1Date2 == "Scarlett":
    k "But really, I only want you to be asking three of them. Basically, everybody but Terra and Scarlett."
elif P1Date1 == "Terra" and P1Date2 == "Violet":
    k "But really, I only want you to be asking three of them. Basically, everybody but Terra and Violet."
elif P1Date1 == "Terra" and P1Date2 == "Yui":
    k "But really, I only want you to be asking three of them. Basically, everybody but Terra and Yui."
elif P1Date1 == "Violet" and P1Date2 == "Allie":
    k "But really, I only want you to be asking three of them. Basically, everybody but Violet and Allie."
elif P1Date1 == "Violet" and P1Date2 == "Scarlett":
    k "But really, I only want you to be asking three of them. Basically, everybody but Violet and Scarlett."
elif P1Date1 == "Violet" and P1Date2 == "Terra":
    k "But really, I only want you to be asking three of them. Basically, everybody but Violet and Terra."
elif P1Date1 == "Violet" and P1Date2 == "Yui":
    k "But really, I only want you to be asking three of them. Basically, everybody but Violet and Yui."
elif P1Date1 == "Yui" and P1Date2 == "Allie":
    k "But really, I only want you to be asking three of them. Basically, everybody but Yui and Allie."
elif P1Date1 == "Yui" and P1Date2 == "Scarlett":
    k "But really, I only want you to be asking three of them. Basically, everybody but Yui and Scarlett."
elif P1Date1 == "Yui" and P1Date2 == "Terra":
    k "But really, I only want you to be asking three of them. Basically, everybody but Yui and Terra."
elif P1Date1 == "Yui" and P1Date2 == "Violet":
    k "But really, I only want you to be asking three of them. Basically, everybody but Yui and Violet."

# OLD UNTRANS FORMAT
# k "But really, I only want you to be asking three of them. Basically, everybody but [#P1Date1] and [#P1Date2]."
m "...Why's that?"
show k neutral
k "Let's just say we think we'll be getting higher ratings that way."
show k flirt
k "...And you know how important it is to get high ratings, right?"
m "I don't really have a choice, do I?"
show k laugh
k "Nope! Glad we're on the same page, [name]."
show k neutral
k "So without further ado..."
show y neutral at pos90y with dissolve # former look:left
show a happy at pos15a with dissolve # former look:right
show t neutral at pos75t with dissolve # former look:left
show s happy at pos60s with dissolve # former look:left
show v neutral at pos30v with dissolve # former look:left
show k neutral at pos45k with dissolve # former ,,-1 # former look:left
"We walked back to the girls."
show k flirt

menu:
    k "Who do you want to go on your first date with?"
    "Allie" if P1Date1 != "Allie" and P1Date2 != "Allie":
        jump p2i_Allie
    "Scarlett" if P1Date1 != "Scarlett" and P1Date2 != "Scarlett":
        jump p2i_Scarlett
    "Terra" if P1Date1 != "Terra" and P1Date2 != "Terra":
        jump p2i_Terra
    "Violet" if P1Date1 != "Violet" and P1Date2 != "Violet":
        jump p2i_Violet
    "Yui" if P1Date1 != "Yui" and P1Date2 != "Yui":
        jump p2i_Yui

label p2i_Allie:
m "Allie."
$ selectedDate="Allie"
jump p2i_Chosen

label p2i_Scarlett:
m "Scarlett."
$ selectedDate="Scarlett"
jump p2i_Chosen

label p2i_Terra:
m "Terra."
$ selectedDate="Terra"
jump p2i_Chosen

label p2i_Violet:
m "Violet."
$ selectedDate="Violet"
jump p2i_Chosen

label p2i_Yui:
$ selectedDate="Yui"
jump p2i_Chosen

label p2i_Chosen:

show k happy
k "Alright! We'll make it happen."
show k bored
k "*sigh*"
#stop music fade:0.35
jump DateSelector
