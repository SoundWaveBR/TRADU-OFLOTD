label ScarlettDate3:

show bg Library with dissolve
show s neutral at pos50s with dissolve
play music LoveTheme
$ scarlettAffection=3

"Encontrei Scarlett no mesmo lugar em que a conheci. Ela estava absorta em um livro, com uma pilha de livros ao lado dela."
"Eles pareciam gastos, como se tivessem sido lidos várias vezes ao longo dos anos."
m "Olá, Scarlett. O que você está lendo?"
show s surprised
show s happy
s "Oi, [name]. Só um velho conto de fadas."
m "Sério! Estou surpreso que você tenha lido algo que jogaria a ciência pela janela."
show s laugh
s "Sou uma mulher de gostos variados."
show s tease
s "Gosto bastante dessas histórias, especialmente desta."
m "Qual delas você está lendo?"
show s neutral
s "Esse aqui, ele se chama {i}A Princesa de Avoranda{/i}."
show s tease
s "Sério, é bobagem, duvido que você esteja interessado em..."
m "Experimente."
show s happy
"Eu sorri para ela e ela sorriu de volta para mim da mesma forma."
show s laugh
s "Ok... Não vejo por que não!"
hide s with dissolve
show bg ScarlettReading with dissolve
#show s neutral
s "Há uma jovem garota, Nera, que era a princesa do reino de Avoranda, que ficava muito, muito longe da civilização."
#show s happy
s "Ao contrário de outras princesas antes dela, ela não tinha tempo para política ou festas. Ela passava o tempo todo construindo todo tipo de engenhocas para sua família e seus amigos."
#show s laugh
s "Como um cão robô que comeria os vegetais que não quisesse comer! Ooh, tenho que tentar fazer isso algum dia..."
"Scarlett riu como uma criança."
#show s happy
s "Nera tem uma infância feliz e abençoada. Ela até se apaixona - por uma plebeia chamada Aloria."
#show s neutral
s "Embora seu reino nunca aprovasse o relacionamento deles, Nera e Aloria nunca deixam de se ver em segredo. Toda noite, perto das árvores tortas nas Florestas Ocidentais."
#show s worried
s "...Mas esses dias não duram. Um dia, sua mãe, a rainha, é levada por uma bruxa, para nunca mais ser vista. E Nera é forçada a se tornar rainha aos 16 anos."
#show s neutral
s "Na ausência de sua mãe, Nera faz o melhor que pode para liderar o reino, e por anos, ele prospera. Ela é diferente de qualquer outra líder que eles já tiveram antes."
#show s worried
s "Mas secretamente, ela quer ir embora. Como rainha, ela não tem mais tempo para as coisas, ou pessoas, que ela amava de todo o coração. Ela chora toda noite, sozinha."
#show s sad
s "Mas ela sabe que não pode. Muita responsabilidade recai sobre ela."
#show s serious
s "Então um dia... Nera é amaldiçoada pela mesma bruxa que levou sua mãe, e esquece tudo. Seu nome, sua família, seu reino..."
#show s neutral
s "...Tudo, exceto Aloria e o desejo de ir embora."
#show s happy
s "E então ela vai embora, e ninguém na aldeia nunca mais a vê."
show bg Library with dissolve
show s laugh at pos50s with dissolve
#show s laugh
s "...Não vou te aborrecer com o resto da história. Mas obrigada por ouvir até agora."
m "Ah, vamos lá! Acredite em mim, Scarlett, eu quero ouvir isso até o fim."
m "Principalmente porque você gosta tanto."
"Olhei fundo nos olhos dela e percebi o quanto ela amava essa história."
show s tease
s "...Bem, não sobrou muita coisa, mas..."
show s happy
s "Bem... Nera e Aloria vivem uma vida maravilhosa em um reino vizinho por muitos anos."
show s serious
s "Mas um dia, ela se lembra de tudo e corre para casa, preocupada com seu povo."
show s neutral
s "Quando ela chega lá, ela vê que seu povo foi governado pela mesma bruxa que roubou sua memória - e que seu povo não prospera mais como prosperou sob seu governo."
show s serious
s "Com raiva, Nera confronta a bruxa, na fronteira de Avoranda."
show s neutral
s "A bruxa tira seu capuz, revelando-se a mãe de Nera — a rainha perdida."
show s worried
s "A mãe de Nera lhe dá um ultimato. Ela pode voltar a governar o reino, mas nunca mais poderá sair - ou pode sair agora e nunca mais voltar."
show s happy
s "...E é aí que a história termina. Você nunca sabe qual escolha Nera faz."
m "Isso é um grande suspense!"
m "Eu quero saber o que acontece depois."
show s laugh
s "Acredite em mim, eu também!"
show s neutral

menu:
    s "...Estou curioso, o que você faria no lugar de Nera?"

    "Eu deixaria o reino":
        jump sd3_c1
    "Eu ficaria no reino":
        jump sd3_c2

label sd3_c1:
m "...Acho que eu iria embora e nunca mais voltaria."
show s surprised
s "Interessante. Por quê?"
show s happy
m "Não há sentido em viver sem amor. Mesmo que fosse melhor para o reino que Nera ficasse, isso garantiria que seu amor nunca pudesse ser realizado."
m "E isso é... muito triste."
show s tease
s "Eu penso da mesma forma!"
jump sd3_pc

