label P2Day9postMorning:

show bg MansionMorning with dissolve
play music AlmostBliss

if (P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie") and P2Date7 != "Allie" and P2Date8 != "Allie":
    $ selectedDate = "Allie"
if (P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett") and P2Date7 != "Scarlett" and P2Date8 != "Scarlett":
    $ selectedDate = "Scarlett"
if (P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra") and P2Date7 != "Terra" and P2Date8 != "Terra":
    $ selectedDate = "Terra"
if (P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet") and P2Date7 != "Violet" and P2Date8 != "Violet":
    $ selectedDate = "Violet"
if (P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui") and P2Date7 != "Yui" and P2Date8 != "Yui":
    $ selectedDate = "Yui"


show k serious at pos70k with dissolve
show d evil_smile at pos30d with dissolve
d "You're running out of time, Kit Kat."
show k neutral
k "It's going to be fine. Just watch."
m "Good morning, Kat."
show k happy
k "'Morning, [name]! How'd you sleep?"
m "Pretty well, thanks."
show d laugh
d "You bet you did. That bed is worth more than your life!"
show k flirt
k "Ah, that reminds me. Why can't the staff have the same kind of bed that [name] has?"
show d surprised
d "Do I look like I'm made of money?"
show k angry
k "You literally own this island!"
show d laugh
d "If I give the staff beds, the next thing they'd ask for is minimum wage. No thanks!"
hide d with dissolve
show k surprised at pos50k with dissolve
"He walked away."
show k neutral
m "So how about that five year plan, huh?"
show k sassy
k "...Maybe the Brothers were onto something with this whole accounting thing."
show k neutral

if selectedDate == "Allie":
    k "Anyway, it's time for your last date with your last soulmate candidate, Allie."
elif selectedDate == "Scarlett":
    k "Anyway, it's time for your last date with your last soulmate candidate, Scarlett."
elif selectedDate == "Terra":
    k "Anyway, it's time for your last date with your last soulmate candidate, Terra."
elif selectedDate == "Violet":
    k "Anyway, it's time for your last date with your last soulmate candidate, Violet."
elif selectedDate == "Yui":
    k "Anyway, it's time for your last date with your last soulmate candidate, Yui."

# OLD UNTRANS VERSION
# k "Anyway, it's time for your last date with your last soulmate candidate, [#selectedDate]."
show k flirt
k "You ready? It's time to make or break!"
m "I'm ready as I'll ever be, Kat."
show k happy
k "Then without further ado..."
show k flirt
k "Lights! Camera!"
show k happy
k "...Don't get yourself killed!"
jump DateSelector
