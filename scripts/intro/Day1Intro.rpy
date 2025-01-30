
label Day1Intro:

stop music

default persistent.AllieEnding = 0
default persistent.ScarlettEnding = 0
default persistent.TerraEnding = 0
default persistent.VioletEnding = 0
default persistent.YuiEnding = 0
default persistent.KatEnding = 0

menu:

    n "Eu me identifico como..."
    "Ele/Dele":
        window hide dissolve
    "Ela/Dela":
        window hide dissolve
    "Eles/Deles":
        window hide dissolve
default playthrough = 1
default currentDay = 1
default allieAffection=0
default scarlettAffection=0
default terraAffection=0
default violetAffection=0
default yuiAffection=0
default meetAllie=0
default meetScarlett=0
default meetTerra=0
default meetViolet=0
default meetYui=0

default P1Date1="none" # label first pick
default P1Date2="none" # label second pick // the two main contendors!"
default P1Date3="none"
default P1Date4="none"
default P1Date5="none"
default P1Date6="none"
default P2Date1="none"
default P2Date2="none"
default P2Date3="none"
default P2Date4="none"
default P2Date5="none"
default P2Date6="none"
default P2Date7="none"
default P2Date8="none"
default P2Date9="none"

# START OF GAME

play sound MysteryHarp
show bg Episode1 with dissolve
$ renpy.pause(delay = 2.0, hard = True) # wait
# pause 2.25

label MainStory:

$ dejaVu = 0

label WakeUp:
stop music
play music ItemStore2

scene bg black with fade
m "Zzzzz..."
with vpunch # replaces SHakeBackground

q "Ei, não fique aí deitado. Levanta!"
m "Só mais 5 minutinhos..."
with vpunch
q "Você é a estrela do show! Você não pode simplesmente ficar aí dormindo!"
m "Ah, é? Então veja só... (e volta a dormir)..."
q "Ah, é assim que você quer jogar?"
q "Vamos começar!"
jump hit

label yesdejavu:
    q "Ah que droga. Voltamos para o começo."
    q "*Suspiro*"
    jump hit

label hit:
    stop music
    play sound hit
    with vpunch
    play music TheShowMustBeGo
    m "WOW!!!!"
    show bg PlaneBar with dissolve # with fade
    show k happy at mid with dissolve
    q "Levante e brilhe, dorminhoco."
    m "Ai ai ai... Você acabou de me bater?"

if dejaVu == 1:
    jump yesdejavu2
else:
    jump nodejavu2

label yesdejavu2:
    m "Espera, isso não aconteceu?"
    show k laugh at mid
    q "Claro que não! Não tem como eu te bater duas vezes."
    jump C1end

label nodejavu2:
    show k surprised at mid
    q "Nah, eu cheguei agora. Acabei de expulsar a pessoa que te bateu."
    show k flirt at mid

    menu:
        q "Fala sério, você deveria me agradecer."

        "Obrigado, eu acho.":
            jump Thanks

        "Não, eu tenho quase certeza de que foi você.":
            jump Doubt


label Thanks:
    m "Obrigado, eu acho."
    show k flirt at mid
    q "Não há de quê, tudo isso faz parte de um bom dia de trabalho."
    jump C1end

label Doubt:
    m "Não, eu tenho quese certeza de que foi você."
    show k sassy at mid
    m "O que há com esse seu olhar em seu rost-"
    play sound hit
    with vpunch
    show bg Black with dissolve
    hide k
    $ dejaVu = 1
    $ dejaVu = 1
    jump yesdejavu

