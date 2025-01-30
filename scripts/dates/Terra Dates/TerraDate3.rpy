label TerraDate3:

play music LoveTheme
show bg GamesRoomMorning with dissolve
$ terraAffection=3

#; NNEEEEDS REWRITE!"
#; she needs to show you the completed game
"I found Terra sleeping on the sofa in the Games Room."
"She looked so peaceful."
"...Maybe I'll come back later."
show t surprised at pos50t with vpunch
t "...Zombies everywhere!!!!!! Ahhhhhhh!!!!!"
"She bolted up suddenly."

menu:
    "You okay?":
        jump td3_c1
    "Crazy dream?":
        jump td3_c2

label td3_c1:
m "Woah! You okay, Terra?"
show t worried
t "Whew, it was just a dream."
show t neutral
t "I'm good now, no worries."
m "Seems like it was a pretty crazy dream."
jump td3_pc

label td3_c2:
m "...Crazy dream?"

label td3_pc:

show t surprised
t "No kidding! I dreamed that we all got turned into zombies."
show t happy
t "Luckily, there's no way that could ever happen."
show t neutral
m "...Did you go to bed late?"
show t happy
t "Hell yeah! I spent all night working on the game."
show t neutral
t "And I've finished it, too!"
show t happy
t "Care to join me in testing it out?"
show t blush
t "I, uh... added some new features I'd like you try."
m "Sure! I'd love to."
"It looked like the same game I had played before."
m "What am I looking for?"
show t happy
t "You'll see!"
stop music
play music BlippyTrance
show bg LakeMorning with dissolve
"I started up the game."
"Moments later, I saw Terra's avatar run up to me."
show t happy
t "You've made it just in time, the new event is about to start!"
m "What's the new event?"
stop music
play music RocketPower
"As if on cue, giant robotic pigeons flew from the sky and started to attack our avatars."
m "Aggggghhh!!!!"

menu:
    "Run for my life":
        jump td3_c3
    "Fight the pigeons":
        jump td3_c4


label td3_c3:
"I ran for dear life."
jump td3_pc2

label td3_c4:
"I ran towards the pigeons, preparing for the fight of a lifetime."

label td3_pc2:

show t neutral
t "Don't worry, I gotcha!"
"Terra pulled out a giant can of pigeon repellant and started blasting away."
show t surprised
t "Woah! I think something's bugged, it's not working at all!"
show t happy
t "Guess I gotta fix that. Hehehe..."
"While Terra was laughing at her own mistake, I was being lifted into the sky by the pigeons."
m "Uh... I think I'm screwed."
m "Where are these pigeons taking me?"
"I tried to move my avatar, but there was no way to resist the death grip of the robo pigeon."
show t neutral
t "Don't worry! They're about to fly into the territory of the Maple Syrup Dragon!"
m "The... what?"
show t worried
t "Uh oh."
show t surprised
"The screen lit up with a blast of flying maple syrup."
"...I never thought I'd ever say something like that, but here we are."
"The maple syrup slammed into the pigeons, and forcefully stuck their wings together."
"As a consequence, they started to fall to the ground at breakneck speed."
m "AaaaaaAAAAHHHH!!!"
m "Save me, I hadn't saved yet!"
show t surprised
t "Ah, I knew I forgot something! I forgot to add the ability to save."
show t happy
t "I'll have to write that down!"
"As Terra took notes, I rapidly fell to my doom."
m "I'm happy for you, but if you could just for a minute -"
play sound Hit
with vpunch
"My avatar smacked into the ground, pigeon-first, and instantly died on impact."
m "Aw man, I had so much stuff!"
show t neutral
m "Is there at least a respawn mechanic? I've never died before in this game."
show t happy
t "Of course!"
show t neutral
t "Just hit the 'Retry' button."
"I pressed the button, and watched the world around me reset to the village, sans the giant beasts of death."
show t surprised
"Except now, the village seemed ten times bigger than before."
m "Wait, when did the village get so big?"
"And then it dawned on me."
m "Wait... it's not the village that got big."
with vpunch
m "I got small!!!"
"I took a more careful look at my avatar."
"...I was a pigeon again."
"I sighed deeply."
show t happy
"At the same time, Terra was giggling like a child."
#...Pigeons, man."
hide t with dissolve

