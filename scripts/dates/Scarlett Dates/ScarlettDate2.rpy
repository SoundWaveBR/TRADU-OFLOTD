label ScarlettDate2:

show bg MansionMorning with dissolve
$ scarlettAffection=2
show s sad at pos50s with dissolve
play music Sincerely
"I found Scarlett out for a stroll outside the mansion."
"She seemed a little down."
m "Hey, Scarlett. You doing okay?"
show s surprised with vpunch
s "A-Ah! Jeez!"
show s worried
s "Ah... It's just you, [name]. You almost gave me a heart attack."
m "Sorry, I didn't mean to."
show s neutral
s "It's, uh, not your fault. I'm just a bit on edge after the whole zombie... date? thing? Whatever it was."
show s worried
s "I guess I'm feeling a little sad about all that."
m "Why? You saved everybody."
show s sad
s "We wouldn't have needed to save anybody if it wasn't for me."

menu:
    "Don't worry about it":
        jump sd2_c1
    "At least you fixed the situation":
        jump sd2_c2


label sd2_c1:
m "We all make mistakes, Scarlett. Don't worry about it anymore."
show s annoyed
s "Most people don't make mistakes that turn everybody into zombies."
m "Well, yes, but hey, it makes for good TV!"
jump after_sd2_c1

label sd2_c2:
m "Hey, at least we don't have banana zombies running around anymore."
m "Without your help, they'd still be running rampant."
show s annoyed
s "Still, they wouldn't have been running around in the first place if it wasn't for me."
m "Well, that's true, but hey, it makes for great TV!"

label after_sd2_c1:
"Which inadvertently, is pretty good for keeping me alive... but I'll keep quiet on that."
m "Besides, you did it because you were trying to help me get my memories back."
show s happy
m "That means more to me than I can say."
show s sad
s "...I'm sorry I couldn't do it."
show s surprised
s "If it's okay with you, I'll try again, and I'm sure this time -"
m "Let's not worry about that for now. Thanks, though. I appreciate it."
show s happy
m "For now, I just want to get to know you better, Scarlett."
show s neutral
m "We got... interrupted, last time. To say the least."
m "Care to join me in making up for some lost time?"
show s happy
s "That would be fantastic!"
show s neutral
s "There's somewhere I'd like to go, if it's okay with you...?"
m "Lead the way!"
show s laugh
s "You won't regret it!"
show s worried
show s neutral
show s worried
show s neutral
s "At least, I think you won't."
m "Should I be worried?"
show s laugh
s "Come on, let's go!"
"She grabbed my hand and pulled me along with her."
"Who could say no to a girl who could turn you to a zombie?"
hide s with dissolve
show bg Black with dissolve # time:3
$ renpy.pause(delay = 2.0, hard = False)
stop music
play music ElectroCabello
show bg ScarlettNightclub with dissolve # time:2
s "Behold!!!"
m "...There's a nightclub in the mansion?"
s "There is now! I made it myself!"
s "Granted, I use it more as a testing ground than a real nightclub, but the staff really wanted something to blow off steam in..."
s "And okay, I cheated a little bit, I made a robot that made the nightclub for me, but it still counts."
m "I think you're probably the first person ever to say something like that."
m "Also, I didn't know you knew how to build robots! That's amazing."
s "Hell yeah, it's cool."
s "I get the feeling that building things to make people happier was what I enjoyed the most before I came here."
m "...What do you mean by that?"
show bg Nightclub with dissolve
show s laugh at pos50s with dissolve
s "You wouldn't believe me if I told you!"
show s surprised
s "Actually... maybe you're the one person who would, maybe it's worth a shot."
"Could she... be like me?"
stop music

