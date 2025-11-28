label MeetTerra:

$ meetTerra=1
show bg GamesRoomMorning with dissolve
play music BlippyTrance
$ renpy.sound.play("audio/sfx/controller.mp3", loop=True)
show t annoyed at pos50t with dissolve
"Quando entrei na sala de jogos, meus olhos foram atraídos para uma garota jogando em um videogame portátil."
q "..."
show t annoyed
"Ela parecia pensativa enquanto seus dedos se moviam e apertavam botões na velocidade da luz."
show t happy
with vpunch # Terra,1
stop sound
q "Uau! Nova pontuação máxima!"
show t sad
q "Ah cara, é uma pena que eu não possa enviar."
show t surprised
"Ah, e aí, cara."
show t neutral
t "Você sabe o que aconteceu com a internet?"
m "O quê?"
show t worried
t "Desde que cheguei a esta ilha, não consigo obter nenhum sinal."
show t sad
show t annoyed  at pos50t
t "Eu... vou literalmente morrer nesse ritmo."
m "Você está bem?"
show t sad  at pos50t_fall1
t "Diga aos meus seguidores... que eles foram... os melhores..."
show t annoyed  at pos50t_fall2
with vpunch
t "...*Bleh*"
hide t with dissolve
"..."
"O que uma pessoa faz nessa situação?"
m "...Você está bem?"
with vpunch
play sound Intercom
k "Não se preocupe, [name]. Ela vai ficar bem."
m "Oh, oi Kat. O que houve?"
k "Tivemos que desligar toda a internet para garantir que nenhum spoiler do show vazasse."
k "Terra é um pouco dramática demais sobre isso. Você vai se acostumar."
show t worried  at pos50t
with vpunch # Terra,1
"Ei! Você me diz que estou sendo dramático demais quando você literalmente nos mandou de volta à idade da pedra!"
show t worried  at pos50t
show t annoyed
t "...Com jogos, eletricidade e outras coisas, mas ainda assim!"
show t sad
t "Ah, eu estava tão animado para transmitir para todos quando cheguei aqui."
t ";-;"
m "Você é um streamer?"
show t happy
t "Sim senhor! Sou eu!"
show t neutral
"Sou principalmente um streamer de jogos variados, mas também faço streaming da vida real!"
show t sad
t "E eu não posso agora! QAQ"
m "Talvez você pudesse apenas gravar as coisas e postá-las mais tarde?"
show t neutral
"Acho que é isso que terei que fazer, mas isso é coisa do passado."
show t surprised
t "A propósito, do que se trata todo esse show?"
m "Espera... o quê?"
show t worried
t "Sinceramente, não tenho ideia no que acabei de me meter, em relação a... praticamente tudo a ver com esse show."
m "Você nem fez uma pequena pesquisa antes de decidir vir aqui?"
show t condescending
with vpunch
with vpunch # Terra,1
"Ei, ei, não me chateie com isso!"
show t angry
t "Pelo que ouvi da Kat, você também não!"
m "Ei, amnésia e não fazer um pouco de pesquisa são totalmente diferentes!"
show t annoyed
"Eu esqueci de fazer minha devida diligência, e você esqueceu da sua vida!"
show t happy
t "Mesmo acordo!"
m "Não é o mesmo acordo!"
show t neutral
m "...De qualquer forma, é um programa de namoro chamado {i}Find Love{/i}."
m "Kat pode explicar as regras com mais detalhes, mas é basicamente o que você espera de qualquer programa de TV genérico de namoro."
m "E meu nome é [name]. Eu sou o que Kat chama de pretendente."
show t surprised
t "Huh."
show t annoyed
t "Então é como um jogo de simulação de namoro de romance visual, exceto que estou preso nele, em vez de poder jogá-lo eu mesmo?"
m "Acho que sim?"
show t neutral
t "Bem, já que isso é um jogo..."
stop music
with vpunch #count:2
with vpunch # Terra,1
show t angry
play music RocketPower
t "Eu vou ganhar!!!"
m "Não tenho certeza se essa é a maneira certa de abordar um encontro, mas -"
show t annoyed
t "CUIDADO MUNDO, A TERRA ESTÁ CHEGANDO!"
show t angry
t "E ELA SEMPRE GANHA!"
play sound Whoosh
hide t with dissolve
"..."
"Terra saiu correndo com um olhar feroz nos olhos."
"Não tenho ideia de para onde ela está indo."
"Mas quem faria?"


if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsT


"Acho que não há mais nada a fazer aqui."
menu:
    n "Eu poderia muito bem ir até..."

    "A Biblioteca" if meetScarlett != 1:
        jump MeetScarlett
    "A Cozinha" if meetViolet != 1:
        jump MeetViolet
    "A Sala de Jogos" if meetTerra != 1:
        jump MeetTerra
    "O Quintal" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsT:
stop music
play music ItemStore2
play sound Intercom
k "Certo, certo, chega de brincadeira."
k "Se você estiver no programa e não for um soldado mal pago, venha até a entrada da mansão."
"Acho que isso me inclui. Eu deveria começar a ir até lá."
with vpunch
k "Isso inclui você também, Terra! Eu posso ver você jogando, sabia!"
show t angry  at pos50t
t "Você não é minha chefe, Kat!"
"No que eu me meti?"
jump MetAllGirls
