label P2Day2postDate:

$ currentDay=3
$ P2Date2=selectedDate

play music PastSadness
show bg MansionIndoorsNight with dissolve
"I was about to enter my room, when I felt a familiar tap on my shoulder."
show k flirt at pos50k with dissolve
k "Hey there, [name]. Got a minute?"
show k laugh


if P2Date1 == "Allie" and P2Date2 == "Scarlett":
    k "Let me just make sure Allie or Scarlett see me come in here... fan some flames..."
elif P2Date1 == "Allie" and P2Date2 == "Terra":
    k "Let me just make sure Allie or Terra see me come in here... fan some flames..."
elif P2Date1 == "Allie" and P2Date2 == "Violet":
    k "Let me just make sure Allie or Violet see me come in here... fan some flames..."
elif P2Date1 == "Allie" and P2Date2 == "Yui":
    k "Let me just make sure Allie or Yui see me come in here... fan some flames..."
elif P2Date1 == "Scarlett" and P2Date2 == "Allie":
    k "Let me just make sure Scarlett and Allie see me come in here... fan some flames..."
elif P2Date1 == "Scarlett" and P2Date2 == "Terra":
    k "Let me just make sure Scarlett and Terra see me come in here... fan some flames..."
elif P2Date1 == "Scarlett" and P2Date2 == "Violet":
    k "Let me just make sure Scarlett and Violet see me come in here... fan some flames..."
elif P2Date1 == "Scarlett" and P2Date2 == "Yui":
    k "Let me just make sure Scarlett and Yui see me come in here... fan some flames..."
elif P2Date1 == "Terra" and P2Date2 == "Allie":
    k "Let me just make sure Terra and Allie see me come in here... fan some flames..."
elif P2Date1 == "Terra" and P2Date2 == "Scarlett":
    k "Let me just make sure Terra and Scarlett see me come in here... fan some flames..."
elif P2Date1 == "Terra" and P2Date2 == "Violet":
    k "Let me just make sure Terra and Violet see me come in here... fan some flames..."
elif P2Date1 == "Terra" and P2Date2 == "Yui":
    k "Let me just make sure Terra and Yui see me come in here... fan some flames..."
elif P2Date1 == "Violet" and P2Date2 == "Allie":
    k "Let me just make sure Violet and Allie see me come in here... fan some flames..."
elif P2Date1 == "Violet" and P2Date2 == "Scarlett":
    k "Let me just make sure Violet and Scarlett see me come in here... fan some flames..."
elif P2Date1 == "Violet" and P2Date2 == "Terra":
    k "Let me just make sure Violet and Terra see me come in here... fan some flames..."
elif P2Date1 == "Violet" and P2Date2 == "Yui":
    k "Let me just make sure Violet and Yui see me come in here... fan some flames..."
elif P2Date1 == "Yui" and P2Date2 == "Allie":
    k "Let me just make sure Yui and Allie see me come in here... fan some flames..."
elif P2Date1 == "Yui" and P2Date2 == "Scarlett":
    k "Let me just make sure Yui and Scarlett see me come in here... fan some flames..."
elif P2Date1 == "Yui" and P2Date2 == "Terra":
    k "Let me just make sure Yui and Terra see me come in here... fan some flames..."
elif P2Date1 == "Yui" and P2Date2 == "Violet":
    k "Let me just make sure Yui and Violet see me come in here... fan some flames..."
# old untrans format
# k "Let me just make sure [#P2Date1] or [#P2Date2] see me come in here... fan some flames..."
m "...Sorry, what?"
show k happy
play sound DoorOpen
"Kat looked around, smiled, then went into my room."
show bg RoomNight with dissolve
play sound DoorClose
"I followed suit."
show k neutral
k "First, the good news."
show k flirt
k "Thanks to my plan, we've gotten enough ratings to avoid early canning!"
show k happy

if P2Date1 == "Allie" and P2Date2 == "Scarlett":
    k "People loved it when you and Allie were the main ship, but loved it even more after Scarlett kicked off this competition."
elif P2Date1 == "Allie" and P2Date2 == "Terra":
    k "People loved it when you and Allie were the main ship, but loved it even more after Terra kicked off this competition."
elif P2Date1 == "Allie" and P2Date2 == "Violet":
    k "People loved it when you and Allie were the main ship, but loved it even more after Violet kicked off this competition."
elif P2Date1 == "Allie" and P2Date2 == "Yui":
    k "People loved it when you and Allie were the main ship, but loved it even more after Yui kicked off this competition."
elif P2Date1 == "Scarlett" and P2Date2 == "Allie":
    k "People loved it when you and Scarlett were the main ship, but loved it even more after Allie kicked off this competition."
elif P2Date1 == "Scarlett" and P2Date2 == "Terra":
    k "People loved it when you and Scarlett were the main ship, but loved it even more after Terra kicked off this competition."
