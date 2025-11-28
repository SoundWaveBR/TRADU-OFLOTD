label P1Day2postDate:

$ currentDay=3
$ P1Date2=selectedDate
play music PastSadness
show bg MansionIndoorsNight with dissolve

"I was about to enter my room, when I felt a familiar tap on my shoulder."
show k neutral at pos50k with dissolve
k "Hey there, [name]. Got a minute?"
show k laugh

if P1Date1 == "Allie" and P1Date2 == "Scarlett":
    k "I want to make Allie and Scarlett jealous - It'd be good for ratings!"
elif P1Date1 == "Allie" and P1Date2 == "Terra":
    k "I want to make Allie and Terra jealous - It'd be good for ratings!"
elif P1Date1 == "Allie" and P1Date2 == "Violet":
    k "I want to make Allie and Violet jealous - It'd be good for ratings!"
elif P1Date1 == "Allie" and P1Date2 == "Yui":
    k "I want to make Allie and Yui jealous - It'd be good for ratings!"
elif P1Date1 == "Scarlett" and P1Date2 == "Allie":
    k "I want to make Scarlett and Allie jealous - It'd be good for ratings!"
elif P1Date1 == "Scarlett" and P1Date2 == "Terra":
    k "I want to make Scarlett and Terra jealous - It'd be good for ratings!"
elif P1Date1 == "Scarlett" and P1Date2 == "Violet":
    k "I want to make Scarlett and Violet jealous - It'd be good for ratings!"
elif P1Date1 == "Scarlett" and P1Date2 == "Yui":
    k "I want to make Scarlett and Yui jealous - It'd be good for ratings!"
elif P1Date1 == "Terra" and P1Date2 == "Allie":
    k "I want to make Terra and Allie jealous - It'd be good for ratings!"
elif P1Date1 == "Terra" and P1Date2 == "Scarlett":
    k "I want to make Terra and Scarlett jealous - It'd be good for ratings!"
elif P1Date1 == "Terra" and P1Date2 == "Violet":
    k "I want to make Terra and Violet jealous - It'd be good for ratings!"
elif P1Date1 == "Terra" and P1Date2 == "Yui":
    k "I want to make Terra and Yui jealous - It'd be good for ratings!"
elif P1Date1 == "Violet" and P1Date2 == "Allie":
    k "I want to make Violet and Allie jealous - It'd be good for ratings!"
elif P1Date1 == "Violet" and P1Date2 == "Scarlett":
    k "I want to make Violet and Scarlett jealous - It'd be good for ratings!"
elif P1Date1 == "Violet" and P1Date2 == "Terra":
    k "I want to make Violet and Terra jealous - It'd be good for ratings!"
elif P1Date1 == "Violet" and P1Date2 == "Yui":
    k "I want to make Violet and Yui jealous - It'd be good for ratings!"
elif P1Date1 == "Yui" and P1Date2 == "Allie":
    k "I want to make Yui and Allie jealous - It'd be good for ratings!"
elif P1Date1 == "Yui" and P1Date2 == "Scarlett":
    k "I want to make Yui and Scarlett jealous - It'd be good for ratings!"
elif P1Date1 == "Yui" and P1Date2 == "Terra":
    k "I want to make Yui and Terra jealous - It'd be good for ratings!"
elif P1Date1 == "Yui" and P1Date2 == "Violet":
    k "I want to make Yui and Violet jealous - It'd be good for ratings!"

# k "I want to make [#P1Date1] and [#P1Date2] jealous - It'd be good for ratings!"
m "Sorry, what?"
show k annoyed
k "You're no fun. Anyway..."
play sound DoorOpen
"She opened the door to my room, and walked inside."
show bg RoomNight with dissolve
play sound DoorClose
"I followed suit."
show k happy
k "I've got some good news!"
m "I'm all ears."
show k flirt
k "Turns out my strategy worked! We've gotten enough ratings to avoid early canning."
show k happy
if P1Date1 == "Allie":
    k "Don't get me wrong, people loved it when you and Allie were the main ship, but..."
elif P1Date1 == "Scarlett":
    k "Don't get me wrong, people loved it when you and Scarlett were the main ship, but..."
elif P1Date1 == "Terra":
    k "Don't get me wrong, people loved it when you and Terra were the main ship, but..."
elif P1Date1 == "Violet":
    k "Don't get me wrong, people loved it when you and Violet were the main ship, but..."
