label P3Intro:
window show dissolve
show bg Lab with dissolve
play music LeavingHome

"..."
"...Where... am I?"
"I'm... underwater?"
"It's so dark... and cold."
"I try to move, but I'm... so tired..."
"It takes all my strength to reach my hand out forward."
"...Feels like glass. I'm trapped in some kind of tank."
"...I..."
"...I want to sleep... for just a..."
show bg Black with dissolve
"..."
"..."
"..."
show bg Lab with dissolve
"...Is someone... there?"
"...I can feel somebody's presence."
"I open my eyes... and I can see."
show a serious at pos50a with dissolve
a "...Hang on, just a little longer, [name]."
"...Who are you?"
show a worried
"The woman in front of me looked at me with pity."

menu:
    n "I..."

    "Say something":
        jump p3i_addChoice1

    "Hit the glass":
        jump p3i_addChoice2

label p3i_addChoice1:
"I try to speak, but it's no use. My mouth won't speak the words I want them too."
jump p3i_addAfter

label p3i_addChoice2:
"I hit the glass, with what little strength I have."

label p3i_addAfter:

show a surprised
a "...You're awake!"
show a happy
a "I'm so glad, but..."
show a worried
a "...You're gonna wish you were asleep for this next bit, trust me. And... sorry in advance."
"...?"
show a neutral
"She moved towards some kind of terminal next to my tank, and pressed a button."
play sound Gunshot
"As if on cue, it was if every nerve in my body was set on fire."
"I screamed and thrashed around, but it did nothing to alleviate the pain."
play sound Glitch1
hide a #with dissolve

show d laugh at pos50d # former look:right
d "{glitch=50}{b}Oh, will you look at that! Looks like our little hero's got some life left in him.{/b}{/glitch}"
show d happy
d "You know, [name]... you're in luck."
show d neutral
d "Usually, I'd just kill you for this - but a new opportunity's just opened up, and I think..."
show d evil_smile
d "...You'd be the perfect fit."

play sound Glitch2
show d evil_smile at pos30d # former look:right
show k flirt at pos70k # former look:left
k "{glitch=50}{b}...I'm sorry [name], but it's true.{/b}{/glitch}"
m "I... I don't understand."
show d laugh
d "Why don't you tell him, dear?"
show k neutral
k "...Damian is my father."

play sound Glitch1
hide k
hide d
with dissolve
show bg KatShootingYouSmug with dissolve
k "{glitch=50}{b}Always the hero, aren't you, [name]?{/b}{/glitch}"
k "...You should be more worried about yourself."
k "You knew the rules. If you try to escape the island, you die."
k "It didn't have to be like this, but you..."
k "...I'm done talking."
play sound Glitch2
k "{glitch=50}{b}Goodbye, [name].{/b}{/glitch}"
play sound Gunshot

show bg Lab #with dissolve

show a worried at pos50a
a "Hold on just a little longer, [name]!"
"She looked away from me, as if she had heard something. What, I couldn't tell."
show a surprised
a "Shit, they're almost here! We're running out of time."
show a sad
a "I'm sorry, [name]. I won't be able to give you back all your memories, but... this will have to be enough."
show a serious
"She pressed another button on the terminal."
show a sad
a "I've got to run back to my tank, or they'll know something's up."
"She pressed her hand against the glass."
show a happy
a "...Hold on just a little longer, okay?"
show a serious
a "I'll get us out of here."
hide a with dissolve
hide k with dissolve
hide d with dissolve
show bg Black with dissolve
"The pain... it stopped..."
"I..."
"The world turned dark."
"..."
"..."
stop music
play music MasterDisorder
show bg PlaneBar with dissolve
"...?"
"I've... been here before."
"I... I'm [name]."
"I'm on some kind of dating show... {i}Find Love or Die Trying{/i}."
"Allie, she... helped me. I've got to find her, I..."
show k flirt at pos50k with dissolve
k "You're up early!"
show k laugh
k "Most people around here usually need a little more to wake them up!"
"...Kat."
"I... remember now. I tried to escape this island with her."
"She pretended to be my lover. She betrayed me, and shot me too. She's the reason why I'm trapped here."
"It's only fragments I can remember, but I remember enough to know that that she's bad news."
"We've done this song and dance, over and over, more times than I can count by now."
"I've been in love with, and chosen Allie, Scarlett, Terra, Violet, and Yui... each of them, countless times."
"...Am I a bad person?"
#I remember what happened... but not the feelings I once had."
"Come to think of it... I can't remember what happened before this show started, either."
"...I need to find Allie. But first, for the problem at hand..."
"If I want to get out of here, I can't let Kat know that I remember what's happened before."

