label VioletMorning1:

show bg KitchenMorning with dissolve
play music BlippyTrance
show v neutral at pos70v with dissolve# former look:left
show t worried at pos30t with dissolve # former look:right
v "...Then you set the meat at around... 300 degrees for 40 minutes."
show t serious
t "Mmhm, okay... got it."
"Terra furiously scribbled down notes."
show t surprised
t "Wait a minute! Couldn't I just cook it for 600 degrees for 20 minutes?"
show v worried
v "That's not quite how this works, I'm afraid."
show t worried
t "But the math checks out!"
m "What's going on?"
show v happy
v "Oh! Good morning, [name]. How do you do?"
show v laugh
v "I'm teaching Terra the proper way to prepare a pot roast."
show t happy
show v worried
t "So far I'd say it's going pretty well!"
show v happy
v "...Terra will be the one to prepare lunch today, instead of me."
show t annoyed
"Terra turned one of the dials on the stove as far as it would go to the right."
show t happy
t "And the student... has surpassed the master."
show v worried
v "On second thought... perhaps I'll prepare an alternative course. One moment, please."
hide v with dissolve
show t angry
t "Oh ye of little faith!!"
hide t with dissolve
show bg Black with dissolve
"Time for the moment of truth - lunch is served!"
show bg KitchenMorning with dissolve

show y neutral at pos10y with dissolve # former look:left
show a happy at pos90a with dissolve # former look:right
show s neutral at pos70s with dissolve # former look:left
show t neutral at pos50t with dissolve# former look:right
show v neutral at pos30v with dissolve# former ,,-1 # former look:left


show t worried at pos50t
t "..."
"Terra was nervously clasping her hands tight."
show s surprised
s "...!"
show y surprised
y "...!"
show a happy
a "...!"
m "...!"
show s happy
show y laugh
show t surprised
show a happy
show v happy
stop music
play music CheeryMonday
all "It's delicious!"
show t happy with vpunch
t "...! I did it, oh my gosh!!!"
"Terra did a little dance in celebration, and gave Violet a high five."
show t surprised
t "...Should I become a food Vlogger? I'm a cooking savant. This talent shouldn't be wasted..."
#hide t
show t happy at pos30t
show v happy at pos50v
# show s happy at pos70s

with dissolve
m "Psst, Hey Violet."
#show v happy at pos50v with dissolve
v "What is it, [name]?"
m "Is this what you cooked, or is this what Terra cooked?"
show v happy
"Violet smiled and winked at me."
show v laugh
v "I don't know what you are talking about."
"She sipped on her soup contently."
"I couldn't help but smile back at her. Damn, this was the best meal I've ever had."

if currentDay == 1:
    jump OneDayOnly

"...Granted, my memory only goes back about [currentDay] days, but still, it counts for something!"
jump postMorningSelector

label OneDayOnly:
"...Granted, my memory only goes back [currentDay] day, but still, it counts for something!"
jump postMorningSelector
