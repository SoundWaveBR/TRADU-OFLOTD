label P3Day3:

window show dissolve
play music Morning
show bg MansionMorning with dissolve

"It's hardly a surprise, but I didn't sleep well last night."
"Who could, after what happened?"
show k happy at pos50k with dissolve
k "And just like that, we're onto day three!"
show k laugh
k "I gotta thank you, [name]! You're making my job easy!"
show k bored
k "I actually get to spend my nights doing productive things, now."
m "I'm happy to help with that... however that works."
show k surprised
k "You alright? You don't seem to have your usual energy."
"...Careful, [name]. One slip up with Kat and this is all over."
m "I'm good. Thanks, Kat. I just didn't sleep too well."
show k laugh
k "Happens to the best of us."
show k flirt
k "Anyway, it goes without saying that Yui is definitely a contender for the final ceremony, hmm?"

menu:
    "Of course!":
        jump p3d3_addChoice1
    "We'll see":
        jump p3d3_addChoice2

label p3d3_addChoice1:
m "Of course!"
m "A woman like Yui... anyone would be lucky to have her."
show k sassy
k "Damn straight."
show k laugh
k "Though she's a very different kind of woman than Scarlett. You've got a tough choice down the road."
show k flirt
k "...Though you've also got a tough choice to make right now!"
show k sassy
k "Who's the unlucky girl today?"
jump p3d3_addAfter

label p3d3_addChoice2:
m "We'll see. I'm... not so sure just yet."
show k surprised
k "Oh, really? That's a surprise."
show k flirt
k "Well, not my problem."
show k sassy
k "Anyway, who's today's unlucky girl?"

label p3d3_addAfter:
m "..."
hide k with dissolve
stop music
play music Sincerely
show bg Lab with dissolve
show a serious at pos20a with dissolve
show s neutral at pos40s with dissolve
show t neutral at pos60t with dissolve
show y surprised at pos80y with dissolve
m "...So who should I be asking on a date tomorrow?"

show t worried
t "Honestly, joking aside..."
show t happy
t "...I think you should ask Violet."
show a surprised
a "Really? I don't think she's in any shape to put on a good show."
show t worried
t "I mean... we need all of us to be able to work together well, to get out of here, right?"
show t sad
t "I don't think Violet would be able to until she's feeling better."
show t happy
t "And what better way to do that, then for a date to make ya feel special!"
show s happy
s "Terra does have a great point."
show t neutral
t "I always make great points!"
show t happy
t "Like seeing if I could arm-wrestle one of the zombies Scarlett made, that went great!"
show y laugh
y "Oh, I remember that!"
show y surprised
y "Wait, I was the zombie. That was not a good idea at all."
show s surprised
s "Can I take my vote back?"
show a surprised
a "What do you think, [name]?"
m "I like the idea."
m "We could kill two birds with one stone. I'm sure there's something that we could do to help us escape, that we could only do on a date with Violet."
show a serious
a "Hmm...."
show a laugh
a "I've got it!"
show a sassy
a "Tomorrow, you'll be going on a date with Violet. Here's what you gotta do..."
hide a with dissolve
hide s with dissolve
hide y with dissolve
hide t with dissolve
show bg MansionMorning with dissolve
stop music
play music Morning
show k flirt at pos50k with dissolve
m "...Violet."
show k happy
m "I've always wanted to spend more time with her, and there's no time like the present."
show k laugh
k "We'll make it happen!"
m "I do have one small request, though..."
show k surprised
k "What's that?"
show k flirt
k "And will it give me ratings?"
m "...I think it will."
show k happy
k "Then let's hear it!"
m "I've noticed Violet being a little down lately, so I wanted to cheer her up."
m "I heard that she really likes cooking, especially in groups. Would you mind if we cooked with the staff at noon?"
show k surprised
k "...I don't see why not."
show k sassy
k "Let's hope it goes better than the last time."
show bg Black with dissolve
hide k with dissolve
stop music
play music AlmostBliss
"..."
show bg KitchenMorning with dissolve
show v sad at pos50v with dissolve
v "...Oh. Hi, [name]."
show v sad
v "...Why'd you bring me here?"
m "I'm in a bit of predicament. You see, I... may have made an irresponsible bet."
show v surprised
v "...I did not take you for a gambler!"
show v neutral
m "Well, I'm not, but the thing is..."
m "...I heard the cooks bragging that they were the best chefs on the island."
show v surprised
m "But hey, I've tried the food you've made before. I know nobody else could come close to how good you are."
m "So I... may have challenged them all to a competition... in your name."
v "..."
show v laugh
v "You are ridiculous, [name]."
"Violet laughed out loud."
"There's that smile I like so much. It was nice to see it again."
show v happy
v "...Are you being serious?"
m "Dead serious."
m "In a few hours, hundreds of staff are going to come here. Some of them as challenging cooks, some of them as judges, the rest of them looking for lunch."
m "...All of them hungry."
m "Think you're up for the challenge?"
show v neutral
v "..."
stop music
play music RocketPower
show v happy
v "I am ready to crush the opposition."
show v angry
v "They will rue the day they challenged me!"
m "That's the Violet I like to see."
show v neutral
v "Anyway, what is the theme of this contest?"
m "I can't tell you just yet! It'll be announced when it's cooking time."
show v sassy
v "I do like a challenge."
stop music
play music SmoothLovin
show v neutral
v "...Would you care to stay with me as I prepare for the festivities?"
m "Of course, Violet."
show v happy
v "...Thank you, [name]."
show v neutral
v "I know why we're doing this, and I... I appreciate it."
show v laugh
v "I'm not ready to talk about it just yet, but... I feel happier already, knowing you are looking out for me."

