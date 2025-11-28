label P3Day4:

window show dissolve
play music Morning
show bg MansionMorning with dissolve
show k flirt at pos50k with dissolve


k "...What are you smiling about?"

menu:
    "Yesterday's date with Violet":
        jump p3d4_addChoice1
    "Things are going well":
        jump p3d4_addChoice2

label p3d4_addChoice1:
m "It just feels like things are going my way lately."
m "Yesterday's date with Violet still has me feeling as giddy as a little kid."
show k sassy
k "It's almost like there's perks to being on a killer dating show."
jump p3d4_addAfter

label p3d4_addChoice2:
m "It just feels like things are going pretty well."
m "Here's to hoping it stays that way."

label p3d4_addAfter:
show k happy
k "Well, don't get too comfortable. You've still got a few days left, and then it's back to the regular."
m "...I'm looking forward to that."
show k flirt
k "I bet! Better sooner than later, you cost too much to keep around."
show k sassy
k "Anyway... the million dollar question. Who's today's lucky girl?"
m "That'd be..."

hide k with dissolve
stop music
play music ShavingMirror
show bg Lab with dissolve

show y neutral at pos90y with dissolve
show v neutral at pos10v with dissolve
show t neutral at pos30t with dissolve
show a neutral at pos70a with dissolve
show s neutral at pos50s with dissolve
m "...So tomorrow, it's going to be either Terra or Allie."
show s serious
s "Hmm... it's probably best if we go with Terra."
show a surprised
a "But doesn't Terra need time to crack the code?"
show t happy
t "Nah, I already finished making the codebreaker. It's trying every password as we speak!"
show t serious
t "...No guarantee it'll finish before we're both done our dates, but... it's worth a shot."
show a happy
a "...Thank you, Terra."
show t neutral
t "Don't worry about it!"
show t happy
t "Besides, I think it's better if we save your date for last."
show a surprised
a "Why's that?"
show t surprised
t "I don't know, you're some super spy from some super secret organization!"
show t happy
t "You definitely got bigger heist potential than I do."
show a laugh
a "...I don't know about that, but sounds good to me."
show a neutral
a "I'll use the time to prepare some contingency plans."
show a happy
a "Scarlett, Violet, Yui - I'm gonna need you guys for this."
show v happy
v "I'm happy to provide assistance."
show y laugh
y "You bet!"
show y happy
y "I'll help however I can!"
hide y with dissolve
hide s with dissolve
hide v with dissolve
hide a with dissolve
show t neutral at pos50t with easeinleft
stop music
play music BlippyTrance
t "Sweet! Alright, uh... right. [name]."
m "What's up?"
show t happy
t "I didn't just build a codebreaker - I've built a game that works with it too!"
m "What do you mean?"
show t neutral
"She handed me her console."
show t annoyed
t "I just whipped it up real quick. It looks like a code breaking game, but really, it works directly with the computer we found."
show t happy
t "If you get the password right in this game, we'll have access to the computer. Make sense?"
m "Amazing! I can't believe you whipped up something so fast."
show t neutral
t "It wasn't hard."
show t angry
t "It was just a big middle finger to my mom, who thought all my screentime was a waste of time."
#m: ...I'm not gonna touch that."
show t happy
t "Anyway, I figure we can play this \"game\" here and there during our date, try whatever passwords come to mind."
show t worried
t "Obviously, not for the whole date, because ratings and all, but... as much as we can."

menu:
    "Sounds like a plan":
        jump p3d4_addChoice3
    "Are you sure this will work?":
        jump p3d4_addChoice4

label p3d4_addChoice3:
m "Sounds good to me, Terra."
show t happy
t "Bwahahahahaahahah!!! I'm a genius, [name]!"
"She cackled maniacally."
m "...You are."
jump p3d4_addAfter2

label p3d4_addChoice4:
m "...Are you sure this will work?"
show t happy
t "Trust me! When have I ever been wrong?"
"She cackled maniacally."
"...Let's hope this works."

