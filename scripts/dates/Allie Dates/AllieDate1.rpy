
label AllieDate1:

play music CarpeDiem
show bg RoadMorning with dissolve
$ allieAffection=1

"Como eu deixei a Allie me convencer a isso, eu nunca vou saber."
m "Tem certeza que isso é uma boa ideia?"
show a laugh at pos50a with dissolve
a "Só tem um jeito de descobrir, não é?"
"Allie segurou minha mãe e me puxou em direção à ladeira da colina."
show a happy
a "Relaxa, [name]. Qual é o pior que pode acontecer?"
m "Bem, eu posso morrer."
"Será pedir demais participar de um programa de TV que não termina comigo morto?"
show a laugh
a "Não se preocupe. Eu cuido de você -"
show a surprised
stop music
play music LeGrandChase
show a surprised with vpunch
a "Ah merd-"
"Allie escorregou nos patins, me puxando para baixo da colina com ela."
"Tentei dar um passo para trás por reflexo, mas era tudo que eu podia fazer para continuar de pé com os patins."
m "Ah por-"
with vpunch
play sound Rollerblade
"We started rolling down the hill - faster, and faster, and faster."
with vpunch # Allie
"Allie was rolling down the hill backwards at full speed. I could see panic in her eyes."
"I couldn't figure out how to stop, we were going faster and faster."
with vpunch # Allie
"I screamed -"
show a laugh
"Allie laughed and pointed at me."
show a happy
a "Gosh, your face is priceless! I love it."
stop music
play music CarpeDiem
"Allie turned around effortlessly, and somehow glided next to me, without ever having letting go of my hand."
"Our breakneck pace became slower and slower as she steered us back and forth repeatedly."
"Before I knew it, we were gliding down the roads smoothly."
"The wind felt so nice."
hide a with dissolve
show bg AllieRollerblading with dissolve
#show a laugh
a "Now you've got the hang of it!"
m "You've got a funny way of teaching."
#show a happy
a "The best way to teach a bird to fly is throwing it off a cliff, no?"
m "That's definitely a.. way of looking at it."
#show a neutral
a "Don't worry about it! You weren't ever in danger."
m "Have you been rollerblading for a long time?"
#show a laugh
a "Nope!"
#show a neutral
a "I actually just learned how to today."
m "Er... what was that about never being in danger?"
show bg Hills with dissolve
show a happy at pos50a with dissolve
a "Shhhh."
m "You're quite the daredevil, aren't you?"
show a laugh
a "What gave that away?"
with vpunch
"She laughed as she slapped me on the back."
show a happy
a "You know, you're a pretty quick learner!"
show a neutral
a "You picked up roller blading almost as fast as I did."
m "Well, I've got a pretty great teacher."
m "It's a lot of fun hanging out with you, Allie."
show a laugh
a "Shucks, I feel the same way, [name]!"
show a happy
a "It's great to be around someone willing to go on an adventure."
show a laugh
a "The world's gone crazy, we're all gonna die, you might as well be around people that make life worth living."
m "I couldn't say it better myself."
show a sassy
a "You know, I bet you can't skate backwards."
# with vpunch # Allie
show a sassy with vpunch
play sound Rollerblade
"Allie reversed and started skating backwards, as if to taunt me."
m "Oh? Why's that?"
show a happy
a "I just think it's a bit too scary for a person who screams when they start going down a little bump."
show a worried
a "'I'm [name], and I can't handle a little bump!! AAAAAAH!! HELP ME!!!'"
m "Come on, it was a hill!"
show a laugh
a "Yeah, yeah."
"I felt a fire light inside me."
m "Bring it on, Allie!"
show a surprised
a "Oh, are you sure?"
m "Did I stutter?"
"There comes a time in every person's life where we know we're taking a stupid bet, but do it anyway."
play sound Rollerblade

menu:
    n "With the power of misplaced confidence and adrenaline, I jumped high into the air..."

    "...and did a 360 rotation!":
        jump rotation360
    "...and did a backflip!":
        jump backflip

label rotation360:
"...and did a 360 rotation!!"
"Wait, am I spinning, or is the world spinning? I'm not sure."
jump after_stunt

label backflip:
"...and did a backflip!!!"
"Wait, am I doing a flip, or is the world flipping? I'm not sure."

label after_stunt:
"Then it dawned on me."
show a surprised
m "Oh fu-"
hide a with dissolve
show bg Black with dissolve
stop music
stop sound
# @stopsfx Rollerblade
play sound Hit
play music Smile
"..."
play sound Glitch1
# "Here's a {glitch=50}{color=#0f0}{b}Some Dialogue{/b}{/color} Tag{/glitch}"
q "{glitch=50}{b}No. I won't let you kill [name].{/b}{/glitch}"
"What...?"
play sound Glitch2
q "{glitch=50}{b}You're going to wish we had.{/b}{/glitch}"
stop music
show bg RoomMorning with dissolve
"What just...?"
show a worried at pos50a with dissolve
m "What the hell?"
show a surprised
play music CarpeDiem
a "You're up! You okay, [name]?"
show a worried
a "Try not to move. You're a little banged up right now, but you'll be just fine in no time."
show a happy
a "Kat and I treated your injuries. Pretty well if I do say so myself!"
m "What... what happened?"
show a laugh
a "You uh... well, 'skated backwards'."
show a worried
a "We're defining skating quite liberally, huh?"
m "How'd I get here?"
show a neutral
a "I carried you here."
m "Oh man, my head..."
show a worried
a "Take it easy. It's only been a few hours since you KO'd yourself."
show a blush
a "Um, well, it's sorta my fault, but..."
show a worried
a "I made you some food, it should help you get your strength back up quick."
m "Thanks, Allie. That's really nice of you."
show a laugh
a "Don't expect something that Violet would make!"
show a worried
a "All I can promise is that the food is probably healthier than my last suggestion before you knocked yourself out."
m "I'll take my chances."
"I took a bite of the food cautiously."
show a surprised
m "Gah!!!! I- *Cough* I'm - I'm dying...! *Cough*"
show a worried
"For a moment, Allie was wide-eyed with shock and horror."
show a angry
m "Haha, I'm just messing with you. The food's delicious. Thanks Allie."
m "I just figured I'd get a little bit of payback."
show a laugh
a "You know, no one forced you to jump!"
"She laughed and slapped me on the shoulder, then ran her hand through my hair and scratched it."
"I found myself smiling and admiring the blue of her eyes."
show a happy
a "I'm looking forward to our next adventure, [name]."
show a laugh
a "But promise to not be too stupid again, okay?"
m "I'll try my best. But people can't help but do stupid things to impress a pretty girl."
show a blush
a "I guess 'impressed' is what we'll call it."
"We spent the rest of the day making fun of each other for how stupid we were being."
"Somehow, someway, Allie could take the ordinary and turn it into an adventure."
"I was laughing so hard that I could barely feel any pain."
hide a with dissolve
show bg Black with dissolve

"Before I knew it, it was night time."

$ allieAffection=1
jump postDateSelector
