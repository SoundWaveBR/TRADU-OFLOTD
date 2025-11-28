
label P1Day1postDate:

play music PastSadness
show bg RoomNight with dissolve
$ currentDay=currentDay+1

$ P1Date1=selectedDate
"I stumbled back to my room and plopped onto my bed."
play sound DoorKnock
"I was just about to close my eyes, when I heard a knock at the door."
"I shuffled over in a haze."
play sound DoorOpen
show k neutral at pos50k with dissolve
k "Hey there, [name]. Sorry to bother you this late."
m "It's alright. What's up, Kat?"
show k laugh
k "Don't mind me, just gonna make myself real comfortable~"
hide k with dissolve
show bg KatInYourRoom with dissolve #time:1
"Kat walked by me and comfortably sat herself on my bed."
k "Oh my god, you have no idea how much better your beds are compared to the staff."
k "You'd think the ones actually working here would get treated nicely."
play sound DoorClose
"I closed the door, then sat facing her on the opposite side of the bed."
m "I'm guessing you're not coming to my room at night to start a worker's union."
k "I wonder... what would you want me to come to your room for instead?"
m "I can think of a few things."
show bg RoomNight with dissolve
show k laugh at pos50k with dissolve
k "You'd think five women would be enough for a person! You're incorrigible, [name]."
show k neutral
k "Anyway... as the producer, I'm obliged to help you survive until the end of the show."
m "Just until the end of the show? I'm heartbroken."
show k laugh
k "Being your babysitter doesn't pay well enough to make it a long-term gig!"
show k neutral
k "I'll be checking in with you each night, to let you know how you're doing, and give you some advice here and there."
m "That's nice of you. Thanks, Kat."
show k laugh
k "Well, to be honest, finding a new person to take your place would be a recruiting nightmare!"
show k neutral
stop music
play music TechLive
# k "Back to topic - our audiences really loved your date with [#selectedDate] today!"

if selectedDate == "Allie":
    k "Back to topic - our audiences really loved your date with Allie today!"
    jump p1d1pd_allie
elif selectedDate == "Scarlett":
    k "Back to topic - our audiences really loved your date with Scarlett today!"
    jump p1d1pd_scarlett
elif selectedDate == "Terra":
    k "Back to topic - our audiences really loved your date with Terra today!"
    jump p1d1pd_terra
elif selectedDate == "Violet":
    k "Back to topic - our audiences really loved your date with Violet today!"
    jump p1d1pd_violet
elif selectedDate == "Yui":
    k "Back to topic - our audiences really loved your date with Yui today!"
    jump p1d1pd_yui

label p1d1pd_allie:

show k happy
k "You and Allie were the fan favorite pair. I gotta say, she knows how to make exciting TV."
show k surprised
k "She's got potential for her own show, now that I think about it..."
m "...You were saying?"
show k happy
k "Ah, Sorry. Got sidetracked."
show k neutral
k "The whole world knows now that Allie is your first soulmate candidate, and they're hungry for more content."
show k flirt
k "That said, we need a little more drama in the mix now. A love triangle!"
jump p1d1pd_after

label p1d1pd_scarlett:
show k surprised
k "I don't know if I'd call what you two had a date, but you two have become quite the popular ship for our viewers."
m "We did put on quite a show, didn't we?"
show k happy
k "No kidding! There's not a person who watched today's broadcast who doubts that she's your first soulmate candidate."
show k flirt
k "That said, let's sprinkle a little more drama into the mix!"
show k laugh
k "More romance, more love triangles. Less zombies."
jump p1d1pd_after

label p1d1pd_terra:
show k surprised
k "Honestly, I've got no idea what to say about your date today with Terra..."
show k flirt
k "...Except that I'm surprised anyone thought it was a good one."
m "Can I really be picky when my life's on the line?"
show k laugh
k "I guess not!"
show k flirt
k "That said, I'm hoping we can sprinkle a little more drama into this show!"
show k laugh
k "More romance, love triangles... less pigeons."
jump p1d1pd_after

label p1d1pd_violet:
show k laugh
k "You and Violet started out a little frosty, but by the end, I think we saw you two warm up to each other... a bit!"
m "...Thank you?"
show k flirt
k "That said, we need something more than that, if we're going to make the world believe she's your first soulmate candidate."
show k happy
k "So let's heat things up with some more competition! Love triangles! Pizzazz!!"
jump p1d1pd_after