menu:
    "I'm always going to be here for you":
        jump p3d3_addChoice3
    "I'm glad to hear that":
        jump p3d3_addChoice4

label p3d3_addChoice3:
m "...I'm always here for you, Violet."
show v blush
v "...and I for you as well, [name]."
jump p3d3_addAfter2

label p3d3_addChoice4:
m "...I'm glad to hear that."
show v happy

label p3d3_addAfter2:
"We spent the time before the contest just talking about pleasant things completely unrelated to the show, completely unrelated to anything of consequence."
"Sometimes, when bad things happen... what you need most is just a semblance of normalcy."
stop music
play music RavingEnergy
hide v with dissolve
show bg KitchenNoon with dissolve
show b1 happy at pos10b with dissolve
show b2 happy at pos25b with dissolve
show b3 happy at pos40b with dissolve

show b4 happy at pos70b with dissolve
show b5 laugh at pos85b with dissolve
show v sassy at pos55v with dissolve
"By the time noon rolled around, hundreds of staff members were filling up the kitchen."
show b1 angry
b1 "I don't want to face you, Violet, but I will if I must!!"
show v surprised
v "...Oh? You're challenging me?"
show v sassy
v "Like a snail, challenging the mighty eagle. You have my respect."
show b1 worried
b1 "Eep! Is it too late to change sides?"
show b2 angry
b2 "You're going down, Violet!! We're the Brothers Five! The best chefs on the island!!"
show v laugh
v "What's that, Two?"
show b2 laugh
b2 "What I meant to say is, wow! You really are the best chef on the island!"
show v sassy
v "That's right!"
show b3 angry
b3 "Dammit bros, you can't let her intimidate you like this!"
show b3 worried
b3 "If we do, she's already won!"
show b3 sad
b3 "Say something, Four!"
show b4 serious
b4 "...We will meet on the culinary battlefield, Violet."
show b4 happy
b4 "You may have my brothers running for the hills, but not me and Five."
show b4 angry
b4 "Come at me! Let us brandish our forks against each other!"
m "...Five, do you have anything to say?"
show b5 surprised
b5 "Wait, what's happening?"
show v laugh
v "I do hope you'll entertain me, brothers."
"Violet raised a pan towards them."
show v angry
v "Let us begin!!"
m "It's time for the cookoff to end all cookoffs!!!!"
m "Each cook will cook their own version of a mystery dish - a dish that I will soon reveal for the first time ever."
m "The judges will be... everyone who is not a contestant!"
show v surprised
v "...!"
show b4 angry
b4 "You must be joking! There's hundreds of people here!"
show b3 angry
b3 "How could we ever feed everybody?"
m "That's not my problem."
m "...And I definitely didn't come up with rules for this tournament on the spot!"
show v happy
v "...Liar."
"Violet laughed once more."
"...That was enough to keep this charade going."
m "The mystery dish... will be spaghetti and meatballs!!"
show v sassy
v "Like taking candy from a baby."
show b1 worried
b1 "Not this again. Oh god, I think I'm gonna faint -"
play sound Hit
hide b1
"One collapsed on the ground."
show v laugh
v "One down. Four to go."
show b2 worried
b2 "Bro!!!!"
show b3 worried
b3 "I knew we should have been accountants! Why are we fooling ourselves?"
m "You each have one hour - no late submissions will be accepted!"
m "Let the games... BEGIN!"

