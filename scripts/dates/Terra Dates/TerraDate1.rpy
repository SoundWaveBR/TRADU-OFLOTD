label TerraDate1:

$ terraAffection=1

play music RavingEnergy
show bg MansionIndoorsMorning with dissolve
"As I walked closer and closer to the games room, I could hear people screaming bloody murder."
q "Help!!"
t "You're not going anywhere."
q "Take him!! I'm too young to die!"
"I rushed inside as fast as I could."
show bg GamesRoomMorning with dissolve
play sound ControllerSounds # loop:true

show b2 surprised  at pos50b  with dissolve
show b3 happy at pos65b  with dissolve
show b4 worried at pos80b  with dissolve
show t happy at pos30t with dissolve
b2 "What kind of brother would sacrifice his own flesh and blood to survive?"
show b3 laugh
b3 "Life is tough, buttercup!"
show b2 sad
b2 "Noooooo!!!!!"
show b4 angry
b4 "I'll save you, bro!!"
show b2 happy
b2 "Bro!!!"
play sound Explosion
show b4 sad
b4 "Agh!!!!!!!!!!"
hide b4 with dissolve
show t neutral
t "It's the heroes that die first, you know~"
show b2 surprised
b2 "BROOOOO!!!"
show t happy
t "Where was I... oh, right."
play sound Gunshot
hide b2 with dissolve
show t neutral
t "One down, two to go!"
show t angry
t "Get over here!!"
"...They were playing a fighting video game."
show t happy
t "Oh, 'Sup, [name]!"
show t annoyed
t "Give me a second, I've got to do a bit of pest control."
show b2 worried  at pos50b
show b3 worried at pos65b
"2 and 3: Kill him first!!!"
show t happy
show bg Black with dissolve
play sound Gunshot
play sound Gunshot
play sound Explosion
hide b2 with dissolve
hide b3 with dissolve
hide b4 with dissolve
hide t with dissolve
stop music
stop sound #@stopsfx
"..."
show bg TerraGaming with dissolve
play music BlippyTrance
# show t happy
t "Alright, alright! Y'all lost, fair and square."
# show t neutral
t "As promised, you guys know what you have to do."
"The Brothers Five groaned as they each put on some kind of futuristic helmet."
#show t happy

menu:
    "You're incredible, Terra!":
        jump td1c1
    "Not bad":
        jump td1c2

label td1c1:
m "You're incredible, Terra!"
m "You decimated those guys without breaking a sweat."
jump td1pc

label td1c2:
m "Damn! Not bad, Terra."
m "You wiped the floor with those guys."

label td1pc:


#show t neutral
t "I do make a living doing this, believe it or not."
#show t neutral
t "Though lately, it's been a little boring."
m "Why's that?"
t "It's just... same old, same old, you know?"

#show t happy
menu:
    t "...Though I do have something new in store, if you're down."

    "I'm down!":
        jump td1c3

    "Why not?":
        jump td1c4

label td1c3:
m "I'm down for anything."
jump td1pc2

label td1c4:
m "Sure, why not?"

label td1pc2:

#show t neutral
t "Good!"
#show t happy
t "I'm just gonna need you to put on this non-suspicious at all headset~"
"Terra picked up a helmet from behind the couch and placed it on my head."
#show t worried
t "This won't hurt a bit, don't worry!"
m "Wait, why would it-"
hide t with dissolve
show bg Black with dissolve
play sound Glitch1
"It was like lightning ran through my head."
show bg Black with dissolve
show bg LakeMorning with dissolve # time:2
show b1 surprised at pos10b with dissolve
show b2 surprised at pos25b with dissolve
show b3 surprised at pos40b with dissolve
show b4 surprised at pos75b with dissolve
show b5 surprised at pos90b with dissolve
"...I'm... in some kind of forest...?"
b2 "Woah! [name], you're here too!"
show b3 worried
b3 "W-Where are we? I want to go home!"
show t annoyed at pos60t with dissolve# former ,,-1
t "Oh, stop whining!"
show t happy
t "You're just in a videogame! Come on, this isn't the first time you've seen this happen in fiction."
m "That kind of thing exists now?"
show t annoyed
t "It's been around for at least a million years by now, get with the times!"
show b3 worried
b3 "Uh, last time I checked, I'd never heard of anything like this."
show t worried
t "Alright, alright, so maybe it was some weird kind of weird device I'd never seen before."
show t annoyed
t "Can you blame me for wanting to try messing with it?"
show b2 surprised
b2 "Wait, there's no way this could be a game. It looks too real!"
"I had to admit, I had my doubts too. Everything looked as if it were really there."
show t surprised
t "Hey, if you want proof, just try walking outside of this forest."
show b2 worried
"Two took a few cautious steps forward, then some more."
with vpunch
show b2 surprised
play sound Hit
b2 "Oof!"
"He smacked against some kind of invisible wall."
show b2 worried
b2 "There's... some kind of invisible wall here."
show b4 surprised
b4 "It really is a video game, huh!"
show t neutral
t "Actually, that's the wall of the Games Room."
show t worried
t "I thought this console would be like a 'deep dive' sort of virtual reality video game too, but it seems like everything we do here is replicated in the real world."
show t happy
t "Walk too many steps in a certain way, and... SMACK!"
m "...Doesn't that make this kind of useless?"
show t surprised
t "I guess, if you're allergic to fun?"

