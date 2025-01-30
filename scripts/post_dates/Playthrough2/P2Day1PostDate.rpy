label P2Day1postDate:

play music PastSadness
show bg RoomNight with dissolve
$ currentDay=2

$ P2Date1=selectedDate
"I stumbled back to my room and plopped onto my bed."
play sound DoorKnock
"...? Who'd be coming at this hour?"
"I shuffled over in a haze."
play sound DoorOpen
show k neutral at pos50k with dissolve
k "Hey there, [name]! Sorry to bother you this late."
m "It's alright. What's up, Kat?"
show k laugh
k "Don't mind me, just gonna make myself real comfortable~"
hide k with dissolve
show bg KatInYourRoom with dissolve #time:1
"Kat walked by me and comfortably sat herself on my bed."
k "I really gotta get one of these beds for myself already."
play sound DoorClose
"I closed the door, then sat facing her on the opposite side of the bed."
m "So what brings you here tonight? Can't stop thinking about me?"
show bg RoomNight with dissolve
show k laugh at pos50k with dissolve
k "You wish! Unfortunately, it's my job to help you survive until the end of the show."
show k flirt
k "And that means checking in with you every night to see how you're doing, and making sure you're doing your best on ratings."
m "That's nice of you. Thanks, Kat."
show k laugh
k "Well, to be honest, I don't have a choice! Finding a new person to take your place would be a recruiting nightmare."
show k neutral
stop music
play music TechLive
show k flirt

#k "Back to what I'm here for. Your date today with [#selectedDate] was a ratings knockout!"
if selectedDate == "Allie":
    k "Back to what I'm here for. Your date today with Allie was a ratings knockout!"
if selectedDate == "Scarlett":
    k "Back to what I'm here for. Your date today with Scarlett was a ratings knockout!"
if selectedDate == "Terra":
    k "Back to what I'm here for. Your date today with Terra was a ratings knockout!"
if selectedDate == "Violet":
    k "Back to what I'm here for. Your date today with Violet was a ratings knockout!"
if selectedDate == "Yui":
    k "Back to what I'm here for. Your date today with Yui was a ratings knockout!"

if selectedDate == "Allie":
    jump p2d1pd_allie
if selectedDate == "Scarlett":
    jump p2d1pd_scarlett
if selectedDate == "Terra":
    jump p2d1pd_terra
if selectedDate == "Violet":
    jump p2d1pd_violet
if selectedDate == "Yui":
    jump p2d1pd_yui

label p2d1pd_allie:
show k happy
k "You and Allie were the fan favorite pair! I gotta say, she knows how to make exciting TV."
show k surprised
k "Hmm... she's got potential for her own show, now that I think about it..."
m "...You were saying?"
show k happy
k "Ah! Sorry, I'm getting distracted."
show k neutral
k "The whole world knows now that Allie is your first soulmate candidate, and they're hungry for more content."
show k flirt
k "That said... we need a little more drama in the mix now."
jump p2d1pd_AfterElse

label p2d1pd_scarlett:
show k surprised
k "I don't know if I'd call what you two had a date, but you two have become quite the popular ship for our viewers."
m "We did put on quite a show, didn't we?"
show k happy
k "No kidding! There's not a person who watched today's broadcast who doubts that she's your first soulmate candidate."
show k flirt
k "That said, let's sprinkle a little more drama into the mix!"
show k laugh
k "More romance. Less zombies."
jump p2d1pd_AfterElse

label p2d1pd_terra:
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
k "More romance, love triangles... and less pigeons."
jump p2d1pd_AfterElse

label p2d1pd_violet:
show k laugh
k "You and Violet started out a little frosty... but by the end, I think we saw you two warm up to each other... a bit!"
m "...Thank you?"
show k flirt
k "That said... we need something more than that, if we're going to make the world believe she's your first soulmate candidate."
show k happy
k "So let's heat things up with some more competition! Pizzazz! Romance!"
jump p2d1pd_AfterElse

label p2d1pd_yui:
show k happy
k "People can't stop raving about your date with Yui today."
show k laugh
k "I mean, mostly death threats, because they'd want to be in your position, but eh..."
m "Nice to know that the outside world is safer than here..."
show k happy
k "They're just jealous. Most people would dream of having someone like Yui be their soulmate candidate."
show k flirt
k "Then again, it's no fun if this is just the Yui show. We need more drama! Betrayal! Romance!"
jump p2d1pd_AfterElse

label p2d1pd_AfterElse:
show k flirt

menu:
    k "Tomorrow, I want you to find who your second soulmate candidate is, and ask them out on a date instead."

    "Alright":
        jump p2d1pd_alright

    "I'd rather go on a second date with Allie tomorrow" if selectedDate == "Allie":
        jump p2d1pd_2nd
    "I'd rather go on a second date with Scarlett tomorrow" if selectedDate == "Scarlett":
        jump p2d1pd_2nd
    "I'd rather go on a second date with Terra tomorrow" if selectedDate == "Terra":
        jump p2d1pd_2nd
    "I'd rather go on a second date with Violet tomorrow" if selectedDate == "Violet":
        jump p2d1pd_2nd
    "I'd rather go on a second date with Yui tomorrow" if selectedDate == "Yui":
        jump p2d1pd_2nd

    # OLD UNTRANSLATEABLE FORMAT
    #"I'd rather go on a second date with [#selectedDate] tomorrow":
    #    jump p2d1pd_2nd


