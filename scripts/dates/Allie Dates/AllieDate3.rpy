label AllieDate3:

play music CarpeDiem
show bg BeachMorning with dissolve
play sound Waves # loop:true
$ allieAffection=3

"I found Allie by the beach - or more accurately, she came running to me."
show a happy at pos50a with dissolve
a "You are not gonna believe this, [name]!"
m "What's that?"
show a surprised
play sound Intercom
k "Alright... who took my keys?"
k "You've got ten seconds before I take it out of Four's paycheck."
b4 "Oh, come on!"
show a laugh
a "Er... we'll walk and talk, come on!"
show a happy
a "Well, less \"walk\", maybe more like run like hell. Four is not going to be happy when he finds out that I..."
show a laugh
a "Ah, whatever. Come on, let's go!"
show bg LakeMorning with dissolve
stop sound # @stopsfx Waves
"She grabbed my hand and pulled me with her into the forest clearing nearby."
m "What's going on?"
show a laugh
a "You are not gonna believe what I just found."
m "What's that?"
show a happy
a "Well, I was wondering how to top the two previous dates, when I stumbled upon..."
show a surprised
a "Ah, wait a minute! It's better if I surprise you."
m "I'm gonna have to close my eyes again, right?"
show a happy
a "I love how fast you learn things, [name]~"
hide a with dissolve
show bg Black with dissolve
"She was singing as she covered my eyes with one hand and pulled me along with the other."

"She pulled me along, step by step. I can't say I wasn't enjoying it."
"Is this... a staircase? It feels like metal beneath me."
"...In the middle of a forest?"
a "Just a bit more now... alright!"
"...?"
a "You can open your eyes now!"
show bg PlaneBar with dissolve
show a happy at pos50a with dissolve
m "How on earth -"
"We were inside a small plane, the very same one I'd been rudely awakened in my first day here."
m "How did you even...?"
show a laugh
a "It was just sitting in the forest! So I thought, why not, right?"
"I have so many questions."
m "Wait a minute, are you planning on-"
hide a #with dissolve
play sound Whoosh
"Without even bothering to answer me, Allie rushed to the cockpit."
"Oh crap."
m "Here's to hoping that this goes better than the rollerblades..."
stop music
play music LeGrandChase
a "Huh, I wonder what this big red button does?"
m "Oh god, get me outta here!"
"I ran for the door, but it was already shut tight."
show a happy at pos50a with dissolve
a "And awaaaaay... we go!!!"
play sound Engine # loop:true
with vpunch
"The engine of the plane roared as we took off. I slammed into the side of the door."
show a surprised
stop sound #@stopsfx Engine
with vpunch
"Oof..!"
show a sassy
a "Come on, be honest. You were thinking the same thing!"
show a laugh
a "You put a big, juicy red button there, completely unattended, and you expect a good citizen like me to not press it? You're bonkers!"
m "You've got a point, but do you have any idea how to fly this thing?"
m "...Wait a minute, if you're talking to me here, then who's flying the plane?"
show a neutral
a "..."
show a happy
a "Technically, nobody, but -"
show a surprised
with vpunch
play sound PlaneCrash
"*Crash*"
"The right wing of the plane smashed into a tree. We hit it hard enough for it to be slightly deformed."
with vpunch
m "Ooof!!"
play sound PlaneCrash
with vpunch
"I slammed into the wall yet again."
show a annoyed
a "Tch! Well, we didn't need that wing anyway, we still have the other one."
show a laugh
a "Exactly like kidneys."
"Forget killer dating death shows, forget Damian and Kat. Allie was going to be the death of me."
"I tried to run to the cockpit, but it was all I could do to stay upright as the plane teetered back and forth."
show a sassy
a "I'm just kidding, I've got this."
hide a with dissolve
"Allie ran to the cockpit without breaking a sweat. Meanwhile, I did my best impression of a ball in a pinball machine."
a "Alright, I got this!"
stop music
"The plane seemed to stabilize in a matter of seconds."
m "Oh thank god, I really thought we were gonna..."
play music LeGrandChase
play sound PlaneCrash
with vpunch
"*Crash*"
a "Oops."
"Once again, the right wing of the plane smashed into a tree. Somehow, it was bent back into its original shape."
show a laugh at pos50a with dissolve
a "Not so bad, if I do say so myself!"
m "Alright, that was dumb luck, and you know it."
show a happy
a "And now, for the moment you've all been waiting for..."
stop music
play music AlmostBliss
"We started gaining altitude. Slowly at first, then faster, and faster, higher and higher."
"Before long, we were soaring high above the trees."
"Allie yelled out in triumph."
show a laugh
a "Woooooooooooooooooooooooooo!!!!!"
"I joined it and yelled out with glee."
show a happy
a "It's a pretty great feeling, huh?"
m "Not dying in a fiery plane crash?"
show a neutral
a "Flying free. Without it, what's the point of living?"
m "You talking about freedom, or flying?"
show a laugh
a "Ahh, why not both."
show a serious
a "That said, there's another reason I flew us up here."
m "What's that, Allie?"
stop music
play music Twisting
show a neutral
a "This is the only place I could find on the island that wasn't bugged. No one can eavesdrop on us here."
show a worried
a "And sorry for the turbulence, but without it, {i}they{/i} might have heard me disable the bugs in here."
show a serious
a "Believe me, I looked for a safe place as hard as I could. That's why I got the roller blades and the boat earlier - to find a safe place to talk, as fast as possible."
m "...I'm guessing you know what the show is really about, then."
show a laugh
a "Unfortunately, yeah. What a bummer, am I right?"
show a sad
a "Unfortunately, I don't think you do. And... I can't risk telling you everything, either."
m "What!? Why?"
show a angry
a "Believe me, you're better off not knowing."
m "What..."
m "Allie... what are you hiding? Who are you really?"
show a annoyed
a "Look, we don't have too much time, before we'll have to land. This thing's already almost out of fuel."
"Sure enough, we had already started descending."
show a worried
a "Please, just trust me. I'm on your side, [name]."
show a sad
a "I know there's so many lies going around here. But I really want to help you get out of here."
show a sassy
a "Though I have to admit, it wasn't on my to-do list at first!"
show a laugh
a "It's a good thing you're so cute."
m "..."
show a surprised
a "I'm kidding, geez!"
show a worried
a "...Do you trust me?"

