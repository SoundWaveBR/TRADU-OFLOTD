label VioletDate2:

show bg MansionMorning with dissolve
play music JazzBrunch
$ violetAffection=2

show v neutral at pos50v with dissolve
"I found Violet taking a walk outside the mansion."
m "Hey Violet, what's up?"
show v happy
v "Hello there, [name]. I just thought I'd take a nice afternoon walk. This place truly does bring back memories of home."
m "You lived on your own personal island?"
show v laugh
v "Nothing quite that... bourgeousie."
m "Anyway, I've got a surprise for you. Wanna see?"
show v surprised
v "For me? I..."
show v neutral
"I motioned for her to follow me into the mansion."
show bg MansionIndoorsMorning with dissolve #time:1
$ renpy.pause(delay = 1.0, hard = False)
show bg KitchenMorning with dissolve #time:1
show v surprised
stop music
play music CrinolineDreams
m "I asked Kat to pull a few strings, and, well... we have everything we need to bake whatever we want now."
show v happy
v "Oh my..."
"Violet looked at me with childlike wonder in her eyes."
show v laugh
v "Let's get right to it then, why don't we!"
"She was practically shaking with excitement. Her smile and laughter was positively infectious."
show v happy
"We decided to make a chocolate cake. It was her favorite flavor, and I don't remember mine."
"That said, I also don't remember a thing about how to make cakes... but with Violet, that wasn't a problem."
show v laugh
"She got me up to speed with a soft and steady hand, and before long, we had the cake in the oven, baking away."
"I wish it took longer to make. Seeing Violet do what she loved most was a treat."
"When she pulled the cake out of the oven, she looked like a kid on Christmas Day."
hide v with dissolve
show bg VioletBaking with dissolve
v "Now, just for the finishing touches...! A little more here, a little more there..."
"She was in her own world, humming away as she danced around the cake, decorating it as she went along."
"I couldn't help but smile and watch her in adoration."
"She's pure happiness right now. I wish I could take this moment and just freeze it in time, for safekeeping."
v "I can't wait to share this with the others!"
v "But first... [name], would you mind testing it?"
m "You don't have to ask, believe me! I'm first in line to try it out."
show bg KitchenMorning with dissolve
show v worried at pos50v with dissolve
v "Thank you, I just... am unsure if what I make is worth eating... or not."
m "Why's that?"
show v happy
v "My family's caretaker, Shirley, was the one who taught me to bake."
show v neutral
v "Besides my sister, Shirley was the only one who ever bothered to try what I made."
show v worried
v "...Sometimes I worry they told me it's delicious just to make me feel better."
"I took a little off the top of her cake with my finger and licked it off."
m "It's delicious, Violet. You better believe it!"
show v blush
v "...Would you want to help me a little longer? I'm having far too much fun to just stop now."
show v laugh
v "I've just started making some cookies, and I find I quite enjoy your company and help, [name]."
m "I'd love to! Let me know how I can help."
"Violet passed me a bowl full of cookie dough, then a tray."
show v happy
v "All you need to do is make little cookie shaped pieces out of this dough, then put them on the tray."
show v worried
v "Do try not to put any of them too close together on the tray, or it'll become something of a mutant cookie in the oven."
m "Got it. No mutant cookies here."
"I ripped off a piece of dough from the bowl, and rolled it into the size and shape of a cookie."
show v laugh
v "Perfect. You're a natural."
m "Thanks, Violet! I..."
"Wow."
"In the time it took me to make one, Violet had made six perfect cookies."
"She moved with mechanical efficiency as she kneaded balls of dough into perfectly shaped cookies."
m "Wow. I thought you were great before, but you're really incredible. How long have you been doing this?"
show v neutral
v "Perhaps... since I was about, say, five?"
show v happy
v "To this day, it remains the only thing I can best my sister at."
"I finished making another cookie as Violet finished three more."
show v neutral
"She held up one of the cookies and raised it to her face."
show v happy
v "You've gotten quite skilled at this, [name]."
show v laugh
v "I just wanted to say again... thank you for arranging this. I'm on top of the world right now."
m "It was my pleasure, Violet."
"Gosh, she's adorable when she smiles."
"For a few seconds, we kept working on the cookies in amiable silence, our eyes locked on each other's."
m "You said you had a sister?"
show v happy
v "Why yes indeed! Viola Valentine. First twins in the family. She..."
show v surprised
v "Oh, I'm out of my room on my tray."
show v laugh
stop music
play music TheShowMustBeGo
"She flashed a devious smile in my direction, right before she lightly threw a dough ball at my face."
m "What's with that cheeky -"
play sound Hit
show v laugh
with vpunch
"Before I could react, it splatted against and stuck to my face."
"She burst into childlike laughter."
v "Nice catch, [name]! Perhaps you might try using your hands next time?"
m "Oh, it's on."
show v happy
"I couldn't stop myself from smiling as I grabbed some 'ammo' from my own cookie tray, and threw them at her."
play sound Whoosh
show v neutral at pos30v
show v happy  at pos50v
"She dodged them with ease and laughed."
show v laugh
v "It's quite humorous how an old caretaker managed to do what you are struggling to do now."
"I interrupted her gloating with another dough ball throw."
show v surprised
play sound Hit
with vpunch
"This time, it made a satisfying 'SPLAT!' against her left cheek."
m "STRIIIIIIIIIKE!!!!!!!"
show v serious
v "Oh... you are so going down."
show v laugh
"Her smile turned devilish as she grabbed another dough ball."
"Oh shit."