label C1end:
    q "De qualquer forma, qual era seu nome mesmo?"
    m "Oh, meu nome é..."
    with vpunch
    m "...Não consigo lembrar meu nome!"

    show k surprised at mid
    q "Espera, o quê? Juro que eu nem te bati com tanta força!"
    m "Então você me bateu!"
    q "Isso não é importante! Tente se lembrar!"
    show k worried at mid
    q "Se você não consegue se lembrar de nada, nós dois vamos ter um grande problema."
    m "Por que isso?"
    show k serious at mid
    q "Podemos falar sobre o porquê depois. Qual era seu nome?"
    m "...! É..."

    $ name = renpy.input(_('Meu nome é...'), length=14)


    m "Meu nome é [name]. Isso [name]!"
    m "Não consigo me lembrar de mais nada, infelizmente."
    show k surprised at mid
    q "Wow, eu deveria tentar bater no meu contador qualquer dia desse."
    show k worried at mid
    q "Você se lembra onde estamos, o que você está fazendo aqui?"
    m "Não, não consigo me lembrar de nada. Está tudo tão nebuloso..."
    show k happy at mid
    q "Tudo bem, posso te dar um resumo. Você está em um reality show chamado {i}Find Love or Die Trying{/i} - embora o chamemos apenas de {i}Find Love{/i} para os... desinformados."
    show k neutral at mid
    k "Eu sou a produtora - Com o o nome de Kat."
    show k happy at mid
    k "A premissa é que você, o {i}pretendente{/i}, está vivendo com cinco mulheres bonitas, e uma delas é sua alma gêmea."
    m "Eu nem as conheci ainda, como você saberia que uma delas é minha alma gêmea?"
    show k flirt at mid
    k "É assim que funciona, bem-vindos ao Reality de TV!"
    show k happy at mid
    k "Você conhecerá duas das garotas nos próximos seis dias, em três encontros com cada uma delas."
    show k neutral at mid
    k "Então, no sétimo dia, você terá que pedir uma delas em casamento na cerimônia final!"
    show k laugh at mid
    m "Isso parece... bastante direto para mim."
    show k flirt at mid
    k "Não tão rápido, parceiro!"
    show k neutral at mid
    k "A garota que você escolher terá uma escolha: aceitar ou não sua proposta."
    show k happy at mid
    k "Se ela disser sim, vocês dois vão desaparecer em direção ao pôr do sol em um iate banhado a ouro no último dia."
    show k laugh at mid
    k "Felizes para sempre. Exceto sem o iate. É um empréstimo."
    show k neutral at mid
    stop music
    play music Smile
    show k serious at mid
    k "Mas se ela disser não..."
    show k flirt at mid

    k "...Bem, vamos ter que te matar."
    m "Espera, o quê? Matar?"
    m "Você está me zoando, certo?"
    play sound CameraShutter

    show k sassy at r
    show d laugh at dl with dissolve
    d "ISSO, essa é a reação que nós queriamos ver!"
    m "???"
    show d happy at dl
    d "Sério, parece que eu acabei de cagar no seu cereal!"
    m "O que está acontecendo? Quem é você?"
    show d laugh at dl
    d "Oh, onde estão as minhas maneiras."
    show d neutral at dl
    d "Meu nome é Damian. Damian Black."
    show d serious at dl
    d "Sou o CEO da Royal Black Media, a maior rede de jogos Battle Royale do planeta."
    m "Jogos Battle Royale? Como jogos de computador?"
    show d surprised at dl
    d "Você tem vivido debaixo do sovaco fedorento de uma pedra?"
    show d sassy at dl
    d "Pessoas de verdade matando umas às outras está na moda nesta temporada."
    m "O quê...?"
    show d annoyed at dl
    d "Bem, *estava* nesta temporada. Juro, eu me esforcei muito e honestamente para fazer programas de matar de primeira linha, e o que eu ganho por isso..."
    show d evil_smile at dl
    d "Então estamos tentando um novo tipo de jogo de matar. Apimentando um pouco o romance para as pessoas que peidam sonhos e assam bolos de arco-íris."
    show d laugh at dl
    d "É aí que você entra. E, ei, não é um mau negócio!"
    show d neutral at dl
    d "Você pode encontrar o amor! Ou morrer. Tanto faz."
    show d laugh at dl
    d "Só faça um bom show para mim, hein?"
    show b1 serious at br2 with dissolve # look left?
    q "Com licensa, Sr. Black?"
    show d annoyed at dl
    d "O que foi, Um?"
    show b1 worried at br2
    b1 "Estamos sem uma das câmeras aéreas para os campos dos fundos."
    show d laugh at dl
    d "Bem, essa é a minha deixa. Se não o estagiário não vai atirar em si mesmo."
    show d evil_smile at dl
    "Dá um inferno a eles, Kit Kat."
    show k sassy at r
    k "Não precisa dizer suad vezes."
    hide d with dissolve
    hide b1 with dissolve
    show k neutral at mid with dissolve
    stop music
    play music MysteryLoop
    show k annoyed at mid


    m "Olha, eu não sei o que está acontecendo aqui, mas vou sair daqui."
    m "Para começar, mal consigo lembrar do meu próprio nome, muito menos se já tenho um parceiro."
    show k laugh at mid
    k "Se é isso que te preocupa, você não fez isso!"
    show k sassy at mid
    k "E não por falta de tentativa."
    m "Como você sabe disso?"
    show k bored at mid
    "Kat suspirou." # label narrator
    show k serious at mid
    k "Olha, você não tem escolha."
    show k annoyed at mid
    k "Damian vai te matar se você tentar escapar, ou se você contar a qualquer uma das garotas sobre a verdade por trás do show."
    m "...As garotas não sabem?"
    show k serious at mid
    k "Eles não têm ideia de que sua vida está em perigo - eles apenas acham que é um programa de namoro comum sobre encontrar sua alma gêmea, chamado {i}Find Love{/i}."
    show k annoyed at mid
    k "Se você contar a verdade a qualquer um deles, você não vai apenas acabar morto. Você vai acabar matando eles também."
    m "Como você pôde -"
    show k angry at mid
    k "Eu não faço as regras, [name]. Me desculpe."
    show k laugh at mid
    k "Realmente, você é uma pessoa bem séria, [name]!"
    show k happy at mid
    k "A maioria das pessoas ficaria um pouco mais feliz em saber que estão sozinhas no paraíso com cinco lindas mulheres."
    show k sassy at mid
    k "O que há para se preocupar?"
    m "Ah, você sabe, a coisa toda de ser executado se a garota que eu perguntar disser não, o pouco de não lembrar quem diabos eu sou."
    show k annoyed at mid
    k "...Que tal isso."
    show k neutral at mid
    k "Preciso que meu show seja bem-sucedido e ocorra conforme o planejado."
    show k flirt at mid
    k "E você quer suas memórias de volta e, presumivelmente, deixar esse show vivo."
    show k surprised at mid
    m "Isso depende de quais são as memórias, mas sim."
    show k neutral at mid
    k "Se você for um bom pretendente para o meu show, eu te ajudarei a recuperar suas memórias."
    show k happy at mid
    k "Não é um mau acordo. A maioria das pessoas mataria por uma oportunidade como essa."
    show k surprised at mid
    k "Sério! Tudo o que você precisa fazer é conhecer cinco mulheres adoráveis e convidar uma para sair."
    show k happy at mid
    k "Estarei com você em cada passo do caminho, fora das câmeras. Antes que você perceba, tenho certeza de que estará se divertindo muito!"
    show k sassy at mid
    k "Quem sabe, você pode até se apaixonar. Você não seria o primeiro!"
    show k neutral at mid
    k "Mas se você sobreviver ao show inteiro, prometo que vou te contar tudo o que você quer saber."
    show k happy at mid


    menu:
        k "Promessa de mindinho. O que você acha?"

        "Parece um acordo.":
            jump HellYeah

        "Não, valeu, me tira daqui!":
            jump NTY

