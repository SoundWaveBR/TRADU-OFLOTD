label TerraDate1:

$ terraAffection=1

play music RavingEnergy
show bg MansionIndoorsMorning with dissolve
"Conforme eu andava cada vez mais perto da sala de jogos, eu podia ouvir pessoas gritando assassinato sangrento."
q "Socorro!!"
t "Você não vai a lugar nenhum."
q "Levem ele!! Eu sou muito jovem para morrer!"
"Eu corri para dentro o mais rápido que pude."
show bg GamesRoomMorning with dissolve
play sound ControllerSounds # loop:true

show b2 surprised  at pos50b  with dissolve
show b3 happy at pos65b  with dissolve
show b4 worried at pos80b  with dissolve
show t happy at pos30t with dissolve
b2 "Que tipo de irmão sacrificaria sua própria carne e sangue para sobreviver?"
show b3 laugh
b3 "A vida é dura, docinho!"
show b2 sad
b2 "Nããããooooo!!!!!"
show b4 angry
b4 "Eu vou te salvar, mano!!"
show b2 happy
b2 "Mano!!!"
play sound Explosion
show b4 sad
b4 "Agh!!!!!!!!!!"
hide b4 with dissolve
show t neutral
t "São os heróis que morrem primeiro, sabia~"
show b2 surprised
b2 "MANOOOOOOO!!!"
show t happy
t "Onde eu estava... ah, certo."
play sound Gunshot
hide b2 with dissolve
show t neutral
t "Um já foi, faltam dois!"
show t angry
t "Venha aqui!!"
"...Eles estavam jogando um videogame de luta."
show t happy
t "Ah, e aí? [name]!"
show t annoyed
t "Me dê um segundo, preciso fazer um pouco de controle de pragas."
show b2 worried  at pos50b
show b3 worried at pos65b
"2 e 3: Mate-o primeiro!!!"
show t happy
show bg Black with dissolve
play sound Gunshot
play sound Gunshot
play sound Explosion
hide b2 with dissolve
hide b3 with dissolve
hide b4 with dissolve
hide t with dissolve
stop music
stop sound #@stopsfx
"..."
show bg TerraGaming with dissolve
play music BlippyTrance
# show t happy
t "Tudo bem, tudo bem! Vocês perderam, de forma justa."
# show t neutral
t "Como prometido, vocês sabem o que têm que fazer."
"Os Cinco Irmãos gemeram enquanto cada um colocava algum tipo de capacete futurista."
#show t happy

menu:
    "Você é incrível, Terra!":
        jump td1c1
    "Nada mal":
        jump td1c2

label td1c1:
m "Você é incrível, Terra!"
m "Você dizimou aqueles caras sem nem suar."
jump td1pc

label td1c2:
m "Boa! Nada mal, Terra."
m "Você limpou o chão com aqueles caras."

label td1pc:


#show t neutral
t "Eu ganho a vida fazendo isso, acredite ou não."
#show t neutral
t "Embora ultimamente, esteja um pouco chato."
m "Por quê?"
t "É só... a mesma coisa de sempre, sabe?"

#show t happy
menu:
    t "...Embora eu tenha algo novo guardado, se você estiver a fim."

    "Estou caído!":
        jump td1c3

    "Why not?":
        jump td1c4

label td1c3:
m "Estou pronto para qualquer coisa."
jump td1pc2

label td1c4:
m "Claro, por que não?"

label td1pc2:

