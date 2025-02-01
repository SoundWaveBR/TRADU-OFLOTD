label ScarlettDate1:

$ scarlettAffection=1

#; Scarlett seems like the sexy whatever person on the outside
#; but on the inside, she's really just a girl who's looking for love."
#; maybe she's super awkward the first time, so she tries to make up for it by being cool the second time."
show bg RoomMorning with dissolve
play music MasterDisorder
"Não demorou muito para encontrar Scarlett. Ela me encontrou primeiro."
play sound DoorOpen
"Ela tinha acabado de entrar pela minha porta e estava tentando recuperar o fôlego quando a fechou com força atrás de si."
play sound DoorClose
show s worried at pos50s with dissolve
s "[name]! Graças a Deus você está bem, meu Deus."
m "O que está acontecendo, Scarlett?"
show s sad
s "Resumindo a história, eu experimentei um pouco da fauna local da ilha antes, não há nada igual, é realmente incrível, e ugh, eu errei minha introdução com você antes, e -"
m "Uau! Devagar."
show s worried
s "*suspiro*"
show s laugh
s "...Eu fiz um novo composto químico que causa amnésia! É incrível!"
m "Uau! Isso não é algo que você ouve todo dia."
show s happy
s "O legal é que aplicar a quantidade certa em uma pessoa pode fazê-la esquecer coisas específicas — quem ela é, como escrever, qualquer coisa."
show s worried
s "O ruim é que..."
stop music
play sound Hit
play music RavingEnergy
with vpunch
"Algo bateu na porta lá fora. Quase pulei de surpresa."
b4 "Dê-me cérebros!!!!! E bananas!!!"
show s serious
s "...Aplicar muito transforma as pessoas em macacos zumbis raivosos, determinados a comer cérebros humanos."
show s worried
s "...E bananas."
m "Meu Deus, as bananas não..."
with vpunch
play sound Hit
"A porta bateu novamente. Parecia que ela estava prestes a ser derrubada."
show s angry
s "Precisamos sair daqui, e rápido!"
show b4 angry at pos30b
show s surprised at pos70s
with dissolve
play sound Hit
with vpunch
"Quatro arrombaram a porta e bloquearam nossa única saída."
b4 "ME DÊ CÉREBROS! E BANANAS!"
m "Vou tirá-lo do caminho! Vai dar tempo de você correr!"
show s serious
s "Tenho uma ideia melhor."
stop music
play music RunAmok
play sound AnimeShine
show s happy
with vpunch
"Scarlett atingiu Quatro com um pó branco, cobrindo seu rosto completamente."
hide b4 # with dissolve
play sound Hit

"Ele se debateu violentamente por alguns segundos e depois caiu no chão, inconsciente."

menu:
    "O que é que foi isso!?":
        jump sd1_c1
    "Ele vai ficar bem?":
        jump sd1_c2

label sd1_c1:
m "Uau, o que foi isso?"
show s laugh  at pos50s with dissolve
s "Uh, vamos apenas dizer que Quatro está vendo todas as bananas que quer agora, e vamos deixar por isso mesmo. Siga-me!"

jump after_cd1_choice

label sd1_c2:
m "Uau, ele vai ficar... bem?"
show s laugh  at pos50s with dissolve
s "...Acho que vamos descobrir!"
show s worried
s "Por enquanto, vamos nos concentrar em sair daqui!"

label after_cd1_choice:

