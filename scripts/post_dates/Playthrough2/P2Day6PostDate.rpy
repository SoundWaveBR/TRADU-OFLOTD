label P2Day6postDate:

$ currentDay=7

$ P2Date6=selectedDate

if P2Date6 == "Allie":
    $ selectedAffection = allieAffection
if P2Date6 == "Scarlett":
    $ selectedAffection = scarlettAffection
if P2Date6 == "Terra":
    $ selectedAffection = terraAffection
if P2Date6 == "Violet":
    $ selectedAffection = violetAffection
if P2Date6 == "Yui":
    $ selectedAffection = yuiAffection

play music PastSadness
#; 2 girls rank 2 now

show bg RoomNight with dissolve
"I'm feeling a little bit of the late night munchies. Guess I'll go head downstairs."
#show bg MansionIndoorsNight time:2
#; if there was a previous date with Violet,

if violetAffection == 2:
    jump p2d6pd_VioletCookie

show bg KitchenNight with dissolve
show k surprised at pos50k with dissolve
k "Oh! Hey, [name]. I was just about to go up to check in on you."
m "Hey there, Kat. What's up?"
show k neutral
k "Huh..."
show k annoyed
k "There were some fancy desserts here from last week, but I can't find them anymore."
show k bored
k "Guess I'll take that out of the Brothers Five's paychecks..."
m "How do you know it was them?"
show k laugh
k "They're like clockwork."
show a surprised at pos20a with dissolve
a "..."
show a surprised
a "...*munch*..."
show k flirt
k "This was the Brothers Five, no doubt about it."
play sound BambooHit
hide a with dissolve
"Allie made direct eye contact with me, then hightailed it out."
jump p2d6pd_meetKat

label p2d6pd_VioletCookie:

show bg KitchenNight with dissolve
"I walked to the kitchen, and opened the fridge."
"...! Sweet!"
"There's some leftover cookies that Violet and I had made together."
"I grabbed a few and wolfed them down."
"Delicious, mmm."
show k happy at pos50k with dissolve
k "Got a case of the midnight munchies?"
m "I figured I'd do my civil duty and help finish the cookies Violet and I made."
show k flirt
k "Right. Only a good samaritan would finish all the cookies, so no one else would have to make that sacrifice."
m "I'm just too good of a person, I know... it gets me in trouble sometimes."
jump p2d6pd_meetKat

label p2d6pd_meetKat:
show k neutral at pos50k with dissolve
k "Anyway, I've been meaning to talk with you."
m "What's up?"
show k flirt
stop music
play music TechLive
show k flirt


if P2Date6 == "Allie":
    k "How'd your date with Allie today go?"
elif P2Date6 == "Scarlett":
    k "How'd your date with Scarlett today go?"
elif P2Date6 == "Terra":
    k "How'd your date with Terra today go?"
elif P2Date6 == "Violet":
    k "How'd your date with Violet today go?"
elif P2Date6 == "Yui":
    k "How'd your date with Yui today go?"


menu:
    # k "How'd your date with [#P2Date6] today go?"

    "Awesome":
        jump p2d6pd_awesome
    "Ehh":
        jump p2d6pd_ehh

label p2d6pd_ehh:
m "It was... alright, I guess."
show k surprised
k "Oh, really! That's too bad."

show k neutral
if P2Date6 == "Allie":
    k "Allie said in a interview after your date that she thought you two really connected."
elif P2Date6 == "Scarlett":
    k "Scarlett said in a interview after your date that she thought you two really connected."
elif P2Date6 == "Terra":
    k "Terra said in a interview after your date that she thought you two really connected."
elif P2Date6 == "Violet":
    k "Violet said in a interview after your date that she thought you two really connected."
elif P2Date6 == "Yui":
    k "Yui said in a interview after your date that she thought you two really connected."
# OLD UNTRANS FORMAT
# k "[#P2Date6] said in a interview after your date that she thought you two really connected."

show k laugh
k "Well, doesn't matter. The audience thinks you did, and that'll keep you alive!"
m "I guess so..."
jump p2d6pd_advice

label p2d6pd_awesome:

if selectedDate == "Allie":
    jump p2d6pd_secondAllie
if selectedDate == "Scarlett":
    jump p2d6pd_secondScarlett
if selectedDate == "Terra":
    jump p2d6pd_secondTerra
if selectedDate == "Violet":
    jump p2d6pd_secondViolet
if selectedDate == "Yui":
    jump p2d6pd_secondYui

label p2d6pd_secondAllie:
m "It was pretty great! There's never a dull moment with Allie."
m "I'm just scratching the surface, but I like what I see, and I really want to get to know her more."
show k happy
k "Interesting, interesting! That's good."
show k neutral
k "Allie's pretty out there as far as people go. I can see why she'd have a hard time opening up."
show k flirt
k "But from what I saw today, I'm sure if she'd open up to anybody, it'd be you."
show k laugh
k "People thought she didn't have much of a chance here - I guess you two are proving them wrong!"
m "I guess so."
jump p2d6pd_advice