label sd3_c2:
m "...Acho que ficaria."
show s surprised
s "...Por que isso?"
show s neutral
m "Quer dizer, eu não posso simplesmente deixar meu povo sofrer desse jeito."
m "...Mas eu nunca deixaria Aloria ir."
show s happy
m "Eu encontraria uma maneira de fazer isso funcionar."
show s tease
s "...Você é um verdadeiro romântico, não é?"

label sd3_pc:

show s happy
s "...Eu adoro essa história desde que perdi minhas memórias."
show s laugh
s "Tenho certeza de que não tenho um reino nem nada, mas às vezes você se pergunta, sabe?"
m "É, eu também tenho a mesma sensação."
m "É só a vida, sabe? Você só tem que seguir em frente."
show s tease
s "...Sim. Você está certo."
show s happy
s "Estou... muito feliz que você é a pessoa com quem eu posso seguir em frente, [name]."
m "Eu também, Scarlett. Não há mais ninguém com quem eu preferiria estar, aqui e agora."
m "E falando nisso... há um lugar que eu quero te levar."
show s neutral
s "Onde é isso?"
show s surprised
m "Vou te dar uma dica: tenho pensado nesse lugar desde que você mencionou que amava contos de fadas."
show bg Palace with dissolve
stop music
play music RomanticJazz
show s laugh
s "Meu Deus. Tem tartarugas aqui embaixo, tartarugas!!!"
"Ela estava praticamente dançando pela sala, absorvendo todas as vistas."
"Era impossível não sorrir."
m "Achei que o Ocean Palace poderia ser sua praia."
show s tease with vpunch
"Scarlett praticamente pulou em cima de mim e me espremeu até a morte num abraço de urso mortal."
show s happy
s "Isso é maravilhoso, [name]. Muito obrigado!"
show s laugh
s "Você tornou tudo tão especial, de um jeito que eu sinceramente não conseguia acreditar... mas você conseguiu."
show s happy
m "E isso é só o começo, Scarlett."
m "Estamos juntos nessa."
show s flirt
"Segurei Scarlett e a beijei nos lábios. Foi como se uma explosão de paixão tivesse me incendiado, enquanto ela me beijava de volta e me envolvia com os braços."
s "Sempre."

if playthrough == 1 and currentDay == 6:
    jump LastDateScarlett
elif playthrough == 2 and currentDay == 9:
    jump LastDateScarlett
else:
    jump NotLastDateScarlett

label LastDateScarlett:
"Nós olhamos profundamente nos olhos um do outro, então..."
stop music
play music Smile
show bg Black with dissolve
show s surprised
play sound Shutdown
"Em uma fração de segundo, a sala ficou escura como breu. Eu não conseguia nem ver minha mão na frente do meu rosto, muito menos Scarlett."
hide s with dissolve
s "[name]? Parece que houve um apagão."
"Scarlett segurou minha mão com força - talvez ela estivesse com medo do escuro."

play sound GroupRun

"Não tive a chance de responder antes de ouvir uma onda de passos vindo em nossa direção no escuro."
"Algo não está certo - Oh não."
stop sound #@stopsfx GroupRun
"Nós estávamos cercados."
"Uma voz familiar cortou o curto silêncio em que prendi a respiração."
q "Sinto muito, [name]. Você só... não conseguiu."
"Nós temos que sair daqui."
q "...Só faça rápido, por favor."
"Eu podia ouvir a mulher a quem aquela voz pertencia indo embora."
"Eu corri da mesa, puxando Scarlett comigo."
s "O-O que está acontecendo, quem são -"
m "Só venha comigo, nós temos que sair de -"
play sound Hit
"Eu nem dei 5 passos antes de ser derrubado e algemado nas costas."
play sound Handcuffs
s "[name]!"
"Eu gritei para ela correr, mas eles se certificaram de que nenhum som pudesse escapar enquanto me prendiam ao chão."
m "Scarlett, você tem que correr, saia daqui -"
"Não adiantou. Mesmo que ela estivesse a apenas alguns metros de distância - eu não tinha forças para chegar nem um centímetro mais perto."
play sound Handcuffs
"Eles a derrubaram em um segundo. Ouvi o tilintar das algemas enquanto a arrastavam para longe."
"Lutei com todas as minhas forças para me levantar, para salvá-la, para correr... pelo que pareceu uma eternidade."
"Então... nada."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending


label NotLastDateScarlett:

show s happy
"Passamos o resto da noite desfrutando de um jantar adorável, em um lugar saído de um conto de fadas, com nada além de amor em nossos corações, risos e sorrisos em nossos rostos."
show s happy
s "Mal posso esperar para deixar esta ilha com você, [name]."
show s laugh
s "Nunca fiquei tão animado, tão feliz, desde... sempre!"
show s happy
s "...Você me faz sentir como se estivesse vivendo em um conto de fadas."
show s tease
s "Sabe... Tenho uma ideia de como poderíamos passar a noite, se estiver interessado."
m "E o que é isso?"
show s flirt
s "Vou lhe mostrar por que os contos de fadas foram escritos por adultos."
show bg Black with dissolve # time:2
#(Display CG here of sexy scene for a few seconds)
#; decided against this route lol."
$ scarlettAffection=3
jump postDateSelector