elif P2Date1 == "Scarlett" and P2Date2 == "Violet":
    k "People loved it when you and Scarlett were the main ship, but loved it even more after Violet kicked off this competition."
elif P2Date1 == "Scarlett" and P2Date2 == "Yui":
    k "People loved it when you and Scarlett were the main ship, but loved it even more after Yui kicked off this competition."
elif P2Date1 == "Terra" and P2Date2 == "Allie":
    k "People loved it when you and Terra were the main ship, but loved it even more after Allie kicked off this competition."
elif P2Date1 == "Terra" and P2Date2 == "Scarlett":
    k "People loved it when you and Terra were the main ship, but loved it even more after Scarlett kicked off this competition."
elif P2Date1 == "Terra" and P2Date2 == "Violet":
    k "People loved it when you and Terra were the main ship, but loved it even more after Violet kicked off this competition."
elif P2Date1 == "Terra" and P2Date2 == "Yui":
    k "People loved it when you and Terra were the main ship, but loved it even more after Yui kicked off this competition."
elif P2Date1 == "Violet" and P2Date2 == "Allie":
    k "People loved it when you and Violet were the main ship, but loved it even more after Allie kicked off this competition."
elif P2Date1 == "Violet" and P2Date2 == "Scarlett":
    k "People loved it when you and Violet were the main ship, but loved it even more after Scarlett kicked off this competition."
elif P2Date1 == "Violet" and P2Date2 == "Terra":
    k "People loved it when you and Violet were the main ship, but loved it even more after Terra kicked off this competition."
elif P2Date1 == "Violet" and P2Date2 == "Yui":
    k "People loved it when you and Violet were the main ship, but loved it even more after Yui kicked off this competition."
elif P2Date1 == "Yui" and P2Date2 == "Allie":
    k "People loved it when you and Yui were the main ship, but loved it even more after Allie kicked off this competition."
elif P2Date1 == "Yui" and P2Date2 == "Scarlett":
    k "People loved it when you and Yui were the main ship, but loved it even more after Scarlett kicked off this competition."
elif P2Date1 == "Yui" and P2Date2 == "Terra":
    k "People loved it when you and Yui were the main ship, but loved it even more after Terra kicked off this competition."
elif P2Date1 == "Yui" and P2Date2 == "Violet":
    k "People loved it when you and Yui were the main ship, but loved it even more after Violet kicked off this competition."

# OLD UNTRANS FORMAT
#k "People loved it when you and [#P2Date1] were the main ship, but loved it even more after [#P2Date2] kicked off this competition."
m "I'm glad to hear I get to live another day."
show k neutral
k "For now, at least. But that can change on a dime, so keep it up."
stop music
play music TechLive
#show k neutral
# k "Also... I'm curious how you're feeling about [#P2Date1] and [#P2Date2]."
#show k happy
menu:
    k "Between those two, do you have a favorite?"

    # NEW FORMAT TO ALLOW TRANSLATION for P2DATE1
    "Allie" if P2Date1 == "Allie":
        jump p2d2pd_sd1

    "Scarlett" if P2Date1 == "Scarlett":
        jump p2d2pd_sd1

    "Terra" if P2Date1 == "Terra":
        jump p2d2pd_sd1

    "Violet" if P2Date1 == "Violet":
        jump p2d2pd_sd1

    "Yui" if P2Date1 == "Yui":
        jump p2d2pd_sd1

    # NEW FORMAT TO ALLOW TRANSLATION for P2DATE2
    "Allie" if P2Date2 == "Allie":
        jump p2d2pd_sd2

    "Scarlett" if P2Date2 == "Scarlett":
        jump p2d2pd_sd2

    "Terra" if P2Date2 == "Terra":
        jump p2d2pd_sd2

    "Violet" if P2Date2 == "Violet":
        jump p2d2pd_sd2

    "Yui" if P2Date2 == "Yui":
        jump p2d2pd_sd2

    # NON-TRANSLATED ORIGINAL
    #"[#P2Date1]":
    #    jump p2d2pd_sd1
    #"[#P2Date2]":
    #    jump p2d2pd_sd2

    #"Allie" if P2Date1 == "Allie"
    #   jump p2d2pd_sd1

    # "Allie" if P2Date2 == "Allie"
    #   jump p2d2pd_sd2

label p2d2pd_sd1:

$ P2favoriteDate=P2Date1
#m "I think I have a better connection with [#P2Date1] right now."

if P2Date1 == "Allie":
    m "I think I have a better connection with Allie right now."
    jump p2d2pd_FlavorCommentAllie
if P2Date1 == "Scarlett":
    m "I think I have a better connection with Scarlett right now."
    jump p2d2pd_FlavorCommentScarlett