menu:
    "Sorry, who are you?":
        jump p3i_addChoice3
    "Where am I?":
        jump p3i_addChoice4

label p3i_addChoice3:
"I've got to play dumb."
m "...Sorry, who are you?"
jump p3i_addAfter2

label p3i_addChoice4:
"I've got to play dumb."
m "...I know this sounds weird, but do you know where we are?"

label p3i_addAfter2:
show k serious
k "..."
"Will she buy it...?"
show k flirt
k "...Walk with me. There's a lot to get you up to speed on."
show k happy
k "The name's Kat! I'm the producer for a new show, {i}Find Love or Die Trying{/i}."
show k flirt
k "And what's your name?"
m "I..."
m "...I don't remember."
show bg MansionMorning with dissolve # time:2
"Looks like it's the same beginning as usual - learn about the killer dating show's rules, meet the girls before the show starts."

hide k with dissolve
show bg MansionIndoorsMorning with dissolve
show y happy  at pos50y with dissolve
"...Yui. I don't remember meeting you before this show, but I'm glad I got to meet you again."
"It's impossible not to feel happier when I see your smile."
hide y with dissolve

show bg KitchenMorning with dissolve
show v happy  at pos50v with dissolve
"...You'd think that the staff would have learned to cook better by now."
"There's so much more to you than you show the world, Violet."
hide v with dissolve

show bg Library with dissolve
show s surprised at pos50s with dissolve
"...Scarlett. You're still hiding that you're reading that magazine with another book. It brings a smile to my face every time."
"I think I know what happened to you now."
hide s with dissolve
show bg GamesRoomMorning with dissolve
show t happy at pos50t with dissolve
"...You still have no idea what you got into, Terra. Killer dating show or not."
"I'd love to see the way you see the world."
hide t with dissolve
show bg Hills with dissolve

show a neutral at pos50a with dissolve # former look:left  at pos50
"...And finally, Allie."
"You never gave up on getting us out of here, even after all this time."
a "Howdy, [name]! I hear you're the suitor!"
show a happy
a "Care to join me for a jog?"
show a laugh
a "There's a place in the forest I'd love to go for a run around with you."
m "It'd be my pleasure."

