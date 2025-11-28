label P1Day4postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k worried at pos50k with dissolve
k "Ugh, my head..."
m "You okay? You don't look so good."
show k sad
k "Not... so loud... ugh. My head's killing me after I had a ton of wine last night."
show k annoyed
k "I still had to edit our broadcast after that, which didn't help..."
show k flirt
m "Ladies and gentlemen, I present the woman who decides whether I get to live or die every night."
m "...And she was very, very drunk when she did just that."
show k laugh
k "Thank you, thank you! I'll be here all week!"
show k flirt
k "Clearly, you're still alive, [name], so it's all good."
show k annoyed
k "Believe me, you'd drink too if you worked here. Just look at the Brothers Five."
m "Working at Futuristic Evil Corp. (TM) has to come with some benefits, right?"
show k angry
k "You'd think, but we still have to pay for dental out of pocket!"
show k surprised
k "Ahem... before I forget what this show's all about..."
show k neutral
k "Today's the day you go on a date with..."
show k surprised
k "...Who was your other soulmate candidate again?"
m "..."

menu:
    "Allie" if (P1Date1 == "Allie" or P1Date2 == "Allie") and P1Date3 != "Allie":
        jump p1d4pm_Allie
    "Scarlett" if (P1Date1 == "Scarlett" or P1Date2 == "Scarlett") and P1Date3 != "Scarlett":
        jump p1d4pm_Scarlett
    "Terra" if (P1Date1 == "Terra" or P1Date2 == "Terra") and P1Date3 != "Terra":
        jump p1d4pm_Terra
    "Violet" if (P1Date1 == "Violet" or P1Date2 == "Violet") and P1Date3 != "Violet":
        jump p1d4pm_Violet
    "Yui" if (P1Date1 == "Yui" or P1Date2 == "Yui") and P1Date3 != "Yui":
        jump p1d4pm_Yui


label p1d4pm_Allie:
$ selectedDate="Allie"
m "...Allie."
jump p1d4pm_DateSelection

label p1d4pm_Scarlett:
$ selectedDate="Scarlett"
m "...Scarlett."
jump p1d4pm_DateSelection

label p1d4pm_Terra:
$ selectedDate="Terra"
m "...Terra."
jump p1d4pm_DateSelection

label p1d4pm_Violet:
$ selectedDate="Violet"
m "...Violet."
jump p1d4pm_DateSelection

label p1d4pm_Yui:
$ selectedDate="Yui"
m "...Yui."
jump p1d4pm_DateSelection

label p1d4pm_DateSelection:
# OLD UNTRANS VERSION
#m "...[#selectedDate]."
m "How much did you drink last night, Kat?"
show k bored
k "Whatever, I knew that. Just testing you, duh."
m "Right..."
show k happy

if selectedDate == "Allie":
    k "Alright, let's get this second date with Allie started! Woo!"
elif selectedDate == "Scarlett":
    k "Alright, let's get this second date with Scarlett started! Woo!"
elif selectedDate == "Terra":
    k "Alright, let's get this second date with Terra started! Woo!"
elif selectedDate == "Violet":
    k "Alright, let's get this second date with Violet started! Woo!"
elif selectedDate == "Yui":
    k "Alright, let's get this second date with Yui started! Woo!"

# OLD UNTRANS
#k "Alright, let's get this second date with [#selectedDate] started! Woo!"
show k surprised at pos50k #,40
with vpunch
k "Woah. Someone tell the world to stop spinning like a little bitch."
"...I'm pretty much fucked, huh?"
jump DateSelector
