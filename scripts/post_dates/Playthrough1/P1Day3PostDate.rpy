label P1Day3postDate:

$ currentDay=4
$ P1Date3=selectedDate

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

show bg RoomNight with dissolve
play sound DoorKnock
play music PastSadness
"I was about to turn in for the night, when I heard a knock on my door."
play sound DoorOpen
show k neutral at pos50k with dissolve
m "Hey, Kat. I thought you weren't going to come over tonight."
show k flirt
k "Sorry about that, I got tied up in some things."
m "Is everything okay?"
show k laugh
k "Good as always."
show k neutral
k "Care to join me for a walk?"
m "Sure, that sounds nice."
play sound DoorClose
show k laugh
k "Then away we go!"
show bg MansionNight with dissolve
$ renpy.pause(delay = 1.0, hard = True)
show k neutral

show bg RoadNight with dissolve

play sound WalkingOnDirt
"We walked at a relaxed pace, with Kat slightly ahead, leading the way."
stop music
play music TechLive
show k happy
stop sound
k "So how are you feeling about day three, [name]?"



show k laugh

menu:
    #k "You still feeling [favoriteDate], or is [nonfavoriteDate] the frontrunner now?"
    k "Who's your frontrunner now?"

    # NEW TRANSLATEABLE FORMAT
    "I still like Allie the most" if favoriteDate == "Allie":
        jump p1d3pd_oldFav
    "I still like Scarlett the most" if favoriteDate == "Scarlett":
        jump p1d3pd_oldFav
    "I still like Terra the most" if favoriteDate == "Terra":
        jump p1d3pd_oldFav
    "I still like Violet the most" if favoriteDate == "Violet":
        jump p1d3pd_oldFav
    "I still like Yui the most" if favoriteDate == "Yui":
        jump p1d3pd_oldFav

    "I like Allie the most now" if nonfavoriteDate == "Allie":
        jump p1d3pd_newFav
    "I like Scarlett the most now" if nonfavoriteDate == "Scarlett":
        jump p1d3pd_newFav
    "I like Terra the most now" if nonfavoriteDate == "Terra":
        jump p1d3pd_newFav
    "I like Violet the most now" if nonfavoriteDate == "Violet":
        jump p1d3pd_newFav
    "I like Yui the most now" if nonfavoriteDate == "Yui":
        jump p1d3pd_newFav

    # OLD UNTRANSLATEABLE FORMAT
    #"I still like [favoriteDate] the most":
    #    jump p1d3pd_oldFav
    #"I like [nonfavoriteDate] the most now":
    #    jump p1d3pd_newFav


label p1d3pd_oldFav:
#m "[favoriteDate] is still the girl I like the most."
#m "If anything, getting to meet and know the other girls made me like her even more."

if favoriteDate == "Allie":
    m "Allie is still the girl I like the most."
    m "If anything, getting to meet and know the other girls made me like her even more."
    jump p1d3pd_FlavorCommentAllie
if favoriteDate == "Scarlett":
    m "Scarlett is still the girl I like the most."
    m "If anything, getting to meet and know the other girls made me like her even more."
    jump p1d3pd_FlavorCommentScarlett
if favoriteDate == "Terra":
    m "Terra is still the girl I like the most."
    m "If anything, getting to meet and know the other girls made me like her even more."
    jump p1d3pd_FlavorCommentTerra
if favoriteDate == "Violet":
    m "Violet is still the girl I like the most."
    m "If anything, getting to meet and know the other girls made me like her even more."
    jump p1d3pd_FlavorCommentViolet
if favoriteDate == "Yui":
    m "Yui is still the girl I like the most."
    m "If anything, getting to meet and know the other girls made me like her even more."
    jump p1d3pd_FlavorCommentYui

label p1d3pd_FlavorCommentAllie:
m "It's all I can do to just keep up with her, but each moment with her is so worth it."
jump Afterp1d3pd_FlavorComment

label p1d3pd_FlavorCommentScarlett:
m "She's full of surprises. But more importantly, I'm the happiest when I'm with her."
m "That said, so far hanging out with her has been more than a little dangerous, but... I like that."
jump Afterp1d3pd_FlavorComment

label p1d3pd_FlavorCommentTerra:
m "There's no one I'd rather spend a day with than Terra, you know? There's nothing quite like that."
jump Afterp1d3pd_FlavorComment

label p1d3pd_FlavorCommentViolet:
m "Violet's an incredible woman, in every way. Something about her just keeps pulling me in."
m "I just can't get enough of that, you know?"
jump Afterp1d3pd_FlavorComment

label p1d3pd_FlavorCommentYui:
m "It's Yui, you know? It's got be her. She's one of a kind."
m "No one else gives me that same warm feeling inside."
jump Afterp1d3pd_FlavorComment

label Afterp1d3pd_FlavorComment:

show k happy
k "Aww, that's cute! Also a perfect answer for the cameras, thank you very much."
show k happy
k "I guess you'll be giving her fanbase some more things to go rabid over soon, hmm?"
m "You can say that again."
show k laugh
k "Perfect!"
jump p1d3pd_afterFav