"We went for a jog, exchanging banter like we'd always done when we met each other."
show bg LakeMorning with dissolve
stop music
play music Twisting
"The second we got to the unrecorded area of the forest, her smile faded."
show a neutral
a "I'm glad you got the hint, [name]."
show a serious
a "You haven't given yourself away to anyone yet, right?"
m "No, I haven't. As far as Kat knows, I don't remember anything as usual."
show a happy
a "Sweet! I knew I was right to help you first."
m "Really... thank you so much. I can't thank you enough."
m "I've got to ask, how did you escape the tank in the first place?"
show a sassy
a "Honestly? I got lucky."
show a neutral
a "Usually, the tank knocks me out right away - but that last time, I think something must've bugged out."
show a sassy
a "I saw my chance, and took it. Anything's better than being stuck here forever."
show a sad
a "I'm... sorry I couldn't get all your memories back."
m "Don't worry about it, Allie. All I could ask for is a fighting chance, and you gave that to me."
show a blush
a "Don't - don't mention it."
show a angry
a "I mean, duh. I'm hands down the MVP."
show a neutral
a "Anyway... it's about time I tell you the truth, [name]."
show a serious
a "I'm from the Resistance."
show a laugh
a "You can think of us as a covert group of... concerned citizens, who have a... few bones to pick with the world's current management."
show a angry
a "And those bones are their necks."
show a annoyed
a "Joking aside, we are fighting a war here."
show a serious
a "That war will be won with information - information that lives on this island, and only here."
show a worried
a "There was no way that we could ever find this place, not by conventional means."
show a happy
a "But then we found out about the show."
m "...And so they sent you here."
show a laugh
a "Actually, I volunteered!"
show a worried
a "Believe me, the others didn't want me to, but I knew I had to."
show a sad
a "...I was the one with the least to lose."
m "Allie..."
show a laugh
a "It was pretty easy getting in, all things considered!"
show a happy
a "All I had to do was write a report that labeled me as \"suspicious of conspiring against the government\", take a few cute selfies, and BOOM! I was flown here."
show a worried
a "Didn't go too great since then, though."
show a happy
a "But that was when I was a lone wolf. I've got you now."
show a sassy
a "And we'll get out of here together. Sound good to you?"
m "Sounds like a plan!"
show a surprised
a "...I haven't even told you the plan yet."
show a sassy
a "But since you're so excited, let's get right to it!"
show a neutral
a "There's two things we need to do."
show a serious
a "One - we need to bring the other girls' memories back."
show a annoyed
a "We won't be able to get their trust, or work with them till we do."
show a serious
a "...And we'll need their help for part two."
m "And what's that?"
show a sassy
a "Two - we need to get the fuck outta here."
m "Sounds about right."
show a worried
a "Easier said than done, though. It's going to take a hell of a lot of setup and coordination."
show a serious
a "There's a small army of armed and trained staff tasked with keeping us here, not to mention us needing a way off the island."
show a worried
a "...I'll figure it out as we go, but for now..."
show a sassy
a "...How about you go on a date with Scarlett today?"
m "I can do that, but how does that relate to us getting out of here?"
show a laugh
a "I'd tell you, if I thought you could be a better actor!"
show a happy
a "Believe me, you'll know why later."
show a serious
a "Anyway, let's head back to the mansion. We don't want Kat to start looking for us."
m "Sounds good to me."
m "You're really something, you know?"
show a sassy
a "That's putting it lightly!"
hide a with dissolve
show bg Black with dissolve

"..."
show bg MansionMorning with dissolve
stop music
play music MasterDisorder
show k happy  at pos50k with dissolve
k "[name]! There you are!"
m "Sorry, I got carried away exploring the island."
"I've got to be careful around Kat."
"I know exactly what she's capable of, first-hand."
show k flirt
k "...Is that so?"
show k laugh
k "Well, it's no harm, but you'll have a whole week to explore, you know?"
show k happy
k "You'll get one date with each of the girls, for the first five days."
show k sassy
k "A little something special for day six..."
show k flirt
k "And then the final ceremony, where you propose to one of the girls."
m "That sounds like the perfect amount of time to figure out if we're meant together."
show k laugh
k "You'd be surprised!"
show k flirt
k "Anyway, let's get the show on the road!"
show k happy
k "Who do you want to spend today's date with?"
m "...Scarlett. There's just something about her, you know?"
show bg Black with dissolve
hide k with dissolve


"..."
stop music
play music CrinolineDreams
show bg Library with dissolve
show s happy  at pos50s with dissolve
"I found Scarlett inside the library - the place I'd most often meet her for the first time."
"She always looked so happy when she was reading."
"It did the heart good to try to make her smile in the same way when I talked with her."
show s laugh
"We became fast friends again. The similarity of our situations might've played a part in that."
"Still, I'm not sure why Allie insisted in me going on a date with Scarlett today."
"Sure, getting her memories back will be a huge win, but..."
show s surprised at pos30s with dissolve
show k worried at pos70k with dissolve
stop music
play music RavingEnergy
k "Hey! Scarlett, [name]!"
show k worried
k "I'm glad you're safe. Things are going crazy out there!"
show s worried
s "What's happening?"
show k serious
k "I know it sounds crazy, but there's a horde of zombies outside!"
show k worried
k "The Brothers Five, and a lot of our behind-the-scenes help went crazy, and..."
show k flirt
k "...Scarlett, you did this, didn't you?"
show s surprised
show k surprised
s "Wait, what? I-I've been here the whole time with [name], I couldn't have!"
show s worried
s "I've never heard of anything like this!"
"...Wait, what?"
show k serious
k "...?"

