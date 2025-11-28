label P1Day5postDate:

play music PastSadness
$ P1Date5=selectedDate
$ currentDay=6

#; the night of your first 3rd date!  So we know selectedAffection is 3."
if P1Date5 != P1Date1:
    $ P1Date6 = P1Date1
if P1Date5 != P1Date2:
    $ P1Date6 = P1Date2

show bg RoomNight with dissolve
"After today's date, I decided to take a stroll around the mansion."
# OLD UNTRANS
#"After today's date with [#selectedDate], I decided to take a stroll around the mansion."
show bg MansionNight with dissolve #time:2
"The night was clear as could be. A light breeze made it just a bit chilly, but not enough that I'd need to put on more."
"I found myself fixating on the moon without thinking."
show k happy at pos50k with dissolve
k "I thought I'd find you here."
m "Why's that?"
show k laugh
k "Just a gut feeling... and the island-wide surveillance system."
show k neutral
k "You doing okay?"
m "Yeah, I'm just thinking."
m "I can't believe the show's almost over. It didn't feel real earlier today."
show k laugh
k "Time sure flies, doesn't it!"
show k neutral

if P1Date6 == "Allie":
    k "You've only got the last third date with Allie tomorrow, then the final ceremony on the day after."
elif P1Date6 == "Scarlett":
    k "You've only got the last third date with Scarlett tomorrow, then the final ceremony on the day after."
elif P1Date6 == "Terra":
    k "You've only got the last third date with Terra tomorrow, then the final ceremony on the day after."
elif P1Date6 == "Violet":
    k "You've only got the last third date with Violet tomorrow, then the final ceremony on the day after."
elif P1Date6 == "Yui":
    k "You've only got the last third date with Yui tomorrow, then the final ceremony on the day after."


# OLD UNTRANS FORMAT
#k "You've only got the last third date with [#P1Date6] tomorrow, then the final ceremony on the day after."
stop music
play music TechLive
show k neutral

menu:
    # k "Speaking of which, how was your date with [P1Date5] today?"
    k "Speaking of which, how was your date today?"

    "Awesome":
        jump p1d5pd_awesome
    "Alright":
        jump p1d5pd_alright

label p1d5pd_alright:
m "...It was alright. Not the way I wanted it to go."
show k neutral
k "Ah, I'm sorry to hear that. I won't pry."
show k laugh
k "I guess three dates wasn't enough to see if someone's marriage material after all! Who knew."
jump p1d5pd_AfterEh

label p1d5pd_awesome:

if selectedDate == "Allie":
    jump p1d5pd_thirdAllie
if selectedDate == "Scarlett":
    jump p1d5pd_thirdScarlett
if selectedDate == "Terra":
    jump p1d5pd_thirdTerra
if selectedDate == "Violet":
    jump p1d5pd_thirdViolet
if selectedDate == "Yui":
    jump p1d5pd_thirdYui

label p1d5pd_thirdAllie:
"I probably shouldn't tell the whole truth, but enough of it should be good."
m "...It was awesome! I don't know how, but the more time I spend with Allie, the better it gets."
m "Being married to her would make every day an adventure... and I like the sound of that."
show k laugh
k "I'm sure it'd be an adventure, but the jury's out on if it's one you'd walk away from!"
show k happy
k "But I can see she makes you happy, and really, that counts for a lot nowadays."
show k bored
k "Though you might want to start wearing body armor, if you want to stay that way."
jump p1d5pd_advice

label p1d5pd_thirdScarlett:
m "...It was the best."
m "My connection with Scarlett's one of a kind, and there's no one I'd rather be beside me than her."
m "Being married to her would be like a dream come true."
show k sassy
k "Well, aren't you a romantic, [name]!"
show k flirt
k "But I'm happy to hear that. If it's you two, I'm sure that whatever you two face out there..."
show k laugh
k "...You'll be fine, as long as you stick together!"
show k worried
k "...And if she stops turning people into zombies."
m "Yeah, that's a conversation we have to have..."
show k laugh
k "Don't forget that in the prenup!"
jump p1d5pd_advice

label p1d5pd_thirdTerra:
#; NEED TO UPDATE THIS;;
m "It was nice! We didn't do anything too crazy, but... it didn't have to be."
show k flirt
k "I could tell! It was cute watching you guys."
show k laugh
k "Though to be honest, I wish your relationship would move along a little faster! This show's not getting any longer, you know."
show k happy
k "That said, I feel like you two would make a pretty good team in the long run."
jump p1d5pd_advice


label p1d5pd_thirdViolet:
m "Being with Violet makes me feel like we're on top of the world."
m "Somehow, she takes my breath away with how cool she can be... and at the same time, makes me laugh like a child alongside her."
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
jump p1d5pd_advice

