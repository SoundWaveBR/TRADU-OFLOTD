label AllieMorning1:

play music Morning
show bg KitchenMorning with dissolve
show y worried at pos65y with dissolve # former look:left


show s neutral  at pos20s with dissolve # former look:left

show v neutral at pos80v with dissolve # posleft
show t neutral at pos35t with dissolve # former ,,-1 # former look:left
show a happy at pos50a with dissolve # former ,,-1 # former look:right
with dissolve
y "Meu Deus, ouvi o que aconteceu ontem. Você está bem?"
m "Não se preocupe, estou bem. Obrigada, Yui."
show y happy
y "Estou tão aliviado!"
show v surprised
v "Você não deveria estar descansando depois de ontem?"
m "Não, não precisa. Só tenho alguns arranhões e hematomas."
show s surprised
s "Estou surpreso que vocês dois não estejam mortos depois do que fizeram."
show a worried
show y surprised
a "Acredite em mim, eu também."
m "Espere, o quê?"
show v laugh
show a laugh
a "Quer dizer, *tosse*, não se preocupe, Scarlett. Eu ando de patins há mais tempo do que a maioria das pessoas."
"Tecnicamente, isso provavelmente é verdade, mas..."
show t happy
show v worried
t "Você deveria nos ensinar a andar de patins, Allie!"
show t happy
t "Parece que seria divertido."
show s worried
show y worried
y "Uh, você tem certeza, Terra? Acho que isso pode não ser uma boa ideia."
show t neutral
t "Qual é a pior coisa que poderia acontecer?"
show a happy
a "Gostei da sua atitude, garota! Vamos, vamos pegar a estrada!"
"Allie agarrou a mão de Terra e a puxou para longe."
show bg KitchenNoon with dissolve

hide y
hide v
hide a
hide t
hide s
with dissolve
"-- Algum tempo depois --"
show s happy at pos75s with dissolve
s "Olá Terra! Como foi a patinação?"
show t worried at pos25t with dissolve
t "..."
show t worried at pos25t with dissolve
t "Não há palavras..."
show t worried at pos25t with dissolve
play sound Hit
hide t with dissolve
show s worried  at pos50s with moveinright
s "...Acho que Allie quebrou Terra."
"Scarlett agitou as mãos freneticamente na frente do rosto de Terra, como se para verificar se ainda havia alguém lá dentro."
show s surprised
s "Terra, você está aí?"
show s happy
s "...Ei, Terra, a internet voltou!"
t "..."
"Acho que não tem ninguém em casa."
show s surprised
s "Uh, tem algum médico na ilha?"

if scarlettAffection >= 1:
    jump ScarlettJoke
if scarlettAffection == 0:
    jump PastScarlettJoke


label ScarlettJoke:
show s happy
s "Espere um minuto, eu fiz um novo soro outro dia que pode ser a solução para restaurar a mente de Terra."
show s neutral
s "Só me dê um segundo para administrar..."
m "Espere aí, você está falando da coisa que transformou todo mundo em zumbis?"
show s laugh
s "Bem, eu só acho que um teste de campo realmente não é o suficiente para ver se está errado ou não, então por que não apenas -"
"Eu tentei impedi-la de administrá-lo, mas era tarde demais."
show s surprised at pos70s
show t surprised at pos30t # former look:right
with vpunch
t "Gaaaaaaah!!!!"
m "Ah cara..."
show t angry
t "Me dê CÉREBROS!!! BANANAS!!!!"
show s sad
s "Acho que esse também é um fracasso."
m "Você tem um antídoto??"
show s happy
s "..."
m "..."
show s laugh
s "Brincadeira, brincadeira. Eu entendi bem aqui. Só me dê um momento."
"Felizmente, Terra acabou ficando bem."
"Passamos o resto da manhã jogando videogame como terapia para Terra."
jump postMorningSelector

#; Opportunity here to have a thing here if you've been on a ScarlettDate here
#; like, oh shit, i got something i could try to revitalize her mind
label PastScarlettJoke:
"..."
"Felizmente, Terra estava bem."
"Depois que isso foi resolvido, passamos o resto da manhã jogando videogame como terapia para Terra."
"Ela ainda não se lembra de nada sobre o que aconteceu."
"O que você viu, Terra?"
"...Acho que nunca saberemos."
jump postMorningSelector
