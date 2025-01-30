label TerraDate2:

$ terraAffection=2

play music Sincerely
show bg MansionIndoorsNoon with dissolve
play sound DoorKnock
"I knocked on the door to the games room."
play sound DoorOpen
show t neutral at pos50t with dissolve
t "Hey [name]! What's up?"
m "I thought I'd check in and see how you're doing with your game."
show t happy
t "Let me show you what I'm working on, then!"
"Terra handed me her game device."
show t neutral
t "Not all the art's ready yet, but I'm hoping it'll be done soon."
show t happy
t "It's a farming game!!"
show t worried
t "I had to ditch the pigeon dating idea after, well... finding out it was already done."
m "That's... really a shame. For the whole world, really."
show t happy
t "But in this game, you get to live in a village out in the country, make friends, raise crops, and..."
show t blush
t "...Decimate all the invaders with your giant mecha pigeon death machine."
show t neutral
t "And there's 1,000,000 possible weapon combinations, and..."

menu:
    "That sounds cool!":
        jump td2c1
    "That sounds... different":
        jump td2c2

label td2c1:
m "Wow. That sounds cool! I'd love to play it."
jump td2pc

label td2c2:
m "Wow, that sounds... different!"
m "I don't know what to expect, but I'd love to play it."

label td2pc:
m "I'm curious, how come you decided to make a farming game?"
show t surprised
t "Um, good question."
show t happy
t "They've just got a special place in my heart!"
show t blush
t "I used to just play these, morning till night, every day."
show t worried
t "You can probably tell, I'm not really a 'go out and party' kind of person."
show t sad
t "To be honest, I don't know enough people to go to parties anyway, but whatever."

menu:
    "Sometimes it's more fun to just do your own thing":
        jump td2c3
    "Hey, it's your choice on how you spend your time":
        jump td2c4

label td2c3:
m "Sometimes it can be more fun to stay indoors and just do what you enjoy."
show t happy
t "That's how I feel about it!"
jump td2pc2

label td2c4:
m "Hey, it's your life! It's your choice on how you spend your time."
m "Just do what you want, you know?"
show t happy
t "That's pretty much how I feel about it!"

label td2pc2:

show t neutral
t "Enough talk, try playing it!"
show t happy
t "I want to see how you feel about it."
m "Alright, here we go!"
show bg Black with dissolve
hide t with dissolve
stop music
play music MoveForward
"The title screen displayed with a click."
"'Starblue Valley'."
"I was a mecha pilot who got tired of life in the mecha corps, and decided to move out to the country to become a farmer."
"I was a pretty good one at that! Every season, I'd learn to plant, water, and harvest new kinds of crops."
"Terra would give me advice for farming in every season."
"Her face was so close to mine - she'd watch my every move with a pensive expression."
"Farming and fishing felt great, but fishing was almost impossible to do at first."
"The mecha parts of the game felt incredible."
"You could even get to know the villagers, and have relationships with them too."
"There was just one thing that was a bit weird..."
stop music
play music BlippyTrance
show bg GamesRoomMorning with dissolve
m "First, wow. What you have so far is incredible, Terra!"
show t blush at pos50t with dissolve
t "You think so?"
m "Yeah, really! It's incredible. I never thought you could combine farming and being a mecha pilot in the same game, but you did it just fine."
show t happy
t "Thanks, [name]. That's nice of you to say."
m "There's just one thing I think that was a little off."
show t surprised
t "What's that? Any feedback would be great!"
show t worried
m "I feel like the relationships with the townspeople were a little weird."
m "The dating aspects didn't really feel right?"
show t sad
t "Ah, I knew you'd notice that!"
show t worried
t "It's kind of embarassing, but..."
show t surprised
t "I've never actually dated before, so I have no idea what it's really like."
show t worried
t "...And to be honest, I've never really had a real friend, either."
show t blush
t "If it's not too much to ask..."
"Her voice suddenly reduced to a whisper."
show t happy
t "...Maybe you and I could be friends?"
m "...I'd be honored to be your friend."
m "...That said... please don't trap me in a video game again."
show t surprised
t "...? Sorry, What?"
show t neutral
t "Anyway, watching you play gave me some ideas. Want to help me with testing them?"
m "Sure! I'd be happy to help however I can."
hide t with dissolve
show bg Black with dissolve
"We'd both suggest ideas, she'd implement it, and we'd test it together - and repeat."
"It just kept getting better and better."
show t happy at pos50t with dissolve
"Terra's smile and enthusiasm was contagious. I couldn't help but be excited for her, and in awe of her drive."
"We spent the rest of the day working on her game, but it only felt like minutes."
"...I'm just glad it wasn't another virtual reality game."
$ terraAffection=2
jump postDateSelector


#; OLD