menu:
    "It's true":
        jump p3i_addChoice5
    "Actually...":
        jump p3i_addChoice6

label p3i_addChoice5:
m "I can vouch for her, we've both been here since our date started."
show k flirt
k "...Well, either way, I bet you can create a cure for it, no?"
jump p3i_addAfter3

label p3i_addChoice6:
m "Actually..."
show k bored
k "Whatever, it doesn't matter."
show k flirt
k "Either way, I bet you can create a cure for it, no?"

label p3i_addAfter3:
show s sad
s "...I mean, I probably could, but I'd need my equipment."
show s worried
s "I'm not sure why, but I can't find it anywhere."
show k annoyed
k "Tch."
show k serious
k "..."
show k worried
k "...Follow me, you can use our lab."
"...!"
hide k with dissolve
hide s with dissolve
show bg GamesRoomMorning with dissolve
"We followed Kat to the Games Room."
stop music
play music HalfMystery
"Kat put her hand against the wall of the Games Room, revealing a hidden trap door."
"She walked in, and beckoned for us to follow."
show bg Black with dissolve
"We walked down spiraling stairs for who knew how long - I lost track more than a few times."
$ renpy.pause(delay = 1.0, hard = True)
show bg Lab with dissolve
"...I remember this place."
show k serious at pos70k with dissolve
k "You should have everything you need in this room to make a cure."
show k laugh
k "Just don't go snooping around. This lab belongs to... R&D, and we could all get in trouble if you do."
show s worried at pos30s with dissolve
s "...Actually, this place doesn't have everything I need."
show k surprised
k "...What else do you need?"
show s serious
s "To build a cure, I'm going to need a sample of whatever this is. I need a live specimen."
show k worried
k "..."
stop music
play music ShavingMirror
show k laugh
k "I'm sure you can help with that, [name]!"
show k happy
k "I've got, uh... some editing that needs my attention. You got this!"
hide k with dissolve
show s surprised at pos50s with dissolve
"...And just like that, she was gone."
show s happy
s "If it makes you feel better, I'll help you catch somebody."
m "You sure? If you're the only one who can make the cure, then it might be better for you to stay back."
show s laugh
s "No thanks!"
show s happy
s "There's no way I'm letting you out there alone."
show s worried
s "I don't want you to think I'm weird, but... I've just got this feeling that I'd be pretty good at collecting... unwilling zombie specimens."
"That is weird, but in this case, she's absolutely correct."
"Some memories must be intact, even if they're kept below the surface."
show s neutral
s "Well, let's get on with this!"
hide s with dissolve
show bg Black with dissolve
$ renpy.pause(delay = 1.0, hard = True)
stop music
show bg MansionMorning with dissolve
play music RocketPower
"We went back up to the surface."
"Everywhere we looked was overrun by zombies."
"We wouldn't stand a chance against a group, so we spend the day trying to split them up, as well as searching for lone wolves."
show bg BeachEvening with dissolve
show s serious at pos30s with dissolve # former look:right
show b4 angry at pos70b with dissolve # former look:left
b4 "BRAINS!!!! BANANAS!!!!"
show s flirt
s "We're in luck! We've finally got an isolated sample."
m "How are we supposed to bring him in, though?"
m "One bite and we're finished."
show s laugh
s "I've got just the thing!"
show s happy
"Scarlett pulled out a pair of brass knuckles."
m "...Where did you even get that?"
show s laugh
s "Is that really important right now?"
show s flirt
s "You mind looking the other way for a second? It's embarassing."
m "...Sure, Scarlett."
# hide s with dissolve
"I turned around."
b4 "BRAIIIIIINS!!!! BANANASSSS!"
s "I hope your health insurance covers this!"
show s angry at pos70s with easeinleft
play sound Hit
with vpunch
hide b4 with dissolve