label p1d1pd_yui:
show k happy
k "People online can't stop raving about you and Yui."
show k laugh
k "I mean, it's mostly death threats targeted at you, because they'd want to be in your position, but it's something!"
m "Nice to know that the outside world is safer than here..."
show k happy
k "They're just jealous. Most people would dream of having someone like Yui be their soulmate candidate."
show k flirt
k "Then again, it's no fun if this is just the Yui show. We need drama! Love triangles! Betrayal!"
jump p1d1pd_after

label p1d1pd_after:
show k flirt

menu:
    k "So tomorrow... I want you to find who your other soulmate candidate is, and ask them out on a date."

    "Alright":
        jump p1d1pd_alright
    #"I'd rather go on a second date with [#selectedDate] tomorrow":
    #    jump p1d1pd_rather
    "I'd rather go on a second date with Allie tomorrow" if P1Date1 == "Allie":
        jump p1d1pd_rather
    "I'd rather go on a second date with Scarlett tomorrow" if P1Date1 == "Scarlett":
        jump p1d1pd_rather
    "I'd rather go on a second date with Terra tomorrow" if P1Date1 == "Terra":
        jump p1d1pd_rather
    "I'd rather go on a second date with Violet tomorrow" if P1Date1 == "Violet":
        jump p1d1pd_rather
    "I'd rather go on a second date with Yui tomorrow" if P1Date1 == "Yui":
        jump p1d1pd_rather

label p1d1pd_alright:
m "Alright, sounds good to me."
show k surprised
k "...Really!"

if selectedDate == "Scarlett":
    jump p1d1pd_if_scarlett
if selectedDate == "Violet":
    jump p1d1pd_if_violet
if selectedDate != "Scarlett":
    jump p1d1pd_if_not_scarlett

label p1d1pd_if_scarlett:

show k sassy
k "I would have expected you to want to spend more time with Scarlett right away, especially considering what just happened."
show k neutral
m "I get that, but at the end of the day, we need ratings - and those are coming from people who want to see love triangles and what not, right?"
show k flirt
k "That's exactly right!"
show k serious
stop music
play music HalfMystery
k "Without those ratings being high every day, they'll axe the show, and your life."
m "I guess that makes sense, in a messed up way."
show k surprised
k "I'm impressed at how well you took that!"
show k laugh
k "Is this not your first time on a life-or-death killing dating show?"
m "Can't say that it is..."
jump p1d1pd_after_feedback

label p1d1pd_if_violet:
show k sassy
k "I would have expected you to want to spend more time with Violet right away, especially considering what just happened."
show k neutral
m "I get that, but at the end of the day, we need ratings - and those are coming from people who want to see love triangles and what not, right?"
show k flirt
k "That's exactly right!"
show k serious
stop music
play music HalfMystery
k "Without those ratings being high every day, they'll axe the show, and your life."
m "I guess that makes sense, in a messed up way."
show k surprised
k "I'm impressed at how well you took that!"
show k laugh
k "Is this not your first time on a life-or-death killing dating show?"
m "Can't say that it is..."
jump p1d1pd_after_feedback

label p1d1pd_if_not_scarlett:
show k neutral
k "Since you had such a great date today, I'm surprised you agreed so easily."
m "Well, it is a bit weird, but..."
m "At the end of the day, this is a TV show. You need ratings to survive."
show k serious
stop music
play music HalfMystery
k "You're exactly right. And more specifically..."
show k neutral
k "You need those ratings to survive, or they'll axe the show before the last day."
m "What happens to me if that happens?"
show k serious
k "Well... it'd be as if you didn't end up with anyone at the end of the show."
m "Ah... Got it."
m "Well, that's simple enough."
show k surprised
k "I'm impressed at how well you took that!"
show k laugh
k "Have you been on a life-or-death killing dating show before?"
m "Can't say I have..."
jump p1d1pd_after_feedback

# 2nd:
label p1d1pd_rather:


if selectedDate == "Allie":
    jump p1d1pd_allie2nd
if selectedDate == "Scarlett":
    jump p1d1pd_scarlett2nd
if selectedDate == "Terra":
    jump p1d1pd_terra2nd
if selectedDate == "Violet":
    jump p1d1pd_violet2nd
if selectedDate == "Yui":
    jump p1d1pd_yui2nd



label p1d1pd_allie2nd:
m "Look, I get the whole thing about ratings, but I'd rather just spend another day with Allie."
m "Every moment with her is so much fun, and honestly, all things considered, that's what I'd like most."
show k sad
k "I understand that, [name]. Really, I do. But..."
jump DirectlyAfter2nd

