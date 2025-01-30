label AllieMorning1:

play music Morning
show bg KitchenMorning with dissolve
show y worried at pos65y with dissolve # former look:left


show s neutral  at pos20s with dissolve # former look:left

show v neutral at pos80v with dissolve # posleft
show t neutral at pos35t with dissolve # former ,,-1 # former look:left
show a happy at pos50a with dissolve # former ,,-1 # former look:right
with dissolve
y "Oh my gosh, I heard what happened yesterday. Are you okay?"
m "No worries, I'm good. Thanks, Yui."
show y happy
y "I'm so relieved!"
show v surprised
v "Should you not be resting after yesterday?"
m "Nah, no need. I've only got a few scrapes and bruises."
show s surprised
s "I'm surprised the both of you aren't dead after what you pulled."
show a worried
show y surprised
a "Believe me, me too."
m "Wait, what?"
show v laugh
show a laugh
a "I mean, *cough*, no worries, Scarlett. I've been rollerblading for longer than most people have ever."
"Technically, that's probably true, but..."
show t happy
show v worried
t "You should teach us how to rollerblade, Allie!"
show t happy
t "It seems like it'd be fun."
show s worried
show y worried
y "Uh, you sure, Terra? I feel like that might not be a good idea."
show t neutral
t "What's the worst that could happen?"
show a happy
a "I like your attitude, girl! Come on, let's hit the road!"
"Allie grabbed Terra's hand and pulled her away."
show bg KitchenNoon with dissolve

hide y
hide v
hide a
hide t
hide s
with dissolve
"-- Some time later --"
show s happy at pos75s with dissolve
s "Hey Terra! How was skating?"
show t worried at pos25t with dissolve
t "..."
show t worried at pos25t with dissolve
t "There's no words..."
show t worried at pos25t with dissolve
play sound Hit
hide t with dissolve
show s worried  at pos50s with moveinright
s "...I think Allie broke Terra."
"Scarlett waved her hands frantically in front of Terra's face, as if to check if anyone was still in there."
show s surprised
s "Terra, you in there?"
show s happy
s "...Hey Terra, the internet's back!"
t "..."
"I guess nobody's home."
show s surprised
s "Uh, is there a medic on the island?"

if scarlettAffection >= 1:
    jump ScarlettJoke
if scarlettAffection == 0:
    jump PastScarlettJoke


label ScarlettJoke:
show s happy
s "Wait a minute, I made a new serum the other day that just might be the thing to restore Terra's mind."
show s neutral
s "Just give me a second to administer it..."
m "Hold on, are you talking about the thing that turned everyone to zombies?"
show s laugh
s "Well, I just think, one field test really isn't enough to see if it's botched or not, so why not just -"
"I tried to stop her from administering it, but it was too late."
show s surprised at pos70s
show t surprised at pos30t # former look:right
with vpunch
t "Gaaaaaaah!!!!"
m "Oh boy..."
show t angry
t "Gimme BRAINS!!! BANANAS!!!!"
show s sad
s "Guess this one's a bust, too."
m "Do you have an antidote??"
show s happy
s "..."
m "..."
show s laugh
s "Just kidding, kidding. I've got it right here. Just give me a moment."
"Luckily, Terra ended up being okay."
"We spent the rest of the morning playing video games as therapy for Terra."
jump postMorningSelector

#; Opportunity here to have a thing here if you've been on a ScarlettDate here
#; like, oh shit, i got something i could try to revitalize her mind
label PastScarlettJoke:
"..."
"Luckily, Terra was fine."
"After that was resolved, we spend the rest of the morning playing video games as therapy for Terra."
"She still doesn't remember a thing about what happened."
"What did you see, Terra?"
"...I guess we'll never know."
jump postMorningSelector