label p3d4_addAfter2:


hide t with dissolve
stop music
play music Morning
show bg MansionMorning with dissolve
show k flirt  at pos50k with dissolve
m "...I'd like to spend today with Terra."
show k neutral
k "...Is that so? Well, we'll make it happen."
show k sassy
k "Try not to spend all of it playing games, though. Believe it or not, that isn't what viewers want in a prime time slot."
m "No promises, but I'll try my best."
show k bored
k "It ain't much, but I'll take that."
hide k with dissolve
show bg Black with dissolve
stop music
play music JazzBrunch
$ renpy.pause(delay = 1.0, hard = True)
show bg MansionIndoorsMorning
show t happy at pos50t with dissolve
"Sorry, Kat - that's pretty much the plan."
t "Hey, [name]! You up to play some games?"
m "I'd love too, but Kat wants us to do some other -"
show t neutral
t "Games it is - sweet!"
"There's no stopping Terra when she puts her mind to something."
show bg GamesRoomMorning with dissolve
"We started \"playing\" together in the games room, while making pleasant conversation."
"Normal enough to seem like a regular conversation, cryptic enough to disguise what we were trying to do."
"...Even if Terra and I never went on crazy adventures like I did with Allie, it didn't make moments with her any less special."
"If I forget that we're trying to hack into some confidential database... this really is like a fun day at home with your partner."
show t happy
t "How about... \"Terra is the best\"?"
m "...It's worth a shot?"
m "Nope, doesn't work."
show t surprised
t "The nerve of them!"
show t happy
t "...\"Terra rules\"?"
m "...That's a miss."
show t surprised
t "Was the T capitalized?"
show t worried
t "Maybe add a \"0123\" at the end of it."
"...Thank goodness we have the codebreaker running in the background."
"Time to switch gears - let's give Kat some footage to work with to keep us alive."
stop music
play music LeGrandChase
show bg BeachMorning #with dissolve
show t surprised at pos50t_fall1
t "Good god, [name]! Why the sun!?!?"
show t angry
t "Aaraarrrrrraaarrrrghghhhghghghgh!!!!!!"
show t worried  at pos50t_fall2
t "G-go on without me.... ;-;"
play sound Hit
hide t #with dissolve
"...Okay, maybe this wasn't the best idea."
stop music
play music Wholesome
show bg MansionIndoorsNoon with dissolve
m "Some way or another, we always end up back inside the mansion, huh?"
show t happy at pos50t with dissolve
t "And there's nothing wrong with that!"
m "I guess you're right."
show t neutral
t "...Up for a few more rounds of that game we just played?"
m "Sure!"
show t surprised
t "How 'bout... \"DamianBlackSux\"? >:)"
m "...Nope, doesn't work."
show t worried
t "\"KatBlackSux\"? ;)"
m "Not that either."
show t happy
t "How about \"[name]\"?"
m "Oh come on, now you're just guessing!"
show t neutral
t "Like I wasn't before!"
m "Well, I'll try it..."
stop music
play music RocketPower
show t surprised
play sound AnimeShine
"*Ding Ding*"
"The two of us looked at each other like deer in the headlights."
show t surprised
t "Whuuuuuu-"
with vpunch
"We cheered as if our favorite team just won at a sporting event."
show t worried
t "...Wait a minute, why would the password be your name?"
show t serious
t "That doesn't make any sense."
m "My guess is as good as yours."
m "Maybe we'll find out tonight."
show t neutral
t "I hope so."
show t happy
t "Well... I think I've had enough of games for today."
m "I never thought I'd hear you say that, Terra."
show t angry
t "I'm full of surprises!"
show t happy
t "We can spread the good news after. How about we try something new today?"
show t neutral
t "...Something outside?"
m "Sounds like a plan to me."
show t happy
t "Awesome! Let's go!"
"...We ended up going back inside a minute later, but the rest of the day with Terra was still a lot of fun."
hide t with dissolve
show bg Black with dissolve
"..."
stop music
play music BlippyTrance
show bg ProducerRoom with dissolve
show a surprised at pos50a with dissolve
show s neutral at pos10s with dissolve
show y happy at pos30y with dissolve
show t happy at pos70t with dissolve
show v neutral at pos90v with dissolve
t "...And we're in!"
"The password prompt closed with a satisfying \"ding ding\"."
#; show bg ProducerRoom with dissolve
show t surprised
t "...Woah, there's a lot of stuff in here."
show y surprised
y "Why would there be a folder called \"Homework\"?"
show t worried
t "Woah, that is definitely a porn folder name -"
"Terra was about to open it,  until Allie intervened."
show a laugh
a "...Do you mind if I take a look?"
show t surprised
t "Ah, forgot why we were here for a second. Sure."
show y surprised
y "...?"
show a serious
a "Let's see..."
"Allie started going through folders, databases, reports - anything that could be useful."
"At the same time, Terra started downloading all of the files to her console."
"...Doesn't look like there's anything here about why my name was the password."

