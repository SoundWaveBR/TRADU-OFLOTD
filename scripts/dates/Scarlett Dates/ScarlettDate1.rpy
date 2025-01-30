label ScarlettDate1:

$ scarlettAffection=1

#; Scarlett seems like the sexy whatever person on the outside
#; but on the inside, she's really just a girl who's looking for love."
#; maybe she's super awkward the first time, so she tries to make up for it by being cool the second time."
show bg RoomMorning with dissolve
play music MasterDisorder
"It didn't take long to find Scarlett. She found me first."
play sound DoorOpen
"She had just burst through my door, and was trying to catch her breath as she slammed it shut behind her."
play sound DoorClose
show s worried at pos50s with dissolve
s "[name]! Thank god you're okay, oh my god."
m "What's going on, Scarlett?"
show s sad
s "Long story short, I experimented with some of the local fauna on the island earlier, there's really nothing like it, it's really incredible, and ugh I messed up my intro with you earlier, and -"
m "Woah! Slow down."
show s worried
s "*sigh*"
show s laugh
s "...I made a new chemical compound that causes amnesia! It's amazing!"
m "Wow! That's not something you hear every day."
show s happy
s "The cool thing is, applying just the right amount to a person can make them forget specific things - who they are, how to write, anything."
show s worried
s "The bad thing is..."
stop music
play sound Hit
play music RavingEnergy
with vpunch
"Something slammed into the door outside. I almost jumped up from the surprise."
b4 "Gimme brains!!!!! And bananas!!!"
show s serious
s "...Applying too much turns people to rabid monkey zombies, hell-bent on eating human brains."
show s worried
s "...And bananas."
m "Dear god, not the bananas..."
with vpunch
play sound Hit
"The door slammed again. It sounded like it was about to be knocked down."
show s angry
s "We need to get out of here, and fast!"
show b4 angry at pos30b
show s surprised at pos70s
with dissolve
play sound Hit
with vpunch
"Four busted through the door, and blocked our only exit."
b4 "GIMME BRAINS! AND BANANAS!"
m "I'll get him out of the way! It'll give you time to run!"
show s serious
s "I've got a better idea."
stop music
play music RunAmok
play sound AnimeShine
show s happy
with vpunch
"Scarlett blasted Four with a white powder, covering his face entirely."
hide b4 # with dissolve
play sound Hit

"He flailed wildly for a few seconds, then fell to the ground, unconscious."

menu:
    "What was that!?":
        jump sd1_c1
    "Is he going to be okay?":
        jump sd1_c2

label sd1_c1:
m "Woah, what was that?"
show s laugh  at pos50s with dissolve
s "Uh, let's just say Four's seeing all the bananas he wants now, and we'll leave it at that. Follow me!"

jump after_cd1_choice

label sd1_c2:
m "Woah, is he gonna be... okay?"
show s laugh  at pos50s with dissolve
s "...I guess we'll find out!"
show s worried
s "For now, let's focus on getting out of here!"

label after_cd1_choice:

show bg MansionMorning with dissolve
stop music
play music Sincerely
"We ran outside of the mansion as fast as we could."
m "How did this even happen?"
show s worried
s "Ooh, I was afraid you'd ask that."
show s sad
s "...I heard from Terra that you lost your memories, and I... I wanted to see if I could help you get them back."
show s laugh
s "So I, uh... may have experimented on the Brothers Five... to see if I could erase their memories... and bring them back."
show s surprised
s "I must have done the numbers wrong - I added way too much, I didn't realize their brains were so empty in the first place!"
show s happy
m "In a weird way... that's really sweet, Scarlett. Thanks. Crazy, but still, thanks."
show s neutral
s "I'll fix this, I swear. I just need time to make an antidote."
show s happy
s "Luckily, I left my tools and supplies pretty near here. We can stay there till we've got an antidote."
m "Sounds like a plan. Lead the way!"
m "Wait... where are the other girls? Do you think they're still inside?"
show s worried
s "...They're... actually trapped inside the library right now."
m "Oh shit! We've got to go back and save them!"
show s sad
s "Um... I don't know how to say this, but..."
show s laugh
s "I accidentally turned them to zombies too, hahaha..."
show s worried
s "But they were a little bit much so I locked them in the library, ha... ha... ha...?"
"...We're doomed, aren't we."
show s happy
"Scarlett and I passed the time talking about the craziness that was going on, and coming up with a plan to save everybody."
"She seemed to be quite frazzled, despite seeming so put together - but I could tell she really did care about the infected."
"...Not enough to prevent this from happening in the first place, but enough."
"I watched her build a machine that she insists can turn them back to normal, but..."
"...Looking at it, I can't help but be a little skeptical."
show bg MansionEvening with dissolve
show s happy
stop music
play music RavingEnergy
s "Alright, it's showtime."
m "You really think this will work?"
show s laugh
s "You bet! I made it, after all!"
show bg MansionIndoorsNight with dissolve# time:1
"Looks like the coast is clear here..."
"We walked to the outside of the library undetected, but we definitely weren't alone in here."
show s serious
s "Alright! It's time to save our friends!"
hide s with dissolve
play sound DoorOpen
show bg Library with dissolve # time:2
show y angry at pos80y
show a angry at pos20a
show t angry at pos40t
show v angry at pos60v

with dissolve
all "Braiiiiins!!!!"
with vpunch
m "They're coming right at us!!"
s "Nothing to worry about."
hide s
hide a
hide t
hide v
hide y
with dissolve
stop music
play music RunAmok
show bg ScarlettShooting with dissolve # time:2
#play ambient Minigun # loop:true
$ renpy.sound.play("audio/sfx/minigun.mp3", loop=True)
s "This is payback for you guys acing your introductions!!"
m "I'm sorry... what?"
s "Oh, uh... nothing."
m "...You sure that's gonna cure them?"
s "Of course, what does it look like I'm doing?"
m "..."
"Something told me Scarlett was enjoying this a little too much..."
k "Uh... what the hell? I take my eyes off the cameras for one second, and... there's zombies in the house."
s "Not for much longer, promise!!"
"We spent the rest of the day administering the antidote to each person. Each of them knocked out as soon as we delivered the cure."
#I was exhausted by the time night rolled around."
show bg MansionEvening with dissolve
stop music
stop sound #@stopsfx Minigun
play music Sincerely
show s happy at pos50s with dissolve
s "Not quite the first date you expected, huh?"
m "You can say that again."
m "It was... definitely a first though."
show s laugh
s "Kat told me that to make a date exciting, I had to get your heart racing."
show s happy
s "I think I did a pretty good job at that!"
"...I guess that's technically true, but aren't there easier ways?"
"Something tells me this woman is full of more surprises."
$ scarlettAffection=1
jump postDateSelector
