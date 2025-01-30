label P2Day6postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k flirt at pos50k with dissolve
k "'Morning, [name]! How'd you sleep?"
m "Pretty well, considering how you edit the footage that keeps me alive... drunk."
show k laugh
k "That sounds like an win-win to me, if you ask me."
show k flirt
k "Can you believe it? We're already on the sixth day of the show!"
m "Is it already? Time sure goes by fast."
show k laugh
k "No kidding."
show k neutral
k "Anyway, it's time to wrap up phase two. You just need to go on a second date with your last soulmate candidate."
show k flirt
k "Shouldn't be too hard, no?"
m "Please don't jinx me."
show k laugh
k "Break a leg!"
show k surprised
k "Seriously, actually breaking a leg would be a lot better for you than messing up today's date."
m "Not helping, Kat!"

if (P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie") and P2Date4 != "Allie" and P2Date5 != "Allie":
    $ selectedDate = "Allie"
if (P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett") and P2Date4 != "Scarlett" and P2Date5 != "Scarlett":
    $ selectedDate = "Scarlett"
if (P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra") and P2Date4 != "Terra" and P2Date5 != "Terra":
    $ selectedDate = "Terra"
if (P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet") and P2Date4 != "Violet" and P2Date5 != "Violet":
    $ selectedDate = "Violet"
if (P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui") and P2Date4 != "Yui" and P2Date5 != "Yui":
    $ selectedDate = "Yui"

$ P1Date6=selectedDate

if selectedDate == "Allie":
    "Time to get today's date started with none other than my third soulmate candidate, Allie!"
elif selectedDate == "Scarlett":
    "Time to get today's date started with none other than my third soulmate candidate, Scarlett!"
elif selectedDate == "Terra":
    "Time to get today's date started with none other than my third soulmate candidate, Terra!"
elif selectedDate == "Violet":
    "Time to get today's date started with none other than my third soulmate candidate, Violet!"
elif selectedDate == "Yui":
    "Time to get today's date started with none other than my third soulmate candidate, Yui!"

# OLD UNTRANS VERSION
# "Time to get today's date started with none other than my third soulmate candidate, [#selectedDate]!"

jump DateSelector