label p1d1pd_scarlett2nd:
m "I get that it'd be more dramatic to date someone else, but I'd rather just spend more time with Scarlett tomorrow."
m "She's really unique, and I can't wait to get to know her better."
show k neutral
k "I'm surprised to hear you say that, considering what happened today."
show k laugh
k "But hey, that's just show biz."
jump DirectlyAfter2nd

label p1d1pd_terra2nd:
m "I get that it would be better for ratings to date somebody else, but I like what I have with Terra so far."
m "I don't want her to give her the wrong idea, this early on, you know?"
show k serious
k "I understand that, really I do. But really, it's out of our hands."
m "What do you mean?"
show k worried
k "Look..."
jump DirectlyAfter2nd

label p1d1pd_violet2nd:
m "I get that it would be worse for ratings, but I'd rather just spend more time with Violet tomorrow."
m "I feel like there's something just under the surface that I'm reaching, and... I want to know what that is with her."
show k happy
k "It's sweet of you to say that, really. And..."
jump DirectlyAfter2nd

label p1d1pd_yui2nd:
m "Honestly, I don't really care about ratings."
m "What I care about is getting more time to spend with Yui. It's only been a day with her, and already I can't wait for the next one."
show k happy
k "I'm glad to hear that, really."
k "And believe me, I know! I saw your whole date. I know you and Yui really hit it off."
"She sighed."
show k sad
k "Look..."
jump DirectlyAfter2nd

label DirectlyAfter2nd:
stop music
play music HalfMystery
show k serious
k "...In a perfect world, you'd be able to do just that."
show k worried
k "But if you do that, the shows ratings won't be high enough."
m "And how's that my concern?"
show k bored
k "If the show's ratings aren't high enough, they'll just axe the show before the last day."
show k sad
k "...And it'd be treated as if you didn't end up with anyone at the end, if you catch my drift."
m "Ah..."
show k serious
k "I get why you wouldn't want to, but that's exactly what the last person in your shoes did."
show k sad
k "...And they're not around to tell you about how it went anymore."
m "..."
show k neutral
m "Alright... I'll ask somebody else tomorrow."

if P1Date1 == "Allie":
    m "Can I least explain why I have to do this to Allie?"
if P1Date1 == "Scarlett":
    m "Can I least explain why I have to do this to Scarlett?"
if P1Date1 == "Terra":
    m "Can I least explain why I have to do this to Terra?"
if P1Date1 == "Violet":
    m "Can I least explain why I have to do this to Violet?"
if P1Date1 == "Yui":
    m "Can I least explain why I have to do this to Yui?"

#m "Can I least explain why I have to do this to [#P1Date1]?"
show k bored
k "You already know the answer to that, [name]."
show k neutral
k "Would that be good for ratings?"
m "..."
jump p1d1pd_after_feedback

label p1d1pd_after_feedback:

show k neutral
stop music
play music PastSadness
k "Well, that's pretty much what I needed to tell you before tomorrow."
show k happy
k "It's getting late, and we've both got big days tomorrow. How about we call it a night?"
m "Sounds good to me."
show k sad
k "If it's worth anything... I'm sorry."
show k neutral
k "I'll see you tomorrow. Good night, [name]."
m "Good night, Kat."
hide k with dissolve
"She left my room, closing my door behind her."
"I went back to laying on my bed, and closed my eyes."
show bg Black with dissolve

if P1Date1 == "Allie":
    "I kept thinking about Allie before I slept."
elif P1Date1 == "Scarlett":
    "I kept thinking about Scarlett before I slept."
elif P1Date1 == "Terra":
    "I kept thinking about Terra before I slept."
elif P1Date1 == "Violet":
    "I kept thinking about Violet before I slept."
elif P1Date1 == "Yui":
    "I kept thinking about Yui before I slept."
#"I kept thinking about [#P1Date1] before I slept."

#; FLASHBACK 1

stop music
play music LeavingHome
"..."
"The sound of waves, crashing against the shore."
play sound Glitch1
q "{glitch=50}{b}Hey.{/b}{/glitch}"
"...?"
"I can hear a woman's voice call out to me within a dream."
q "You probably can't hear me in there, but..."
"I try to respond, but no words come out."
q "...[name]. Promise me one thing."
q "Don't forget... don't you dare forget."
q "You promised."
q "Promises are unbreakable, right? That's what you told me."
"..."
play sound Glitch2
q "{glitch=50}{b}You promised.{/b}{/glitch}"
q "...But you lied, didn't you?"
$ currentDay=2
jump MorningSelector
