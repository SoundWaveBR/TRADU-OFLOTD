label YuiDate3:



show bg RoomMorning with dissolve
$ yuiAffection=3
play music AlmostNew
"I could see Yui from my room's window, walking around the front of the mansion. It looked like she was looking for something."
"I practically jumped down the stairs, then ran outside to see her."
show bg MansionMorning with dissolve
show y happy at pos50y with dissolve
y "Hey there, [name]!"
show y surprised
y "What's the hurry? You look like you're in quite the rush!"
m "I just wanted to see you a little earlier."
show y blush
y "Gosh, that's really sweet of you."
show y happy
y "I've been meaning to see you too, uh..."
show y neutral
y "I've just been doing a lot of thinking since you helped me get Bunbunbun."
m "Ah, How's the big B doing?"
show y surprised
y "Ah, come to think of it! That's why I came out here!"
show y worried
y "He ran out here in a hurry, and I was trying to catch up."
show y laugh
y "Though this has already happened a few times, and each time, he somehow ends up back in my room."
m "I'm sure he's fine, I wouldn't be worried."
show y happy
y "I just can't help myself, you know?"
m "You're a really sweet person, Yui. I love that about you."
show y blush
y "...You are too, [name]."
show y happy
y "Do you have time today to hang out? There's something I'd like to do with you."
m "Of course I do, for you."
show y shy
y "Even if... it's a little boring?"
m "I'm sure it can't be that boring if it's with you, you know?"
m "Whatever it is, I'm down."
show y happy
y "Okay! Here we go!!"
show bg BeachMorning with dissolve
show y neutral
stop music
play music AlmostBliss
"And so we walked together to the beach..."
"...and started fishing, side-by-side."
show y happy
y "Ahhhh... now this is the life."
m "I have to admit, this wasn't what I expected."
show y laugh
y "This was, by far, the best way to pass the time out in the countryside!"
show y shy
y "To be honest, I'm not much for crazy activities, like skydiving, or shopping trips."
show y happy
y "I'd rather just spend my days quietly, with the person I love, talking from dusk till dawn."
show y laugh
y "Just enjoying each other's company, y'know? That's the best."
show y worried
y "Is... is this okay with you?"
m "Of course it is, Yui."
m "Getting the chance to learn more about you, to try the things you like... that's where the real fun is."
m "I'd also much prefer that to doing crazy things all the time, too."
m "Though I do think shopping trips aren't really in the same category as skydiving."
show y laugh
y "They are when you live deep in the country!"
m "Hey, you up for a little contest?"
show y happy
y "Sure! Let's do it! What is it?"
m "Want to see who can catch more fish?"
show y laugh
stop music
play sound AnimeShine
y "..."
play music CarpeDiem
show y angry
y "You're on! Hmph!"
"Apparently I had fanned the flames of Yui's competitive spirit."
"For the next few hours, we kept on at it, while we enjoyed each other's conversation and company."
show y surprised
"Yui was a natural. She was catching fish left and right."
show y neutral
"Each time she caught one, she let it back into the ocean, and each time, I wondered when my first one would bite."
"...I never ended up catching a single one."
show y happy
"But that didn't matter. What did was that we were having a ball."
stop music
play music LoveTheme
show y neutral
y "Thanks for indulging me, [name]."
m "Hey, I had a lot fun too, Yui. Don't worry about it."
show y laugh
y "You don't have to lie."
show y worried
y "I... know I'm not like the other girls."
show y sad
y "I grew up with nothing, and...it shows in how I spend my time, what I wear, everything."
show y neutral
y "...I love you so much, you know?"
show y happy
y "If I had you, I'd give you all the love in my heart, every moment of every day."
show y blush
y "I really would live for love. That's what I've always wanted."
show y sad
y "But I know I could never give you all the things everyone else could. The money, the acclaim, the excitement."
show y worried
y "And I find myself worrying, what if you picked me, and the second we leave this island..."
show y sad
y "...You realize that I can't give you the life you deserve, and you start to hate me."
show y laugh
y "I... don't know what I'd do if it came to that."
show y happy
y "So before it comes to that, I want to ask you."
show y blush
y "...Would just me be enough?"

if playthrough == 1 and currentDay == 6:
    jump LastDateYui
elif playthrough == 2 and currentDay == 9:
    jump LastDateYui
else:
    jump NotLastDateYui

label NotLastDateYui:

menu:
    "Yes":
        jump YuiYes
    "No":
        jump YuiNo

label YuiYes:

$ YuiDate3Good=1
m "Of course you'd be enough, Yui."
show y happy
m "I don't need to be in the spotlight, I don't need to be rich."
show y blush
m "More than all that... I want you, and just you."
show y blush
y "...I've waited so long to hear you say that."
"She pulled me close and kissed me."
show y laugh
y "I love you so much. I always have, and I always will."
show y happy
y "I'll always put our happiness first. I'll make you so happy every day..."
m "I'll do the same, I promise."
show y laugh
y "Pinch me... I must be dreaming."
m "This is as real as it gets, Yui."
m "Here on out, it's just going to be me and you."
show y blush
y "I... I just can't hold myself back anymore, [name]."
"She pushed me onto the warm sand of the beach, and pressed herself against me."
m "Yui..."
"She kissed me once more. Her hands wrapped around me as mine pulled her closer."
hide y with dissolve
y "Let's make up for lost time, [name]..."
"What happened next was imagination come to life."
"I lost all track of time and the outside world - only Yui mattered."
"...And I wouldn't have it any other way."
jump postDateSelector

label YuiNo:

$ YuiDate3Good=0
stop music
play music Smile
"...Though I know how I feel, it doesn't take a rocket scientist to saying this would be a terrible idea for ratings."
"After all, the more girls that are in the running, the higher the ratings are."
m "...Of course you'd be enough, Yui."
show y happy
m "I don't need to be in the spotlight, I don't need to be rich."
show y blush
m "More than all that... I want you, and just you."
show y blush
y "...I've waited so long to hear you say that."
"She pulled me close and kissed me."
show y laugh
y "I love you so much, I always have, and I always will."
show y happy
y "I'll always put our happiness first. I'll make you so happy every day..."
"...I'm sorry, Yui."
m "Here on out... it's just going to be me and you."
show y blush
y "I... I just can't hold myself back anymore, [name]."
"She pushed me onto the warm sand of the beach, and pressed herself against me."
m "Yui..."
"She kissed me once more. Her hands wrapped around me as mine pulled her closer."
"...But my heart isn't in it."
$ yuiAffection=3

jump postDateSelector


label LastDateYui:

show y surprised
stop music
play music Smile
"...My breath was taken away before I had a chance to say what I wanted to."
"I saw something I'd never seen before - and would never see again."
hide y with dissolve
play sound Shutdown
"The sky rapidly turned from bright blue to black, as if it were water being drowned in the darkest ink."
show bg Black with dissolve
"Then the bright sun in the sky... went out, like a candle in the wind."
play sound GroupRun

"The last thing I saw was Yui screaming as shadowy figures grabbed her from behind."
stop sound #@stopsfx GroupRun
"A second later, it was pitch black. I couldn't even see my hands reaching out to try to save her."
"Then I felt somebody grab me from behind. No, not somebody - there must have been several people."
play sound Hit
"They forced me to the ground and cuffed me behind my back."
play sound Handcuffs
"I screamed, but there was no sound."
"I tried to fight, but there was no way out."
"I screamed for Yui, for her to run as far as she could - but I heard no response."
"Then... nothing."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending
