label P2Day8postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k happy at pos50k with dissolve
k "'Morning, [name]!"
show k flirt
if P2Date7 == "Allie":
    k "You'll be happy to know your third date with Allie yesterday was pretty well received!"
elif P2Date7 == "Scarlett":
    k "You'll be happy to know your third date with Scarlett yesterday was pretty well received!"
elif P2Date7 == "Terra":
    k "You'll be happy to know your third date with Terra yesterday was pretty well received!"
elif P2Date7 == "Violet":
    k "You'll be happy to know your third date with Violet yesterday was pretty well received!"
elif P2Date7 == "Yui":
    k "You'll be happy to know your third date with Yui yesterday was pretty well received!"
# OLD UNTRANS FORMAT
#k "You'll be happy to know your third date with [#P2Date7] yesterday was pretty well received!"
show k neutral
k "Not the highest rated we've had so far, but enough to give us more room to keep going."
m "Sounds good enough to me."
show k flirt
k "For your next date, make sure you pick someone who you think the audience will respond well too!"
show k happy
k "Though at this point, I think you're in a pretty good spot either way."
show k flirt



menu:
    k "Without further ado... which soulmate candidate is it going to be?"

    "Allie" if (P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie") and P2Date7 != "Allie":
        jump p2d8pm_Allie
    "Scarlett" if (P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett") and P2Date7 != "Scarlett":
        jump p2d8pm_Scarlett
    "Terra" if (P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra") and P2Date7 != "Terra":
        jump p2d8pm_Terra
    "Violet" if (P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet") and P2Date7 != "Violet":
        jump p2d8pm_Violet
    "Yui" if (P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui") and P2Date7 != "Yui":
        jump p2d8pm_Yui

label p2d8pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k laugh
k "To be honest, I'm not sure if your dates with Allie are really dates, or more of just trying different kinds of transportation."
show k sassy
k "But hey, whatever floats your boat."
show k flirt
k "Let's get those cameras rolling!"
jump DateSelector

label p2d8pm_Scarlett:
m "Scarlett."
$ selectedDate="Scarlett"
show k happy
k "Can't say I'm surprised there. You're two birds of a feather."
show k laugh
k "Here's to hoping you both have a day you'll both remember for a change!"
m "..."
show k laugh
k "It's funnier when you're not an amnesiac."
jump DateSelector

label p2d8pm_Terra:
m "Terra."
$ selectedDate="Terra"
show k neutral
show k laugh
k "Man, if I'd known you were going to spend all your dates with Terra indoors, I would've just booked the mansion!"
show k happy
k "But sometimes the best things in life aren't the most expensive ones. Who knew?"
show k laugh
k "Just kidding. You ever seen a depressed person who owns an island?"
show k flirt
k "Go get 'er, tiger!"
jump DateSelector

label p2d8pm_Violet:
m "Violet."
$ selectedDate="Violet"
show k happy
k "You didn't let me down, [name]!"
show k laugh
k "I had my doubts with Violet at first, but now... I can see why she's the audience favorite."
show k flirt
k "Don't mess it up!"
m "Wouldn't dream of it."
jump DateSelector

label p2d8pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "...The moment's finally here! The final date with the best girl."
show k flirt
k "Remember... if you mess this up, there's an army of people out there waiting to take your place!"
m "Not planning on it, Kat."
show k laugh
k "You didn't plan to lose your memories and end up on an insane TV show either, but look how that turned out!"
m "Life sure is funny, huh?"
show k flirt
k "You're telling me! Life's never what you'd expect."
show k happy
k "But having a life with Yui? You'd be the luckiest person alive!"
show k flirt
k "And I'm not saying that because I've got money on you picking her."
m "You promise?"
show k laugh
k "Let's get those cameras rolling, people!"
jump DateSelector