"*Thwack*"
#hide b4 with dissolve
b4 "Bleeegh..."
s "Once more, with feeling!"
play sound Hit
with vpunch
"*Thwack*"
hide s with dissolve
show bg Black with dissolve
"...Are we the bad guys?"
"We dragged him back to the mansion, paying careful attention to not run into any more of the zombies running amok."
show s neutral at pos50s with dissolve
"Scarlett opened the hidden trapdoor in the games room, and I pulled Four's unconscious body in."
m "Oh, fu-"
show s surprised
"My hand slipped, causing Four's body to tumble down the stairs."
play sound Hit
with vpunch
"*Bonk* *Bonk* *Bonk*"
play sound Hit
with vpunch
"He just kept going and going."
show s serious
s "..."
m "I know, I know, I'll get him."
show s laugh
s "Better get him quick, or we're not going to have a live specimen!"
show bg Lab with dissolve
show s happy
stop music
play music Sincerely
"...Luckily, I managed to catch him pretty quickly."
"We put him on the operating table for Scarlett to analyze."
show s surprised
s "...Interesting."
m "What's up, Scarlett?"
show s worried
s "This virus... it's pretty clear it's man-made."
show s surprised
s "Even more interesting is that it looks like... something I would make."
show s worried
s "Err... not that I ever made zombie viruses, [name]. Hahaha..."
"...Yes you have. It's kind of cute how you try to hide it."
show s serious
s "..."
show s neutral
s "Kat, you there?"
"..."
show s worried
s "Weird. I thought Kat was supposed to be able to hear us from anywhere on the island."
m "Maybe there's no microphones all the way down here?"
show s neutral
s "I guess so."
show s happy
s "I was going to tell her we've got the cure now!"
m "Sweet! Great work, Scarlett."
show s flirt
s "You bet I did."
show bg GamesRoomEvening with dissolve
"We administered the cure to Four, then went back upstairs together."
show s neutral
s "Kat, you there?"
play sound Intercom
k "What's up, Scarlett? I've been waiting hours for you guys. You two done yet?"
show s happy
s "We've got the cure now! We'll need your people's help to help administer it."
k "We'll be right on it! Lay low for now, we're coming to get you."
stop music
play music AlmostBliss
show s flirt
s "In the meantime, [name]... how about you tell me about yourself?"
m "...It'd be my pleasure."
show bg Black with dissolve
hide s with dissolve
#..That confirmeds it - there's no microphones down in the lab."
"With Kat's help, we managed to quell the zombie plague, with just enough time left in the day for a lovely dinner with Scarlett."
show bg LakeNight with dissolve
stop music
play music ICanFeelItComing
"After that, I went for a night walk with Allie - to somewhere safe from prying eyes."
show a surprised at pos50a with dissolve
a "You should buy a girl dinner first before you murder her in the woods, you know."
m "I think I found the way to bring the others' memories back."
show a happy
a "...You found their lab, didn't you?"
m "Pretty much!"
show a sassy
a "Sweet. I wasn't sure how to get back there after they shipped us out of there, so that's a huge win."
show a happy
a "So where is it?"
m "There's a secret trapdoor in the games room - you just have to press a hidden panel in the wall."
m "That said, how are we supposed to get in without being seen?"
m "There's cameras everywhere, and Scarlett and I were only allowed to enter because of the whole pandemic."
show a sassy
a "Don't you worry about that. I've got an inside man."
show a happy
a "Four's gonna be helping us override a few cameras and microphones in the mansion with old recordings."
"...Four?"
show a sassy
a "That way, we can get in and stay inside along enough to get their memories back, without raising any sort of fuss."
"...The brother that we KO'd today down the stairs?"
show a surprised
a "What's that look for?"
m "...I'm surprised he's still standing after today, to be honest."
show a laugh
a "I wouldn't work with people who go down that easy!"
m "Was Four always working with you?"
show a neutral
a "Nope, never till now. But we can't afford to refuse his help."
show a happy
a "I've had him prove he's trustworthy, don't worry. You can count on him."
m "Alright, if you say so."
show a sassy
a "Anyway, we have everything we need for the first part of the plan."
show a laugh
a "Up for a trip down memory lane together?"
m "Sounds like a plan."
hide a with dissolve
show bg GamesRoomNight with dissolve

