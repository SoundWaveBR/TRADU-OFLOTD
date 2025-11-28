label P2Day3postDate:

$ currentDay=4
$ P2Date3=selectedDate

play music PastSadness
show bg MansionNight with dissolve
"After today's date, I went out for a short walk outside the mansion."
show k neutral at pos50k with dissolve
k "Oh. Hey, [name]."
m "Hey, Kat. What's up?"
show k sassy
k "Let's not waste any time. I gotta get back to editing, and you know what I want to hear."
show k flirt

if P2favoriteDate == "Allie" and P2Date3 == "Scarlett":
    k "I know Allie was your favorite till now, but maybe Scarlett has shaked things up a bit!"
elif P2favoriteDate == "Allie" and P2Date3 == "Terra":
    k "I know Allie was your favorite till now, but maybe Terra has shaked things up a bit!"
elif P2favoriteDate == "Allie" and P2Date3 == "Violet":
    k "I know Allie was your favorite till now, but maybe Violet has shaked things up a bit!"
elif P2favoriteDate == "Allie" and P2Date3 == "Yui":
    k "I know Allie was your favorite till now, but maybe Yui has shaked things up a bit!"
elif P2favoriteDate == "Scarlett" and P2Date3 == "Allie":
    k "I know Scarlett was your favorite till now, but maybe Allie has shaked things up a bit!"
elif P2favoriteDate == "Scarlett" and P2Date3 == "Terra":
    k "I know Scarlett was your favorite till now, but maybe Terra has shaked things up a bit!"
elif P2favoriteDate == "Scarlett" and P2Date3 == "Violet":
    k "I know Scarlett was your favorite till now, but maybe Violet has shaked things up a bit!"
elif P2favoriteDate == "Scarlett" and P2Date3 == "Yui":
    k "I know Scarlett was your favorite till now, but maybe Yui has shaked things up a bit!"
elif P2favoriteDate == "Terra" and P2Date3 == "Allie":
    k "I know Terra was your favorite till now, but maybe Allie has shaked things up a bit!"
elif P2favoriteDate == "Terra" and P2Date3 == "Scarlett":
    k "I know Terra was your favorite till now, but maybe Scarlett has shaked things up a bit!"
elif P2favoriteDate == "Terra" and P2Date3 == "Violet":
    k "I know Terra was your favorite till now, but maybe Violet has shaked things up a bit!"
elif P2favoriteDate == "Terra" and P2Date3 == "Yui":
    k "I know Terra was your favorite till now, but maybe Yui has shaked things up a bit!"
elif P2favoriteDate == "Violet" and P2Date3 == "Allie":
    k "I know Violet was your favorite till now, but maybe Allie has shaked things up a bit!"
elif P2favoriteDate == "Violet" and P2Date3 == "Scarlett":
    k "I know Violet was your favorite till now, but maybe Scarlett has shaked things up a bit!"
elif P2favoriteDate == "Violet" and P2Date3 == "Terra":
    k "I know Violet was your favorite till now, but maybe Terra has shaked things up a bit!"
elif P2favoriteDate == "Violet" and P2Date3 == "Yui":
    k "I know Violet was your favorite till now, but maybe Yui has shaked things up a bit!"
elif P2favoriteDate == "Yui" and P2Date3 == "Allie":
    k "I know Yui was your favorite till now, but maybe Allie has shaked things up a bit!"
elif P2favoriteDate == "Yui" and P2Date3 == "Scarlett":
    k "I know Yui was your favorite till now, but maybe Scarlett has shaked things up a bit!"
elif P2favoriteDate == "Yui" and P2Date3 == "Terra":
    k "I know Yui was your favorite till now, but maybe Terra has shaked things up a bit!"
elif P2favoriteDate == "Yui" and P2Date3 == "Violet":
    k "I know Yui was your favorite till now, but maybe Violet has shaked things up a bit!"

# OLD UNTRANS FORMAT
# k "I know [#P2favoriteDate] was your favorite till now, but maybe [#P2Date3] has shaked things up a bit!"
show k sassy

menu:
    k "Who's number one now?"

    # NEW TRANSLATEABLE FORMAT
    "I still like Allie the most" if P2favoriteDate == "Allie":
        jump p2d3pd_sd1
    "I still like Scarlett the most" if P2favoriteDate == "Scarlett":
        jump p2d3pd_sd1
    "I still like Terra the most" if P2favoriteDate == "Terra":
        jump p2d3pd_sd1
    "I still like Violet the most" if P2favoriteDate == "Violet":
        jump p2d3pd_sd1
    "I still like Yui the most" if P2favoriteDate == "Yui":
        jump p2d3pd_sd1

    "I like Allie the most now" if P2Date3 == "Allie":
        jump p2d3pd_sd2
    "I like Scarlett the most now" if P2Date3 == "Scarlett":
        jump p2d3pd_sd2
    "I like Terra the most now" if P2Date3 == "Terra":
        jump p2d3pd_sd2
    "I like Violet the most now" if P2Date3  == "Violet":
        jump p2d3pd_sd2
    "I like Yui the most now" if P2Date3  == "Yui":
        jump p2d3pd_sd2

    # OLD UNTRANS FORMAT
    #"[#P2favoriteDate]":
    #    jump p2d3pd_sd1
    #"[#P2Date3]":
    #    jump p2d3pd_sd2