label p2d1pd_alright:
m "Alright, sounds good to me."
show k sassy
k "...I would have expected more resistance, but I guess you understand your situation."
stop music
play music HalfMystery
show k serious
k "Without those ratings getting higher and higher every day, they'll axe the show, and your life with it."
m "I guess that makes sense, in some warped way."
show k surprised
k "I'm impressed at how well you took that!"
show k flirt
k "I'd almost think it wasn't your first time on a life-or-death killing dating show."
jump p2d1pd_After

label p2d1pd_2nd:

if selectedDate == "Allie":
    jump p2d1pd_ifAllie2nd
elif selectedDate == "Scarlett":
    jump p2d1pd_ifScarlett2nd
elif selectedDate == "Terra":
    jump p2d1pd_ifTerra2nd
elif selectedDate == "Violet":
    jump p2d1pd_ifViolet2nd
elif selectedDate == "Yui":
    jump p2d1pd_ifYui2nd

label p2d1pd_ifAllie2nd:
m "...Look, I get the whole thing about ratings, but I'd rather just spend another day with Allie."
m "Every moment with her is so much fun, and honestly, all things considered, that's what I'd like most."
show k sad
k "I understand that, [name]. Really, I do. But..."
jump p2d1pd_DirectlyAfter2nd

label p2d1pd_ifScarlett2nd:
m "...I get that it'd be more dramatic to date someone else, but I'd rather just spend more time with Scarlett tomorrow."
m "She's really unique, and I can't wait to get to know her better."
show k neutral
k "I'm surprised to hear you say that, considering what happened today."
show k laugh
k "But hey, that's just show biz."
jump p2d1pd_DirectlyAfter2nd

label p2d1pd_ifTerra2nd:
m "...I get that it would be better for ratings to date somebody else, but I want to spend more time with Terra."
show k surprised
k "Interesting! Well..."
show k serious
k "...Even so, it's out of our hands."
m "What do you mean?"
show k worried
k "Look..."
jump p2d1pd_DirectlyAfter2nd

label p2d1pd_ifViolet2nd:
m "...I get that it would be worse for ratings, but I'd rather just spend more time with Violet tomorrow."
m "I feel like there's something just under the surface that I'm reaching, and... I want to know what that is with her."
show k happy
k "It's sweet of you to say that, really. And..."
jump p2d1pd_DirectlyAfter2nd

label p2d1pd_ifYui2nd:
m "...Honestly, I don't really care about ratings."
m "What I care about is getting more time to spend with Yui. It's only been a day with her, and already I can't wait for the next one."
show k happy
k "...I'm glad to hear that, really."
k "And believe me, I know. I saw your whole date. I know you and Yui really hit it off."
"She sighed."
show k sad
k "Look..."
jump p2d1pd_DirectlyAfter2nd

label p2d1pd_DirectlyAfter2nd:
stop music
play music HalfMystery
show k serious
k "...In a perfect world, you'd be able to do just that."
show k worried
k "...But if you do that, the shows ratings won't be high enough. And if ratings aren't high enough..."
show k serious
k "They'll axe the show, and your life with it, even if it's not the last day yet."
m "..."
m "In some messed up way, that almost makes sense."
show k surprised
k "You're quick on the uptake!"
show k flirt
k "I'd almost think it wasn't your first time on a life-or-death killing dating show."
jump p2d1pd_After

label p2d1pd_After:

stop music
play music PastSadness
show k neutral
k "...Well, that's pretty much what I needed to tell you."
show k happy
k "It's getting late, and we've both got big days tomorrow. I'll see you tomorrow."
show k neutral
k " 'Night, [name]."
m "Good-"
play sound DoorClose
hide k with dissolve
"She was gone before I had a chance to finish."
show bg Black with dissolve
"...Guess it's time to call it a night."
stop music
play music LeavingHome
"..."
"The sound of waves."
q "Hey."
"I can hear her call out to me within a dream."
"...It's you."
play sound Glitch1
q "{glitch=50}{b}I love you, [name].{/b}{/glitch}"
q "...I always will."
m "And I'll always love you too."
"My mouth moves on its own."
q "Even if there's so many other women on this show?"
m "They could never be you."
"I held her tight and kissed her."
q "You promise?"
m "I promise."
q "Promises are unbreakable, you know. That's what you told me."
play sound Glitch2
m "{glitch=50}{b}I meant every word I said.{/b}{/glitch}"
"She smiled at me."
q "You better have!"
"Your face is becoming clearer to me with every day that goes by."
"I know you're here with me... but which one are you?"
jump MorningSelector
