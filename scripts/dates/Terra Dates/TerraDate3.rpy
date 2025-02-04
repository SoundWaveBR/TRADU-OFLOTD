label TerraDate3:

play music LoveTheme
show bg GamesRoomMorning with dissolve
$ terraAffection=3

#; NNEEEEDS REWRITE!"
#; she needs to show you the completed game
"Encontrei Terra dormindo no sofá da Sala de Jogos."
"Ela parecia tão em paz."
"...Talvez eu volte mais tarde."
show t surprised at pos50t with vpunch
t "...Zumbis por todo lugar!!!!!! Ahhhhhhh!!!!!"
"Ela pulou de repente."

menu:
    "You okay?":
        jump td3_c1
    "Crazy dream?":
        jump td3_c2

label td3_c1:
m "Uau! Você está bem, Terra?"
show t worried
t "Onde, era apenas um sonho."
show t neutral
t "Estou bem agora, sem preocupações."
m "Parece que foi um sonho bem louco."
jump td3_pc

label td3_c2:
m "...Sonho louco?"

label td3_pc:

show t surprised
t "Sério! Sonhei que todos nós fomos transformados em zumbis."
show t happy
t "Felizmente, isso não tem como acontecer."
show t neutral
m "...Você foi dormir tarde?"
show t happy
t "Claro que sim! Passei a noite toda trabalhando no jogo."
show t neutral
t "E eu terminei também!"
show t happy
t "Você quer se juntar a mim para testar?"
show t blush
t "Eu, uh... adicionei alguns novos recursos que gostaria que você experimentasse."
m "Claro! Eu adoraria."
"Parecia o mesmo jogo que eu tinha jogado antes."
m "O que estou procurando?"
show t happy
t "Você verá!"
stop music
play music BlippyTrance
show bg LakeMorning with dissolve
"Eu comecei o jogo."
"Momentos depois, vi o avatar de Terra correndo até mim."
show t happy
t "Você chegou bem na hora, o novo evento está prestes a começar!"
m "Qual é o novo evento?"
stop music
play music RocketPower
"Como se fosse uma deixa, pombos robóticos gigantes voaram do céu e começaram a atacar nossos avatares."
m "Aggggghhh!!!!"

menu:
    "Corra pela minha vida":
        jump td3_c3
    "Lute contra os pombos":
        jump td3_c4


label td3_c3:
"Corri para salvar minha vida."
jump td3_pc2

label td3_c4:
"Corri em direção aos pombos, me preparando para a luta da minha vida."

label td3_pc2:

show t neutral
t "Não se preocupe, eu te peguei!"
"Terra pegou uma lata gigante de repelente de pombos e começou a atirar."
show t surprised
t "Uau! Acho que tem algo bugado, não está funcionando de jeito nenhum!"
show t happy
t "Acho que tenho que consertar isso. Hehehe..."
"Enquanto Terra ria do próprio erro, eu estava sendo erguido para o céu pelos pombos."
m "Uh... Acho que estou ferrado."
m "Para onde esses pombos estão me levando?"
"Tentei mover meu avatar, mas não havia como resistir ao aperto mortal do pombo robô."
show t neutral
t "Não se preocupe! Eles estão prestes a voar para o território do Dragão de Xarope de Bordo!"
m "O... o quê?"
show t worried
t "Uh oh."
show t surprised
"A tela se iluminou com uma explosão de xarope de bordo voador."
"...Eu nunca pensei que diria algo assim, mas aqui estamos."
"O xarope de bordo bateu nos pombos e uniu suas asas com força."
"Como consequência, eles começaram a cair no chão em uma velocidade alucinante."
m "AaaaaaAAAAHHHH!!!"
m "Salve-me, eu ainda não tinha salvado!"
show t surprised
t "Ah, eu sabia que tinha esquecido de algo! Esqueci de adicionar a capacidade de salvar."
show t happy
t "Vou ter que anotar isso!"
"Enquanto Terra tomava notas, eu rapidamente caí na minha desgraça."
m "Estou feliz por você, mas se você pudesse por um minuto -"
play sound Hit
with vpunch
"Meu avatar caiu no chão, como um pombo, e morreu instantaneamente com o impacto."
m "Nossa, cara, eu tinha tanta coisa!"
show t neutral
m "Existe pelo menos uma mecânica de respawn? Eu nunca morri antes neste jogo."
show t happy
t "Claro!"
show t neutral
t "Basta apertar o botão 'Repetir'."
"Apertei o botão e vi o mundo ao meu redor voltar à vila, sem as feras gigantes da morte."
show t surprised
"Só que agora, a vila parecia dez vezes maior do que antes."
m "Espera, quando a vila ficou tão grande?"
"E então me dei conta."
m "Espera... não foi a vila que ficou grande."
with vpunch
m "Fiquei pequeno!!!"
"Olhei com mais cuidado para o meu avatar."
"...Eu era um pombo novamente."
"Suspirei profundamente."
show t happy
"Ao mesmo tempo, Terra estava rindo como uma criança."
#...Pigeons, man."
hide t with dissolve

