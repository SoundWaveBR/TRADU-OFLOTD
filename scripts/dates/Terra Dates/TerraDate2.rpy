label TerraDate2:

$ terraAffection=2

play music Sincerely
show bg MansionIndoorsNoon with dissolve
play sound DoorKnock
"Bati na porta da sala de jogos."
play sound DoorOpen
show t neutral at pos50t with dissolve
t "Olá [name]! O que houve?"
m "Pensei em dar uma olhada e ver como você está indo no seu jogo."
show t happy
t "Deixe-me mostrar no que estou trabalhando, então!"
"Terra me entregou seu dispositivo de jogo."
show t neutral
t "Nem toda a arte está pronta ainda, mas espero que fique pronta em breve."
show t happy
t "É um jogo de fazenda!!"
show t worried
t "Eu tive que abandonar a ideia de namorar pombos depois, bem... de descobrir que já estava feito."
m "Isso é... realmente uma pena. Para o mundo inteiro, sério."
show t happy
t "Mas neste jogo, você vive em uma vila no interior, faz amigos, cultiva plantas e..."
show t blush
t "...Dizem todos os invasores com sua máquina gigante de morte de pombos mecha."
show t neutral
t "E há 1.000.000 de combinações possíveis de armas, e..."

menu:
    "Isso parece legal!":
        jump td2c1
    "Isso soa... diferente":
        jump td2c2

label td2c1:
m "Uau. Isso parece legal! Eu adoraria tocar."
jump td2pc

label td2c2:
m "Uau, isso parece... diferente!"
m "Não sei o que esperar, mas adoraria jogar."

label td2pc:
m "Estou curioso, como você decidiu fazer um jogo de fazenda?"
show t surprised
t "Hum, boa pergunta."
show t happy
t "Eles ganharam um lugar especial no meu coração!"
show t blush
t "Eu costumava tocar isso, de manhã até a noite, todos os dias."
show t worried
t "Você provavelmente já percebeu que eu não sou o tipo de pessoa que gosta de 'sair e festejar'."
show t sad
t "Para ser sincero, não conheço pessoas o suficiente para ir a festas, mas tudo bem."

menu:
    "Às vezes é mais divertido fazer as suas próprias coisas":
        jump td2c3
    "Ei, a escolha de como você gasta seu tempo é sua":
        jump td2c4

label td2c3:
m "Às vezes pode ser mais divertido ficar em casa e fazer apenas o que você gosta."
show t happy
t "É assim que me sinto!"
jump td2pc2

label td2c4:
m "Ei, é a sua vida! É sua escolha como você gasta seu tempo."
m "Só faça o que você quer, sabia?"
show t happy
t "É mais ou menos assim que me sinto!"

label td2pc2:

show t neutral
t "Chega de conversa, tente tocar!"
show t happy
t "Quero ver como você se sente sobre isso."
m "Certo, aqui vamos nós!"
show bg Black with dissolve
hide t with dissolve
stop music
play music MoveForward
"A tela de título foi exibida com um clique."
"'Starblue Valley'."
"Eu era um piloto de mecha que se cansou da vida no corpo de mechas e decidiu se mudar para o interior para se tornar um fazendeiro."
"Eu era muito bom nisso! A cada estação, eu aprendia a plantar, regar e colher novos tipos de plantações."
"Terra me dava conselhos sobre agricultura em todas as estações."
"Seu rosto estava tão perto do meu - ela observava cada movimento meu com uma expressão pensativa."
"Agricultura e pesca eram ótimas, mas pescar era quase impossível de fazer no começo."
"As partes de mecha do jogo eram incríveis."
"Você podia até conhecer os aldeões e ter relacionamentos com eles também."
"Só tinha uma coisa que era um pouco estranha..."
stop music
play music BlippyTrance
show bg GamesRoomMorning with dissolve
m "Primeiro, uau. O que você tem até agora é incrível, Terra!"
show t blush at pos50t with dissolve
t "Você acha?"
m "Sim, sério! É incrível. Nunca pensei que você pudesse combinar agricultura e ser um piloto de mecha no mesmo jogo, mas você fez isso muito bem."
show t happy
t "Obrigado, [name]. É legal da sua parte dizer isso."
m "Só tem uma coisa que eu acho que estava um pouco errada."
show t surprised
t "O que é isso? Qualquer feedback seria ótimo!"
show t worried
m "Sinto que os relacionamentos com os moradores da cidade eram um pouco estranhos."
m "Os aspectos do namoro não pareciam realmente certos?"
show t sad
t "Ah, eu sabia que você notaria isso!"
show t worried
t "É meio constrangedor, mas..."
show t surprised
t "Na verdade, nunca tive um encontro antes, então não tenho ideia de como é realmente."
show t worried
t "...E para ser sincero, eu também nunca tive um amigo de verdade."
show t blush
t "Se não for pedir muito..."
"Sua voz de repente se reduziu a um sussurro."
show t happy
t "...Talvez você e eu pudéssemos ser amigos?"
m "...Eu ficaria honrado em ser seu amigo."
m "...Dito isso... por favor, não me prenda em um videogame novamente."
show t surprised
t "...? Desculpe, o quê?"
show t neutral
t "De qualquer forma, assistir você jogar me deu algumas ideias. Quer me ajudar a testá-las?"
m "Claro! Ficarei feliz em ajudar no que puder."
hide t with dissolve
show bg Black with dissolve
"Nós dois sugeríamos ideias, ela as implementava e nós as testávamos juntos - e repetíamos."
"Foi ficando cada vez melhor."
show t happy at pos50t with dissolve
"O sorriso e o entusiasmo de Terra eram contagiantes. Não pude deixar de ficar animado por ela e admirado com sua motivação."
"Passamos o resto do dia trabalhando no jogo dela, mas pareceram apenas minutos."
"...Estou feliz que não foi outro jogo de realidade virtual."
$ terraAffection=2
jump postDateSelector


#; OLD