if P2Date1 == "Terra":
    m "I think I have a better connection with Terra right now."
    jump p2d2pd_FlavorCommentTerra
if P2Date1 == "Violet":
    m "I think I have a better connection with Violet right now."
    jump p2d2pd_FlavorCommentViolet
if P2Date1 == "Yui":
    m "I think I have a better connection with Yui right now."
    jump p2d2pd_FlavorCommentYui

label p2d2pd_FlavorCommentAllie:
m "She makes every moment exciting, and... I just can't get enough of that."
jump Afterp2d2pd_FlavorComment

label p2d2pd_FlavorCommentScarlett:
m "It's amazing how brilliant she is. And I can't ever quite place her. She's fascinating."
jump Afterp2d2pd_FlavorComment

label p2d2pd_FlavorCommentTerra:
m "Say what you will about Terra, it's always exciting to be around her."
jump Afterp2d2pd_FlavorComment

label p2d2pd_FlavorCommentViolet:
m "I don't know as much as I'd like about Violet just yet, but I know more than anything that I just want to keep learning more about her."
jump Afterp2d2pd_FlavorComment

label p2d2pd_FlavorCommentYui:
m "It's Yui, you know? It's practically self-explanatory. She's the best."
jump Afterp2d2pd_FlavorComment

label Afterp2d2pd_FlavorComment:

show k neutral
k "Ah, I had a feeling you'd say that. And you're right to say that!"
show k flirt
k "Well, we'll see where things go with her. Something tells me you'll get a chance to hang out with her again soon."
jump p2d2pd_After

label p2d2pd_sd2:

$ P2favoriteDate=P2Date2
#m "Though I've known her for less time, I think I like [#P2Date2] more right now."

if P2Date2 == "Allie":
    m "Though I've known her for less time, I think I like Allie more right now."
    jump p2d2pd_FlavorCommentAllie2
if P2Date2 == "Scarlett":
    m "Though I've known her for less time, I think I like Scarlett more right now."
    jump p2d2pd_FlavorCommentScarlett2
if P2Date2 == "Terra":
    m "Though I've known her for less time, I think I like Terra more right now."
    jump p2d2pd_FlavorCommentTerra2
if P2Date2 == "Violet":
    m "Though I've known her for less time, I think I like Violet more right now."
    jump p2d2pd_FlavorCommentViolet2
if P2Date2 == "Yui":
    m "Though I've known her for less time, I think I like Yui more right now."
    jump p2d2pd_FlavorCommentYui2

label p2d2pd_FlavorCommentAllie2:
m "She makes every moment exciting, and I just can't get enough of that."
jump Afterp2d2pd_FlavorComment2

label p2d2pd_FlavorCommentScarlett2:
m "It's amazing how brilliant she is. And I can't ever quite place her. She's fascinating."
jump Afterp2d2pd_FlavorComment2

label p2d2pd_FlavorCommentTerra2:
m "Say what you will about Terra, it's always exciting to be around her."
jump Afterp2d2pd_FlavorComment2

label p2d2pd_FlavorCommentViolet2:
m "I don't know as much as I'd like about Violet just yet, but I know more than anything that I just want to keep learning more about her."
jump Afterp2d2pd_FlavorComment2

label p2d2pd_FlavorCommentYui2:
m "It's Yui, you know? It's practically self-explanatory. She's the best."
jump Afterp2d2pd_FlavorComment2

label Afterp2d2pd_FlavorComment2:
show k neutral
k "Really! Well, can't say I'm surprised."
show k flirt
k "Let's see where things go with her. You'll be hanging out with her again soon enough!"
jump p2d2pd_After

label p2d2pd_After:
stop music
play music PastSadness
show bg RoomNight with dissolve
show k laugh
k "Anyway, that's it for today."
show k neutral
k "Keep it up, and who knows... you might just be the first one to make it out of here."
show k neutral
k "'Night, [name]."
m "Good night, Kat."
hide k with dissolve
"She left my room, closing the door behind her."

"...Guess it's time to turn in for the night."
show bg Black with dissolve
stop music
play music LoveTheme
"..."
#; Terra Flashback
"Sometimes the most precious moments are the most mundane."
"It's just the two of us, spending the evening together in the Games room."
"I'm reading a book, and at the same time, watching her rage against an opponent in a fighting game."
"It's fun to watch her savor each victory, or explode with profanity when she loses."
"...Life is good."
"It's time like these where you wish life could always be this simple."
"Sometimes in those moments, people wish for more excitement - for fame, for fortune, for anything but the ordinary."
"But all I want is the ordinary with you."
with vpunch
q "FUuuuuuuuUUUUCK YOU!!!!!"
# ???: [name], something must be wrong with the internet, I'm lagging like crazy."
"...I love this woman so much."
jump MorningSelector
