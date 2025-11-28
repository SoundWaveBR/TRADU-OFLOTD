label P2Day7postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k happy at pos50k with dissolve
k "'Morning, [name]!"
show k flirt
k "Let's kick off phase three!"
show k neutral
k "Hopefully, we can wrap this up quickly, and you'll be back to your old life soon."
m "I better be!"
m "As nice as this island is, it's a gilded cage."
show k neutral
k "You'll be able to go back to your old life soon. That's a promise!"
show k laugh
k "Well, unless you make a mess out of your next three dates. I can't help you there."
show k happy
# OLD UNTRANS VERSION
#k "But assuming you do, you'll get to leave here with one of [#P2Date4], [#P2Date5], or [#P2Date6]!"
k "But assuming you do, you'll get to leave here with one of the three girls you're dating now!"
show k flirt
k "But first... it's time to pick which of them you'll be going on a third date with today."
show k sassy


menu:
    k "Who's it gonna be?"
    "Allie" if P2Date1 == "Allie" or P2Date2 == "Allie" or P2Date3 == "Allie":
        jump p2d7pm_Allie
    "Scarlett" if P2Date1 == "Scarlett" or P2Date2 == "Scarlett" or P2Date3 == "Scarlett":
        jump p2d7pm_Scarlett
    "Terra" if P2Date1 == "Terra" or P2Date2 == "Terra" or P2Date3 == "Terra":
        jump p2d7pm_Terra
    "Violet" if P2Date1 == "Violet" or P2Date2 == "Violet" or P2Date3 == "Violet":
        jump p2d7pm_Violet
    "Yui" if P2Date1 == "Yui" or P2Date2 == "Yui" or P2Date3 == "Yui":
        jump p2d7pm_Yui


label p2d7pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k laugh
k "To be honest, I'm not sure if your dates with Allie are really dates, or more of just trying different kinds of transportation."
show k sassy
k "But hey, whatever floats your boat."
show k flirt
k "Let's get those cameras rolling!"
jump DateSelector

label p2d7pm_Scarlett:
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

label p2d7pm_Terra:
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

label p2d7pm_Violet:
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

label p2d7pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "The moment's finally here! The final date with the best girl."
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
k "...Let's get those cameras rolling, people!"
jump DateSelector