label p2d3pd_sd1:

if P2favoriteDate == "Allie":
    m "...Allie is still my number one."
elif P2favoriteDate == "Scarlett":
    m "...Scarlett is still my number one."
elif P2favoriteDate == "Terra":
    m "...Terra is still my number one."
elif P2favoriteDate == "Violet":
    m "...Violet is still my number one."
elif P2favoriteDate == "Yui":
    m "...Yui is still my number one."

# m "...[#P2favoriteDate] is still my number one."
m "I've been counting the days till I can see her again."
m "...And I know it's going to be worth the wait."
show k laugh
k "Damn! That's definitely going to go in the broadcast. I couldn't write that much cheese if I tried!"
show k sassy
k "I've got some good news for you, then."
jump p2d3pd_After

label p2d3pd_sd2:
#m "Though I've known her for less time, I think I like [#P2Date3] more than [#P2favoriteDate] now."

if P2Date3 == "Allie":
    m "Though I've known her for less time, I think I like Allie more."
elif P2Date3 == "Scarlett":
    m "Though I've known her for less time, I think I like Scarlett more."
elif P2Date3 == "Terra":
    m "Though I've known her for less time, I think I like Terra more."
elif P2Date3 == "Violet":
    m "Though I've known her for less time, I think I like Violet more."
elif P2Date3 == "Yui":
    m "Though I've known her for less time, I think I like Yui more."

$ P2favoriteDate=P2Date3

if P2Date3 == "Allie":
    jump p2d3pd_FlavorCommentAllie2
if P2Date3 == "Scarlett":
    jump p2d3pd_FlavorCommentScarlett2
if P2Date3 == "Terra":
    jump p2d3pd_FlavorCommentTerra2
if P2Date3 == "Violet":
    jump p2d3pd_FlavorCommentViolet2
if P2Date3 == "Yui":
    jump p2d3pd_FlavorCommentYui2

label p2d3pd_FlavorCommentAllie2:
m "She makes every moment exciting, and I just can't get enough of that."
jump Afterp2d3pd_FlavorComment2

label p2d3pd_FlavorCommentScarlett2:
m "It's amazing how brilliant she is. And I can't ever quite place her. She's fascinating."
jump Afterp2d3pd_FlavorComment2

label p2d3pd_FlavorCommentTerra2:
m "Say what you will about Terra, it's always exciting to be around her."
jump Afterp2d3pd_FlavorComment2

label p2d3pd_FlavorCommentViolet2:
m "I don't know as much as I'd like about Violet just yet, but I know more than anything that I just want to keep learning more about her."
jump Afterp2d3pd_FlavorComment2

label p2d3pd_FlavorCommentYui2:
m "It's Yui, you know? It's practically self-explanatory. She's the best."
jump Afterp2d3pd_FlavorComment2

label Afterp2d3pd_FlavorComment2:
m "...I can't wait to see her again."
show k laugh
k "You really do change your mind like the wind, huh?"
show k sassy
k "Doesn't matter to me, though. I'm your producer, not your life coach."
show k flirt
k "Anyway, I've good news that you might be interested in!"
m "What's that?"
jump p2d3pd_After

label p2d3pd_After:
show k happy
k "My plan was a success! Having three soulmate candidates has worked magic for our ratings!"
show k laugh
k "Which of course... means the show will go on!"
m "That's awesome! So I'm safe now?"
show k neutral
k "Just for now, though we're not out of the woods just yet. We need to make sure the next stretch of the show rates even higher."
show k flirt
# OLD UNTRANS: k "It's time for phase two! Over the next three days, you'll go a second date with each of [#P2Date1], [#P2Date2], and [#P2Date3]."
k "It's time for phase two! Over the next three days, you'll go a second date with each of the girls you've already dated."
show k laugh
k "Just imagine how much higher our ratings would be if our viewers got to see even more of their favorites falling in love!"
show k sassy
k "Just imagine that sweet ad revenue rolling in. Mmm..."
show k laugh
k "Sorry, I got distracted for a second. Sound good to you?"
m "Sounds like a plan to me."
show k laugh
k "Good! That's what I like to hear."
show k neutral
k "Tomorrow morning, I'll be asking you who you want to have your first second date with."
show k flirt
k "Put some thought into that. Sometimes the order of content is just as important as the content itself for ratings."
m "Will do. Thanks, Kat."
show k neutral
k "No biggie. I gotta get back to work, so I'll seeya later."
show k laugh
k "'Night!"
hide k with dissolve
"I waved goodbye to her as she walked away from the mansion."
show bg Black with dissolve
"...Guess it's time to turn in for the night."

#; Allie Flashback

stop music
play music LoveTheme
"..."
"We borrowed a boat and went for a cruise around the island."
q "I love the way the wind feels."
m "Why's that?"
q "Feels like freedom! Can't get enough of it."
q "No cameras, no people, nothing to stop me from..."
"She pulled me close and kissed me on the lips."
"For a moment, time stopped, and we were the only two people that existed."
q "...Doing what I want."
"I smiled."
m "I'm pretty sure we don't need to be all the way out here just for a kiss."
q "I guess you're right. After all, it's hotter if people are watching."
"We laughed together as we cruised along till the sun went down. The world was ours."
"The sound of waves grows louder and louder, threatening to pull me back into reality."
"...Will I know you, before I'm taken under?"
jump MorningSelector