elif P1Date1 == "Yui":
    k "Don't get me wrong, people loved it when you and Yui were the main ship, but..."

show k surprised

if P1Date2 == "Allie":
    "Now, with Allie as some serious competition?"
elif P1Date2 == "Scarlett":
    "Now, with Scarlett as some serious competition?"
elif P1Date2 == "Terra":
    "Now, with Terra as some serious competition?"
elif P1Date2 == "Violet":
    "Now, with Violet as some serious competition?"
elif P1Date2 == "Yui":
    "Now, with Yui as some serious competition?"

# OLD UNTRANSLATEABLE FORMAT
#k "Don't get me wrong, people loved it when you and [#P1Date1] were the main ship, but..."
# show k surprised
#k "Now, with [#P1Date2] as some serious competition?"


show k laugh
k "Let's just say online threads went from optimistic and united to downright murderous."
m "Well, I'm glad to hear I get to live another day."
show k happy
k "For now, at least. But that'll change quickly if our viewers don't feel like your relationships with both of them are progressing!"
hide k with dissolve
"Kat laughed, then took a seat on my bed."
show bg KatInYourRoom with dissolve
stop music
play music TechLive

# OLD UNTRANSLATEABLE FORMAT
# k "You know, I'm curious how you're feeling about [#P1Date1] and [#P1Date2]."

if P1Date1 == "Allie" and P1Date2 == "Scarlett":
    k "You know, I'm curious how you're feeling about Allie and Scarlett."
elif P1Date1 == "Allie" and P1Date2 == "Terra":
    k "You know, I'm curious how you're feeling about Allie and Terra."
elif P1Date1 == "Allie" and P1Date2 == "Violet":
    k "You know, I'm curious how you're feeling about Allie and Violet."
elif P1Date1 == "Allie" and P1Date2 == "Yui":
    k "You know, I'm curious how you're feeling about Allie and Yui."
elif P1Date1 == "Scarlett" and P1Date2 == "Allie":
    k "You know, I'm curious how you're feeling about Scarlett and Allie."
elif P1Date1 == "Scarlett" and P1Date2 == "Terra":
    k "You know, I'm curious how you're feeling about Scarlett and Terra."
elif P1Date1 == "Scarlett" and P1Date2 == "Violet":
    k "You know, I'm curious how you're feeling about Scarlett and Violet."
elif P1Date1 == "Scarlett" and P1Date2 == "Yui":
    k "You know, I'm curious how you're feeling about Scarlett and Yui."
elif P1Date1 == "Terra" and P1Date2 == "Allie":
    k "You know, I'm curious how you're feeling about Terra and Allie."
elif P1Date1 == "Terra" and P1Date2 == "Scarlett":
    k "You know, I'm curious how you're feeling about Terra and Scarlett."
elif P1Date1 == "Terra" and P1Date2 == "Violet":
    k "You know, I'm curious how you're feeling about Terra and Violet."
elif P1Date1 == "Terra" and P1Date2 == "Yui":
    k "You know, I'm curious how you're feeling about Terra and Yui."
elif P1Date1 == "Violet" and P1Date2 == "Allie":
    k "You know, I'm curious how you're feeling about Violet and Allie."
elif P1Date1 == "Violet" and P1Date2 == "Scarlett":
    k "You know, I'm curious how you're feeling about Violet and Scarlett."
elif P1Date1 == "Violet" and P1Date2 == "Terra":
    k "You know, I'm curious how you're feeling about Violet and Terra."
elif P1Date1 == "Violet" and P1Date2 == "Yui":
    k "You know, I'm curious how you're feeling about Violet and Yui."
elif P1Date1 == "Yui" and P1Date2 == "Allie":
    k "You know, I'm curious how you're feeling about Yui and Allie."
elif P1Date1 == "Yui" and P1Date2 == "Scarlett":
    k "You know, I'm curious how you're feeling about Yui and Scarlett."
elif P1Date1 == "Yui" and P1Date2 == "Terra":
    k "You know, I'm curious how you're feeling about Yui and Terra."
elif P1Date1 == "Yui" and P1Date2 == "Violet":
    k "You know, I'm curious how you're feeling about Yui and Violet."


