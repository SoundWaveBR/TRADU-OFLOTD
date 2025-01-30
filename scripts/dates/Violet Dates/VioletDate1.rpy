label VioletDate1:

$ violetAffection=1
show bg MansionMorning with dissolve
play music Morning
"I had just gone outside the mansion to find Violet, when a white limousine drove up and stopped in front of me."
show b1 neutral at pos50b with dissolve
"One stepped out from the driver's seat, and walked towards me."
b1 "[name], good day. Please do enter."
m "What's with the formal talk?"
show b1 worried
b1 "Please just get in the car, [name]! You already heard what she did to my bro!"
m "...?"
show b1 serious
"He opened the passenger door and ushered me inside."
hide b1 with dissolve
show bg Black with dissolve
"I shrugged and went inside. What's the worst that could happen on a death game dating show?"
stop music
"We sat in silence as One drove me to what looked like some sort of fancy restaurant, then escorted me inside."
show bg Palace with dissolve
play music CrinolineDreams
show v happy at pos50v with dissolve
v "Bonjour, Suitor! I trust my new butler brought you here safely?"
m "Yeah, he did. What's going on, Violet?"
show v laugh
v "I thought I would give you a chance to have some alone time with the star of the show, is all."
show v neutral
v "I am told this is what people do when they are... 'courting'."
m "...Have you never been on a date before?"
show v surprised
v "O-Of course I have! And I've read all the manuals on the subject."
show v sassy
v "I'll have you know, I've studied every book of the 'The Lusty New Asian Maid' series, and know them all by heart."
show v laugh


menu:
    v "Impressed, I'm sure."

    "I'm impressed":
        jump vd1c1
    "...Sure":
        jump vd1c2

label vd1c1:
m "...I'm impressed, Violet."
show v sassy
v "Oh, it was nothing."
jump vd1pc

label vd1c2:
m "That's... yeah, a word for it."

label vd1pc:

show v neutral at pos30v with dissolve
show b1 happy at pos70b with dissolve

b1 "Pardon my interruption. I've brought your food. Please be seated, honored guests."
"Violet and I sat at a table in the center of the palace, as One placed each dish onto the table one by one."
show b1 worried
"He seemed to linger over the meatballs as he brought them over."
show v happy
v "Thank you, One."
hide b1 with dissolve
show v laugh at pos50v with dissolve # former look:left
v "Please, don't hold yourself back."
m "Don't think I will! This food looks incredible, and probably worth more than my life."
show v happy
v "You're right on both counts, [name]."
show v laugh
v "I'm ecstatic you like the assortment. I planned it myself!"
m "You're a chef?"
show v blush
v "...You could say that."
m "...? What do you mean?"
show v neutral
v "...Anyway, tell me more about yourself, [name]."
m "There's not too much to say. Amnesia is a hell of a drug."
show v surprised
v "You do not... remember your past?"
m "Yeah. Bummer, right?"
show v happy
v "Then rest assured, I will find the finest scientists in all the land to help you recover your memory when this is over."
m "That... that would be great. Thanks, Violet."
show v neutral
v "Think nothing of it. It's the duty of those with more to give back, no?"
show v worried
stop music
play music MysteryLoop
v "Though... have you ever thought, perchance, that this is actually a blessing in disguise?"
m "What do you mean?"
show v sad
v "Many of us would be happier not knowing what drags us down."
m "...That may be true, but still, I need to know."
show v happy
v "You sound just like the reference examples in the romance manuals! Consider me impressed."
m "...You know, those manuals... are just regular ol' fiction novels, right?"
stop music
play music CrinolineDreams
show v laugh
v "Hah! You're quite funny, [name]. An admirable trait to have... I like that."
m "..."
m "Anyway, you haven't told me about yourself, Violet."
m "Who are you, what do you do for fun? I'd like to know!"
show v worried
v "...Being the scion of the Valentines does not leave much time for fun, I'm afraid."
show v laugh
v "Even on this show, I spend most of my waking hours managing the Valentine's restaurant businesses."
show v happy
v "But I suppose... if I have a spell of time, I enjoy..."
show v blush
v "...Baking..."
m "I don't get it, why are you embarassed by liking baking?"
m "Everyone has a hobby."
show v sad
v "Baking is something of a ...servant hobby, according to my parents."
show v worried
v "When they found out I was enjoying that... well, they made sure to stop me from ever doing it again, with all the restaurant work."
show v laugh
v "It's a bit ironic, isn't it?"
m "...You know what?"
show v surprised
v "I do know of 'what', but... what do you mean?"
show v neutral
m "Who cares what your parents think? Here, on this island a million miles out, they can't stop you."
m "How about we find some time together to... bake up for lost time?"
show v happy
"She laughed like a child."
v "That would be... That would be wonderful, [name]."
show v laugh
v "I'll make some time on my calendar for you."
"We spent the next few hours enjoying the finest meal that money could buy."
"Each course was better than the last - just like each chapter of 'The Lusty New Asian Maid', according to Violet."
"Something tells me that the same applies to every moment I'll share together with Violet."
$ violetAffection=1
jump postDateSelector
