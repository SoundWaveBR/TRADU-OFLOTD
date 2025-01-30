label P2Day5postDate:

$ currentDay=6
$ P2Date5=selectedDate

if P2Date5 == "Allie":
    $ selectedAffection = allieAffection
if P2Date5 == "Scarlett":
    $ selectedAffection = scarlettAffection
if P2Date5 == "Terra":
    $ selectedAffection = terraAffection
if P2Date5 == "Violet":
    $ selectedAffection = violetAffection
if P2Date5 == "Yui":
    $ selectedAffection = yuiAffection

#; 2 girls rank 2 now
play music PastSadness
show bg RoomNight with dissolve
"...Seems like a nice night for a walk."
#show bg MansionIndoorsNight time:2
show bg MansionNight with dissolve # time:2
show k surprised at pos50k with dissolve
k "Oh! Hey, [name]. What are you doing out here?"
m "Just going out for a walk. Care to join me?"
show k neutral
k "Sure, why not. I got a few minutes. How about we do a circle around the mansion grounds?"
m "Sounds good to me!"
show k happy
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) # loop:true

if P2Date5 == "Allie":
    k "So how'd your date with Allie go?"
elif P2Date5 == "Scarlett":
    k "So how'd your date with Scarlett go?"
elif P2Date5 == "Terra":
    k "So how'd your date with Terra go?"
elif P2Date5 == "Violet":
    k "So how'd your date with Violet go?"
elif P2Date5 == "Yui":
    k "So how'd your date with Yui go?"

# OLD FORMAT
# k "So how'd your date with [#P2Date5] go?"
m "Ah, are we already back to our daily interviews?"
m "Did the island run out of wine?"
show k laugh
k "That's wholly unrelated!"
show k annoyed
k "...But yes."
show k flirt
stop sound

if P2Date5 == "Allie":
    m "Anyway, my date with Allie today was..."
elif P2Date5 == "Scarlett":
    m "Anyway, my date with Scarlett today was..."
elif P2Date5 == "Terra":
    m "Anyway, my date with Terra today was..."
elif P2Date5 == "Violet":
    m "Anyway, my date with Violet today was..."
elif P2Date5 == "Yui":
    m "Anyway, my date with Yui today was..."

menu:
    #OLD UNTRANS: m "Anyway, my date with [#P2Date5] today was..."

    "Awesome":
        jump p2d5pd_awesome
    "Ehh":
        jump p2d5pd_ehh

label p2d5pd_ehh:
m "...Alright, I guess."
show k surprised
k "Oh, really! That's too bad."
show k neutral

if P2Date5 == "Allie":
    k "Allie said in a interview that she thought you two really connected, but I guess it wasn't both ways."
elif P2Date5 == "Scarlett":
    k "Scarlett said in a interview that she thought you two really connected, but I guess it wasn't both ways."
elif P2Date5 == "Terra":
    k "Terra said in a interview that she thought you two really connected, but I guess it wasn't both ways."
elif P2Date5 == "Violet":
    k "Violet said in a interview that she thought you two really connected, but I guess it wasn't both ways."
elif P2Date5 == "Yui":
    k "Yui said in a interview that she thought you two really connected, but I guess it wasn't both ways."
# OLD FORMAT k "[#P2Date5] said in a interview that she thought you two really connected, but I guess it wasn't both ways."
show k laugh
k "Well, doesn't matter. The audience thinks you did, and that's enough to keep you breathing!"
jump p2d5pd_advice


label p2d5pd_awesome:
    if selectedDate == "Allie":
        jump p2d5pd_secondAllie
    if selectedDate == "Scarlett":
        jump p2d5pd_secondScarlett
    if selectedDate == "Terra":
        jump p2d5pd_secondTerra
    if selectedDate == "Violet":
        jump p2d5pd_secondViolet
    if selectedDate == "Yui":
        jump p2d5pd_secondYui


label p2d5pd_secondAllie:
m "...Pretty great! There's never a dull moment with Allie."
m "I'm just scratching the surface, but I like what I see, and I really want to get to know her more."
show k happy
k "Interesting, interesting! That's good."
show k neutral
k "Allie's pretty out there as far as people go. I can see why she'd have a hard time opening up."
show k flirt
k "But from what I saw today, I'm sure if she would open up to anybody, it'd be you."
show k laugh
k "People thought she didn't have much of a chance here - I guess you two are proving them wrong!"
m "I guess so."
jump p2d5pd_advice