label p1d3pd_newFav:
# m "[favoriteDate] is a great girl... but I feel like I've got the most going with [nonfavoriteDate] now."

if nonfavoriteDate == "Allie":
    m "I feel like I've got the most going with Allie now."
elif nonfavoriteDate == "Scarlett":
    m "I feel like I've got the most going with Scarlett now."
elif nonfavoriteDate == "Terra":
    m "I feel like I've got the most going with Terra now."
elif nonfavoriteDate == "Violet":
    m "I feel like I've got the most going with Violet now."
elif nonfavoriteDate == "Yui":
    m "I feel like I've got the most going with Yui now."


#m "I feel like I've got the most going with [nonfavoriteDate] now."

#; SWITCH FAVS
$ tempFavorite=favoriteDate
$ favoriteDate=nonfavoriteDate
$ nonfavoriteDate=tempFavorite

if favoriteDate == "Allie":
    jump p1d3pd_FlavorCommentAllie2
if favoriteDate == "Scarlett":
    jump p1d3pd_FlavorCommentScarlett2
if favoriteDate == "Terra":
    jump p1d3pd_FlavorCommentTerra2
if favoriteDate == "Violet":
    jump p1d3pd_FlavorCommentViolet2
if favoriteDate == "Yui":
    jump p1d3pd_FlavorCommentYui2


label p1d3pd_FlavorCommentAllie2:
m "It's all I can do to just keep up with her, but each moment with her is so worth it."
jump Afterp1d3pd_FlavorComment2

label p1d3pd_FlavorCommentScarlett2:
m "She's full of surprises. But more importantly, I'm the happiest when I'm with her."
m "That said, so far hanging out with her has been more than a little dangerous, but... I like that."
jump Afterp1d3pd_FlavorComment2

label p1d3pd_FlavorCommentTerra2:
m "There's no one I'd rather spend a day with than Terra, you know? There's nothing quite like that."
jump Afterp1d3pd_FlavorComment2

label p1d3pd_FlavorCommentViolet2:
m "Violet's an incredible woman, in every way. Something about her just keeps pulling me in."
m "I just can't get enough of that, you know?"
jump Afterp1d3pd_FlavorComment2

label p1d3pd_FlavorCommentYui2:
m "It's Yui, you know? It's got to be her. She's one of a kind."
m "No one else gives me that same warm feeling inside."
jump Afterp1d3pd_FlavorComment2

label Afterp1d3pd_FlavorComment2:


show k surprised
k "Really!"
show k laugh
k "Damn, you sure change your mind quickly, [name]!"
show k neutral
k "I feel like anyone who has to date you is in for a nasty surprise."
m "Hey! I've only just gotten to know each of them."
m "Isn't it natural for things to change up quickly this early on?"
show k laugh
k "I guess so, but that's not what the internet will think."
show k bored
k "But that's not my problem~"
jump p1d3pd_afterFav

label p1d3pd_afterFav:
stop music
play music PastSadness

show k happy
k "Well, I'm happy you've at least got one girl you're really interested in, but it helps you've got chemistry with both!"
show k flirt
k "Tomorrow, we'll milk this love triangle by having you date the girl you didn't today."
show k laugh
k "Sound good to you?"
m "I'm noticing a pattern in making it sound like I have a choice, when I really don't."
show k sad
k "...None of us really have a choice nowadays, I'm afraid."
show k flirt
k "Alright, I gotta get back to editing today's footage. You ready to head back to the mansion?"
m "Sounds good to me."
play sound WalkingOnDirt
"We walked back in comfortable silence."
# @stopsfx WalkingOnDirt
stop sound
show bg MansionNight with dissolve # time:1
$ renpy.pause(delay = 1.0, hard = True)
show k neutral
k "'Night."
m "See you later, Kat."
hide k with dissolve
show bg RoomNight with dissolve # time:1
$ renpy.pause(delay = 1.0, hard = True)
show bg Black with dissolve # time:2

#; FLASHBACK 3
stop music
play music Twisting
"..."
m "If we get caught trying to escape... there's no telling what would happen to us."
q "It's a chance we have to take."
m "I know, but we need to know what we're up against."
q "We know the island better than anyone by now, [name]. We'll be fine."
m "I'm not so sure. Damian's brought in that scientist for his latest experiment."
m "All I've heard is that she's the one who built the prototype - the one Damian used to turn Six into a vegetable."
q "Not to mention the old test audiences, too. Shit."
m "I think they must've killed at least a hundred people by now, and they still haven't perfected it."
m "...If we get caught..."
q "I get what you're trying to say."
q "Are you still with me on this? It's not too late..."
m "You didn't even have to ask. Of course I'm with you."
"..."
"Who... are you?"
#I can always remember the way you made me feel - but never more than that."
"Somehow, I know you're close by."
"But every time I try to see your face... the dream ends."
jump MorningSelector





jump MorningSelector