"Passamos mais algumas horas testando o restante dos novos recursos do jogo."
"Felizmente, não houve mais ovos de páscoa de pombos."
stop music
play music LoveTheme
show bg LakeMorning with dissolve
show t blush at pos50t with dissolve
t "Há, uh... uma última coisa que eu quero testar, se estiver tudo bem?"
m "Isso vai acabar comigo sendo transformado em um pombo?"
show t surprised
t "Nã-ã-ã-ã-ã-o..."
show t happy
t "Só venha comigo!"
"Eu segui o avatar dela até a cabana que dividíamos na floresta."
show t blush
"Quando chegamos lá, ela se virou, veio até mim e me mostrou um item que eu nunca tinha visto antes."
hide t with dissolve
show bg TerraProposal with dissolve
"Ela veio até mim e me deu um item chamado {i}Anel de Você é Bem Legal{/i}."
m "...O que é isso?"
#show t surprised
t "Hum. Deixe-me tentar explicar!"
#show t happy
t "...Eu vim para esse programa sem ter a mínima ideia do que se tratava."
t "Pessoalmente, eu achei estúpido no começo."
t "Mas... sair com você tem sido muito divertido."
t "Eu nunca consegui trabalhar meus hobbies com ninguém, até te conhecer."
t "Sinceramente, eu nunca tive alguém para compartilhar todas as minhas loucuras, mas você... você é diferente."
t "Então... eu acho que o que eu estou tentando dizer é..."
t "...Você é bem legal, e eu espero que a gente possa continuar fazendo isso, mesmo depois que o programa acabar."

menu:
    "Eu adoraria":
        jump td3_c5
    "Parece um plano":
        jump td3_c6

label td3_c5:
m "Eu adoraria, Terra."
m "Você nem precisa pedir!"
jump td3_pc3

label td3_c6:
m "Parece um plano, Terra."

label td3_pc3:

m "Tenho que dizer que você me pegou desprevenido com isso."
show bg LakeMorning with dissolve
show t surprised at pos50t with dissolve
t "Por que isso?"
m "Você me dar esse anel, isso... uh, bem, pode ser um pouco enganoso."
show t blush
t "V-você não está fazendo sentido algum!"
show bg GamesRoomEvening with dissolve
"Nós rimos juntos, então voltamos para a mansão com um salto em nossos passos."
"Nós brincamos o dia todo, sem nenhuma preocupação no mundo."

if playthrough == 1 and currentDay == 6:
    jump LastDateTerra
elif playthrough == 2 and currentDay == 9:
    jump LastDateTerra
else:
    jump NotLastDateTerra

label LastDateTerra:

show t neutral
t "...Bem, chega de jogos por hoje!"
show t happy
t "Você está a fim de um encontro no cinema?"
m "Claro! O que você quer assistir?"
show t surprised
t "Que tal... uau."
stop music
play music Smile
play sound Shutdown
"E então vi algo que nunca tinha visto antes - e nunca mais veria."
show t worried
show bg GamesRoomNight with dissolve
"O céu lá fora rapidamente mudou de laranja para preto, como se fosse água sendo afogada na tinta mais escura."
show bg Black with dissolve
show t surprised
hide t with dissolve
"Então o sol brilhante no céu... se apagou, como uma vela ao vento."
t "Uau! O que está acontecendo?"
"Ela segurou minha mão com força - eu podia sentir que ela estava assustada."

play sound GroupRun

"Não tive a chance de responder antes de ouvir uma onda de passos vindo em nossa direção no escuro."
"Algo não está certo - Oh, não."
"Estávamos cercados."
stop sound #@stopsfx GroupRun

"Uma voz familiar cortou o curto silêncio em que prendi a respiração."
q "Sinto muito, [name]. Você só... não conseguiu."
"Temos que sair daqui."
q "...Só faça isso rápido, por favor."
t "[name], estou com medo, o que está acontecendo!?"
"Apertei a mão dela o mais forte que pude."
m "Precisamos sair daqui, vamos!"
play sound Hit
"Eu nem dei 3 passos antes de ser derrubado e algemado nas costas."
play sound Handcuffs
t "[name]! Espere, eu vou -"
"Eu gritei para ela correr, mas ela voltou para tentar me ajudar."
m "Terra, você tem que sair daqui, eu -"
"Ela gritou - eles devem tê-la pegado."
"Não adiantou. Mesmo que ela estivesse bem na minha frente, eu não tinha forças para chegar nem um centímetro mais perto."
play sound Handcuffs
"Eles a derrubaram em um instante. Ouvi o tilintar das algemas enquanto a arrastavam para longe."
"Lutei com todas as minhas forças para me levantar, para salvá-la, para correr... pelo que pareceu uma eternidade."
"Então... nada."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending

label NotLastDateTerra:

show t neutral
t "...Bem, chega de jogos por hoje!"
show t happy
t "Você está a fim de um encontro no cinema?"
m "Claro! O que você quer assistir?"
show t neutral
t "É um filme do Hitchcock! Sempre quis vê-lo."
m "Como se chama?"
show t happy
t "...Os Pássaros."
"...Senti um vaso sanguíneo estourar na minha cabeça."
"Essa mulher faz mal para o meu coração."
"...Mas ela nunca deixa de colocar um sorriso no meu rosto."
$ terraAffection=3
jump postDateSelector