"We spent a few more hours testing out the rest of the game's new features."
"Thankfully, there were no more pigeon easter eggs."
stop music
play music LoveTheme
show bg LakeMorning with dissolve
show t blush at pos50t with dissolve
t "There's, uh... one last thing I want to test out, if that's okay?"
m "Will it end with me getting turned into a pigeon?"
show t surprised
t "No-o-o-o...."
show t happy
t "Just come with me!"
"I followed her avatar to the cabin we shared in the woods."
show t blush
"When we got there, she turned around, walked up to me, and held out an item I'd never seen before."
hide t with dissolve
show bg TerraProposal with dissolve
"She walked up to me, and gave me an item called {i}Ring of You're Pretty Cool{/i}."
m "...What's this?"
#show t surprised
t "Um. Let me try to explain!"
#show t happy
t "...I came onto this show with no idea of what it was about."
t "Personally, I thought it was stupid at first."
t "But... hanging out with you has been so much fun."
t "I've never really got to work on my hobbies with anybody, till I met you."
t "Honestly, I've never had someone to share all my crazy shit with, but you... you're different."
t "So... I guess what I'm trying to say, is...."
t "...You're pretty cool, and I hope we can keep doing this, even after the show is over."

menu:
    "I'd love to":
        jump td3_c5
    "Sounds like a plan":
        jump td3_c6

label td3_c5:
m "I'd love to, Terra."
m "You don't even have to ask!"
jump td3_pc3

label td3_c6:
m "Sounds like a plan, Terra."

label td3_pc3:

m "I've got to say, you caught me off guard with this."
show bg LakeMorning with dissolve
show t surprised at pos50t with dissolve
t "Why's that?"
m "You giving this ring to me, it... uh, well, it could be a little misleading."
show t blush
t "Y-You're not making any sense!"
show bg GamesRoomEvening with dissolve
"We laughed together, then walked back to the mansion with a spring in our step."
"We played the day away, without a care in the world."

if playthrough == 1 and currentDay == 6:
    jump LastDateTerra
elif playthrough == 2 and currentDay == 9:
    jump LastDateTerra
else:
    jump NotLastDateTerra

label LastDateTerra:

show t neutral
t "...Well, that's enough gaming for today!"
show t happy
t "You up for a movie date?"
m "Sure! What do you want to watch?"
show t surprised
t "How about... woah."
stop music
play music Smile
play sound Shutdown
"And then I saw something I'd never seen before - and would never see again."
show t worried
show bg GamesRoomNight with dissolve
"The sky outside rapidly turned from orange to black, as if it were water being drowned in the darkest ink."
show bg Black with dissolve
show t surprised
hide t with dissolve
"Then the bright sun in the sky... went out, like a candle in the wind."
t "Woah! What's going on?"
"She held my hand tight - I could feel that she was scared."

play sound GroupRun

"I didn't have a chance to respond before I heard a rush of footsteps coming towards us in the dark."
"Something isn't right - Oh no."
"We were surrounded."
stop sound #@stopsfx GroupRun

"A familiar voice cut through the short silence of me holding my breath."
q "I'm sorry, [name]. You just.... didn't make the cut."
"We've got to get out of here."
q "...Just make it quick, please."
t "[name], I'm scared, what's happening!?"
"I clasped her hand as tight as I could."
m "We need to get out of here, come on!"
play sound Hit
"I didn't even make 3 steps before I was tackled down and cuffed behind my back."
play sound Handcuffs
t "[name]! Hold on, I'll -"
"I yelled at her to run, but she came back to try to help me."
m "Terra, you've got to get out of here, I -"
"She screamed - they must have got her."
"It was no use. Even though she was right in front of me, I was powerless to get even an inch closer."
play sound Handcuffs
"They tackled her down in an instant. I heard the clink of the cuffs as they dragged her away."
"I struggled with everything I had to get up, to save her, to run... for what felt like an eternity."
"Then... nothing."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending

label NotLastDateTerra:

show t neutral
t "...Well, that's enough gaming for today!"
show t happy
t "You up for a movie date?"
m "Sure! What do you want to watch?"
show t neutral
t "It's a Hitchcock film! I've always wanted to see it."
m "What's it called?"
show t happy
t "...The Birds."
"...I felt a blood vessel in my head pop."
"This woman is bad for my heart."
"...But she never fails to put a smile on my face."
$ terraAffection=3
jump postDateSelector
