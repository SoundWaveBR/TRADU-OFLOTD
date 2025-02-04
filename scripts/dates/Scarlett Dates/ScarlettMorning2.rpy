label ScarlettMorning2:

play sound Explosion
play music RavingEnergy

show bg RoomMorning with dissolve
#; could try to give a secret message
#; could use a sound blocker and say i think i know what's going on with this game
#;
"No dia seguinte, acordei com o som de uma explosão lá fora."
"Corri para fora o mais rápido que pude."
m "O que..."
stop music
show bg MansionMorning with dissolve
play music Wholesome
show s surprised at pos50s with dissolve
"A primeira coisa que vi foi Scarlett e fumaça preta saindo do chão perto dela."
show s worried
s "Oh, olá, [name]. Estamos tendo um clima agradável, hein?"
m "Ei, Scarlett... você está bem?"
show s happy
s "Estou muito bem, considerando tudo!"
show s annoyed
s "Estou experimentando novamente tentar trazer de volta as memórias das pessoas. Sem toda essa coisa de macaco zumbi."
show s flirt
s "Imagino que se você e eu um dia, bem... você sabe, eu gostaria que soubéssemos tudo um sobre o outro."
show s neutral
s "...Sem segredos."
m "Eu gostaria disso, Scarlett. Obrigada."
show s happy
s "Eu te aviso se eu fizer algum progresso com isso."
show s laugh
s "...Ugh, preciso limpar isso."
show s happy
s "Me dê um minuto, e então podemos ir para a floresta? Estou querendo passar um tempo lá desde que cheguei a esta ilha."
m "Parece bom para mim!"
stop music
play music RomanticJazz
hide s with dissolve
show bg LakeMorning with dissolve #time:2
show s flirt at pos50s with dissolve
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) #loop:true
"Nós andamos juntos pela floresta, de mãos dadas."
"Conversando sobre coisas que faríamos depois que saíssemos desta ilha... falando sobre tudo e qualquer coisa."
stop sound
show s happy
s "Depois que sairmos desta ilha, o que quer que aconteça... você talvez... queira assistir a um filme juntos?"
m "Claro, mas por que um filme?"
show s laugh
s "Você pode rir, mas há uma parte de mim que só quer ser uma garota normal por um dia. Isso é algo que eu nunca poderia esquecer."
show s flirt
s "E eu gostaria de poder ser assim, com você."
show s happy
s "O que você diz?"
m "Eu gostaria disso."
show s flirt
s "Yay!"
"Scarlett fez uma dancinha de felicidade."
show s happy
"Passamos o resto da manhã juntos na floresta, aproveitando a companhia um do outro... e talvez um pouco mais do que isso."
"De alguma forma, no meio de tudo isso, eu esqueci em que tipo de show eu estava em primeiro lugar. Éramos só eu e ela."
"Neste momento, mais do que nunca, eu estava feliz por estar vivo."
jump postMorningSelector