show bg MansionMorning with dissolve
stop music
play music Sincerely
"Corremos para fora da mansão o mais rápido que pudemos."
m "Como isso aconteceu?"
show s worried
s "Ooh, eu estava com medo que você perguntasse isso."
show s sad
s "...Ouvi de Terra que você perdeu suas memórias, e eu... eu queria ver se poderia ajudar você a recuperá-las."
show s laugh
s "Então eu, uh... posso ter feito experimentos nos Cinco Irmãos... para ver se eu conseguia apagar suas memórias... e trazê-los de volta."
show s surprised
s "Devo ter feito as contas errado. Somei demais. Não percebi que os cérebros deles eram tão vazios!"
show s happy
m "De uma forma estranha... isso é muito fofo, Scarlett. Obrigada. Loucura, mas ainda assim, obrigada."
show s neutral
s "Eu vou consertar isso, eu juro. Só preciso de tempo para fazer um antídoto."
show s happy
s "Por sorte, deixei minhas ferramentas e suprimentos bem perto daqui. Podemos ficar lá até termos um antídoto."
m "Parece um plano. Lidere o caminho!"
m "Espere... onde estão as outras garotas? Você acha que elas ainda estão lá dentro?"
show s worried
s "...Eles estão... na verdade presos dentro da biblioteca agora."
m "Oh merda! Temos que voltar e salvá-los!"
show s sad
s "Hum... Não sei como dizer isso, mas..."
show s laugh
s "Eu acidentalmente os transformei em zumbis também, hahaha..."
show s worried
s "Mas eles eram um pouco demais, então eu os tranquei na biblioteca, ha... ha... ha...?"
"...Estamos condenados, não estamos."
show s happy
"Scarlett e eu passamos o tempo conversando sobre a loucura que estava acontecendo e bolando um plano para salvar todo mundo."
"Ela parecia estar bem estressada, apesar de parecer tão organizada - mas eu podia dizer que ela realmente se importava com os infectados."
"...Não o suficiente para evitar que isso acontecesse em primeiro lugar, mas o suficiente."
"Eu a vi construir uma máquina que ela insiste que pode fazê-los voltar ao normal, mas..."
"...Olhando para isso, não posso deixar de ficar um pouco cético."
show bg MansionEvening with dissolve
show s happy
stop music
play music RavingEnergy
s "Tudo bem, é hora do show."
m "Você realmente acha que isso vai funcionar?"
show s laugh
s "Pode apostar! Afinal, eu consegui!"
show bg MansionIndoorsNight with dissolve# time:1
"Parece que a costa está limpa aqui..."
"Nós andamos até o lado de fora da biblioteca sem sermos detectados, mas definitivamente não estávamos sozinhos aqui."
show s serious
s "Tudo bem! É hora de salvar nossos amigos!"
hide s with dissolve
play sound DoorOpen
show bg Library with dissolve # time:2
show y angry at pos80y
show a angry at pos20a
show t angry at pos40t
show v angry at pos60v

with dissolve
all "Céeeerebrooos!!!!"
with vpunch
m "Eles estão vindo direto para nós!!"
s "Nada com que se preocupar."
hide s
hide a
hide t
hide v
hide y
with dissolve
stop music
play music RunAmok
show bg ScarlettShooting with dissolve # time:2
#play ambient Minigun # loop:true
$ renpy.sound.play("audio/sfx/minigun.mp3", loop=True)
s "Isso é vingança por vocês terem arrasado nas apresentações!!"
m "Desculpe... o quê?"
s "Oh, uh... nada."
m "...Tem certeza de que isso vai curá-los?"
s "Claro, o que parece que estou fazendo?"
m "..."
"Algo me disse que Scarlett estava gostando um pouco demais disso..."
k "Uh... que diabos? Eu tiro os olhos das câmeras por um segundo, e... tem zumbis na casa."
s "Não por muito mais tempo, prometo!!"
"Passamos o resto do dia administrando o antídoto em cada pessoa. Cada um deles desmaiou assim que entregamos a cura."
#I was exhausted by the time night rolled around."
show bg MansionEvening with dissolve
stop music
stop sound #@stopsfx Minigun
play music Sincerely
show s happy at pos50s with dissolve
s "Não foi bem o primeiro encontro que você esperava, hein?"
m "Você pode dizer isso de novo."
m "Foi... definitivamente a primeira vez."
show s laugh
s "Kat me disse que, para tornar um encontro emocionante, eu precisava fazer seu coração disparar."
show s happy
s "Acho que fiz um bom trabalho nisso!"
"...Acho que isso é tecnicamente verdade, mas não há maneiras mais fáceis?"
"Algo me diz que essa mulher é cheia de mais surpresas."
$ scarlettAffection=1
jump postDateSelector