"..."
show y surprised at pos10y with dissolve
show t surprised at pos90t with dissolve
show s happy at pos30s with dissolve
show v neutral at pos70v with dissolve
show a happy  at pos50a with dissolve
a "You guys have to see this - trust me."
"Allie put her hand against the secret panel."
"A second later, the wall parted to reveal the winding staircase Four became intimately and repeatedly familiar with."
"...Did Allie \"prove\" Four's trust before, or after his little trip on the stairs?"
stop music
play music TheShowMustBeGo
show t surprised
t "Woah, you guys found my secret spot already?"
show a surprised
a "I'm sorry... what?"
show t happy
t "I found this place this morning!"
show t neutral
t "I sat near the top of the stairs and played for a while. It was more fun to play in the dark."
show a angry
a "...Hold me back, [name]."
show bg Black with dissolve
hide y with dissolve
hide s with dissolve
hide v with dissolve
hide t with dissolve
hide a with dissolve
stop music
play music MiamiNights
"..."
"Allie explained the situation as we walked down the stairs."
"Sure enough, they were skeptical."
"...Except for Scarlett."
show bg Lab with dissolve
show y worried at pos10y with dissolve
show t surprised at pos90t with dissolve
show s serious at pos30s with dissolve
show v serious at pos70v with dissolve
show a serious  at pos50a with dissolve
y "...Okay, your story makes a little more sense when you come down there."
"We walked towards the machines, in a mixture of awe and fear."
show t worried
show v surprised
v "The markings on this machine... my father's company made these. Why...?"
show s sad
s "...They didn't. Not my baby..."
show a worried
a "I'm sorry, everyone."
show a serious
a "I wish what I had to say wasn't true, but it is."
show a sad
a "I don't know why we're being kept here, why they film the show over and over."
show a angry
a "But I know that if we don't escape, and fast, they're going to kill us, sooner or later."
show a serious
a "[name] and I are going to do our very best to make sure all of us get out of here alive."
show a worried
a "But to do that... I need you to trust me."
show v sad
v "...Trust you with what?"
show a serious
a "I need you to trust me enough to step back into the tanks they kept you in."
show a worried
a "For us to escape, we need all of us to have our memories back - otherwise you won't trust us enough."
show v angry
v "I'd have to be quite foolish to just step into this tank because someone said so."
show a sad
a "..."
show s serious
s "Violet, you can trust her."
show v surprised
v "Excuse me?"
show s sad
s "I know she's telling the truth about this machine... because I built this."
show s serious
s "...Allie."
show a surprised
a "?"
show s sad
s "This isn't the first time we've met, is it?"
show a sad
a "...No, it isn't."
show a serious
a "We've gotten to know each other quite a few times by now."
show s happy
s "It's a strange feeling."
show s laugh
s "On one hand, this is horrible."
show s happy
s "On the other... I'm glad that the machine works."
show s sad
s "...Maybe one day, we'll put it to use the way it should be."
show v sad
v "...Alright, I'll trust you."
show v worried
v "We just walk back into the machine?"
show a happy
a "...Thank you, Violet. I know it'd be difficult to trust me, so I appreciate it."
show a neutral
a "There's a machine that should have your name on it - go into it, and then [name] and I will start the reversal process."
show v sad
v "I do hope this works."
show s happy
s "It should, but it might hurt a bit."
show v worried
v "Do spare me from the details, please..."
hide v with dissolve
hide s with dissolve
"Scarlett and Violet walked to their respective machines."
show t happy
t "I don't really get it, but I trust you, [name]."
show t neutral
t "And besides, I got a thing for big things made out of metal - they're like mecha!"
show a surprised
a "I guess?"
hide t with dissolve
show y worried at pos30y with dissolve

