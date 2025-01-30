label MetAllGirls:

play music Morning
show bg MansionMorning with dissolve

show a surprised at pos15a with dissolve # former look:right
show y neutral at pos90y with dissolve # former look:left
show v neutral at pos30v with dissolve # former look:left
show t neutral at pos75t with dissolve # former look:left
show s happy at pos60s with dissolve # former look:left


show k neutral at pos45k with dissolve # former ,,-1 # former look:left
"By the time I got there, Kat and the girls were surrounding a blackboard covered with scribbles and math equations."
show k flirt
k "...And that's why [name] is the perfect soulmate for each of you."
show s surprised
s "I'm sorry, you just drew a bunch of numbers and symbols that don't mean anything."
show t surprised
t "It's like the bullshit math they show on-screen in a movie!"
show k happy
k "Ah, you're late to the party, [name]!"
show k flirt
k "But you're just in time for the first 'alone time' segment!"
m "Alone time segment?"
show k laugh
k "You can't find your soulmate without having a little alone time, together!"
show k neutral
show y blush
show a laugh
show s tease
show t neutral
show k flirt
k "It's time to pick your first soulmate candidate - one of two lovely ladies you'll get to spend time with this week."
show k neutral
k "So without further ado... who's it going to be?"
m "Wait, I have to choose already?"
m "I haven't even had the chance to really talk with any of them yet."
show k flirt
k "Don't think of it that way! Think of it more like, well... who do you want to talk to the most right now."
m "Alright, I guess."

menu:
    m "I'd like to spend today's alone time with..."

    "Allie":
        jump MetAllGirlsAllie
    "Scarlett":
        jump MetAllGirlsScarlett
    "Terra":
        jump MetAllGirlsTerra
    "Violet":
        jump MetAllGirlsViolet
    "Yui":
        jump MetAllGirlsYui

label MetAllGirlsAllie:
show a surprised
m "Allie."
show a happy
$ selectedDate="Allie"
show k happy
k "We'll make it happen!"
show k angry
k "Let's get the cameras rolling, people! We're in for a bumpy ride on day one!"
b "Yes ma'am!"
show k flirt
k "Now be a dear and give us a minute to set up the scene, hmm?"
jump DateSelector

label MetAllGirlsScarlett:
show s laugh
m "Scarlett."
$ selectedDate="Scarlett"
show s happy
show k happy
k "Alright! We'll make it happen."
show k angry
k "Places, people! Let's have [name] start in the mansion... and you know where to bring Scarlett."
b "Yes ma'am!"
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label MetAllGirlsTerra:
show t surprised
m "Terra."
show t happy
$ selectedDate="Terra"
show k happy
k "Alright! Our work's cut out for us."
show k angry
k "Places, people! You know where to put Terra."
b "Yes ma'am!"
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label MetAllGirlsViolet:
show v happy
m "Violet."
show v sassy
$ selectedDate="Violet"
show k happy
k "Alright! We'll make it happen."
show k angry
k "Places, people! Let's have [name] start in the mansion... and you know where to put Violet."
b "Yes ma'am!"
show k happy
k "Give us a minute to set up the scene, then go find her!"
jump DateSelector

label MetAllGirlsYui:
show y surprised
m "Yui."
$ selectedDate="Yui"
show k happy
show y blush
k "Yessss! Cough it up, Four! I won the bet."
b4 "But that was my whole salary!! How am I gonna -"
show k laugh
k "And great choice, [name]! I knew I could count on you!"
m "..."
show k angry
k "Alright, places, people! Let's get this show on the road!"
b "Yes ma'am!"
show k flirt
k "And... action!"
jump DateSelector
