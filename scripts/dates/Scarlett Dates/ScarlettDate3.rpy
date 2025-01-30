label ScarlettDate3:

show bg Library with dissolve
show s neutral at pos50s with dissolve
play music LoveTheme
$ scarlettAffection=3

"I found Scarlett in the same place I met her. She was engrossed in a book, with a pile of books next to her."
"They looked worn, as if they've been read over and over through the years."
m "Hey there, Scarlett. Whatcha reading?"
show s surprised
show s happy
s "Hi, [name]. Just an old fairy tale."
m "Really! I'm surprised you'd read something that would throw science out the window."
show s laugh
s "I'm a woman of varied tastes."
show s tease
s "I quite like these stories, especially this one."
m "Which one are you reading?"
show s neutral
s "It's called {i}The Princess of Avoranda{/i}."
show s tease
s "Really, it's silly, I doubt you'd be interested in..."
m "Try me."
show s happy
"I smiled at her - she smiled back at me in kind."
show s laugh
s "Okay... I don't see why not!"
hide s with dissolve
show bg ScarlettReading with dissolve
#show s neutral
s "There's a young girl, Nera, who was the princess of the kingdom of Avoranda, which was far, far away from civilization."
#show s happy
s "Unlike other princesses before her, she had no time for politicking or parties. She spent all her time building all sorts of gadgets for her family and her friends."
#show s laugh
s "Like a robot dog that would eat the vegetables they didn't want to eat! Ooh, I gotta try my hand at this sometime..."
"Scarlett giggled like a child."
#show s happy
s "Nera has a blissfully happy childhood. She even falls in love - with a commoner named Aloria."
#show s neutral
s "Though her kingdom would never approve of their relationship, Nera and Aloria never fail to see each other in secret. Every night, by the crooked trees in the Western Forests."
#show s worried
s "...But those days don't last. One day, her mother, the queen, is taken by a witch, never to be seen again. And Nera is forced to become queen at the age of 16."
#show s neutral
s "In her mother's absence, Nera does her best to lead the kingdom, and for years, it prospers. She's like no other leader they've had before."
#show s worried
s "But secretly, she wants to leave. As queen, she has no more time for the things, or people, that she loved with all her heart. She cries every night, alone."
#show s sad
s "But she knows she can't. Too much responsibility falls on her."
#show s serious
s "Then one day... Nera is cursed by the same witch that took her mother, and forgets everything. Her name, her family, her kingdom..."
#show s neutral
s "...Everything, except for Aloria, and the desire to leave."
#show s happy
s "And so she leaves, and no one in the village ever sees her again."
show bg Library with dissolve
show s laugh at pos50s with dissolve
#show s laugh
s "...I won't bore you with the rest of the story. But thanks for listening till now."
m "Aw, c'mon! Believe me, Scarlett, I want to hear this to the end."
m "Especially because you like it so much."
"I looked deep in her eyes, and I could tell just how much she loved this story."
show s tease
s "...Well, there's really not much left, but..."
show s happy
s "Well... Nera and Aloria live a wonderful life in a neighbouring kingdom for many years."
show s serious
s "But one day, she remembers everything, and rushes home, worrying for her people."
show s neutral
s "When she gets there, she sees her people have been ruled by the very same witch who took her memory - and that her people no longer prosper the way they did under her rule."
show s serious
s "In anger, Nera confronts the witch, on the border of Avoranda."
show s neutral
s "The witch takes off her cowl, revealing herself to be Nera's mother - the lost queen."
show s worried
s "Nera's mother gives her an ultimatum. She can return to ruling the kingdom, but she can never leave again - or she can leave now, and never come back."
show s happy
s "...And that's where the story ends. You never get to know what choice Nera makes."
m "That's quite the cliffhanger!"
m "I want to know what happens next."
show s laugh
s "Believe me, me too!"
show s neutral

menu:
    s "...I'm curious, what would you do in Nera's shoes?"

    "I'd leave the kingdom":
        jump sd3_c1
    "I'd stay in the kingdom":
        jump sd3_c2

label sd3_c1:
m "...I think I'd leave, and never come back."
show s surprised
s "Interesting. Why's that?"
show s happy
m "There's no point living without love. Even if it was better for the kingdom for Nera to stay, it would guarantee her love could never be realized."
m "And that's... just too sad."
show s tease
s "I think the same way!"
jump sd3_pc

