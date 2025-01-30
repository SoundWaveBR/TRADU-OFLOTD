label YuiMorning3:

show bg RoomMorning with dissolve

if YuiDate3Good == 1:
    jump goodYui
else:
    jump badYui


label badYui:
play music Morning
"...I slept like shit."
"No surprise, considering how yesterday went."
"I lay in bed for a while to try to conserve what energy I could for the day."
"...Guess it's time to find Kat."
jump postMorningSelector


label goodYui:
play music LoveTheme
"I woke up with Yui in my arms."
"We stayed up late last night, going for an unforgettable walk in the woods together."
"She was still fast asleep, and holding onto me so tightly."
"She looked at peace."
"I ran my hand through her chestnut hair."
show y happy at pos50y with dissolve
y "...Mmmm..."
show y happy
y "...I love you, [name]."
"She hugged me a little tighter."
"I couldn't move! Ack!"
"But hell, I didn't want to."
"...Who would?"
"The morning flew by, and it couldn't have been any better."
show y happy
y "If you told me this would happen, all those years ago... I'd have laughed."
show y blush
y "But I'm so, so glad it's happened... I'm the happiest I've ever been."
show y sad
y "...Though it'd be perfect if it wasn't here."
m "What do you mean?"
show y neutral
y "...I know you have to go on a date with someone else today."
m "...Yeah. Sorry about that, Yui."
show y laugh
y "That's okay."
show y happy
y "After you told me how you felt... I'm feeling secure, even if you have to date somebody else."
show y neutral
y "Don't have too much fun, though!"
show y blush
"I kissed her on her forehead."
m "I'll see you later, Yui."
show y happy
y "Come back soon!"
jump postMorningSelector
