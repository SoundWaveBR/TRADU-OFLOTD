
label AllieDate2:

show bg BeachMorning with dissolve
play music CarpeDiem
$ allieAffection=2

show a sassy at pos50a with dissolve
a "Howdy, [name]. You ready for round 2?"
show a laugh
a "I figured you might want to hang out somewhere where rollerblades don't work!"
m "Aw, I spent all night dreaming of the next chance I could use those two little death machines."
show a happy
a "Then I think you'll love what we've got in store today! There's no wheels where we're going."
m "What do you mean?"
show a neutral
a "You'll see. Follow me!"
show a surprised
a "Ah, first I'm gonna need you to close your eyes."
m "...I'm not sure I like where this is going."
show a laugh
a "Nothing to worry about, [name]. I'll be right next to you the whole time."
m "Because that's always gone well."
show a happy
a "Hasn't it?"
hide a with dissolve
show bg Black with dissolve
"Allie moved behind me and covered my eyes with her hands."
a "Now let's just keep walking forward. Trust me!"
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) # loop:true volume:0.6
m "Right..."
"I'd be lying if I said I wasn't somewhat enjoying this. My heart skipped a beat when she wrapped her arms around me."
"I cautiously took step after step forward."
stop sound
play sound Waves # loop:true volume:75
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)

"First, I felt dirt... then sand... then... water?"
m "Are you trying to make me drown myself?"
a "Of course not! Though, I have to admit, this does look a lot like how they killed people back in the day."
m "..."
a "Ah, you're gonna want to take a really high step forward next, or it's gonna hurt."
play sound MetalImpact
"I raised my right leg as high as I could, then stepped forward. Something clanged, like metal."
play sound MetalImpact
"Next, I brought over my left leg."
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)
a "Keep your eyes closed for just a second longer! I just gotta do one thing."
"Allie let go of me, and took a few steps forward."
a "Brace yourself!"
play sound Engine # loop:true
#; SOUND OF THE ENGINE
m "Wait, what's -"
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)

stop music
hide a with dissolve
show bg AllieBoat with dissolve
play music AlmostBliss
"I was knocked off my feet by the sudden movement, and opened my eyes on reflex."
"Water sprayed onto my body as I struggled to regain my balance."
#show a happy
a "All aboard the S.S. St. Allie!"
m "...When and where did you get a boat?"
#show a laugh
a "Pretty cool, right? I found this baby in the back of the mansion this morning."
m "You just 'found' it?"
#show a neutral
a "...Anyway, I asked Kat if I could take it for a spin."
#show a happy
a "She said that as long as we stay within a few clicks of the island, we're good, or the engine will automatically shut off."
#show a laugh


menu:
    a "So I thought, why not have a little joyride around the island?"

    "I like the sound of that":
        jump allieDatec1
    "What could go wrong?":
        jump allieDatec2

label allieDatec1:
m "I like the sound of that."
#show a happy
a "And away... we go!"
jump ad1_post_choice

label allieDatec2:
m "What could go wrong?"
#show a laugh
a "There's no fun in thinking that, is there?"
#show a happy
a "So why bother!"
"Why indeed, thought the person stuck on a life or death dating show."
jump ad1_post_choice

label ad1_post_choice:

"We cruised around the island for a while, taking note of the different buildings covering the island."
"The mansion seemed so small from way out here."
"Hours flew by as we cruised around."
show bg BeachEvening with dissolve
show a serious at pos50a with dissolve
stop music
play music TouchingMomentsOne
"Allie took a deep breath and sighed."
m "You okay, Allie? You don't seem as chipper as usual."
#show a laugh
show a sad
a "...I guess I'm a little homesick."
show a surprised
a "It's nothing to do with you, promise! I just..."
show a worried
a "I'm just worried about my old man."
m "I'm sorry, wasn't your father...?"
show a serious
a "Ah, yeah, he's long gone. You know the old story about New Asia."
show a neutral
a "I'm talking about Bill. He was a good friend of my Dad's, and he's taken care of me and a whole lot of other kids."
m "Sounds like a cool dude."
show a laugh
a "You sure have a way with words, don't you, [name]?"
show a neutral
a "I don't dwell much on the past. It just slows you down."
m "I couldn't agree more."
show a laugh
a "Is that the amnesia talking?"
m "Who knows?"
"She laughed as she put her hand tenderly against my cheek."
show a happy
a "I'm more worried that he'll get himself into trouble if I'm not around to keep him in check."
m "What's he like?"
show a worried
a "Let's just say that a lot of how I act, is from him, but... I'm much more restrained."
show a surprised
m "If you're like this, I guess I wouldn't survive even a single day hanging out with him."
show a angry
a "Hey! What's that supposed to mean?"
m "Oh, nothing at all."
show a laugh
with vpunch
"Allie made a sharp turn. The sudden force almost threw me out of the boat."
m "Hey! What was that for?"
show a happy
a "Oh, nothing at all."
"I couldn't help but smile at her. She was practically shining when she had that devilish grin."
show a neutral
m "I'm sure he's doing just fine, Allie."
m "He's probably watching right now, just to make sure you're safe."
show a surprised
a "You're probably right, now that I think about it."
show a neutral
a "He always wastes the day watching shitty reality TV shows."
show a laugh
a "Which gives me an idea..."
m "What's that?"
stop music
play music CarpeDiem
show a blush
"With one hand on the wheel, Allie turned to me, and kissed me on the lips."
"I kissed her back. It felt like lightning was running through my veins."
with vpunch
"The boat started to rock back and forth more and more uncontrollably, but we didn't stop."
show a laugh
a "That's got to give Bill a heart attack!"
show a angry
a "Seriously! What kind of father lets their daughter go on a trashy show like this?"
"I couldn't help but laugh."
show a sassy
a "Eh, whatever. It's been a fun ride so far."
show a laugh
a "And here's to the next one with you, [name]!"
"She kissed me again, sending the boat into an erratic frenzy."
"We spent the rest of the day together cruising around on the boat, till we ran out of daylight."
stop sound
jump postDateSelector
