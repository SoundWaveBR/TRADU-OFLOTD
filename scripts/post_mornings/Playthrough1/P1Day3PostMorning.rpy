label P1Day3postMorning:

show bg MansionMorning with dissolve
play music ShavingMirror
"I figure it's about time to talk with Kat about my next date, but..."
"I felt a tap on my back."
m "Kat? Is that..."
"I turned around, and the girl in front of me was as surprised as I was."
show a surprised at pos50a with dissolve
a "Kat? No, this is Allie."
m "Ah... sorry, Allie. What's up?"
show a neutral
"She looked to see if anyone else was around before she spoke."
stop music
play music MysteryLoop
show a worried
a "Have you noticed anything... weird lately?"
m "What do you mean?"

if P1Date1 == "Allie" or P1Date2 == "Allie":
    jump DateAllieAlready
else:
    jump DidntDateAllie

label DateAllieAlready:
show a surprised
a "Don't get me wrong, I had a lot of fun on our date earlier... but something about this show is weird."
jump AfterAllieComment

label DidntDateAllie:

show a annoyed
a "...Something about this show gives me the creeps."
jump AfterAllieComment

label AfterAllieComment:
show a worried
a "I went out for a walk in the forest last night, you know, cuz it's gorgeous and all."
show a neutral
a "But after I got there... I must have dozed off for a minute."
m "Taking a nap in a forest at night? You're braver than most, Allie."
show a annoyed
a "Lemme finish!"
show a worried
a "When I woke up... I was back in my room, on my bed."
show a worried
a "And I swear, I don't remember ever walking back."
m "Huh... that sounds pretty crazy, if it really happened."
m "You sure you didn't just have a weird dream?"
show a surprised
a "Now that you mention it, I tried Scarlett's cooking for fun last night. That was... a big mistake."
show a worried
a "Maybe I'm just imagining things, but..."
show a neutral
a "Did you notice anything strange happen last night?"
m "I don't think so, it was just a regular night. I had a conversation with Kat in my room, but that was it."
stop music
play music ShavingMirror
show a laugh
a "Damn, five girls to date wasn't enough, huh?"
show a happy
a "Sorry, I couldn't help myself."
show a neutral
a "Well, I guess I'll just be staying away from Scarlett's cooking, and chalk it up to a weird-ass dream."
show a laugh
a "Thanks for listening, [name]."
m "It's my pleasure, Allie."
show a happy
a "Seeya later."
hide a with dissolve
play sound Whoosh
"She ran off, just as fast as she had come initially."
show k surprised at pos50k with dissolve
k "Someone's in a hurry."
m "Hey Kat! I was looking for you."
show k neutral
k "Afternoon, [name]. Same here."
m "I wanted to ask, did your guys... do anything last night to Allie?"
show k surprised
k "...? Not that I know of. Our staff leaves the cast alone at night."
show k neutral
"...I guess there's nothing to worry about. Kat's been honest with me so far about everything."
show k flirt
k "...?"
"...Right?"
show k neutral
k "Anyway, more importantly - it's time for phase two!"
show k happy