label p2d6pd_secondScarlett:
m "It was amazing. I feel like I really got to know the real Scarlett today."
m "And for the first time, I think I feel like I've truly been understood."
show k happy
k "I'm glad to hear that, [name]. Really."
show k neutral
k "Scarlett puts on a front that's nothing like how she really is. I'm glad you can see behind it."
show k happy
k "She must really trust you."
m "I'm glad she does, believe me."
show k laugh
k "More importantly though, Scarlett's fanbase has been ravenous for new content. From what I saw, you delivered today!"
show k neutral
k "I'm a solid 85\% sure you won't wake up in a torture chamber tomorrow morning. Good job, [name]!"
m "Thanks?"
jump p2d6pd_advice

label p2d6pd_secondTerra:
m "It was great! I have to admit..."
m "...Terra's very different from my initial impression of her."
m "I feel like I'm seeing the real her now, and... I like what I see."
show k laugh
k "I like the sound of that!"
show k flirt
k "Who would have thought you'd say something like this after your... unique... first date, huh?"
m "Life sure is funny."
jump p2d6pd_advice

label p2d6pd_secondViolet:
m "It was wonderful. And that's not a word I say very often."
m "It's not every day where you get to spend it with a woman who can turn a kitchen into a warzone."
m "I can't remember the last time I had so much fun, and that's not the amnesia talking."
show k flirt
k "Violet really is something, ain't she!"
m "No kidding."
show k happy
k "I'd expect no less from the woman who's currently our audience favorite."
show k laugh
k "Whenever we get you both in the same room, ratings just soar through the roof!"
m "I can't say I'm surprised to hear that."
jump p2d6pd_advice

label p2d6pd_secondYui:
m "It felt like it was out of a fairy tale."
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
jump p2d6pd_advice

label p2d6pd_advice:
show k flirt
k "Well, that should be enough footage for today. Thanks, [name]!"
show k happy
k "You'll be happy to know that phase two of the plan was a smashing success!"
m "That's great to hear!"
show k laugh
# old form
#k "No kidding. The love... square? Between [#P2Date4], [#P2Date5], and [#P2Date6] has viewers on the edge of their seats!"
k "No kidding. The love... square? It's got viewers on the edge of their seats!"
show k flirt
k "You've actually broken the record for ratings on a killer dating game show!"
show k surprised
k "It's not as niche as it sounds."
m "Do I get a plaque for that? This has got to count for something, somewhere."
show k laugh
k "We don't have it printed it yet, but I've prepared your tombstone in advance, if you're looking for a souvenir!"
show k flirt
m "Thanks for the vote of confidence, Kat."
show k happy
k "Let it never be said that I am anything but supportive."
show k neutral
k "Anyway, we're on to phase three."
show k flirt
k "It's pretty much the same as phase two, except with third dates this time."
show k neutral
k "...And one caveat."
m "What's that, Kat?"
show k happy
# old version
#k "I'm sure you've got a favorite in mind, between [#P2Date4], [#P2Date5], and [#P2Date6]."
k "I'm sure you've got a favorite in mind, between the three girls you're dating now."
show k flirt
k "If you want to maximize your chances of getting out of here alive, save the best for last. It gives audiences something to look forward to."
show k happy
k "Sounds good to you?"
m "Makes sense to me."
show k flirt
k "Good."
show k neutral
k "That's all for today. I'll seeya later. 'Night, [name]."
m "Good night, Kat."
show k neutral
m "And... thanks for the help till now, Kat. I realize I'd probably be screwed without you."
show k serious
k "...Don't thank me yet."
hide k with dissolve
"Guess I'll call it a night."
#@char MansionIndoorsNight time:2
"I walked back to my room."
show bg RoomNight with dissolve
show bg Black with dissolve #time:2
"Time to get some shuteye...."

stop music
play music LeavingHome
"..."
#; Scarlett Flashback
m "So what's this supposed to do?"
show s happy at pos50s with dissolve
s "It's only a prototype, but technical details aside, you can think of it as a 'memory rewriter'."
m "So it... rewrites memories?"
show s neutral
s "Pretty much. Think of it like a surgeon's scalpel."
show s serious
s "With it, you could make someone forget things as big as who they are, or something as small as a specific conversation."
m "...So if you used this on someone, anything's fair game. You could erase anything you wanted."
show s laugh
s "Exactly!"
show s worried
s "Well, maybe it's not really a scalpel, since it comes with a reset button."
show s sad
s "It's sad, though..."
show s worried
s "...This was supposed to help people after the war."
show s sad
s "...I... was supposed to help people after the war."
m "...I'm sorry, Scarlett."
show s worried
s "Don't worry about it. I may not be able to help them, but..."
show s neutral
s "...It doesn't mean I can't help you and your partner escape from this madness."
m "Thank you, really. Thank you so much."
m "I know you're taking an incredible risk for us, that honestly, most people would never -"
show s happy
s "Don't mention it, [name]. It's what I do."
show s neutral
s "If they manage to trace it back to me, then... I'll accept whatever comes."
show s laugh
s "It'd be the first time I helped somebody in quite some time."
m "Scarlett..."
show s serious
s "...The boat is just past the woods, behind the rocky enclave near the beach."
show s neutral
s "It won't be there forever, so act quickly."
show s serious
s "It'd be suicide to go for it during the day, so I recommend heading there near midnight."
m "...Thank you, Scarlett."
m "You sure you don't want to come with us?"
show s laugh
s "Someone has to stay here to help the people that fall in this spider's web."
m "You don't have to be so noble."
show s sad
s "I envy her, you know. To get to leave this place with you."
show s happy
s "...But someone needs to stay here to do what's right."
"..."
jump MorningSelector