label p1d5pd_thirdYui:
m "Yui's the most wonderful woman in the whole world."
m "Somehow, she can take the most normal things and turn them into irreplaceable memories."
m "More than anything, I just want to make more memories with her, every day."
m "...And make her happier than anyone's ever been."
show k surprised
k "Jeez, we're going to have to edit that to stop people from throwing up!"
show k sassy
k "...I get it, though. You, my friend, are luckier than anyone has any right to be."
show k laugh
k "Better pack your bags! I've got a feeling you'll be heading to the countryside soon!"
jump p1d5pd_advice

label p1d5pd_advice:
#; now that's a zinger
show k flirt
k "Who knew that three dates were all you needed to figure out if a marriage would last?"
show k surprised
k "If this TV gig doesn't work out, maybe I should become a marriage counselor. Hmm..."
m "..."
label p1d5pd_AfterEh:

show k neutral
k "Anyway, I'd love to stay and chat, but I've got to get some work done tonight to prep for the ending of the show."
show k happy
k "You know what, I could use some company! And it's not like you were up to anything."
show k laugh
"Kat reached her hand out to me. I put my hand in hers on instinct."
"With her hand in mine, she pulled me with her to..."
show bg Library with dissolve
stop music
play music MoveForward
"...the library?"
show k laugh
k "Now you're probably wondering, why did I bring you here of all places?"
m "You like to read?"
show k bored
k "Well, yes, but no."
show k annoyed
k "There's no internet for us goons, so here's where we store most of our information."
show k neutral
k "Records of every single run of the show... building and security details... guard schedules... and most importantly, salary records."
show k flirt
k "It's hidden in plain sight, as regular books!"
show k neutral
k "You need to know how to decipher them, though. They're pretty useless to the average person."
m "Interesting, and also a little unnecessary. Who here is going to read a book?"
show k sad
k "Oh, I knew the state of education was bad, but not this bad."
m "...It still doesn't answer why you brought me here."
show k happy
k "Well, you see, I have this lovely chair and table here that I do SO love to work on."
show k worried
k "And it's truly, truly exhausting for me to get up from this lovely arrangement to have to fetch each book I need to reference."
show k happy
k "...So..."
m "...You want me to grab your books for you, so you can just stay here."
show k flirt
k "I'm so glad you understand!"
show k worried
k "And you know, I'm doing everything I can to keep you alive, and it's just a teeny tiny favor..."
"I couldn't help but laugh at her mock pout."
m "Sure, Kat. It's the least I can do."
show k laugh
k "Great! Alright, to start, I need you to grab me {i}The Princess of Avoranda, 100 Easy Recipes for a Philosopher's Stone,{\i} and..."
show bg Black with dissolve
hide k with dissolve
"..."
"I regret everything."
"..."
stop music
play music PastSadness
show bg Library with dissolve
"This must be the 100th batch of books I've had to deliver. It's been hours!"
"Seriously, whoever designed this system should be shot."
#; funny because M designed this."
"I tried to read a few of the books I was delivering, but like Kat said, they just seemed like regular books."
show k laugh at pos50k with dissolve
k "...And that's a wrap! Thanks for the help, [name]."
show k flirt
k "I'll send you a thank you card for when you're off this island or something."
m "At that rate, that was pretty much slave labor."
show k laugh
k "I like to think of it as more of unpaid charity work!"
show k neutral
k "...You've got one last date tomorrow. Don't mess it up."
show k laugh
k "I'm curious, what's the first thing you're going to do when you're out of here?"
show k neutral
m "Honestly, I'm not sure."
m "Maybe try to figure out what my life was before, who knows."
show k happy
k "That's as good a start as any."
show k flirt
k "Well, I gotta get back to editing. 'Night, [name]."
m "See you, Kat."
hide k with dissolve
"Guess I'll head back to my room and call it a night."
show bg MansionIndoorsNight with dissolve #time:2
$ renpy.pause(delay = 1.0, hard = True)
show bg RoomNight with dissolve #time:2
$ renpy.pause(delay = 1.0, hard = True)
show bg Black with dissolve #time:2
stop music
"..."
play music ICanFeelItComing
"The alarms were deafening."
"We planned for every possibility we could, but it wasn't enough."
"We made it to the ship, but it still wasn't enough."
"Our one saving grace, the ship... wouldn't start."
"Someone tampered with it... and there's no time to fix it."
q "That's... that's it, then."
"I couldn't find the words to say."
m "...I love you."
q "..."
q "I love you too, [name]."
q "...I wish we could have met... anywhere but here."
"She held me in her arms with the last of her strength."
"All that's left to do is wait."
"...Goodbye, love."
jump MorningSelector