menu:
    k "Between those two, do you have a favorite?"


    # OLD NON-TRANSLATEABLE FORMAT
    #"[#P1Date1]":
    #    jump p1d2pd_sd1
    #"[#P1Date2]":
    #    jump p1d2pd_sd2

    # NEW FORMAT TO ALLOW TRANSLATION for P1DATE1
    "Allie" if P1Date1 == "Allie":
        jump p1d2pd_sd1

    "Scarlett" if P1Date1 == "Scarlett":
        jump p1d2pd_sd1

    "Terra" if P1Date1 == "Terra":
        jump p1d2pd_sd1

    "Violet" if P1Date1 == "Violet":
        jump p1d2pd_sd1

    "Yui" if P1Date1 == "Yui":
        jump p1d2pd_sd1

    # NEW FORMAT TO ALLOW TRANSLATION for P1DATE2
    "Allie" if P1Date2 == "Allie":
        jump p1d2pd_sd2

    "Scarlett" if P1Date2 == "Scarlett":
        jump p1d2pd_sd2

    "Terra" if P1Date2 == "Terra":
        jump p1d2pd_sd2

    "Violet" if P1Date2 == "Violet":
        jump p1d2pd_sd2

    "Yui" if P1Date2 == "Yui":
        jump p1d2pd_sd2





    #"Allie" if P1Date1 == "Allie"
    #   jump p1d2pd_sd1

    # "Allie" if P1Date2 == "Allie"
    #   jump p1d2pd_sd2

label p1d2pd_sd1:

$ favoriteDate=P1Date1

if allieAffection == 1 and favoriteDate != "Allie":
    $ nonfavoriteDate = "Allie"
if scarlettAffection == 1 and favoriteDate != "Scarlett":
    $ nonfavoriteDate = "Scarlett"
if terraAffection == 1 and favoriteDate != "Terra":
    $ nonfavoriteDate = "Terra"
if violetAffection == 1 and favoriteDate != "Violet":
    $ nonfavoriteDate = "Violet"
if yuiAffection == 1 and favoriteDate != "Yui":
    $ nonfavoriteDate = "Yui"
#m "I think I have a better connection with [#P1Date1] right now."

if P1Date1 == "Allie":
    m "I think I have a better connection with Allie right now."
    jump p1d2pd_FlavorCommentAllie

if P1Date1 == "Scarlett":
    m "I think I have a better connection with Scarlett right now."
    jump p1d2pd_FlavorCommentScarlett
if P1Date1 == "Terra":
    m "I think I have a better connection with Terra right now."
    jump p1d2pd_FlavorCommentTerra
if P1Date1 == "Violet":
    m "I think I have a better connection with Violet right now."
    jump p1d2pd_FlavorCommentViolet
if P1Date1 == "Yui":
    m "I think I have a better connection with Yui right now."
    jump p1d2pd_FlavorCommentYui

label p1d2pd_FlavorCommentAllie:
m "She makes every moment exciting, and... I can't get enough of that."
jump p1d2pd_AfterFlavorComment

label p1d2pd_FlavorCommentScarlett:
m "It's amazing how brilliant she is. And I can't ever quite place her - she's fascinating."
jump p1d2pd_AfterFlavorComment

label p1d2pd_FlavorCommentTerra:
m "Say what you want about her... it's never boring with Terra."
#m: I just feel so at home with Terra... we could be doing anything together, and I know I'd love it."
jump p1d2pd_AfterFlavorComment

label p1d2pd_FlavorCommentViolet:
m "I don't know as much as I'd like about Violet just yet, but... I know more than anything that I just want to keep learning more about her."
jump p1d2pd_AfterFlavorComment

label p1d2pd_FlavorCommentYui:
m "It's Yui, you know? It's practically self-explanatory. She's the best."
jump p1d2pd_AfterFlavorComment

label p1d2pd_AfterFlavorComment:
k "Ah, I had a feeling you'd say that. And you're right to say that!"
k "Well, we'll see where things go with her. Something tells me you'll get a chance to hang out with her again tomorrow!"
jump p1d2pd_last_comment

label p1d2pd_sd2:
    
$ favoriteDate=P1Date2

if allieAffection == 1 and favoriteDate != "Allie":
    $ nonfavoriteDate = "Allie"
if scarlettAffection == 1 and favoriteDate != "Scarlett":
    $ nonfavoriteDate = "Scarlett"
if terraAffection == 1 and favoriteDate != "Terra":
    $ nonfavoriteDate = "Terra"
if violetAffection == 1 and favoriteDate != "Violet":
    $ nonfavoriteDate = "Violet"
if yuiAffection == 1 and favoriteDate != "Yui":
    $ nonfavoriteDate = "Yui"

