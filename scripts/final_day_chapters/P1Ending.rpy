label P1Ending:

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
#play sound DarkAndEmpty
play music Smile
"I woke up on an operating table - the kind you'd see in a nightmare."
"Blood splattered on the floor and the walls. The smell of disinfectant and rotting flesh."
"There was a nearby table littered with metal instruments that could make anybody talk."
" My first instinct was to get up and get off it as fast as possible, but my neck, hands, and legs were cuffed and pinned down in thick metal braces."
with vpunch
"I tried to force myself out with all my strength, but the braces didn't so much as budge."
m "Hello!?"
m "What's going on!?"
m "Where am I!!??"

if selectedDate == "Allie":
    m "...Allie!? You there?"
elif selectedDate == "Scarlett":
    m "...Scarlett!? You there?"
elif selectedDate == "Terra":
    m "...Terra!? You there?"
elif selectedDate == "Violet":
    m "...Violet!? You there?"
elif selectedDate == "Yui":
    m "...Yui!? You there?"

# OLD UNTRANS
#m "...[#selectedDate]!? You there?"
"...All I heard back were echoes of my own screams. Wherever I was, this place must be massive."
show k neutral at pos50k with dissolve
k "...Hey, [name]."
"Kat was holding some kind of helmet, with thick wires extruding from the back of it."
show k serious

if selectedDate == "Allie":
    k "Don't worry. Allie is doing fine. She's just... taking a little nap."
    m "Kat! What's going on?"
    m "You've got to help me, I was just on my date with Allie, when everything went dark, and these guys fucking kidnapped us, and -"
elif selectedDate == "Scarlett":
    k "Don't worry. Scarlett is doing fine. She's just... taking a little nap."
    m "Kat! What's going on?"
    m "You've got to help me, I was just on my date with Scarlett, when everything went dark, and these guys fucking kidnapped us, and -"
elif selectedDate == "Terra":
    k "Don't worry. Terra is doing fine. She's just... taking a little nap."
    m "Kat! What's going on?"
    m "You've got to help me, I was just on my date with Terra, when everything went dark, and these guys fucking kidnapped us, and -"
elif selectedDate == "Violet":
    k "Don't worry. Violet is doing fine. She's just... taking a little nap."
    m "Kat! What's going on?"
    m "You've got to help me, I was just on my date with Violet, when everything went dark, and these guys fucking kidnapped us, and -"
elif selectedDate == "Yui":
    k "Don't worry. Yui is doing fine. She's just... taking a little nap."
    m "Kat! What's going on?"
    m "You've got to help me, I was just on my date with Yui, when everything went dark, and these guys fucking kidnapped us, and -"



# OLD UNTRANS
#k "Don't worry. [#selectedDate] is doing fine. She's just... taking a little nap."
#m "Kat! What's going on?"
#m "You've got to help me, I was just on my date with [#selectedDate], when everything went dark, and these guys fucking kidnapped us, and -"
show k sad
k "...I know, [name]. I know."
"She sighed."
show k serious
k "You did good... but not good enough. That's pretty much it."
show k happy
k "...Would it make you feel better to hear that you're the best one yet?"
m "I don't care, get me out of here!"
show k sad
k "...At this point, there's no point explaining."
show k serious
"She placed the helmet on my head carefully. Even if I wanted to stop her from doing so, the brace around my neck made it impossible to maneuver."
m "Please, Kat. Don't do this."
play sound Engine
"I could hear the hum of a massive generator turning on behind me."
"She raised her hand, revealing a trigger switch, with a single red button."
m "I just want to get out of here. I want to get back to my life, whatever it is. Please."
show k serious
k "...Not today, [name]."
show bg Black with dissolve
"She pressed it -"
hide k with dissolve
play sound Glitch1
"{glitch=50}{b}The sound of crashing waves. A world without time or color.{/b}{/glitch}"
"...I'm back."
"This time, it's as if I'm sitting in an audience, watching myself from afar."
"The escape had failed. I'd been separated from her and captured."
"We really never had a chance, did we."
"I find myself praying that she's safe - if anything happened to her-"
"For a moment, the world exploded with color."
#show bg KatShootingYou1
#; KAT NEEDS TO SHOOT YOU HERE."
show bg KatControl with dissolve
k "Always the hero, aren't you, [name]?"
m "What did you do to her!?"
k "...You should be more worried about yourself."
k "You knew the rules. If you try to escape the island, you die."
k "It didn't have to be like this, but you..."
k "I'm done talking."
k "Goodbye, [name]."
show bg Black with dissolve
stop music
play sound Gunshot
play music SmileEnding
play sound Glitch1
show bg BeachNight #with dissolve
show d laugh at pos50d #with dissolve
d "{glitch=50}{b}Oh, will you look at that! Looks like our little hero's got some life left in him.{/b}{/glitch}"
show d happy
d "You know, [name]... you're in luck."

play sound Glitch2
show d neutral
d "{glitch=50}{b}Usually, I'd just kill you for this. But a new opportunity's just opened up, and I think...{/b}{/glitch}"
stop sound
play sound Glitch1
show d evil_smile
d "{glitch=50}{b}...You'd be the perfect fit.{/b}{/glitch}"
hide d #with dissolve
show bg Black #with dissolve
play sound Shutdown
"..."
q "Hey, don't just lie there."
q "...Just 5 more minutes..."
with vpunch
q "You're the star of the show! You can't just sleep through it!"
m "Watch me... Zzzzz..."
q "Oh, that's how you want to play?"
q "It's ON."
play sound Hit
m "OWW!!!!"
show bg PlaneBar with dissolve
show k happy at pos50k with dissolve
k "Rise and shine, sleepyhead."
m "Ow ow ow... Did you just hit me?"
show k surprised
k "What? Me? Never in a million years."
show k neutral
k "Anyway... what was your name again?"
m "Oh, my name's..."
with vpunch
m "...I can't remember my name!"
show k surprised
k "Really now? You've got to be joking."
m "I'm dead serious. I can't remember a thing."
show k laugh
k "Who knows, it might be for the better!"
show k happy
k "Luckily we've got your name on file, [name]."
#stop music fade:5
show k neutral
k "My name's Kat. It's nice to meet you!"
show k flirt
k "You're the star of our new show, {i}Find Love or Die Trying{/i}. Let me get you up to speed..."
stop music #fade:1

show bg Black
hide k
with dissolve
#window hide dissolve
$ renpy.pause(delay = 1.0, hard = True)


jump P2Intro