#show t neutral
t "Bom!"
#show t happy
t "Eu só preciso que você coloque esse fone de ouvido que não é nada suspeito~"
"Terra pegou um capacete atrás do sofá e colocou na minha cabeça."
#show t worried
t "Isso não vai doer nem um pouco, não se preocupe!"
m "Espere, por que isso-"
hide t with dissolve
show bg Black with dissolve
play sound Glitch1
"Foi como se um raio tivesse passado pela minha cabeça."
show bg Black with dissolve
show bg LakeMorning with dissolve # time:2
show b1 surprised at pos10b with dissolve
show b2 surprised at pos25b with dissolve
show b3 surprised at pos40b with dissolve
show b4 surprised at pos75b with dissolve
show b5 surprised at pos90b with dissolve
"...Eu estou... em algum tipo de floresta...?"
b2 "Uau! [name], você está aqui também!"
show b3 worried
b3 "O-Onde estamos? Quero ir para casa!"
show t annoyed at pos60t with dissolve# former ,,-1
t "Ah, pare de choramingar!"
show t happy
t "Você está apenas em um videogame! Vamos lá, esta não é a primeira vez que você vê isso acontecer na ficção."
m "Esse tipo de coisa existe agora?"
show t annoyed
t "Já existe há pelo menos um milhão de anos, acompanhe os tempos!"
show b3 worried
b3 "Ah, da última vez que verifiquei, nunca tinha ouvido falar de algo assim."
show t worried
t "Tudo bem, tudo bem, então talvez fosse algum tipo de dispositivo estranho que eu nunca tinha visto antes."
show t annoyed
t "Você pode me culpar por querer tentar mexer com isso?"
show b2 surprised
b2 "Espera, não tem como isso ser um jogo. Parece muito real!"
"Eu tinha que admitir, eu também tinha minhas dúvidas. Tudo parecia estar realmente ali."
show t surprised
t "Ei, se você quer uma prova, tente sair desta floresta."
show b2 worried
"Dois deram alguns passos cautelosos para frente, depois mais alguns."
with vpunch
show b2 surprised
play sound Hit
b2 "Oof!"
"Ele bateu contra algum tipo de parede invisível."
show b2 worried
b2 "Há... algum tipo de parede invisível aqui."
show b4 surprised
b4 "É realmente um videogame, hein!"
show t neutral
t "Na verdade, essa é a parede da Sala de Jogos."
show t worried
t "Achei que esse console seria como um videogame de realidade virtual 'deep dive' também, mas parece que tudo o que fazemos aqui é replicado no mundo real."
show t happy
t "Ande muitos passos de uma certa maneira, e... SMACK!"
m "...Isso não torna isso meio inútil?"
show t surprised
t "Acho que sim, se você é alérgico a diversão?"