#m "Though I've known her for less time, I think I like [#P1Date2] more right now."

if P1Date2 == "Allie":
    m "Though I've known her for less time, I think I like Allie more right now."
    jump p1d2pd_FlavorCommentAllie2
if P1Date2 == "Scarlett":
    m "Though I've known her for less time, I think I like Scarlett more right now."
    jump p1d2pd_FlavorCommentScarlett2
if P1Date2 == "Terra":
    m "Though I've known her for less time, I think I like Terra more right now."
    jump p1d2pd_FlavorCommentTerra2
if P1Date2 == "Violet":
    m "Though I've known her for less time, I think I like Violet more right now."
    jump p1d2pd_FlavorCommentViolet2
if P1Date2 == "Yui":
    m "Though I've known her for less time, I think I like Yui more right now."
    jump p1d2pd_FlavorCommentYui2

label p1d2pd_FlavorCommentAllie2:
m "She makes every moment exciting, and... I just can't get enough of that."
jump p1d2pd_AfterFlavorComment2

label p1d2pd_FlavorCommentScarlett2:
m "It's amazing how brilliant she is. And I can't ever quite place her. She's fascinating."
jump p1d2pd_AfterFlavorComment2

label p1d2pd_FlavorCommentTerra2:
m "Say what you will about Terra... it's always exciting to be around her."
#m: I just feel so at home with Terra... we could be doing anything together, and I know I'd love it."
jump p1d2pd_AfterFlavorComment2

label p1d2pd_FlavorCommentViolet2:
m "I don't know as much as I'd like about Violet just yet, but... I know more than anything that I just want to keep learning more about her."
jump p1d2pd_AfterFlavorComment2

label p1d2pd_FlavorCommentYui2:
m "It's Yui, you know? It's practically self-explanatory. She's the best."
jump p1d2pd_AfterFlavorComment2

label p1d2pd_AfterFlavorComment2:

k "Really! Well, I can't say I'm too surprised. But maybe just a little."
k "Let's see where things go with her. Something tells me you'll be hanging out with her again soon enough!"
jump p1d2pd_last_comment

label p1d2pd_last_comment:

stop music
play music PastSadness
show bg RoomNight with dissolve
show k laugh at pos50k with dissolve
k "Anyway, that's it for today."
show k neutral
k "Keep it up, and who knows... you might just be the first one to make it out of here."
show k neutral
k "'Night, [name]."
m "Good night, Kat."
hide k with dissolve
"She left my room, closing the door behind her."
show bg Black with dissolve
"Guess it's time to turn in for the night."
stop music
show bg Black with dissolve

"..."

#; Day2Flashback
play music LeavingHome
"...?"
"I see waves crash soundlessly against the shore, and dissolve to nothing before they reach my feet."
"This must be my dream."
"She's next to me."
"I can't make out her face, or even hear her voice, but I know it's her. The way the pale moonlight dances in her hair is so nostalgic."
q "You look like you've seen a ghost, [name]!"
"...You. Somehow, I can't see your face, nor hear your voice... but I know it's you."
m "I'm fine, don't worry about it."
"I hear my own voice speaking, as if it were coming through an old cassette."
q "Are you thinking about what's going on out there now?"
m "Ten bucks that it's better on this side."
m "Out there, every day's a fight to stay alive. Here, at least there's food. Shelter. A place to call home. And most importantly, high-speed AND unlimited internet."
"I reach for her hand, and hold it tight."
m "...And people that love you."
q "...I know. And I love you too."
q "I know how lucky I am to be here, but... I still want to see the other side."
m "Why? You wouldn't survive a day out there. Same goes for me."
q "Because it's real! It's real life."
q "Where things happen that aren't planned by some producer, where living isn't just following a script."
q "I'd do anything for just a taste of it."
m "...We've been over this."
q "...I know."
q "I'm just so tired of this, I..."
q "What the hell are we doing here, [name]?"
m "..."
"I felt the same way she did, but there was nothing we could do. Not if we valued our lives."
"There's no escaping from here alive."
m "We're living another day."
q "..."
q "But what are we living for?"
"I sighed."
m "You really want to see the other side that badly?"
q "Yes."
"I laughed - when she had that look in her eye, I knew there was no convincing her otherwise. Even if she had to go alone, she'd see it through."
"...And I loved her for that."
m "I guess you'll owe me ten bucks pretty soon."
"She laughed."
q "You'll be the judge of that."
$ currentDay=3
jump MorningSelector