menu:
    n "I've only a second before her next volley, I..."

    "Go on the offensive":
        jump vd2c1
    "Go on the defensive":
        jump vd2c2

label vd2c1:

play sound Hit
with vpunch
"I'd just started to reach for another dough ball from the tray when a dough ball splatted against my forehead, sending me recoiling backwards."
m "Ahhh!!!!"
jump vd2pc2

label vd2c2:
"I ducked behind the kitchen counter."
"An instant later, a dough ball flew above my head."
m "Hah! Nice -"

play sound Hit
with vpunch
"While I was gloating, Violet threw a dough ball that splatted against my forehead."
m "Aghhh!!!"

label vd2pc2:

with vpunch
play sound Hit
"And then another landed, right next to it."
m "Ahhhh!!!!! Mercy!!"
with vpunch
play sound Hit
"And then another."
"I crumpled to the floor in defeat."
show v laugh
v "I declare this... my victory, in absolute confidence!"
"She laughed as she pointed at all the dough on my face."
"I took the opportunity to interrupt her speech with another dough ball."
show v surprised
play sound Hit
with vpunch
"It splatted right against her left cheek."
show v laugh
v "Oh, you're even more dead now."
"Forget surviving this crazy TV show - I don't know if I'm surviving the next five minutes."
"It was like looking a tiger dead in the eye."
"Violet reloaded her ammo and was winding up for another throw."
"It was all I could do to reach for one more ball and scream in defiance."
m "BRING IT ON!!!!!!!!"
play sound Explosion
"..."
"Some say you can still hear my screams in that kitchen to this day."
"..."
stop music
play music CrinolineDreams
"We finished cleaning up after our impromptu food fight, and brought the desserts that survived the great war to the porch."
"Her smile and laughter were infectious."
show v laugh
v "Pardon me, but I guess we can rule out you being a baseball player before you had come to this island."
"She put her hand tenderly against my face as she wiped off some remaining dough."
"We locked eyes yet again. Her eyes were practically magnetic."
show v happy
v "Thanks for playing along, [name], I... I suppose it's been too long since I've had that much fun."
show v blush
v "So... thank you, for indulging my little whim."
m "It was a lot of fun for me too, Violet. Don't mention it."
m "Besides, I think I got a few good hits in to make it worth it."
show v laugh
v "I'm worried for you! It appears your amnesia is getting even worse!"
"Violet laughed as she picked off some more crumbs off my face and licked them off her finger."
show v blush
"Her eyes seemed to linger on mine."
show v happy
v "I do hope we can spend more time together soon, I... quite liked this."
m "I'd like that, Violet. I had a lot of fun with you too."
m "You're full of surprises, you know?"
show v laugh
v "Just wait and see, there's more where that came from!"
"We spend the rest of the day talking and eating little desserts together on the porch."
"Though Violet seemed quite distant when I first met her, I learned that the real Violet was nothing like that at all, and full of surprises."
"She could be unexpectedly shy one moment, then mischevious as a child another."
"One thing's for sure - being around her makes my heart skip a beat, and the time fly."
hide v with dissolve
show bg Black with dissolve
"Before I realized how much time had passed, it was already pitch black outside."
$ violetAffection=2
jump postDateSelector