label p2d5pd_secondScarlett:
m "...Amazing. I feel like I really got to know the real Scarlett today."
m "And for the first time, I feel like I've truly been understood."
show k happy
k "I'm glad to hear that, [name]. Really."
show k neutral
k "Scarlett puts on a front that's nothing like how she really is - I'm glad you can see behind it."
show k happy
k "She must really trust you."
m "I'm glad she does, believe me."
show k laugh
k "More importantly though, Scarlett's fanbase has been ravenous for new content! From what I saw, I'd say you delivered."
show k neutral
k "I'm a solid 85\% sure you won't wake up in a torture chamber tomorrow morning. Good job, [name]!"
m "Thanks?"
jump p2d5pd_advice

label p2d5pd_secondTerra:
m "...Awesome. I have to admit..."
m "...Terra's very different from my initial impression of her."
m "I feel like I'm seeing the real her now, and... I like what I'm seeing."
show k laugh
k "I like the sound of that!"
show k flirt
k "Who would have thought you'd say something like this after your... unique... first date, huh?"
m "Life sure is funny."
jump p2d5pd_advice

label p2d5pd_secondViolet:
m "It was... wonderful. And that's not a word I say very often."
m "It's not every day where you get to spend it with a woman who can turn a kitchen into a warzone."
m "I can't remember the last time I had so much fun, and that's not the amnesia talking."
show k flirt
k "Violet really is something, ain't she!"
m "No kidding."
show k happy
k "I'd expect no less from the woman who's currently our audience favorite."
show k laugh
k "Whenever we get you both in the same room, ratings just soar through the roof!"
m "...I can't say I'm surprised to hear that."
jump p2d5pd_advice

label p2d5pd_secondYui:
m "...Like it was out of a fairy tale."
m "Yui and I spent the whole day, just taking in the nature, talking about home and family..."
m "She's totally wife material."
show k happy
k "Isn't she! Yui's amazing."
show k laugh
k "You know, before the show even started, she was my personal favorite."
m "I can see why."
m "She's got such a big heart. I'm in awe of her."
m "I really love that about her, that she can be so kind and thoughtful, even when life gives her a losing hand."
show k neutral
k "...Yui's really one of a kind, especially nowadays."
show k laugh
k "If you don't get the chance to be engaged to her by the end of this show, good luck ever getting a chance to!"
show k flirt
k "I've got a feeling that she has a long, long line of people wanting to date her after the show."
m "They'll have to get through me, first."
show k laugh
k "Oh, they will."
jump p2d5pd_advice

label p2d5pd_advice:
show k flirt
k "Keep it up with what you're doing! Our ratings have only been climbing higher and higher every day."
show k neutral
k "...But it's not time to celebrate just yet."
m "I know, don't worry. I'm sticking to the plan."
show k laugh
k "That's good to hear!"
show k bored
k "Seriously, if you got yourself killed by not following the plan at this point... you deserve it."
stop sound #stopsfx WalkingOnDirt
"...Looks like we've finished our walk."
show k flirt
k "Anyway, I gotta get back to work, but it was a nice break."
show k neutral
k "'Night, [name]."
m "'Night, Kat."
hide k with dissolve
#show bg MansionIndoorsNight time:2
show bg RoomNight with dissolve # time:2
"I walked back to my room, and plopped on my bed."
show bg Black with dissolve
"Time to get some shuteye..."

stop music
play music LoveTheme
#; Violet Flashback
"..."
"The scent of something delicious being freshly baked wafted through the kitchen."
"It's just the two of us."
q "Looks like this batch didn't turn out well either."
"She frowned."
m "Hey, on the bright side, I can at least tell it's bread this time."
"Uh oh. That wasn't the right thing to say."
q "It... has been a while, since I've done this. Sorry, [name], I... I wanted you to have something good."
"I reached for one of the pieces of bread."
q "Wait, I'm sure it's-"
"I took one bite, then wolfed the bread down like it was the last of its kind."
m "It's delicious!"
"I reached for another, to prove my point."
q "...You really mean it?"
"I took a moment to wolf down the second piece."
m "Cross my heart."
q "You're just saying that!"
"She smiled. Ah, that's the moment I've been waiting for."
"She hugged me with all her might."
q "...But I love that about you, you know?"
q "I love you, [name]."
"I held her tight."
m "I love you too."
"For a moment, the whole world was just me and her."
"And that was all that mattered."
"What I wouldn't give to have you back like this..."
jump MorningSelector