label HellYeah:
    stop music
    play music ShavingMirror
    m "Parece um acordo."
    show k flirt at mid
    k "Esse é o espirito!"
    show k happy at mid
    k "Quem sabe, você pode até me agradecer por isso um dia."
    m "Vamos ver sobre isso."
    show k sassy at mid
    k "Confie em mim, vou garantir que esse show seja o melhor momento da sua vida."
    show k laugh at mid
    k "Será tão bom que tudo depois será uma decepção!"
    m "Essa é uma maneira deprimente de encarar isso. E se eu acabasse com uma das garotas depois do show?"
    stop music
    jump postResponse

label NTY:
    m "Não, valeu, me tira daqui!"
    show k bored at mid
    k "...E para onde você iria?"
    m "Para casa, é claro."
    show k sassy at mid
    k "E onde é a casa?"
    m "...Uhhh..."
    show k flirt at mid
    k "Pensei que sim!"
    show k bored at mid
    k "Olha, as coisas serão muito mais fáceis para nós dois se trabalharmos juntos."
    show k serious at mid
    k "Vou garantir que nada de louco aconteça com você e que você provavelmente chegue em casa em segurança."
    show k neutral at mid
    k "Mais importante, jogar junto lhe dá uma chance de sobreviver. Isso não parece melhor do que ser morto com certeza?"
    m "..."
    show k worried at mid
    k "Você ouviu o que Damian ia fazer com o estagiário."
    m "..."
    stop music
    play music TheShowMustBeGo

    show k sassy at mid
    k "Vai ter comida de graça!"
    m "...Tudo bem, tudo bem. Vou tentar."
    show k flirt at mid
    k "Você não vai se arrempeder, eu prometo!"
    stop music
    jump postResponse