show b2 angry at pos10b
show b3 angry at pos30b
with easeinleft
show b4 angry at pos70b
show b5 angry at pos90b
with easeinright
show v sassy  at pos50v with easeinleft
"The contestants (that were still conscious) rushed off to gather ingredients."
"How are they going to make that much food?"
"...I'm sure they'll figure something out."
"I watched each of them cook furiously, at breakneck speed."
"Violet was hard at work, sweat streaming down her face, with the biggest smile I'd seen her have all day."
"I couldn't help but smile as well."
"At the same time, Four was trying to cook his spaghetti with only a microwave."
"...I'm not sure this will be too much of a contest."
m "One minute left!"
"Violet filled hundreds of laid out bowls with spaghetti and meatballs in a matter of moments. If you blinked, you'd miss her finish a whole row."
"Each looked both delicious and artistic - you would have thought a cook would have spent much longer than an hour putting each of them together."
stop music
play music CarpeDiem
"Five settled on making about... four and a half bowls. I guess everyone has their own pace."
m "...Time's up!!!"
m "It's time to judge!!!"
"The crowd cheered as they stampeded to the laid out bowls. They were practically salivating."
"After everybody wolved down bowls from each of the contestants, they submitted their vote."

m "The people have spoken!"
m "And with a resounding majority, our first ever winner of the \"Best Chef on the Island in the middle of nowhere\" award is..."
show v surprised with vpunch
v "...Violet!!!!!!"
"The crowd cheered - myself included."
show v happy
v "...I did it!! Me! I did it!!"
with vpunch
"Violet jumped up and down with joy."
"I felt like a kid in a candy store, just from one look at her."
show b4 laugh
b4 "You won fair and square! You should be proud of yourself!"
show b5 laugh
b5 "Yeah! Your food was the best I'd ever had!"
show b2 surprised
b2 "...Though if you consider our living standards, that doesn't mean too much."
show b2 happy
b2 "Hey, I just had an idea!"
show b2 laugh
b2 "What if we get Violet to cook for the staff at lunch, instead of us?"
show b2 worried
b2 "Seriously, it's been years since we've had real food."
show b4 angry
b4 "What's that supposed to mean!"
show b5 surprised
b5 "Honestly, I think it's a great idea."
show b5 happy
b5 "I know I hide it well, but... I really have no idea what I'm doing in the kitchen."
show b2 surprised
b2 "No way, bro!!!"
"Violet and I took one look at each other, and couldn't help but laugh."
show v happy
v "...I would love to, you guys."
with vpunch
"The crowd's enthusiasm reached a level of uproarious applause."
crowd "Violet! Violet! Violet! Violet!"
show v blush
v "Oh goodness, I - you're all too kind."
"I put my arm around her and smiled."
m "...Guess you've got a new job now, Violet."
show v happy
v "...I guess I do."
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve
hide b4 with dissolve
hide b5 with dissolve
#show bg Black with dissolve
#$ renpy.pause(delay = 1.0, hard = True)
stop music
play music LoveTheme