play music Bittersweet
show s worried
s "I... there's so much of my life I can't remember, for some reason."
"I couldn't help but raise an eyebrow."
show s sad
s "...There was a lot of broken people after the war in New Asia."
show s serious
s "Not just broken bones and missing limbs... but shattered minds. People trapped in their own heads."
show s neutral
s "... I was told I had a gift for research - a gift that might help those people be able to reclaim their lives."
show s serious
s "So I finished school early, and got my PhD. I led a task force dedicated to helping the survivors."
show s neutral
s "We helped them forget their most painful, most traumatic memories... and move on."
show s laugh
s "It was my life's work, you know! But now..."
show s worried
s "...I can't remember what it was. How it worked, if we even got anywhere with our research."
show s laugh
s "To be completely honest, I can't really remember how I got here either."
m "I'm sorry to ask, but... how on earth did that happen?"
show s sad
s "If I knew before, I definitely don't know now."
show s worried
s "Maybe testing got dangerous, and I wasn't willing to test on someone else."
show s sad
s "Maybe I... I don't know. I don't know."
stop music
play music SmoothLovin
show s laugh
s "The crazy thing is... I went from that... to being on some kind of dating show? What the hell?"
m "I guess it does sound pretty weird."
show s surprised
s "And the idea of getting married in one week? Who wrote this, an idiot?"
"I couldn't help but laugh."
show s happy
s "But... what do I even have to lose at this point?"
m "I wouldn't look at it that way."
m "I can't remember anything either, but... I'm alive."
m "As long as I'm alive - I've got everything to lose, and everything to gain."
show s laugh
s "An optimist, huh. That's... worth something."
show s sad
s "I guess you'd understand, better than anyone."
show s neutral
s "...What do you plan to do after this is all over?"
m "Honestly, I don't know."
m "I want my memories back, but if I can't get them back... I'd just try to make the best of things."
show s tease
s "That's some plan!"
m "I'm still working the details out, give me a break!"
m "At least you remember some things, I couldn't even remember my name at first!"
show s laugh
s "You got me beat there!"
show bg MansionIndoorsNight with dissolve # time:2
"We talked for hours about how we both felt about our situations."
"The good things, the bad things, about forgetting who you are."
"We laughed about forgetting the embarrassing moments that probably plagued others for a lifetime."
"We lamented the moments that truly made life worth living - the moments that made your life unique."
show s neutral
s "...It's nice to have someone that understands."
show s laugh
s "You know, I've got a silly idea, if you're interested."
m "Let's hear it!"
show s happy
s "...Getting engaged in a week is stupid, and a person who'd agree to that is even stupider than that."
show s neutral
s "But I... I think I'd say yes if it were you, [name]. If only to see where life goes with someone like you."
m "That's..."
show s annoyed
s "Shhh, shh, let me finish."
show s happy
s "Regardless of who you ask on the last day, I'd... like to be your friend in the times to come."
show s worried
s "I-If... you'll be mine. I can't remember the last time I had a friend to just... talk to, about how I feel."
show s happy
s "I think this was the first time... that I felt a little better about what happened."
show s laugh
s " I'd want you to feel better about the past too."
show s sad
s "I don't want you to feel alone in this world. It's sad enough, you know?"
show s neutral
s "And maybe I'm just being foolish, but who knows. Maybe if we're still in each other's lives after all this, we'll be able to help each other take back the lives we wanted."
show s laugh
s "What do you say?"
m "I was thinking the same thing, Scarlett."
show s flirt
s "I'm glad. But, uh, how to say...."
show s happy
s "I'd still prefer it if you pick me. What can I say, I'm a bit competitive!"
show s angry
s "On second thought, I'm very competitive!"
show s happy
s "Just saying, but out of all the girls, I'm the best educated, had the most illustrious career, won first place in the National New Asian Science Exhibition, and -"
show s neutral
"I laughed out loud as she listed her accomplishments one by one. She made angry faces at me in mock-anger."
show s happy
s "But most of all... I want you to have a happy life, and I think someone else might... get it wrong."
"We spent the rest of the evening enjoying each other's company."
"The laughter and smiles never stopped, and she never let go of my hand during our walk."
$ scarlettAffection=2
jump postDateSelector
