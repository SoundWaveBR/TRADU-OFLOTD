label P2Day4postDate:

$ currentDay=5
$ P2Date4=selectedDate

if P2Date4 == "Allie":
    $ selectedAffection = allieAffection
if P2Date4 == "Scarlett":
    $ selectedAffection = scarlettAffection
if P2Date4 == "Terra":
    $ selectedAffection = terraAffection
if P2Date4 == "Violet":
    $ selectedAffection = violetAffection
if P2Date4 == "Yui":
    $ selectedAffection = yuiAffection

#; 1st rank 2 date
play music PastSadness
show bg RoomNight with dissolve # time:1
"I was feeling a bit restless after today's date to wait in my room, so I went downstairs to relax."
show bg MansionIndoorsNight with dissolve# time:1
show k laugh at pos50k with dissolve
"...Looks like someone had the same idea I did."
"Kat was relaxing on the sofa, with a bottle of red wine in hand."
show k flirt

menu:
    k "Hey there, [name]. Care for a glass or five?"
    "Sure!":
        jump p2d4pd_sure
    "No thanks":
        jump p2d4pd_nty

label p2d4pd_sure:
m "Sure! I'd love a glass."
show k laugh
k "Now that's what I'm talking about!"
"She handed me a glass and poured until it was full."
m "Woah! Maybe a little too much."
show k happy
k "What's life without a few risks?"
m "Long."
show k flirt
k "Much like your remaining lifespan..."
"Kat filled her glass to the brim, and downed it in one go."
jump p2d4pd_AfterDrink

label p2d4pd_nty:
m "That's okay. I don't want to wake up with a hangover."
show k surprised
k "You're on a killer dating show, and you're worried about a hangover?"
show k laugh
k "Man, I want whatever you're drinking."
"Kat filled her glass to the brim, then downed it in one go."
show k bored
k "...Nope, still not feeling like a hangover is worth worrying about here."
jump p2d4pd_AfterDrink

label p2d4pd_AfterDrink:
show k laugh
"She laughed and lightly jabbed me."
"I felt like I was finally getting to see her real smile."
show k flirt
"Kat started chugging down the bottle."
m "Uh..."
show k laugh
k "Aaaaaaaah..."
m "You okay?"
show k angry with vpunch
k "I work on a TV show that kills innocent people for shits and giggles, how okay do you think I could be?"
m "You... might want to stop drinking that."
show k bored
k "You're more of a buzzkill than Damian, and I don't even know how that's possible. He's killed people with buzzsaws!"
show k sad
k "...Sorry, [name]. I didn't mean that."
m "It's okay, Kat. No worries."
m "Now that you mention it, how did you end up working here anyway?"
show k laugh
k "Oh you know, the ol' career fair down the block..."
"She laid down on the sofa."
show k neutral
k "...If you're here for the daily interview where I ask you about your day, I already have enough footage for today."
m "As strange as it might sound, Kat... I'm here because I'm worried about you."
show k surprised
k "...And why's that?"
m "People who chug a whole bottle of wine in one night usually aren't in the best place."
show k laugh
k "Worry about yourself, [name]."
show k sad
k "If you knew some of the things I'd done to survive, you wouldn't be trying to comfort me."
m "...From what it sounds like, no one really has any choice."
#show k laugh
#k: That's just not true!"
#show k serious
#k: ...I've made choice after choice to survive, no matter how bleak it gets.."
#show k neutral
#k: We all have choices to make."
#show k sad
#k: ...Most of us are just too afraid to make them... and other people take the bullet for it."
show k neutral
k "...You just focus on being a ratings magnet on your dates. I'll be fine."
show k happy
k "...Thanks, [name]."
show k neutral
k "If you don't mind... I'd like to be alone."
m "Good night, Kat."
m "Don't stay up too late."
show k laugh
k "Great, the walking corpse is giving me advice on how to live now."
show k worried
k "Do I really look that bad right now?"
m "...Good night, Kat."
"I hurried along."
show k angry
k "Now hold on just a-"
hide k with dissolve
show bg RoomNight with dissolve# time:2
"...If only I could escape this island as easily as I could from a very, very drunk Kat."
show bg Black with dissolve
"...Wait a minute."
"If Kat's drunk, then who's making sure today's episode is good?"
"..."
"Something tells me I'm not going to sleep very well tonight."

stop music
play music LoveTheme
#; Yui Flashback
"..."
"The two of us were lying down in a grassy field, watching the world pass us by."
m "Where would you want to go, when we're out of here?"
q "...The countryside."
q "Seems like it'd be the only place nowadays that you can get some peace and quiet."
m "That does sound nice."
#;???: Besides, it'd be the farthest place from here."
q "...Would you come with me?"
q "I know it's not for everybody, and it's missing a lot of the..."
m "You don't even have to ask, love."
m "Of course I'm coming with you."
m "We're a team, right?"
q "...We're a team."
"She moved closer. I held her tight in my arms."
q "...Mom would have loved you."
q "I wish you would have had a chance to meet her."
m "...I know."
m "We'll make sure our kid gets a chance to meet theirs, though!"
"Her face turned bright red."
q "W-W-W-"
q "W-W-W-What-"
m "?"
q "S-S-Say that after we're actually e-engaged!"
"It's cute how embarrassed she gets."
q "...You mean it?"
m "Every word."
q "...You're sweet."
m "Not as sweet as you."
jump MorningSelector