show v blush
m "I -"
"Violet leaned in to kiss me on the lips."
"For a moment, time stood still - and the only thing you could hear was the crowd's cheer getting even louder."
with vpunch
crowd "VIOLET!!!! VIOLET!!!! VIOLET!!!!"
show v laugh
"We laughed together."
show v happy
v "...I've had so much fun today, [name] - thanks to you."
show v laugh

menu:
    v "Care to join me by the beach, after we clean this place up?"

    "I wouldn't miss it for anything":
        jump p3d3_addChoice5
    "Sounds like a plan":
        jump p3d3_addChoice6

label p3d3_addChoice5:
m "...I wouldn't miss it for the world."
show v happy
v "The world would pale in comparison!"
jump p3d3_addAfter3

label p3d3_addChoice6:
m "Sounds like a plan!"
show v neutral
v "I will see you there, then!"

label p3d3_addAfter3:

hide v with dissolve
show bg Black with dissolve
"..."
show bg BeachNight with dissolve
show v happy at pos50v with dissolve
v "...Hey."
"She reached her hand out to mine, and I held hers tight in return."
m "Hey, Violet."
m "You really gave them a great show today, you know?"
show v laugh
v "I couldn't have done that without my ever so charming television host."
"We walked along the beach, our feet bare in the inviting water of the ocean."
show v blush
v "...Really, I... I'm so grateful to you, [name]."
show v worried
v "Last night... finding out what my parents did, I... that was the lowest point I'd ever been to."
"I held her hand even tighter."
show v sad
v "Honestly, I... I didn't see a way out. Escaping the island, or not - everything seemed like a dead end."
show v happy
v "But today, you helped me remember that even without them... I've still got me."
show v laugh
v "...And I like me quite a bit."
show v happy
m "...You really are incredible, Violet."
m "That was all you."
show v blush
v "...with you."
"Violet mumbled something under her breath."
m "Sorry, what was that?"
show v worried
v "...Ugh, sorry, let me try again."
show v blush
v "I know I'd be fine on my own... but I'd like me better if I was with you."
show v happy
v "When we get out of here... I do hope you join me for that cruise."
show v blush
"She kissed me again - it felt like magic."
m "Violet, I -"
show v laugh
"She put her finger against my lips."
v "Shhh. I know it's... not quite the time for this conversation yet."
show v happy
v "But please do remember what I've said... when this is all over."
show v blush
v "...Do you mind if we walk for just a little longer? I..."
show v happy
v "...I don't want this to end."

menu:
    "I'm walk with you for as long as you wanted to":
        jump p3d3_addChoice7
    "I'd like that":
        jump p3d3_addChoice8

label p3d3_addChoice7:
show v laugh
m "...I'd walk with you for as long as you wanted to, Violet."
show v happy
m "We can walk till the sun comes up. We can talk about anything and everything."
show v blush
m "So how about we start with planning our cruise together?"
show v laugh
v "...That would be lovely."
jump p3d3_addAfter4

label p3d3_addChoice8:
m "...I'd like that."

label p3d3_addAfter4:

"We walked together till the dead of night."
"It was nothing less than magical."
hide v with dissolve
show bg Black with dissolve
"..."
stop music
play music ShavingMirror
show bg MansionIndoorsNight with dissolve
show y happy at pos10y with dissolve
show s neutral at pos30s with dissolve

show v neutral at pos70v with dissolve
show t neutral at pos90t with dissolve
show a sassy  at pos50a with dissolve
"Just after we came back, a huge storm hit outside. We just missed it."