label postResponse:
    play music ShavingMirror
    show k laugh at mid
    k "De qualquer forma, sem mais delongas..."
    show k happy at mid
    k "Vamos começar o show!"
    show k neutral at mid
    k "Siga-me, vou levá-lo até onde você conhecerá nossos adoráveis concorrentes."
    show k sassy at mid
    "Kat me agarrou pela mão e me puxou."
    show k annoyed at mid
    k "Lempre-se, você não pode dizer a verdade a ninguém sobre esse joguinho."
    show k serious at mid
    k "Não importa o que aconteça, apenas sorria. Entendeu?"
    m "Entendido."
    hide k with dissolve
    show bg Black with dissolve

    "Saímos do bar juntos."
    "Não percebi no começo, mas era um bar em um pequeno avião."
    "Acho que devo ter voado até aqui."
    "Andamos até vermos uma mansão à distância."

    show bg MansionMorning with dissolve
    m "Uau. É enorme."
    m "Não consigo imaginar o quão caro é esse lugar."
    show k laugh at mid with dissolve
    k "Você vai se surpreender!"
    show k neutral at mid
    k "Já que estamos em algum canto esquecido da Nova Ásia, a terra é bem barata."
    m "Nova Ásia?"
    show k sassy at mid
    k "Você nunca leu as notícias na última década?"
    m "Perda de memória, lembra?"
    show k bored at mid
    k "Certo."
    show k neutral at mid
    k "Bem, espero que você não tenha esquecido como falar com garotas."
    show k angry at mid
    k "Cinco! Quatro! Três! Dois! Um!"
    m "Espera, o quê? Já estamos começando?"
    show k bored at b6 with dissolve
    k "Não exatamente."
    stop music
    play music JazzInParis
    #show k bored at b6 with dissolve
    show b1 angry at bl2 with dissolve
    b1 "Para proporcionar ao mundo diversão de alto nível!"
    show b2 angry at bl with dissolve
    b2 "Para proteger nossa bunda do desemprego!"
    show b3 angry at bm with dissolve
    b3 "Para fazer o mundo acreditar no destino e no amor!"
    show b4 angry at br with dissolve
    b4 "Trabalhamos como escravos para os mercenários de cima!"
    show b5 angry at br2 with dissolve
    b5 "Nós somos os Cinco Irmãos!"

    show b1 with vpunch
    b1 "Um!"
    show b2 with vpunch
    b2 "Dois!"
    show b3 with vpunch
    b3 "Três!"
    show b4 with vpunch
    b4 "Quatro!"
    show b5 with vpunch
    b5 "Cinco!"
    b "Preparar para - "
    stop music
    play music ShavingMirror
    show k serious at b6 with dissolve
    k "Prepare o cenário, quero começar a filmar ontem."
    show b1 sad at bl2
    show b2 sad at bl
    show b3 sad at bm
    show b4 sad at br
    show b5 sad at br2
    show k serious at b6
    b2 "Oh."
    show b2 sad
    b4 "Acho que não somos importantes o suficiente para terminar nossas introduções."
    b3 "De quem foi a ideia de trabalhar na indústria da TV, afinal?"
    show b5 angry
    b5 "Isso não teria acontecido se tivéssemos decidido ser contadores!"
    show k annoyed
    k "Espere nas portas da mansão e me agradeça depois."
    hide b3 with dissolve
    show k angry at mid with dissolve
    k "É hora do show, pessoal, vamos trabalhar!"
    play sound GroupRun
    hide b1 with dissolve
    hide b2 with dissolve
    hide b3 with dissolve
    hide b4 with dissolve
    hide b5 with dissolve
    hide k with dissolve
    stop sound
    stop music
    play music CarpeDiem
    "Fui andando até as portas."
    play sound Intercom

    k "Ei [name]! Você pode me ouvir?"
    with vpunch
    "A voz de Kat ecoou pela ilha, embora ela não estivesse à vista."
    m "...Kat?"
    k "Eu não estava brincando quando disse que estaria com você em cada passo do caminho."
    k "Enquanto você estiver nesta ilha, eu poderei ver, ouvir e até falar com você."
    k "Pense em mim como um 'Big Brother' mais fofo e sexy."
    m "Isso não parece tão bom quanto você pensa."
    k "Ei, de que outra forma poderíamos filmar o show?"
    k "Você realmente quer conhecer o amor da sua vida com uma câmera saindo da sua cabeça?"
    m "Boa ideia."
    k "De qualquer forma, vá para a mansão logo e encontre as garotas!"
    k "Eu recomendo dar uma olhada na biblioteca, na cozinha, na sala de jogos e no quintal. *Piscadela* *Piscadela* *Cutucada* *Cutucada*"
    k "De agora em diante, as câmeras estão gravando. Não seja idiota."
    k "Te vejo mais tarde, bochechinha! Kat fora."

    m "Tudo bem, finalmente estou aqui. Só falta uma coisa a fazer..."

    menu:
        "Abrir a porta":
            jump Open

label Open:
    jump MeetYui