label sd3_c2:
m "...I think I'd stay."
show s surprised
s "...Why's that?"
show s neutral
m "I mean, I can't just let my people suffer like that."
m "...But I would never let Aloria go."
show s happy
m "I'd find a way to make it work."
show s tease
s "...You're a real romantic, aren't you!"

label sd3_pc:

show s happy
s "...I've loved this story, ever since I lost my memories."
show s laugh
s "I'm sure I don't have a kingdom or anything, but sometimes you wonder, you know?"
m "Yeah, I get the same feeling too."
m "That's just life, you know? You just have to keep moving forward."
show s tease
s "...Yeah. You're right."
show s happy
s "I'm... really happy that you're the one I get to move forward with, [name]."
m "Me too, Scarlett. There's no one else I'd rather be with, right here, right now."
m "And speaking of right now... there's somewhere I want to bring you."
show s neutral
s "Where's that?"
show s surprised
m "I'll give you a hint - I've been thinking about this place, ever since you mentioned that you loved fairy tales."
show bg Palace with dissolve
stop music
play music RomanticJazz
show s laugh
s "Oh my gosh. There's turtles down here, turtles!!!"
"She was practically dancing around the room, taking in all the sights."
"It was impossible not to smile."
m "I figured the Ocean Palace just might be your thing."
show s tease with vpunch
"Scarlett practically jumped onto me, and squeezed the life out of me in a deathly bear hug."
show s happy
s "This is wonderful, [name]. Thank you so much!"
show s laugh
s "You've made everything so special, in ways I honestly couldn't believe... but you did it."
show s happy
m "And this is just the beginning, Scarlett."
m "We're in this together."
show s flirt
"I held Scarlett and kissed her on the lips. It was like an explosion of passion had set me on fire, as she kissed me back, and wrapped her arms around me."
s "Always."

if playthrough == 1 and currentDay == 6:
    jump LastDateScarlett
elif playthrough == 2 and currentDay == 9:
    jump LastDateScarlett
else:
    jump NotLastDateScarlett

label LastDateScarlett:
"We looked deep into each other's eyes, then..."
stop music
play music Smile
show bg Black with dissolve
show s surprised
play sound Shutdown
"In a split second, the room became pitch black. I couldn't even see my hand in front of my face, much less Scarlett."
hide s with dissolve
s "[name]? Looks like there's a blackout."
"Scarlett held my hand tight - maybe she was afraid of the dark."

play sound GroupRun

"I didn't have a chance to respond before I heard a rush of footsteps coming towards us in the dark."
"Something isn't right - Oh no."
stop sound #@stopsfx GroupRun
"We were surrounded."
"A familiar voice cut through the short silence of me holding my breath."
q "I'm sorry, [name]. You just... didn't make the cut."
"We've got to get out of here."
q "...Just make it quick, please."
"I could hear the woman that voice belonged to walk away."
"I dashed from the table, pulling Scarlett along with me."
s "W-What's going on, who are -"
m "Just come with me, we've got to get out of -"
play sound Hit
"I didn't even make 5 steps before I was tackled down and cuffed behind my back."
play sound Handcuffs
s "[name]!"
"I screamed for her to run, but they made sure no sound could escape as they pinned me to the ground."
m "Scarlett, you've got to run, get out of here -"
"It was no use. Even though she was just a few feet away - I was powerless to get an inch closer."
play sound Handcuffs
"They tackled her down in a second. I heard the clink of the cuffs as they dragged her away."
"I struggled with everything I had to get up, to save her, to run... for what felt like an eternity."
"Then... nothing."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending


label NotLastDateScarlett:

show s happy
"We spent the rest of the night enjoying a lovely dinner, in a place straight out of a fairy tale, with nothing but love in our hearts, and laughter and smiles on our faces."
show s happy
s "I can't wait to leave this island with you, [name]."
show s laugh
s "I've never been this excited, this happy, since... ever!"
show s happy
s "...You make me feel like I'm living in a fairy tale."
show s tease
s "You know... I've got an idea of how we could spend tonight, if you're interested."
m "And what's that?"
show s flirt
s "I'll show you why fairy tales were written by adults."
show bg Black with dissolve # time:2
#(Display CG here of sexy scene for a few seconds)
#; decided against this route lol."
$ scarlettAffection=3
jump postDateSelector