show a happy
a "Hope you two enjoyed your date today!"
show a neutral
a "I'm sorry to interrupt... but it's time we get this show on the road."
"Allie took out the master key from her pocket, span it around the ring with her finger, then put it in the locked door."
show a sassy
a "...Aaand we're in."
"She turned the lock, then pulled the door open."
show a worried
a "Woah, the door's a little heavier than I thought it would be. Must be soundproof or something."
show a happy
a "Whatever. Let's go."
show bg Black with dissolve
stop music
play music HalfMystery
show t worried
t "Aw man, not another staircase?"
show t angry
t "They would have saved so much money if they just put this on the main floor!"
show y worried
y "But it wouldn't be very secret then, would it?"
show t annoyed
t "Secret, schmecret! It's behind a locked door!"
show v surprised
v "I guess you have a point."
"Though there was another staircase, it wasn't nearly as long as the one to the lab."
"We'd been walking down the steps for only a few moments when we saw where they led."
show bg ProducerRoom with dissolve
show a surprised
stop music
play music MasterDisorder
a "...This has to be it."
m "What's \"it\"?"
show a neutral
a "A while back, Kat told me that all the information on this island was stored in books - they didn't use anything digital, or with the internet."
m "I think I remember that too."
show a annoyed
a "Well, it's bullshit! They're an evil corporation, intent on world domination through fear and control. Of course they have the internet."
show a sassy
a "...And I think we've just found a way into their closets - skeletons and all."
show t surprised
t "Sounds like a pretty big deal."
show a laugh
a "That's an understatement!"
show a worried
a "The information in here could change the tide of the war - it could give the Resistance a real fighting chance. I think."
show a sad
a "...But there's more than that, too."
m "What do you mean?"
stop music
play music Bittersweet
show a worried
a "...My dad, mom, and my brother got taken by these guys a long time ago. I... I don't even know if they're still alive."
show a sad
a "...I was too young to really understand what was happening."
show a worried
a "If there's anything that could help me find them again, or at least... find out what happened to them... it's in this computer."
show a sad
a "That was the real reason I came here. The whole reason I risked everything, I..."
show a worried
a "What if it doesn't have what if I'm looking for? What if-"
show y worried
y "...Allie."
"Yui ran to Allie's side, and hugged her tightly."
show y happy
y "It's going to be okay."
show y neutral
y "...You believe in me, right?"
show a sad
a "..."
"She took deep breaths."
show a neutral
a "I'm... sorry you had to see that. I'm okay now."
show a blush
a "...Thanks, Yui."
show y laugh
y "I didn't do anything!"
show y happy
y "...Are you ready?"
stop music
play music MasterDisorder
show a sassy
a "Let's do this."
show v worried
"I looked to Violet as Allie prepared to turn the computer on."
"She looked as concerned as I did, but we couldn't let it show."
"The screen lit up with a single message."
"'Password Required'."
show a laugh
a "Well, I did think it was going a little too smoothly."
show a neutral
a "I'm not giving up just yet, though."
show a worried
"She tried a few different passwords on the keyboard, but none of them worked."
show a angry
a "Damn it. I bet only Damian or Kat know this, and... there's no way we could just ask them."
"Silence fell upon the room."
show a sad
a "It can't end like this, it just can't..."
show t worried at pos70t with dissolve
show v worried at pos90v with dissolve
t "...I've got an idea."
show a laugh
a "It's not going to involve wrestling zombies again, is it?"
show t worried
t "Hey, I've had better ideas than that!"
show t neutral
t "What I mean to say, is that I think I have a way to crack the code."
show a surprised
show t happy
t "...I'm a programmer. I can make something that could try all the possibilities for the password."
show t worried
t "It would take some time, especially if it locks me out after too many attempts, but... eventually I'd get the password."
show t serious
t "...Though there's no guarantee we'd get the answer before the show was over."
show a serious
a "..."
show a neutral
a "...It's a lot better of a shot than I thought we had."
"Allie ran over to Terra and hugged her tightly."
show a laugh
a "Thank you, you awesome little you."
show t blush
t "Uhhh... this is nice. Feel free to compliment me more."
show a neutral
a "In the meantime, the rest of us can try to figure out what the password would be as well."
show a serious
a "...That reminds me, I need to tell you guys something important."
show t surprised
t "What's that?"
show s neutral
s "..."
stop music
play music TakeAChance
show a neutral
show v surprised
show y surprised
show s surprised
a "...I have our escape plan."
"She took out the master key and held it out for us to see."
show a happy
a "There's a hidden hangar I found by the beach, just a little further from where I first found the plane."
show a neutral
a "Now that we have this key, and we know that it works..."
show a happy
a "...We can use it to disable the hangar's security, commandeer a plane, then fly the hell out of here."
"We practically jumped for joy."
show s happy
s "I can't believe it, we're almost out of here!"
show v happy
v "It's been a long time coming."
show a sassy
a "Well, soon, but not just yet."
show a worried
a "With this storm raging... there's no way we're getting anywhere tonight, least of all off the ground."
show a happy
a "But if there's clear skies tomorrow night... that's where we'll be."
show v worried
v "...What about the computer? Don't you need to crack it before we go?"
show y worried # former look:right
y "Yeah! What about your family?"
stop music
play music Bittersweet
show a sad
a "...Well, that'd be the ideal case."
show a happy
a "...But honestly, I've... I've gotten to know you guys, and care about you guys, and I..."
show a neutral
a "...I've decided that it's more important to save the people I care about, that are right in front of me... than chase a pipe dream."