hide a with dissolve
hide t with dissolve
show bg MansionIndoorsNight with dissolve
"All the rest of us could do was give Allie and Terra the space they needed."
show v neutral at pos70v with dissolve
show s neutral  at pos50s with dissolve
show s happy
s "Seems like it's only going to be up from here, team!"
show s neutral
s "I was worried for Allie, especially if we couldn't get into the computer - but it looks like we got it after all."
show v worried
v "...It's too soon to say anything, but I do hope you're right."
show y happy
y "Let's not jinx it!"
show y neutral
y "...So what's the first thing you're going to do when we're out of here?"
show v surprised
v "I thought we weren't going to jinx it!"
show s happy
s "...I'm going to get straight back to helping people, the way I know best."
show s laugh
s "Nothing's changed in that regard!"
show v happy
v "...That is a lovely aspiration."
show y laugh
y "Do me a favor and make sure your inventions don't get used on yourself again, okay?"
show s worried
s "I mean, it's not like I was trying to...?"
show v happy
v "...I admire how you can be so sure."
show v worried
v "As excited as I am to leave this place... I'm not quite sure what I'll be doing after."
show y happy
y "That's totally okay, Violet!"
show y neutral
y "That's part of the fun of life. Just figuring it out as you go."
show v surprised
v "I..."
show v blush
v "...I suppose so."
"Violet looked at me and smiled."
m "...That's pretty much my plan at this point, too."
show s surprised at pos10s with dissolve
show y surprised at pos90y with dissolve
show v happy at pos30v with dissolve
show a happy at pos50a with dissolve
show t happy at pos70t with easeinright

