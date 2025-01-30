label P1Day5postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror

show k happy at pos50k with dissolve
k "'Morning, [name]!"
show k flirt
k "Time sure flies, huh? The show's almost over, and you'll be able to go back to your regular life soon!"
show k laugh
k "No idea if that's gonna have any less headaches though."
m "Who knows?"
m "As strange as it sounds, I've had some fun here."
m "The whole getting murdered thing isn't great, but it hasn't been all bad."
show k flirt
k "I did mention that other people would kill to be in your position."
m "...On second thought, they definitely haven't thought it through enough."
show k laugh
k "Probably not."
show k flirt
k "Well, back to business! It's time to pick who you'll go on your first third date with."
show k laugh
k "Who's the unlucky soulmate candidate today?"

menu:
    "Allie" if P1Date1 == "Allie" or P1Date2 == "Allie":
        jump p1d5pm_Allie
    "Scarlett" if P1Date1 == "Scarlett" or P1Date2 == "Scarlett":
        jump p1d5pm_Scarlett
    "Terra" if P1Date1 == "Terra" or P1Date2 == "Terra":
        jump p1d5pm_Terra
    "Violet" if P1Date1 == "Violet" or P1Date2 == "Violet":
        jump p1d5pm_Violet
    "Yui" if P1Date1 == "Yui" or P1Date2 == "Yui":
        jump p1d5pm_Yui


label p1d5pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k laugh
k "To be honest, I'm not sure if your dates with Allie are really dates, or more of just trying different kinds of transportation."
show k sassy
k "...But hey, whatever floats your boat."
show k flirt
k "Let's get those cameras rolling!"
jump DateSelector

label p1d5pm_Scarlett:
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

label p1d5pm_Terra:
m "Terra."
$ selectedDate="Terra"
show k neutral
show k laugh
k "Man, if I'd known you were going to spend all your dates with Terra indoors, I would've just booked the mansion!"
show k happy
k "But sometimes the best things in life aren't the most expensive ones. Who knew?"
show k laugh
k "...Just kidding. You ever seen a depressed person who owns an island?"
show k flirt
k "Go get 'er, tiger!"
jump DateSelector

label p1d5pm_Violet:
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

label p1d5pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "...The moment's finally here! The final date with the best girl."
show k flirt
k "Remember, if you mess this up, there's an army of people out there waiting to take your place!"
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