#show v serious at pos30v
#show t worried at pos90t
#show a surprised at pos70a
show s worried at pos10s with dissolve
show y angry  at pos30y with dissolve

y "No! I won't accept it!"
show y sad
y "If I were in your shoes, and I was looking for my sisters... and I just gave up looking for them..."
show y worried
y "...I'd regret it forever. And I know you would too."
show a sad
a "...But I can't ask you guys to stay here any longer. We're in danger if we stay here."
show t worried at pos90t with dissolve
show v neutral at pos70v with dissolve

v "...Yui speaks for us too."
show v happy
v "To have family that you really care about, and that cares about you too... you can't give up on that."
show s laugh
s "We're not going anywhere till we crack that code. Even if it takes till the last day!"
show a happy
a "You guys..."
show a worried
a "...No, I can't allow it. I won't take that chance with your lives."
show y angry
y "I'm not backing down on this!"
show a worried

menu:
    a "...What do you think, [name]?"

    "We need to take this chance":
        jump p3d3_addChoice9
    "We can't take this risk":
        jump p3d3_addChoice10

label p3d3_addChoice9:
m "We need to take this chance, Allie."
m "...I think you need this."
show a sad
a "...I..."

jump p3d3_addAfter5

label p3d3_addChoice10:
m "I don't..."

label p3d3_addAfter5:

show y surprised at pos90y with dissolve
show t happy at pos30t with easeinleft
t "Guys, guys. Take a chill pill for a second."
show a surprised

a "...?"
stop music
play music TakeAChance
show t angry
t "...I'm a programming god! BEST OF THE BEST!"
show t happy
t "I'm going to have that code cracked by tomorrow, and that's a promise!"
#show t neutral
#t: After I crack it, I'll download it all onto my console - and you'll be able to take this information
show t neutral
t "...So don't worry, kay?"
show a happy
a "...I love you guys. Thank you so much, really."
show t surprised
t "Why are you thanking all of us? I'm the one who has to write the code and shit."
"We laughed together - something that I thought might've been impossible after the initial bad news."
"We're in this together. And we're getting out together."
"No one gets left behind."
hide a with dissolve
hide s with dissolve
hide v with dissolve
hide t with dissolve
hide y with dissolve
show bg Black with dissolve
stop music
play music Bittersweet
"After we called it a night, I laid in bed, deep in thought."
"Who'd have thought I could have ended today feeling inspired, after everything that happened last night?"
"...We've got this."
"We-"
stop music
play music BlippyTrance
show t surprised at pos50t
t "[name]! One more thing, before we turn in for the night."
m "What's up, Terra?"
show t worried
t "...I got caught up in the heat of the moment earlier, and..."
"Oh no."
show t happy
t "I got no idea -"
"No no no no no I do not like where this is going"
show t surprised
t "- how to do this, cuz..."
show t worried
t "...I remembered that all I know about hacking are videos of people typing really fast and saying \"I'm in\", and..."
show bg RoomNight #with dissolve
hide t #with dissolve
with vpunch
stop music
play music SmoothLovin
m "Gahhhhhh!!!!!"

"I practically flew out of bed."
"....Thank god, it was just a nightmare."
"What does it take to get a good night's sleep on a killer dating show, come on!"

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

jump P3Day4
