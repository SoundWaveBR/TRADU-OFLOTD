label P1Day4postDate:

play music PastSadness
$ currentDay=5
$ P1Date4=selectedDate

if P1Date4 == "Allie":
    $ selectedAffection = allieAffection
if P1Date4 == "Scarlett":
    $ selectedAffection = scarlettAffection
if P1Date4 == "Terra":
    $ selectedAffection = terraAffection
if P1Date4 == "Violet":
    $ selectedAffection = violetAffection
if P1Date4 == "Yui":
    $ selectedAffection = yuiAffection

#; 2 girls rank 2 now

show bg RoomNight with dissolve # time:1
"I was feeling too restless after today's date to wait in my room, so I went for a walk downstairs."

if violetAffection == 2:
    jump p1d4pd_VioletCookie

show bg KitchenNight with dissolve # time:1
show k surprised at pos50k with dissolve
k "Oh! Hey, [name]. I was just about to go up to check in on you."
m "Hey there, Kat. What's up?"
show k neutral
k "Huh..."
show k annoyed
k "There were some fancy desserts here from last week, but I can't find them anymore."
show k bored
k "Guess I'll take that out of the Brothers Five's paychecks."
m "How do you know it was them?"
show k laugh #at pos50k
k "They're like clockwork."
show a surprised at pos20a with dissolve
a "..."
show a surprised
a "...*munch*..."
"Allie looked like a deer in the headlights on the other end of the kitchen. Kat hadn't seen her yet."
play sound BambooHit
hide a with dissolve
"She made direct eye contact with me, then hightailed it out."
"..."
jump p1d4pd_meetKat

label p1d4pd_VioletCookie:
show bg KitchenNight with dissolve # time:1
"I decided to walk to the kitchen, and opened the fridge."
"...!"
"Turns out there were some leftover cookies that Violet and I had made together."
"I grabbed a few and wolfed them down."
"Delicious."
show k happy at pos50k with dissolve
k "Got a case of the midnight munchies?"
m "I figured I'd do my civil duty and help finish the cookies Violet and I made."
show k flirt
k "Right. Only a good samaritan would finish all the cookies, so no one else would have to make that sacrifice."
m "I'm just too good of a person, I know. It gets me in trouble sometimes."
jump p1d4pd_meetKat

label p1d4pd_meetKat:
show k neutral
k "Anyway, I've been meaning to talk to you."
m "What's up?"
show k flirt
stop music
play music TechLive

if P1Date4 == "Allie":
    k "How'd your date with Allie today go?"
elif P1Date4 == "Scarlett":
    k "How'd your date with Scarlett today go?"
elif P1Date4 == "Terra":
    k "How'd your date with Terra today go?"
elif P1Date4 == "Violet":
    k "How'd your date with Violet today go?"
elif P1Date4 == "Yui":
    k "How'd your date with Yui today go?"

menu:
    #k "How'd your date with [#P1Date4] today go?"

    "Awesome":
        jump p1d4pd_awesome
    "Ehh":
        jump p1d4pd_ehh

label p1d4pd_ehh:
m "It was... alright, I guess."
show k surprised
k "Oh, really! That's too bad."
show k neutral
if P1Date4 == "Allie":
    k "Allie said in a interview after your date that she thought you two really connected."
elif P1Date4 == "Scarlett":
    k "Scarlett said in a interview after your date that she thought you two really connected."
elif P1Date4 == "Terra":
    k "Terra said in a interview after your date that she thought you two really connected."
elif P1Date4 == "Violet":
    k "Violet said in a interview after your date that she thought you two really connected."
elif P1Date4 == "Yui":
    k "Yui said in a interview after your date that she thought you two really connected."
# OLD UNTRANSLATEABLE FORMAT
#k "[#P1Date4] said in a interview after your date that she thought you two really connected."

show k laugh
k "Well, doesn't matter. The audience thinks you did, and that'll keep you alive!"
m "I guess so..."
jump p1d4pd_advice

