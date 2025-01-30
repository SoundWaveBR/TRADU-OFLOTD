label ScarlettMorning2:

play sound Explosion
play music RavingEnergy

show bg RoomMorning with dissolve
#; could try to give a secret message
#; could use a sound blocker and say i think i know what's going on with this game
#;
"The next day, I woke to the sound of an explosion outside."
"I ran outside as fast as I could."
m "What the..."
stop music
show bg MansionMorning with dissolve
play music Wholesome
show s surprised at pos50s with dissolve
"The first thing I saw was Scarlett, and black smoke emanating from the ground near her."
show s worried
s "Oh, hey there, [name]. Nice weather we're having, huh?"
m "Hey, Scarlett... you okay?"
show s happy
s "I'm pretty good, all things considered!"
show s annoyed
s "I've been experimenting again on trying to bring back people's memories. Without the whole monkey zombie bit."
show s flirt
s "I figure, if you and I ever, well... you know, I'd want us to know everything about each other."
show s neutral
s "...No secrets."
m "I'd like that, Scarlett. Thanks."
show s happy
s "I'll let you know if I make any progress with that."
show s laugh
s "...Ugh, I gotta clean this up."
show s happy
s "Give me a minute, and then we can head to the forest? I've been meaning to spend some time there since I got to this island."
m "Sounds good by me!"
stop music
play music RomanticJazz
hide s with dissolve
show bg LakeMorning with dissolve #time:2
show s flirt at pos50s with dissolve
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) #loop:true
"We walked together through the forest, hand in hand."
"Talking about things we'd do after we got off this island... talking about everything and anything."
stop sound
show s happy
s "After we're off this island, whatever happens... do you maybe... want to catch a movie together?"
m "Sure, but why a movie?"
show s laugh
s "You can laugh, but there's a part of me that just wants to be a regular girl for a day. That's something I could never forget."
show s flirt
s "And I'd like it if I could be that way, with you."
show s happy
s "What do you say?"
m "I'd like that."
show s flirt
s "Yay!"
"Scarlett did a little dance of happiness."
show s happy
"We spent the rest of the morning together in the woods, enjoying each other's company... and maybe a little more than that."
"Somehow, in the middle of it all, I forgot what kind of show I was on in the first place. It was just me and her."
"In this moment, more than ever, I was glad to be alive."
jump postMorningSelector
