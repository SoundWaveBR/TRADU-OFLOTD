label YuiDate2:

show bg Hills with dissolve
play music Meadow
$ yuiAffection=2

"I could see Yui waving at me from the top of the hill."
show y happy at pos50y with dissolve
y "Hey there, [name]! It's nice to see you again!"
m "It's nice to see you too, Yui!"
m "You wanted to show me something?"
"Now that I was closer, I could see Yui was holding one hand behind her back."
show y laugh
y "Believe me, it's the most amazing thing you've ever seen."
show y angry
y "Behold!!!!"

hide y with dissolve
stop music
play music LoveTheme
show bg YuiHoldingBunny with dissolve

y "It's a bunny!!!"
"It was indeed a bunny."
m "Where did this little guy come from?"
#show y surprised
y "To be honest, I've got no idea."
m "I wonder if he's a wild one, or maybe somebody's pet."
#show y worried
y "I've asked around, but it doesn't look like he belongs to anybody."
#show y neutral
y "So, I... I've been taking care of him since I've found him."
#show y laugh
y "I just couldn't help myself, y'know?"
"Yui's smile was as earnest as could be."
m "Didn't you have a pet bunny back home?"
#show y happy
y "I had two! Bun and Bunbun!"
#show y surprised
y "Both of them are total rascals. But Bunbunbun here is a good boy, aren't you?"
"She nuzzled against Bunbunbun's head."
#show y happy
y "Yes, you are ~
Nuzzle, nuzzle."
"We played with the bunny for a little while."
"She picked the bunny up and held it in her arms. Bunbunbun looked quite content."
m "You know, you're pretty amazing with animals, Yui."
show bg Hills with dissolve
show y laugh at pos50y with dissolve
y "Well, I've been surrounded by animals my whole life!"
show y neutral
y "Back at my house, well... to be honest, it was more of a barn than anything."
show y happy
y "Since my sisters were too young, and grandma was getting up there, I'd take care of all the animals."
show y neutral
y "Grandma's taken care of them ever since they were born."
show y sad
y "My parents were supposed to take care of them after grandma retired, but..."
show y happy
y "Well, you know... life happens. I'm just glad to have what I have."
show y surprised
y "Ah!"
"Bunbunbun had managed to squeeze out of her hands, and ran off."
show y angry
y "We gotta catch him! Let's go!"
m "On it!"
"I ran as fast as I could after Bunbunbun, but it was no use - the distance kept widening."
"Before long, we couldn't even see him anymore."
show y worried
m "Sorry, I couldn't catch him... he's really fast, for something so small."
show y happy
y "Ah, don't worry about it! Bunbunbun likes to do this all the time. He's a bit mischevious, but he won't do anything dangerous."
show y laugh
y "We can take our time looking for him."
show y neutral
y "If you're willing to help!"
m "Of course, Yui!"
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) #loop:true
"We started walking towards where we last saw Bunbunbun, right after we caught our breath again."
show y happy
y "Gosh... isn't it so nice to be outside? The smell of fresh air, the breeze?"
show y laugh
y "There's nothing like it!"
m "There really isn't!"
"I smiled."
show y happy
stop sound
y "At first, I was really excited to go to the city."
show y neutral
y "There's so many people, so many things to do, so many beautiful things..."
show y happy
y "...And most of all, I got to meet you!"
m "Shucks, you're going to make me blush."
show y laugh
"She laughed and touched my arm."
show y neutral
y "Even so, the city's just not my thing."
show y sad
y "...It's a little bit funny. Though the reason I had to come home all of a sudden was terrible, I... a little part of me was glad to be home."
show y neutral
y "Ever had that kind of feeling before?"
m "I have. It's strange, but sometimes, there's good in the bad - and sometimes, that good can outweigh the bad."
show y laugh
y "Exactly. You get it, [name]."
show y happy
y "My family's never been closer."
show y laugh
y "And that's all I want."
show y neutral
y "They told me to make a lot of money in the city... make something of myself, all that."
show y worried
y "It might seem... old-fashioned, but I just want to put the people I love first."
show y happy
y "That's all ya got in life, really!"
show y neutral
#y "I'm curious... what do you put first in life?"

menu:
    y "I'm curious... what do you put first in life?"

    "Family":
        jump Family
    "Career":
        jump Career
    "Happiness":
        jump Happiness

label Family:
m "That'd have to be family, no doubt."
jump AfterValue

label Career:
m "That'd have to be my career."
jump AfterValue

label Happiness:
m "Happiness. If you don't have that, what do you have?"
jump AfterValue

label AfterValue:

show y happy
y "Oh, is that so!"
show y laugh
y "I think we'd make a great team, then."
"We talked for several hours about what we wanted out of life. We seemed to match up perfectly. I was beaming the whole time."
"It was hard to believe that -"
show y surprised
stop sound # stopsfx
y "It's Bunbunbun!!"
"Yui pointed in front of us, and sure enough, there was Bunbunbun, chomping on a bush."
show y angry at pos95y #used to be 100
play sound Whoosh
"I'd never seen anyone move so fast - Yui descended on Bunbunbun like a hawk, and grabbed him in an instant."
show y annoyed  at pos50y with easeinright
y "You are going back to your den, you bad little bunny!"
show y happy
y "But I'm happy you're safe."
"She nuzzled her face against his fur. Bunbunbun was practically purring with delight."
show y blush
"Then she looked right at me."
show y happy
y "I can't promise I could give you the most exciting life, with the most twists and turns around every corner..."
show y neutral
y "But I can promise, that if you chose me, I'd always be by your side. No matter what."
show y blush
y "Wherever you were... I'd come running, always."
"She took a step towards me and kissed my cheek."
"We locked eyes, and for that time, all I could see was her, and how beautiful she was."
show y happy
"Bunbunbun seemed to be a little jealous after that."
show y laugh
y "Thanks again for the help, [name]. Being with you made this all go a lot faster... and made it really special to me."
m "Anytime, Yui. I'm happy to."
"We walked back together to the mansion, holding hands and smiling all the while."
jump postDateSelector