menu:
    "Yes":
        jump TrustYes
    "No":
        jump TrustNo


label TrustYes:
m "Of course I do, Allie. You know that."
show a happy
a "You won't regret it. Promise!"
m "So what can you tell me?"
show a serious
a "There's no time. Long story short, there's something on this island I need to find, that the people I work with need."
show a worried
a "It's life or death - not for just you or me, but for countless others."
show a serious
a "I came here to save you all. And I won't give up until I have."
jump AfterTrust

label TrustNo:
m "..."
show a sad
a "You don't have to trust me. All you have to know is that I came to save you all."
show a serious
a "...And that I won't stop trying until I do just that."

label AfterTrust:
show a neutral
a "Though at this point, I've done all I can. It's in his hands now."
m "Who's...?"
show a worried
a "No time to talk. We're almost back in range of the island's recording network."
show a serious
a "No matter what, don't tell anybody what happened here. Not even a little bit. Not even if you think you can trust them. Are we clear?"
m "Crystal."
"The plane flew lower and lower."
show a serious
a "Alright... we're about to be back in the recording zone."
show a worried
a "What else, what else.... ah."
show a sassy
a "Don't do anything I wouldn't do!"
m "That really doesn't limit it much."
show a surprised
a "I guess not."
hide a with dissolve

show bg Black with dissolve
$ renpy.pause(delay = 1.0, hard = True)

show bg LakeEvening with dissolve
show a serious at pos70a with dissolve
show k angry at pos30k with dissolve
"After we landed, Kat scolded us for taking the plane."
"Kat and Allie seemed to exchanged more than a few uneasy glances as we got off the plane."

