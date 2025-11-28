label P2Ending:

stop sound
show bg Black
hide a
hide s
hide t
hide v
hide y
hide k
hide d
hide b1
hide b2
hide b3
hide b4
hide b5
with dissolve
window hide dissolve
$ renpy.pause(delay = 3.0, hard = True)

show bg Lab with dissolve
stop sound
$ renpy.sound.play("audio/sfx/dark_empty_loop.wav", loop=True)
play music Smile
"...?"
"I woke up on an operating table - the kind you'd see in a nightmare."
"My first instinct was to get up and get off it as fast as possible, but my neck, hands, and legs were cuffed and pinned down in thick metal braces."
with vpunch
"I tried to force myself out with all my strength, but the braces didn't so much as budge."
show k neutral at pos50k with dissolve
k "'Morning, [name]."
m "W-what's going on, Kat?"
m "Get me out of here!!"
show k sad
k "I'm afraid I can't do that."
show k serious
k "...And honestly, I'm getting tired of explaining why."
show k sad
k "Let's just speed this along, shall we?"
m "W-what are you talking about?"
show k serious
"She placed some kind of helmet on my head. I tried to avoid it, but the brace around my neck made it impossible to maneuver."
m "Please, Kat. Don't do this."
play sound Engine
"I could hear the hum of a massive generator turning on behind me."
$ renpy.sound.play("audio/sfx/dark_empty_loop.wav", loop=True)
"She raised her hand, revealing a trigger switch, with a single red button."
show k sad
k "See you soon, [name]."
"She pressed it -"
show bg Black #with dissolve

hide k #with dissolve
play sound Glitch1

#;; EDIT THIS TO REMOVE STAGE REFERENCES.... stage flashbacks were removed

"{glitch=50}{b}The curtain closes.{/b}{/glitch}"
"...You're taking your bow."
"And when you lift your head..."
"...I can see you clearly, for the first time."
"It's you."
"The one I'd been waiting all this time to see."
"The one who made me dream of a life together, far from this island."
"You've been right by me all this time."

show bg Library with dissolve
show k flirt at pos50k with dissolve
k "Tomorrow's the day, [name]."
show k laugh
k "You nervous?"
m "Who wouldn't be?"
show k neutral
k "You've got a point."
show k sad
"She reached for my hand and held it tightly."
m "You okay?"
show k worried
k "...You sure we should be doing this?"
show k sad
k "I... I don't want you to be punished just because I want to get out of here."
m "Hey. Kat."
show k neutral
m "...We've always been a team. You and me."
m "No matter what, we're in this together."
show k blush
k "...Thanks, [name]."
show bg Black #with dissolve
hide k #with dissolve
play sound Glitch2

show bg BeachNight #with dissolve
"{glitch=50}{b}How did things come to this?{/b}{/glitch}"
"The escape failed."
"I've been surrounded, beaten, shot... betrayed."
"The love of my life... she shot me."
"I'm bleeding out rapidly. I try my best to slow the bleeding, but it's no use."
m "What... did you do to her?"
"I choke out every last word."
show d laugh at pos30d with dissolve
d "I didn't do anything."
d "You were too busy making heart eyes at Kat here to see where her true loyalties lied."
show k flirt at pos70k with dissolve
k "...I'm sorry, [name], but it's true."
m "I... I don't understand."
show d neutral
d "Why don't you tell him, dear?"
show k neutral
k "...Damian is my father."
show k serious
k "I knew you were planning something, the moment you came to this island."
show k bored
k "But you didn't trust me enough to tell me what exactly it was."
show k neutral
k "So I became close to you, and told you just what you wanted to hear."
show k laugh
k "...And then you told me everything I needed to know."
show k flirt
k "As soon as you told me your plan, there was no way you were ever going to escape from this island."
m "Why... are you saying this?"
d "Now that's my girl. You really are my daughter."
m "Why...?"
d "I love that look on your face, [name]!"
d "You know... you've got an expression that would be perfect for my next show."
d "And it just so happens... we've got an opening just for you."
"It's no use... I've lost too much blood."
show bg Black with dissolve
hide d with dissolve
hide k with dissolve
#hideChars
"The world turned dark."
"This... is the end."
d "...Keep him alive."
d "[name]."
d "You might think I'm showing you mercy. But believe me, by the end of this..."
d "...You're going to wish that I just let Kat kill you."
"..."
#The curtains close."
"Why?"
"Why, Kat...?"
"Why would you...?"
"I barely have time to breathe before the waves pull me under once more."
jump P3Intro
