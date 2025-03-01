label YuiDate1:

show bg Hills with dissolve
$ yuiAffection=1

play music Meadow

"A floresta ao norte da casa era tão serena quanto possível."
"A cada passo à frente, eu sentia a terra macia ceder sob meus pés, e o vento acariciar minha pele."
"Verde até onde os olhos podem ver... e ela, em um vestido branco esvoaçante, parada no meio de tudo."
show y happy at pos50y with dissolve
y "Ei, [name]. O que você está fazendo aqui fora?"

menu:
    "Eu estava procurando você":
        jump yd1c1
    "Eu ia te perguntar a mesma coisa":
        jump yd1c2

label yd1c1:
m "Eu estava procurando por você, Yui."
show y laugh
m "Eu esperava que poderiamos passar um tempo juntos."
show y happy
y "Então me considere a garota mais sortuda do mundo!"
"Yui tinha uma risadinha fofa, do tido que coloca um sorriso no seu rosto instataneamente."
show y happy
y "Bem, você me encontrou agora."
show y laugh
y "Se importa de se juntar a mim para uma caminhada?"
m "...Eu adoraria."
jump yd1pc

label yd1c2:
m "Eu ia te perguntar a mesma coisa."
show y laugh
y "Acho que sim!"
"Yui tinha uma risadinha fofa, do tido que coloca um sorriso no seu rosto instataneamente."
show y happy
y "Se importa de se juntar a mim para uma caminhada?"
m "...Eu adoraria."

label yd1pc:

hide y with dissolve
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True)
show bg YuiInField with dissolve # time:1
"We started to walk down the forest path together."
"I couldn't help but be fascinated by her hair, flowing like water in the wind."
#show y neutral
y "I doubt you remember, but..."
#show y laugh
y "I'm from way out in the country. I grew up surrounded by animals, nature, you name it!"
#show y happy
y "It was just me and my grandma, my sisters, and the alpacas, and my bunnies Bun and Bunbun, and the chickens, and... too many farm animals to count!"
#show y happy
y "To answer your question from earlier... nature takes me back home."
m "Do you still live there?"
#show y laugh
y "Yep! Wouldn't have it any other way."

#show y neutral
y "Though I had moved to the city for a bit, way back when."
#show y happy
y "You know, that's when I met you!"
m "How'd we meet?"
#show y neutral
y "Well..."
stop sound
show bg Hills with dissolve
show y sad at pos50y with dissolve

y "You know, one thing I hated about the city... is that everyone's in a rush."
show y serious
y "People just walk by each other as if they're obstacles to get past, instead of... well, people."
show y sad
y "I came to the city alone. Didn't know left from right."
show y laugh
y "And... I got lost! I swear every building looks the same."
m "You can say that again."
show y sad
y "I'd try to ask people for directions to where I would live, or where the school was, but no one would give me the time of day."
show y blush
y "Except for you."
m "I helped you?"
show y laugh
y "Yeah. You didn't even know me, but you took the time to help me figure my way around."
show y blush
y "Gosh, I'd never been so embarrassed in my life."
m "Why were you embarrassed?"
show y neutral
y "Uh... you know."
show y blush
y "Hehe. Shy."
m "?"
show y neutral
y "We found out later we went to the same high school, but we never talked too much after that."
m "Aw, I'm sorry about that."
show y surprised
y "Oh, it's not your fault, [name]! I had to move back home pretty soon after, anyway."
m "Well, I'm happy I'm getting a second chance to get to know you better, Yui."
show y happy
y "I feel the same way, [name]!"
show y blush
y "You're just like how I remember."
show y surprised
y "Well, actually, the whole trying to date 5 girls at a time thing came out of nowhere, but... life is full of surprises, I guess."
show y laugh
stop music
play sound MysteryPiano
y "It shouldn't take long to remove them from the equation."
m "Sorry, what did you say? I couldn't hear you."
play music Meadow
show y shy
y "Just a little joke. Hehe..."
show y neutral
y "I was just saying, I'm so happy to see you again!"
show y happy
y "Here's to the future!"
show y laugh
"We spent the rest of the day taking in the nature, and making up for lost time."
"Apparently, I was always ending up in trouble back then."
show y happy
"I guess not much has changed..."
"Something about Yui made it so easy to open up. I found myself almost telling her the truth about the show several times."
"Even though I couldn't tell her the whole truth, I could tell her just enough of what was worrying me to make me feel at home and at ease."
show y laugh
y "Whatever's getting you down... I'm sure it'll all be okay."
show y happy
y "No matter what... I'm on your side, [name]."
$ yuiAffection=1
jump postDateSelector