label p1d4pd_awesome:

    if selectedDate == "Allie":
        jump p1d4pd_secondAllie
    if selectedDate == "Scarlett":
        jump p1d4pd_secondScarlett
    if selectedDate == "Terra":
        jump p1d4pd_secondTerra
    if selectedDate == "Violet":
        jump p1d4pd_secondViolet
    if selectedDate == "Yui":
        jump p1d4pd_secondYui

label p1d4pd_secondAllie:
m "It was pretty great! There's never a dull moment with Allie."
m "I'm just scratching the surface, but I like what I see, and I really want to get to know her more."
show k happy
k "Interesting, interesting! That's good."
show k neutral
k "Allie's pretty out there as far as people go. I can see why she'd have a hard time opening up."
show k flirt
k "But from what I saw today, I'm sure if anyone can, it'd be you."
show k laugh
k "People thought she didn't have much of a chance here, but I guess you two are proving them wrong!"
jump p1d4pd_advice

label p1d4pd_secondScarlett:
m "It was amazing. I feel like I really got to know the real Scarlett today."
m "For the first time... I think I feel like I've truly been understood."
show k happy
k "I'm glad to hear that, [name]. Really."
show k neutral
k "Scarlett puts on a front that's nothing like how she really is... and I'm glad you can see behind it."
show k happy
k "She must really trust you."
m "I'm glad she does, believe me."
show k laugh
k "More importantly though, Scarlett's fanbase has been ravenous for new content. From what I saw, you delivered today!"
show k neutral
k "I'm a solid 85\% sure you won't wake up in a torture chamber tomorrow morning. Good job, [name]!"
m "Thanks?"
jump p1d4pd_advice

label p1d4pd_secondTerra:
m "It was great. I have to admit..."
m "...Terra's very different from my initial impression of her."
m "I feel like I'm seeing the real her now, and I like that."
show k laugh
k "I like the sound of that!"
show k flirt
k "Who would have thought you'd say something like this after your... rather unique first date, huh?"
m "Life sure has a sense of humor."

jump p1d4pd_advice

label p1d4pd_secondViolet:
m "It was wonderful. And that's not a word I say very often."
m "It's not every day where you get to spend it with a woman who can turn a kitchen into a warzone."
m "...I can't remember the last time I had so much fun, and that's not the amnesia talking."
show k flirt
k "Violet really is something, ain't she!"
m "No kidding."
show k happy
k "I'd expect no less from the woman who's currently our audience favorite."
show k laugh
k "Whenever we get you both in the same room, ratings just soar through the roof!"
m "I can't say I'm surprised to hear that!"

jump p1d4pd_advice

label p1d4pd_secondYui:
m "It felt like it was out of a fairy tale."
m "Yui and I spent the whole day just taking in the nature, talking about home and family..."
m "She's totally wife material."
show k happy
k "Isn't she! Yui's amazing."
show k laugh
k "You know, before the show even started, she was my personal favorite."
m "I can see why."
m "She's got such a big heart. I'm in awe of her."
m "I really love that about her.... that she can be so kind and thoughtful, even when life gives her a losing hand."
show k neutral
k "Yui's really one of a kind, especially nowadays."
show k laugh
k "If you don't get the chance to be engaged to her by the end of this show, good luck ever getting a chance to!"
show k flirt
k "I've got a feeling that she has a long, long line of people wanting to date her after the show."
m "They'll have to get through me, first."
show k laugh
k "Oh, they will."

label p1d4pd_advice:

stop music
play music PastSadness
show k flirt