menu:
    y "...Is this going to hurt?"

    "It is":
        jump p3i_addChoice7
    "It won't hurt a bit":
        jump p3i_addChoice8

label p3i_addChoice7:
m "...It is. I'm sorry, Yui."
show y happy
y "...Don't be, [name]."
show y laugh
y "I'm happy you wouldn't lie to me - it makes me even more sure to trust you."
show y worried
y "...Here we go, Yui! Let's do this."
hide y with dissolve
jump p3i_addAfter4

label p3i_addChoice8:
m "I'm sure it won't hurt that much."
show y worried
y "...I'll take your word for it, [name]."
hide y with dissolve

label p3i_addAfter4:

show a serious
a "Alright, they're in their tanks."
#; can put a choice here later for who you undo for
show a neutral
a "Let's do this, [name]."
m "On it."
hide a with dissolve
show bg Black with dissolve
"..."
"Even if it was necessary for all of us, their screams from the reversal process were almost more than I could take."
"Allie and I covered our ears as Violet, Scarlett, Yui, and Terra remembered years of memories in a matter of minutes."
"...After doing all this, we better be getting out of here."
"..."
show bg Lab with dissolve
show a surprised at pos10a with dissolve
show t worried at pos90t with dissolve
show s worried at pos30s with dissolve
show y worried  at pos70y with dissolve
show v worried at pos50v with dissolve

stop music
play music Twisting
"Violet, Scarlett, Yui, and Terra stepped out of their tanks, after what must have felt like hours to them."
m "Guys? You okay?"
show a laugh
a "...This probably isn't the time to mention it, but I made a bet with Four about what would happen when they got their memories back."
m "...? What did you bet?"
show a happy
a "...I'm going to watch from a... safer distance, if you don't mind."
hide a with dissolve
m "...?"
show s angry at pos15s with dissolve
show y angry at pos35y with dissolve
show v angry at pos55v with dissolve
show t angry at pos75t with dissolve
stop music
play music LeGrandChase
"If looks could kill, the girls that had just gotten out of the tanks would have killed me several times over."
"They ran to me yelling and screaming."
with vpunch
all "You five-timing little cheater!!!!"
m "Wait - I can explain, I -"
"Too late - they were on me like hyenas."
with vpunch
m "AaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAA"
show bg Black with dissolve
hide a with dissolve
hide s with dissolve
hide y with dissolve
hide v with dissolve
hide t with dissolve
$ renpy.pause(delay = 1.0, hard = True)
stop music
play music CarpeDiem
show bg Lab with dissolve
"..."
show a laugh at pos50a with dissolve
a "...Now that we've all calmed down... how about we go over the escape plan?"
show y angry at pos30y with dissolve
y "...It better be good, Allie."
show y laugh
y "For your sake, [name]."
show v annoyed at pos70v with dissolve
v "Out with it, then!"
show a happy
a "Alright, listen up..."
"Over the next hour, Allie explained her plan, from start to finish."
show s surprised at pos10s with dissolve
show v surprised
show t surprised at pos90t with dissolve
show y surprised
show a laugh
a "...Trust me, it's the best we got!"
"If this is our plan..."
"...we're doomed."

stop sound
show bg Black
hide a
hide s
hide t
hide v
hide y
hide k
hide d
hide b1
hide b2
hide b3
hide b4
hide b5
with dissolve
window hide dissolve
$ renpy.pause(delay = 2.0, hard = True)

jump P3Day2
#; END OF DAY
