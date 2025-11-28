label P2Day8postDate:

play music PastSadness
$ P2Date8=selectedDate
$ currentDay=9

play music PastSadness
show bg MansionNight with dissolve

if selectedDate == "Allie":
    "After my date with Allie, I waited around outside till the time I'd expect to see Kat, but she never showed up."
elif selectedDate == "Scarlett":
    "After my date with Scarlett, I waited around outside till the time I'd expect to see Kat, but she never showed up."
elif selectedDate == "Terra":
    "After my date with Terra, I waited around outside till the time I'd expect to see Kat, but she never showed up."
elif selectedDate == "Violet":
    "After my date with Violet, I waited around outside till the time I'd expect to see Kat, but she never showed up."
elif selectedDate == "Yui":
    "After my date with Yui, I waited around outside till the time I'd expect to see Kat, but she never showed up."

# OLD UNTRANS
#"After my date with [#selectedDate], I waited around outside till the time I'd expect to see Kat, but she never showed up."
"I guess she already has enough footage for today."
"Might as well try to find her."
show bg KitchenNight with dissolve
"...No one's here. Looks like the snacks from before are gone too."
show bg GamesRoomNight with dissolve
show t gaming at pos50t with dissolve
"...Not here either."
hide t with dissolve
show bg Library with dissolve
"Ah."
show k serious at pos50k with dissolve
"Kat was at a table, writing something down at a frantic pace, with one hand against her head."
m "Hey Kat, what's up?"
show k serious
k "..."
show k surprised
k "...?"
show k flirt
k "Oh, hey [name]. I didn't see you there."
show k neutral
k "How are you doing?"
m "That depends on what you're ominously writing."
m "You looked just like someone who just realized I was dead meat."
show k laugh
k "Oh, this? Don't worry about it."
show k flirt
k "Somebody's dead meat, but it's not you!"
m "...Yay?"
show k laugh
k "I'm just kidding. I'm just fixing up some of the balance sheets Two was working on."
show k surprised
k "Being an accountant was really never in the cards for them, despite what they say."
show k flirt
k "Sit down! I'll be stuck here a while anyway."
m "Sure, sounds good."
"I sat next to Kat at the table."
show k neutral

if selectedDate == "Allie":
    k "So how'd today's date with Allie go?"
elif selectedDate == "Scarlett":
    k "So how'd today's date with Scarlett go?"
elif selectedDate == "Terra":
    k "So how'd today's date with Terra go?"
elif selectedDate == "Violet":
    k "So how'd today's date with Violet go?"
elif selectedDate == "Yui":
    k "So how'd today's date with Yui go?"

menu:
    #old untrans
    #k "So how'd today's date with [#selectedDate] go?"

    "Awesome":
        jump p2d8pd_awesome
    "Alright":
        jump p2d8pd_alright

label p2d8pd_alright:
m "...It was alright. Not the way I wanted it to go."
show k neutral
k "Ah, I'm sorry to hear that. I won't pry."
show k laugh
k "Who knew that three dates wasn't enough to see if someone really is your soulmate!"
jump p2d8pd_advice

label p2d8pd_awesome:

if selectedDate == "Allie":
    jump p2d8pd_thirdAllie
if selectedDate == "Scarlett":
    jump p2d8pd_thirdScarlett
if selectedDate == "Terra":
    jump p2d8pd_thirdTerra
if selectedDate == "Violet":
    jump p2d8pd_thirdViolet
if selectedDate == "Yui":
    jump p2d8pd_thirdYui

label p2d8pd_thirdAllie:
"...I probably shouldn't tell the whole truth, but enough of it should be good."
m "...It was awesome! I don't know how, but the more time I spend with Allie, the better it gets."
m "Being married to her would make every day an adventure... and I like the sound of that."
show k laugh
k "I'm sure it'd be an adventure, but the jury's out on if it's one you'd walk away from!"
show k happy
k "But I can see she makes you happy. Really, that counts for a lot nowadays."
show k bored
k "Though you might want to start wearing body armor, if you want to stay that way."
jump p2d8pd_advice

label p2d8pd_thirdScarlett:
m "...It was the best."
m "My connection with Scarlett's one of a kind, and there's no one I'd rather have beside me than her."
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
jump p2d8pd_advice

label p2d8pd_thirdTerra:
m "It was nice! We didn't do anything too crazy, but... it didn't have to be."
show k flirt
k "I could tell! It was cute watching you guys."
show k laugh
k "Though to be honest, I wish your relationship would move along a little faster! This show's not getting any longer, you know."
show k happy
k "That said, I feel like you two would make a pretty good team in the long run."
jump p2d8pd_advice


label p2d8pd_thirdViolet:
m "Being with Violet makes me feel like we're on top of the world."
m "Somehow, she takes my breath away with how cool she can be... and at the same, make me laugh like a child alongside her."
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
jump p2d8pd_advice

label p2d8pd_thirdYui:
m "Yui's the most wonderful woman in the whole world."
m "Somehow, she can take the most normal things and turn them into irreplaceable memories."
m "More than anything, I just want to make more memories with her, every day."
m "...And make her the happier than anyone's ever been."
show k surprised
k "Jeez, we're going to have to edit that to stop people from throwing up!"
show k sassy
k "I get it, though. You, my friend, are luckier than anyone has any right to be."
show k laugh
k "Better pack your bags! I've got a feeling you'll be heading to the countryside soon!"
jump p2d8pd_advice

label p2d8pd_advice:
show k flirt
k "...Anyway, you've done great till now."
show k laugh
k "I don't know if what you've said to each of the girls really is true, but... don't stop now!"
show k neutral
k "You just have to get through one more day, and you'll be able to finally leave this place."
m "...And you'll tell me what my old life was like?"
show k happy
k "...Of course."
show k laugh
k "I mean, if I didn't, where would you even go?"
m "Fair point."
show k sad
k "..."
m "You look like you've got something on your mind."
show k worried
k "Ah..."
show k neutral
k "I'm just thinking about tomorrow."
show k serious
k "You've been getting the best ratings I'd ever seen... I just hope it's enough."
show k sad
k "The rating requirements for the last date, and the last day, are the highest."
show k surprised
m "...I'm sure it's going to be fine, don't worry."
m "I've made it this far. Nothing's going to stop me from making it to the end."
show k neutral
k "I hope so, for your sake, [name]."
show k surprised
m "So when I'm out of here... what are you going to do?"
show k neutral
m "Are you going to move on to the next killer dating show?"
show k laugh
k "I didn't know you were my career coach!"
show k flirt
k "You want to know my five year plan too?"
m "...I get the feeling that five years from now, you'd rather not be here."
show k sad
k "...There is no plan."
show k neutral
k "I'm just taking it one day at a time."
show k laugh
k "That's really all anyone can do in the crazy world."
show k flirt
k "Anyway, I gotta get back to work."
show k neutral
k "Good luck, [name]. You'll need it."
m "Thanks, Kat. I'll see you later."
show k laugh
k "'Night!"
hide k with dissolve
"...Tomorrow's going to be the last date."
"I'll need all the rest I can get."
#show bg MansionIndoorsNight time:2
"Guess I'll call it a night."
show bg RoomNight with dissolve # time:2
show bg Black with dissolve # time:2
stop music
play music LeavingHome
#; have a dynamic last flashbakc based on


#; REWORD THIS AS ITS NOT A CONCERT ANYMORE!!!!"

#;; reactive based on who you maxed first?"
"The performance is coming to a close."
"The actors and actresses come out, one by one, ready to take their bows."
"I would clap... but I'm waiting for you, and only you."


jump MorningSelector