play sound Intercom
"The sound of the intercom played through the forest."
k "Hey, can you guys hear me?"
m "Kat! We can hear you, what's up?"
#k: I don't know how, but it looks like Terra found an old, er... "experimental" game console that we had in storage."
k "You guys need to log out of that game right now! If you're in the game too long, it'll fry your brain!"
m "What!? How? Why!?"
k "Er... long story short, it's an experimental... how to say... 'game console' that we had in storage."
k "No idea how Terra found it, though."
"This show is always trying to find new ways to kill me, isn't it?"
m "...How much time do we have?"
k "Before it fries your brain, I don't know, maybe a few minutes, maybe several hours - but it'll slowly sap your sanity the longer you're there."
k "Just log out already!"
m "We don't know how!"
"The Brothers Five and I looked around frantically, but there wasn't any way for us to log out."
show t surprised
t "Oh, I don't think you guys can see the log out menu. I think it's an admin-only kind of thing."
show b2 worried
b2 "If you can see it Terra, then come on! Log us out already!"
show t happy
"She cackled like a B-movie maniac."
"...Something tells me that she didn't have much sanity to sap in the first place."
show t neutral
t "But it'd be such a shame to leave so soon!"
show t happy
t "...Let's play a game first."
show t happy
t "It just so happens that as an admin, I can change all of your avatars at will!"
show t angry
t "Check this out! BAM!"
show t neutral
"...?"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve
hide b4 with dissolve
hide b5 with dissolve
show t surprised at pos50t with dissolve
"I looked down to my hands, which had now become tiny little white wings."
"I looked down at my face, and... I have a... beak!????"
"I... became a bird!?"
b1 "Oh god, what did she do to us! We're pigeons!!!"
b2 "LET ME OUTTTTTTTTTT!!!!!"
b3 "We'll never become accountants now!"
b4 "We're gonna die here!!"
b5 "I think I've got a new fetish."
"The Pigeons Five ran around frantically, like chickens with their heads cut off."
"I can't blame them."
"I looked up to Terra, who seemed like a giant compared to us now."
show t neutral
t "...Now, I'm sure you're wondering why I've turned you all to birds."
m "I guess you could say that."
show t neutral
t "It's funny, [name]. Earlier you told me that this whole show was like a dating sim, except that you were in the driving seat."
show t happy
t "Now the shoe is on the other foot!"
"She cackled again, like a wicked witch."
show t neutral
t "Welcome to {b}Pigeon Dating Sim: Battle Royale{/b}."
show t blush
t "You'll have to... seduce me if you want to get out of here."
"With each day that passes, I fear more for humanity's future."
m "...And you wanted us to be... pigeons for this?"
show t surprised
t "I mean, yeah? The ratio of human to pigeon visual novels is totally out of whack, man!"
show t happy
t "I figure we should balance that out!"
"I am trapped in a killer virtual reality game."
"I am also trapped on a killer dating show."
"To make matters worse, I am also trapped in the body of a pigeon."
"Now, I need to seduce a woman with my avian charm."
"You can imagine the kind of stress I am under."
show t angry with vpunch
t "Now... seduce me!!!"
show t annoyed
"One by one, the Pigeons Five fired pickup line after pickup line at Terra, but to no avail."
show t angry
t "Come on, come on! Move those wings like you mean it!"
"I tried my hand at a few too, but it was clear they had no effect."
"I can't imagine that being a pigeon helped with that in any way."
"Hmm... let's try one more."
"How about..."

menu:
    "Damn, girl, you're a hoot":
        jump birb
    "Damn, girl, you're looking so... fly":
        jump birb
    "Damn, girl, you're more addicting than quack":
        jump birb


label birb:

"With my will to live at an all time low, I..."
show bg Black with dissolve
show t surprised
play sound Shutdown
"!?"
hide t
"The game went dark."
show bg GamesRoomMorning with dissolve
show b1 surprised at pos10b
show b2 surprised at pos25b
show b3 surprised at pos40b
show b4 surprised at pos75b
show b5 surprised at pos90b
show t surprised at pos60t
with dissolve
"A moment later, we were back in the games room."
show t surprised
t "Wha...?"
show b3 happy
b3 "We're back, thank god!"
show b4 laugh
b4 "I've got fingers! I can write! I could fill out a balance sheet!"
show b5 sad
b5 "Awww! Just when it was getting good!"
show b5 surprised
b5 "Wait, is something... burning?"
"The 'game console' had smoke coming out of it."
"...Guess it's toast."
show t worried
t "...What... happened? My mind's all foggy..."
m "...You okay, Terra?"
show t annoyed
t "...I'm gonna take a nap."
hide t with dissolve
"She jumped on the couch, and within seconds, was fast asleep."
"The Brothers Five and I decided that it would be best to never talk about this again."
$ terraAffection=1
jump postDateSelector