stop music
play music TheShowMustBeGo
t "Guess who's back, biiiiiiiiitt-"
play music PastSadness
show a sassy
a "...What Terra wants to say is - we did it."
stop music
play music Sincerely
show a happy
a "I've got everything I need to help turn the tide of the war, and..."
show a laugh
a "...I know where my family is. And they're alive!!!!"
"I'd never seen Allie so happy. She jumped towards me and hugged me."
with vpunch
m "Oof!"
show v laugh
v "That's fantastic!"
show s happy
s "That's such a relief!"
show y happy
y "I'm so happy for you, Allie!"
show t happy
t "Good job, Terra! You cracked the code! Not all at once now!"
show a happy
a "...I couldn't have done it without you guys."
show a laugh
a "Thank you so much!"
show a happy
a "...We didn't have to wait this long to leave, but you guys did it for me and my family."
show a neutral
a "I can't ever thank you enough."
stop music
play music MiamiNights
"She pulled out the master key from her back pocket, and swirled it around in her right hand."
show a happy
a "...You guys ready to get outta here?"
show t surprised
t "Actually, I was thinking of staying here for the rest of my life."
show t happy
t "Not having internet is the best thing ever!"
show y happy
y "I couldn't agree more!"
show t worried
t "Er..."
show v happy
v "Let's get out of here."
show s laugh
s "After you, Allie!"
show a sassy
show bg MansionNight with dissolve #time:2
$ renpy.pause(delay = 1.0, hard = True)
show bg LakeNight with dissolve #time:2
$ renpy.pause(delay = 1.0, hard = True)
show bg BeachNight with dissolve #time:2
$ renpy.pause(delay = 1.0, hard = True)
show bg HangarNight with dissolve #time:1
$ renpy.pause(delay = 1.0, hard = True)
"We followed Allie out of the mansion, through the forest, and to the hangar."
show v neutral
show s neutral
show y surprised
show t surprised # former look:left
t "Woah! I did not see this."
show t worried
t "Granted, I don't go outside."
show a laugh
a "I don't blame you. It's pretty out of the way."
#;show a worried
#; a: There's probably even more things on this building I haven't seen. It's just too big."
show a sassy
a "Not that we have to worry about it now."
"Allie pulled out the master key, and swirled it around her right hand."
"She walked to the door of the hangar, and put the key into its lock."
show a surprised
a "...?"
"She tried to turn it, but it didn't work."
show a worried
show t worried
show v worried
show y worried
show s worried
stop music
play music MasterDisorder
"She tried a few more times, but the lock refused to budge."
show a sad
a "I... I don't understand. I've seen Kat use this key everywhere, including here."
show a worried
a "...They must have changed the locks."
show y worried
y "...Does this mean we're stuck here?"
show a sad
a "...I don't..."
"It was rare that Allie tripped over her words. It hurt to see her so defeated."
show a sad
a "I don't know."
show s sad
s "..."
"An uncomfortable silence fell over us."
"Am I... going to die here?"
"Are all of us?"
"I..."
stop music
play music MiamiNights

show a worried at pos30a with dissolve
show v serious  at pos50v with easeinleft# former ,,-1

#show t worried at pos90t
v "...No, we are not out of this just yet. I refuse to give up again."
show a sad
a "...But we can't get into the hangar. There's no way to break in without triggering the alarms."
show v sassy
v "For now, yes - but getting in later is a different story."
show v neutral
v "If I remember correctly... whenever you went on a third date with [name]... you would fly in a plane together."
show v laugh
v "Well, I'm assuming the plane was you two. It's just like you to try something crazy, and drag in [name]."
show a laugh
a "I can't refute that. That was definitely us."
"How we never died on those plane rides, I'll never know."
show v sassy
v "That means the staff don't mind if you take the plane during the date, which means we should be able to ask for the key temporarily."
show a surprised
v " ...We'd still be able to get the plane. It just has to be during tomorrow's date."
show a worried
a "There'd be way more staff around than usual, but we'd still have a chance."
show v serious
v "Exactly! The rest of us can be relatively close by - perhaps at the beach, to avoid suspicion."
show v sassy
v "Then, when you get the plane... we run over, you pick us up, and we are out of here."
show a happy
a "...This could work! It's better than how my plan turned out, anyway."
show s happy
s "I was worried for a second there, but... it was for nothing."
show s laugh
s "We've got this!"
show y happy
y "We'd be in a tight spot without you!"
show v happy
v "...It is a team effort."
show v laugh
v "Without each of us here... we would be stuck here, with no chance of escape, I'm sure."
show t happy
t "*cough* Speak for yourself, I'm sure I could get out of here on my own."
show a laugh
a "You would shut down the second you reached the beach, Terra!"
show t worried
t "...On second thought, maybe teamwork makes the dream work."
show t happy
show s laugh
show a laugh
show y laugh
show v laugh
"We laughed together - the mood was infinitely better than it was just a few moments ago."
"We spent the rest of the night talking through the details of the plan, including what we'd do if... the unexpected happened."
"One thing was for sure though - we weren't giving up on getting out of here."
"It all ends tomorrow."

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

jump P3Day5

#; choose terra as date
#; spend date cracking code (making games)

#; decide terra should go on the date because allie's date should be last...she says just in case."
#; terra finishes coding during the night, and has the cracker running through the day
