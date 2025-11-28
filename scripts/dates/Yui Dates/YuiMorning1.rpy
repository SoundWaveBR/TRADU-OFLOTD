label YuiMorning1:

show bg MansionMorning with dissolve
play music Morning
"In the morning, the girls and I decided to hang out in the garden outside the house."
show t happy at pos30t with dissolve
show y surprised at pos50y with dissolve # former ,,-1
show s happy at pos70s with dissolve
y "Oh, wow! There's all kinds of flowers here that I've never seen here before!"
show s surprised
s "Really! You've never seen a tulip?"
show y happy
y "Grandma and I only grew hyacinths back home, so nope."
show t surprised
t "Not even on the internet?"
show t happy
t "And I thought I had to get out more."
show s neutral
s "I can believe that, the only flowers I ever work with are Venus fly traps."
show t surprised
t "What do you do with those?"
show s laugh
s "Well, we do a lot of experiments at the lab."
show s happy
s "Don't you ever find yourself thinking, wouldn't it be cool to make a Venus fly trap that could walk... and talk?"
show y surprised
y "..."
show t surprised
t "Literally never."
show s sad
s "Ah, It's whatever. She ran away two years ago."
show s neutral
s "Both my neighbors lost their pet cats the same day, too."
show s sad
s "I miss you, Fluffy..."
show y surprised
y "You sure they were lost?"
show v happy at pos10v with easeinleft # former look:right
v "Tea's ready!"
m "Thanks, Violet!"
"I got a cup for everybody. The aroma from the tea really worked up my appetite."

if violetAffection <= 1:
    jump treatversion1
if violetAffection == 2:
    jump treatversion2

label treatversion1:
show v happy
v "I have prepared some treats for us as well. Please enjoy!"
jump aftertreats

label treatversion2:
show v laugh
v "I've prepared some treats for us as well. Please do enjoy!"
show v happy
v "They're not quite up to par with the batch we had made, [name], but rest assured, you'll find no complaints with this either."
m "Who could complain about surprise cookies?"
show v neutral
v "You're quite right."
show v happy
v "Let's make more together soon. I have other recipes I would like to try!"
jump aftertreats

label aftertreats:
"We spent the rest of the morning eating delicious treats and sipping on delicious tea, as we theorized what might have happened to Fluffy."
"Personally, my money's on the felines being the culprits. Every Kat I've met has had a nasty surprise up their sleeve."
jump postMorningSelector