if playthrough == 1 and currentDay == 6:
    jump LastDateAllie
elif playthrough == 2 and currentDay == 9:
    jump LastDateAllie
else:
    jump NotLastDateAllie


label LastDateAllie:

show k serious at pos30k
show a serious at pos70a

show k serious
"As we were walking away, I heard Kat whisper something to Allie."
stop music
play music Smile
show a surprised
k "...Nice try."
"And then I saw something I'd never seen before - and would never see again."
show bg LakeNight with dissolve
"The sky rapidly turned from bright blue to black, as if it were water being drowned in the darkest ink."
hide k with dissolve
hide a with dissolve
show bg Black with dissolve
"Then the bright sun in the sky... went out, like a candle in the wind."
"Even though I knew I was standing outside , I couldn't even see my hands in front of my face."
"Then I felt somebody grab me from behind - no, not somebody - there must be several people."
play sound Hit
"They forced me to the ground and cuffed me behind my back."
play sound Handcuffs
"I screamed, but there was no sound."
#play sound Hit
"I tried to fight, but there was no way out."
"I screamed at Allie, for her to run as far as she could - but I heard no response."
"Then... nothing."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending

label NotLastDateAllie:

hide k with dissolve
hide a with dissolve
show bg MansionEvening with dissolve
stop music
play music Morning
"...But luckily, nothing came of it."
"Next, the production staff separated Allie and I. It looks like Kat had arranged something special for the two of us."
"All I was told was that I wasn't allowed to see Allie until evening - apparently that's the nicest time to film."
"Till then, the production team helped me to look the part of a romantic novel protagonist. I was dressed to the nines."
"I must have sat through a few hundred photoshoots and interviews before they told me it was time to see her."
#show bg Palace with dissolve
stop music
play music RomanticJazz
"...But it was worth it."
show bg Palace with dissolve
m "Wow. Even for this island, this place is fancy with a capital F."
show b2 worried at pos75b with dissolve
b2 "Tell me about it, man. I broke one plate here, and I'll have to pay it off for the rest of my life."
show b2 happy
b2 "I mean, uh, welcome to the Ocean Palace. Allow me to show you to your seat."
"Two gestured at me to follow him."
hide b2 with dissolve
"We'd only taken a few steps when I saw her, and when I did, I couldn't help but crack up."
show a happy at pos50a with dissolve
m "You know, I kind of expected you to be dressed up too, given all the shit the crew put me through."
show a sassy
a "What's the point? It'd just get ruined."
m "...How would it get ruined?"
show a laugh
a "Oh, you'll see. Come on!"
show a sassy
"She reached for my hand - I put mine in hers, with a smile on my face."
"She pulled me along with her towards the door."
show a surprised
with vpunch
a "Woah!"
"We stumbled against a table, which knocked a plate onto the floor."
"It promptly shattered into a million pieces."
show a happy
a "...In case you were watching Kat, that was Two!!"
show b2 worried at pos75b with dissolve
b2 "I knew I should've just been an accountant!"
hide b2 with dissolve
hide a with dissolve

show bg RoadNight with dissolve
show a laugh at pos50a with dissolve
"She laughed as she pulled me along with her to the outside."
"The night air had never tasted so fresh."
"Each breath for air as we ran along the road made my worries and fears just... disappear."
show bg BeachNight with dissolve
"Eventually, we ran all the way to the beach."
show a happy
a "Come on!!!"
"She tightened her hand and pulled me along with her to the water."
show a laugh
m "Wait just a-"
"She laughed like a maniac as she cannonballed us into the ocean."
"My first instinct was to swim back up to the surface, but then Allie put her hands against my face, and looked deep into my eyes."
show a blush
"She smiled, then kissed me passionately."
show a sassy
"It was as if time had stopped."
"A few moments later, we went back up to the surface."
show a happy
a "...I figure you could use a fun distraction from everything that happened earlier."
"Was she doing this for me?"
m "I never know what to expect with you, you know?"
show a sassy
a "And you never will."
"It was a night to remember."
$ allieAffection=3
jump postDateSelector