play sound Intercom
"O som do interfone tocou pela floresta."
k "Ei, vocês conseguem me ouvir?"
m "Kat! Podemos ouvir você, o que houve?"
#k: I don't know how, but it looks like Terra found an old, er... "experimental" game console that we had in storage."
k "Vocês precisam sair desse jogo agora mesmo! Se ficarem muito tempo no jogo, ele vai fritar seu cérebro!"
m "O quê!? Como? Por quê!?"
k "Er... resumindo, é um... como dizer... 'console de jogo' experimental que tínhamos armazenado."
k "Não faço ideia de como Terra o encontrou."
"Esse programa está sempre tentando encontrar novas maneiras de me matar, não é?"
m "...Quanto tempo temos?"
k "Antes que frite seu cérebro, não sei, talvez alguns minutos, talvez várias horas - mas ele vai minar sua sanidade lentamente quanto mais tempo você ficar lá."
k "Só saia logo!"
m "Não sabemos como!"
"Os Irmãos Cinco e eu olhamos em volta freneticamente, mas não havia nenhuma maneira de sairmos."
show t surprised
t "Ah, acho que vocês não conseguem ver o menu de logout. Acho que é algo exclusivo para administradores."
show b2 worried
b2 "Se você consegue ver, Terra, então vamos lá! Desconecte-nos já!"
show t happy
"Ela gargalhou como uma maníaca de filme B."
"...Algo me diz que ela não tinha muita sanidade para minar em primeiro lugar."
show t neutral
t "Mas seria uma pena ir embora tão cedo!"
show t happy
t "...Vamos jogar um jogo primeiro."
show t happy
t "Acontece que, como administrador, posso alterar todos os seus avatares quando quiser!"
show t angry
t "Olha isso! BAM!"
show t neutral
"...?"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve
hide b4 with dissolve
hide b5 with dissolve
show t surprised at pos50t with dissolve
"Olhei para minhas mãos, que agora tinham se tornado pequenas asas brancas."
"Olhei para meu rosto e... eu tenho um... bico!????"
"Eu... me tornei um pássaro!?"
b1 "Meu Deus, o que ela fez conosco! Somos pombos!!!"
b2 "ME DEIXE SAIRRRRR ..."
b3 "Nós nunca seremos contadores agora!"
b4 "Nós vamos morrer aqui!!"
b5 "Acho que tenho um novo fetiche."
"Os Cinco Pombos corriam freneticamente, como galinhas com as cabeças cortadas."
"Não posso culpá-los."
"Eu admirava Terra, que parecia um gigante comparado a nós agora."
show t neutral
t "...Agora, tenho certeza de que vocês estão se perguntando por que eu transformei todos vocês em pássaros."
m "Eu acho que você poderia dizer isso."
show t neutral
t "É engraçado, [name]. Antes você me disse que todo esse show era como um simulador de namoro, exceto que você estava no comando."
show t happy
t "Agora o sapato está no outro pé!"
"Ela gargalhou de novo, como uma bruxa má."
show t neutral
t "Bem-vindo ao {b}Simulador de namoro de pombos: Battle Royale{/b}."
show t blush
t "Você terá que... me seduzir se quiser sair daqui."
"A cada dia que passa, temo mais pelo futuro da humanidade."
m "...E você queria que fôssemos... pombos para isso?"
show t surprised
t "Quer dizer, é? A proporção de romances visuais de humanos e pombos está totalmente fora de sintonia, cara!"
show t happy
t "Acho que deveríamos equilibrar isso!"
"Estou preso em um jogo de realidade virtual matador."
"Também estou preso em um programa de namoro matador."
"Para piorar as coisas, também estou preso no corpo de um pombo."
"Agora, preciso seduzir uma mulher com meu charme aviário."
"Você pode imaginar o tipo de estresse que estou sofrendo."
show t angry with vpunch
t "Agora... me seduza!!!"
show t annoyed
"Um por um, os Pigeons Five dispararam uma cantada atrás da outra contra Terra, mas sem sucesso."
show t angry
t "Vamos, vamos! Mova essas asas como se quisesse!"
"Eu tentei algumas também, mas ficou claro que não tiveram efeito."
"Não consigo imaginar que ser um pombo tenha ajudado nisso de alguma forma."
"Hmm... vamos tentar mais uma."
"Que tal..."

menu:
    "Caramba, garota, você é uma piada":
        jump birb
    "Caramba, garota, você está tão... estilosa":
        jump birb
    "Porra, garota, você é mais viciante que charlatão":
        jump birb


label birb:

"Com minha vontade de viver em baixa, eu..."
show bg Black with dissolve
show t surprised
play sound Shutdown
"!?"
hide t
"O jogo ficou escuro."
show bg GamesRoomMorning with dissolve
show b1 surprised at pos10b
show b2 surprised at pos25b
show b3 surprised at pos40b
show b4 surprised at pos75b
show b5 surprised at pos90b
show t surprised at pos60t
with dissolve
"Um momento depois, estávamos de volta à sala de jogos."
show t surprised
t "O quê...?"
show b3 happy
b3 "Estamos de volta, graças a Deus!"
show b4 laugh
b4 "Eu tenho dedos! Eu sei escrever! Eu poderia preencher um balanço!"
show b5 sad
b5 "Awww! Justo quando estava ficando bom!"
show b5 surprised
b5 "Espera, tem alguma coisa... queimando?"
"O 'console de jogos' tinha fumaça saindo dele."
"...Acho que é torrada."
show t worried
t "...O que... aconteceu? Minha mente está toda nebulosa..."
m "...Você está bem, Terra?"
show t annoyed
t "...Vou tirar uma soneca."
hide t with dissolve
"Ela pulou no sofá e, em segundos, estava dormindo profundamente."
"Os Irmãos Cinco e eu decidimos que seria melhor nunca mais falar sobre isso."
$ terraAffection=1
jump postDateSelector