if P1Date1 == "Allie" and P1Date2 == "Scarlett":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Allie and Scarlett!"
elif P1Date1 == "Allie" and P1Date2 == "Terra":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Allie and Terra!"
elif P1Date1 == "Allie" and P1Date2 == "Violet":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Allie and Violet!"
elif P1Date1 == "Allie" and P1Date2 == "Yui":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Allie and Yui!"
elif P1Date1 == "Scarlett" and P1Date2 == "Allie":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Scarlett and Allie!"
elif P1Date1 == "Scarlett" and P1Date2 == "Terra":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Scarlett and Terra!"
elif P1Date1 == "Scarlett" and P1Date2 == "Violet":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Scarlett and Violet!"
elif P1Date1 == "Scarlett" and P1Date2 == "Yui":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Scarlett and Yui!"
elif P1Date1 == "Terra" and P1Date2 == "Allie":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Terra and Allie!"
elif P1Date1 == "Terra" and P1Date2 == "Scarlett":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Terra and Scarlett!"
elif P1Date1 == "Terra" and P1Date2 == "Violet":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Terra and Violet!"
elif P1Date1 == "Terra" and P1Date2 == "Yui":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Terra and Yui!"
elif P1Date1 == "Violet" and P1Date2 == "Allie":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Violet and Allie!"
elif P1Date1 == "Violet" and P1Date2 == "Scarlett":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Violet and Scarlett!"
elif P1Date1 == "Violet" and P1Date2 == "Terra":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Violet and Terra!"
elif P1Date1 == "Violet" and P1Date2 == "Yui":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Violet and Yui!"
elif P1Date1 == "Yui" and P1Date2 == "Allie":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Yui and Allie!"
elif P1Date1 == "Yui" and P1Date2 == "Scarlett":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Yui and Scarlett!"
elif P1Date1 == "Yui" and P1Date2 == "Terra":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Yui and Terra!"
elif P1Date1 == "Yui" and P1Date2 == "Violet":
    "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between Yui and Violet!"

# OLD UNTRANS FORMAT
#k "Anyway, you're probably safe for at least another day, thanks to the ongoing rivalry between [#P1Date1] and [#P1Date2]!"

show k happy
k "The stakes are rising, and so our are precious ratings - so without further ado, it's time for phase three!"
show k neutral
k "You've only got one date left with each of them before the final day."
show k flirt
k "So make them count! You're not out of the woods just yet."
m "Will do!"
show k laugh
k "Alright, good. Well, I need to get back to preparing for tomorrow's show."
show k neutral
k "And you better rest up for tomorrow. You only get one first third date with a girl, right?"
m "Sounds good to me, Kat."
show k flirt
k "Seeya later, [name]."
m "Good night, Kat."
show k neutral
m "And... thanks for the help. I realize I'd probably be screwed without you."
show k serious
k "...Don't thank me yet."
hide k with dissolve
show bg RoomNight with dissolve # time:2
"I walked back to my room, and plopped on my bed."
show bg Black with dissolve
"Time to get some shuteye."

stop music
play music MiamiNights
"..."
q "Alright, we're out of the mansion... next stop, the beach."
q "I told you the staff wouldn't suspect a thing!"
m "That's because nobody's been stupid enough to try to escape till now."
q "Maybe people should have been a little more stupid, a little sooner."
m "Easier said than done."
"She grabbed my hand and pulled me along."
play sound RunGrass # loop:true
q "We'll go through the forest. Come on!"
"We ran through the forest as if the devil were chasing us - the truth was not far from it."
stop sound #@stopsfx RunOnGrass
q "Okay... I can see the pier now, and the boat. We're this close to getting out of here."
"She always put on her bravest face when she was afraid."
q "We're going to make it... right?"
m "Of course. The boat's just a little further, and no one's on our tail."
q "I... can't believe it. We're finally getting out of here. We're finally..."
q "We're finally going to leave, [name]."
m "About time, if you ask me."
q "I've dreamed of this moment every day since... who knows how long we've been trapped here by now."
q "But I never thought I could escape till I got to know you."
"I laughed."
m "You're giving me too much credit! It was your idea."
m "Find any other sane person, and they would have told you the same things."
q "Sane people didn't try to escape with me."
m "I wouldn't have stayed sane if it weren't for you, though."
"She laughed. That was my favorite sound."
q "Let's get back to matters at hand."
q "We both know that this is where the rubber meets the road."
m "...Yeah."
q "Now it's just a mad dash to the finish."
q "You ready to run?"
m "No."
q "...?"
m "I'm kidding, let's go."
"That favorite sound of mine once more - I hope it's not the last time I hear it."
jump MorningSelector