if P1Date1 == "Allie" and P1Date2 == "Scarlett":
    k "You've done pretty decently with setting up Allie and Scarlett as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Allie" and P1Date2 == "Terra":
    k "You've done pretty decently with setting up Allie and Terra as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Allie" and P1Date2 == "Violet":
    k "You've done pretty decently with setting up Allie and Violet as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Allie" and P1Date2 == "Yui":
    k "You've done pretty decently with setting up Allie and Yui as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Scarlett" and P1Date2 == "Allie":
    k "You've done pretty decently with setting up Scarlett and Allie as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Scarlett" and P1Date2 == "Terra":
    k "You've done pretty decently with setting up Scarlett and Terra as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Scarlett" and P1Date2 == "Violet":
    k "You've done pretty decently with setting up Scarlett and Violet as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Scarlett" and P1Date2 == "Yui":
    k "You've done pretty decently with setting up Scarlett and Yui as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Terra" and P1Date2 == "Allie":
    k "You've done pretty decently with setting up Terra and Allie as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Terra" and P1Date2 == "Scarlett":
    k "You've done pretty decently with setting up Terra and Scarlett as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Terra" and P1Date2 == "Violet":
    k "You've done pretty decently with setting up Terra and Violet as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Terra" and P1Date2 == "Yui":
    k "You've done pretty decently with setting up Terra and Yui as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Violet" and P1Date2 == "Allie":
    k "You've done pretty decently with setting up Violet and Allie as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Violet" and P1Date2 == "Scarlett":
    k "You've done pretty decently with setting up Violet and Scarlett as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Violet" and P1Date2 == "Terra":
    k "You've done pretty decently with setting up Violet and Terra as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Violet" and P1Date2 == "Yui":
    k "You've done pretty decently with setting up Violet and Yui as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Yui" and P1Date2 == "Allie":
    k "You've done pretty decently with setting up Yui and Allie as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Yui" and P1Date2 == "Scarlett":
    k "You've done pretty decently with setting up Yui and Scarlett as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Yui" and P1Date2 == "Terra":
    k "You've done pretty decently with setting up Yui and Terra as your soulmate candidates. People are eating it up!"
elif P1Date1 == "Yui" and P1Date2 == "Violet":
    k "You've done pretty decently with setting up Yui and Violet as your soulmate candidates. People are eating it up!"


# OLD UNTRANS VERSION
#k "You've done pretty decently with setting up [#P1Date1] and [#P1Date2] as your soulmate candidates. People are eating it up!"
show k sassy
k "The romance? Whatever. More importantly, every time they're on screen, we get one hell of a ratings boost!"
show k neutral
k "From here on out, you'll only be going on dates with either of them. That'll be your best bet to get out of here alive."
show k happy
k "That sound good to you?"
m "You almost make it sound like I have a choice."
show k laugh
k "I'm glad we're on the same page as always, [name]!"
show k happy
k "But enough with the pleasantries. Who's the unlucky girl today?"
m "Ha ha ha."

menu:
    m "I guess I'd like to spend today with..."

    "Allie" if P1Date1 == "Allie" or P1Date2 == "Allie":
        jump p1d3pm_Allie
    "Scarlett" if P1Date1 == "Scarlett" or P1Date2 == "Scarlett":
        jump p1d3pm_Scarlett
    "Terra" if P1Date1 == "Terra" or P1Date2 == "Terra":
        jump p1d3pm_Terra
    "Violet" if P1Date1 == "Violet" or P1Date2 == "Violet":
        jump p1d3pm_Violet
    "Yui" if P1Date1 == "Yui" or P1Date2 == "Yui":
        jump p1d3pm_Yui


#; CHANGE dialogue to be exclusively rank 2 based

label p1d3pm_Allie:
m "Allie."
$ selectedDate="Allie"
show k surprised
k "...Really now! I'm surprised, considering how you KO'd yourself last time."
show k laugh
k "But that's none of my business!"
show k happy
k "We'll start filming down at the beach. See you there!"
jump DateSelector

label p1d3pm_Scarlett:
m "Scarlett."
$ selectedDate="Scarlett"
show k surprised
k "...Huh! If making zombies doesn't count as a red flag, I'd love to see what your dating handbook looks like."
show k laugh
k "But that's none of my business!"
show k happy
k "I think Scarlett's somewhere around the mansion. We'll follow you!"
jump DateSelector

label p1d3pm_Terra:
m "Terra."
$ selectedDate="Terra"
show k neutral
k "Alright! Sounds like a plan to me."
show k happy
k "I think she's working on something in the mansion. Lead the way!"
jump DateSelector

label p1d3pm_Violet:
#show v happy
m "Violet."
$ selectedDate="Violet"
show k happy
k "Nice! I kind of had a feeling you would!"
show k neutral
k "I think Violet's somewhere around the mansion. Lead the way!"
jump DateSelector

label p1d3pm_Yui:
m "Yui."
$ selectedDate="Yui"
show k happy
k "I knew it! Damn, I should've made another bet with Four."
show k neutral
k "Anyway, Yui's somewhere in the fields behind the mansion."
show k flirt
k "I'll be filming as usual. Get a move on!"
jump DateSelector
