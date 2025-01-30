label P2Day7postDate:

play music PastSadness
$ P2Date7=selectedDate
$ currentDay=8


show bg MansionNight with dissolve

if selectedDate == "Allie":
    "...And just like that, that's my last date with Allie."
elif selectedDate == "Scarlett":
    "...And just like that, that's my last date with Scarlett."
elif selectedDate == "Terra":
    "...And just like that, that's my last date with Terra."
elif selectedDate == "Violet":
    "...And just like that, that's my last date with Violet."
elif selectedDate == "Yui":
    "...And just like that, that's my last date with Yui."
    
# OLD UNTRANS
#"...And just like that, that's my last date with [#selectedDate]."
"Time sure goes by quickly."
show k happy at pos50k with dissolve
k "I thought I'd find you here."
m "Why's that?"
show k flirt
k "You tend to come out here when you're lost in thought, is all."
show k neutral
k "...You're thinking about how the show's almost over, am I right?"
m "How'd you know?"
show k laugh
k "Lucky guess."
show k flirt
k "Well it's not over yet, so don't let up just yet."
stop music
play music TechLive
show k neutral

if P2Date7 == "Allie":
    k "Speaking of which, how was your date with Allie today?"
elif P2Date7 == "Scarlett":
    k "Speaking of which, how was your date with Scarlett today?"
elif P2Date7 == "Terra":
    k "Speaking of which, how was your date with Terra today?"
elif P2Date7 == "Violet":
    k "Speaking of which, how was your date with Violet today?"
elif P2Date7 == "Yui":
    k "Speaking of which, how was your date with Yui today?"

menu:
    #k "Speaking of which, how was your date with [#P2Date7] today?"

    "Awesome":
        jump p2d7pd_awesome
    "Alright":
        jump p2d7pd_alright

label p2d7pd_alright:
m "...It was alright. Not the way I wanted it to go."
show k neutral
k "Ah, I'm sorry to hear that. I won't pry."
show k laugh
k "I guess three dates wasn't enough to see if someone's marriage material after all! Who knew."
jump p2d7pd_advice

label p2d7pd_awesome:


if selectedDate == "Allie":
    jump p2d7pd_thirdAllie
if selectedDate == "Scarlett":
    jump p2d7pd_thirdScarlett
if selectedDate == "Terra":
    jump p2d7pd_thirdTerra
if selectedDate == "Violet":
    jump p2d7pd_thirdViolet
if selectedDate == "Yui":
    jump p2d7pd_thirdYui


label p2d7pd_thirdAllie:
"...I probably shouldn't tell the whole truth, but enough of it should be good."
m "...It was awesome! I don't know how, but the more time I spend with Allie, the better it gets."
m "Being married to her would make every day an adventure... and I like the sound of that."
show k laugh
k "I'm sure it'd be an adventure, but the jury's out on if it's one you'd walk away from!"
show k happy
k "But I can see she makes you happy. Really, that counts for a lot nowadays."
show k bored
k "Though you might want to start wearing body armor, if you want to stay that way."
jump p2d7pd_advice

label p2d7pd_thirdScarlett:
m "...It was the best."
m "My connection with Scarlett's one of a kind, and there's no one I'd rather have beside me than her."
m "Being married to her would be like a dream come true."
show k sassy
k "Well, aren't you a romantic, [name]!"
show k flirt
k "But I'm happy to hear that. If it's you two, I'm sure that whatever you two face out there..."
show k laugh
k "...You'll be fine, as long as you stick together!"
show k worried
k "And if she stops turning people into zombies."
m "Yeah, that's a conversation we have to have..."
show k laugh
k "Don't forget that in the prenup!"
jump p2d7pd_advice

label p2d7pd_thirdTerra:
m "It was nice! We didn't do anything too crazy, but... it didn't have to be."
show k flirt
k "I could tell! It was cute watching you guys."
show k laugh
k "Though to be honest, I wish your relationship would move along a little faster! This show's not getting any longer, you know."
show k happy
k "That said, I feel like you two would make a pretty good team in the long run."
jump p2d7pd_advice


label p2d7pd_thirdViolet:
m "Being with Violet makes me feel like we're on top of the world."
m "Somehow, she takes my breath away with how cool she can be... and at the same, make me laugh like a child alongside her."
m "I'd no idea that I'd fall for her so hard after our first meeting, but... I couldn't help myself."
m "And now, what I want most is to make her the happiest woman in the world."
show k flirt
k "Now that's what I like to hear!"
show k laugh
k "I had my doubts at first, but you two really stole the show."
show k happy
k "And with good reason. I feel like our viewers got to see a glimpse of what your lives together would be like."
show k sassy
k "Maybe the mess in the kitchen won't be from the dough next time, hmm?"
m "No comment..."
jump p2d7pd_advice

label p2d7pd_thirdYui:
m "Yui's the most wonderful woman in the whole world."
m "Somehow, she can take the most normal things and turn them into irreplaceable memories."
m "More than anything, I just want to make more memories with her, every day."
m "...And make her happier than anyone's ever been."
show k surprised
k "Jeez, we're going to have to edit that to stop people from throwing up!"
show k sassy
k "I get it, though. You, my friend, are luckier than anyone has any right to be."
show k laugh
k "Better pack your bags - I've got a feeling you'll be heading to the countryside soon!"
jump p2d7pd_advice

label p2d7pd_advice:
stop music
play music PastSadness
#; now that's a zinger
show k flirt
k "Anyway, I'd ask you if you're thinking of choosing her at the end, but I'd rather wait and see how it plays out."
show k neutral
k "...You going to stay out here for long?"
m "Nah, I'll probably be going back inside soon."
show k laugh
k "I'll keep you company till then."
show k neutral
k "I figure you might want to have a conversation with someone that won't get you killed if it's not TV worthy."
m "...Thanks, Kat."
show k flirt
k "Don't mention it."
m "You know, I'm curious, Kat..."
show k neutral
k "What's up?"
stop music
play music MysteryLoop
show k surprised
m "Let's say I knew I was screwed. That there was no way of me getting out of here alive."
m "That the only way left for me to survive was just to run."
m "...Would you let me escape?"
show k neutral
k "..."
show k happy
k "...Of course, [name]."
m "...Thanks, Kat. That means a lot."
show k laugh
k "It's no big deal."
"We stayed out for a little longer before we called it a night."
"I'm lucky I have someone I can trust on my side."
jump MorningSelector
