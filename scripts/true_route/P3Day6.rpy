label P3Day6:

window show dissolve
show bg MansionMorning with dissolve
play music CarpeDiem
"Kat was true to her word."
"Instead of having another date on the sixth day of the show..."
"...She planned a huge party for the staff instead. A \"thank you for all your hard work\" party."
"As soon as she told her staff that Violet would be cooking for the event, all of them dropped everything and helped prepare for it."
"While the staff prepared the party grounds during the day, each of us were hard at work, making sure other parts of it went well."

show bg KitchenMorning with dissolve
show v sassy at pos50v with dissolve
"Violet cooked mountains of food as if her life depended on it. In truth, it did."
hide v with dissolve
show bg MansionMorning with dissolve
show y happy at pos50y with dissolve
"Yui was playing games with the staff outside. It didn't take long for her to become a fast favorite for them."
"I'm pretty sure half the staff were playing the games just so they could get her to notice them... and she knew it."
"...I have to admit, I'm really impressed by Yui. Her plan is really coming together."
hide y with dissolve
show bg ProducerRoom with dissolve
show t happy at pos50t with dissolve
"Terra and Scarlett joined forces to make sure all the staff joined the festivities."
"Terra used Kat's producer room to find any stragglers who hadn't joined the festivities."
hide t with dissolve
show bg MansionMorning with dissolve
show s flirt at pos50s with dissolve
"As Terra found them one by one, Scarlett turned on the charm and made sure that they came with her to the party."
hide s with dissolve
show a angry at pos50a with dissolve
#show s laugh at pos40s with easeinleft
"Then when it was time for Scarlett to switch to her other mission, Allie took over - though I'm told she employed more force than charm."
"Meanwhile, I ran around like a chicken with its head cut off, trying to make sure every part of our plan was going smoothly."
"...And for once, it did."
show bg MansionNight with dissolve
show y happy at pos10y with dissolve
show a happy at pos25a with dissolve
show s happy at pos40s with dissolve
show v happy at pos70v with dissolve


show t happy at pos85t with dissolve
show k flirt at pos55k with dissolve

stop music
play music JazzBrunch
"A few hours later, we had every staff member on the island partying their lights out."
show k flirt
k "...Everybody's here?"
show t happy
t "You bet."
show a sassy
a "You should have seen the ones that tried to run!"
show y happy
y "I made sure everyone who came, stayed too!"
show k sassy
k "Perfect. Everybody's eaten?"
show v sassy
v "...As they should have. It is fine food."
show s flirt
s "Looks like it's all going according to plan!"
show s happy
s "I'm just going to ahead and get to the fun part~"
"Scarlett pulled out a remote from her pocket, and pressed a button on it."
play sound Explosion
"A few seconds later, fireworks were shooting into the night sky above the party grounds."
with vpunch
"The cheers of the staff were like thunder."
show y happy
y "...And with that... the plan is going as smoothly as can be!"
show y laugh
y "Great job, team!"
show a happy
a "We owe you one, Yui."
show y happy
y "Right back at you, Allie!"
"We cheered as firework after firework lit up the night sky."
show y surprised
y "Woah! Are fireworks supposed to be this bright?"
"Come to think of it... these fireworks are practically blinding."
show s laugh
s "I have to say, I did a pretty good job with these fireworks!"
show s worried
s "...Though there might be some side effects to watching them from so close. Hmm..."
m "...Let's worry about that later."
"The fireworks were the signal to those trying to escape - that there was nothing left to do except wait."
"...It's going to be a long night."
show s happy
stop music
play music RomanticJazz
s "...I know what we said before, but it'd be such a shame to spend tonight just worrying over what may happen tomorrow."
show s neutral
s "We might live, we might die. Same as any other day."
show s laugh
s "How about instead, we just dance the night away?"
m "...You know what, that sounds great."
show v happy
v "That sounds lovely. let's do it!"
show y laugh
y "Come on! Let's dance like there's no tomorrow!"
show t worried
t "Yuck."
show a happy
a "Don't be like that, Terra! It'd be good for us to blow off some steam."
show t worried
t "Dancing sounds like exercise, and exercise..."
show a laugh at pos90s with easeinright
show t surprised
hide t #with dissolve

"Allie picked up Terra over her shoulder."
show a happy
a "...And away we go!"
hide a with dissolve
show s flirt at pos30s with easeinleft
s "Come on, come on!"
"Scarlett grabbed my hand and pulled me with her to where people were dancing. The others followed close behind."

hide a with dissolve
hide s with dissolve
hide t with dissolve
hide y with dissolve
hide v with dissolve
show k flirt at pos50k with easeinleft
k "They sure are carefree, huh?"
show k sad
k "...Some things never change."
"Maybe we'll get out of here tomorrow."
"Maybe we won't."
"...I hope we do, though."
"I like to think that one day, we'll look back and remember this day."
"It was the most fun night I've ever had - out of the nights that I can remember."
"We lived like there was no tomorrow."
"And now... we'll find out if there is a tomorrow for us."
#hide k with dissolve
#show bg Black with dissolve

stop sound
show bg Black with dissolve
hide k with dissolve
window hide dissolve
$ renpy.pause(delay = 2.0, hard = True)


jump P3Day7
