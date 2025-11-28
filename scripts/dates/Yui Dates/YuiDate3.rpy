label YuiDate3:



show bg RoomMorning with dissolve
$ yuiAffection=3
play music AlmostNew
"Eu podia ver Yui da janela do meu quarto, andando pela frente da mansão. Parecia que ela estava procurando algo."
"Eu praticamente pulei escada abaixo e corri para fora para vê-la."
show bg MansionMorning with dissolve
show y happy at pos50y with dissolve
y "Oi, [name]!"
show y surprised
y "Qual é a pressa? Você parece estar com bastante pressa!"
m "Eu só queria te ver um pouco mais cedo."
show y blush
y "Gosh, isso é realmente doce da sua parte."
show y happy
y "Eu também estava querendo te ver, uh..."
show y neutral
y "Eu estive pensando muito desde que você me ajudou a pegar o Bunbunbun."
m "Ah, como está o grande Bunbunbun?"
show y surprised
y "Ah, agora que eu penso nisso! É por isso que eu vim aqui fora!"
show y worried
y "Ele saiu correndo para cá, e eu estava tentando alcançá-lo."
show y laugh
y "Embora isso já tenha acontecido algumas vezes, e cada vez, ele acaba de alguma forma de volta no meu quarto."
m "Estou certo de que ele está bem, eu não me preocuparia."
show y happy
y "Eu simplesmente não consigo me controlar, sabe?"
m "Você é uma pessoa realmente doce, Yui. Eu amo isso em você."
show y blush
y "...Você também é, [name]."
show y happy
y "Você tem tempo hoje para sair? Tem algo que eu gostaria de fazer com você."
m "Claro que tenho, por você."
show y shy
y "Mesmo que... seja um pouco chato?"
m "Tenho certeza de que não pode ser tão chato se for com você, sabe?"
m "O que quer que seja, estou dentro."
show y happy
y "Okay! Aqui vamos nós!!"
show bg BeachMorning with dissolve
show y neutral
stop music
play music AlmostBliss
"E assim caminhamos juntos até a praia..."
"...e começamos a pescar, lado a lado."
show y happy
y "Ahhhh... agora isso é vida."
m "Eu tenho que admitir, isso não era o que eu esperava."
show y laugh
y "Esta foi, de longe, a melhor maneira de passar o tempo no campo!"
show y shy
y "Para ser honesta, eu não sou muito fã de atividades malucas, como paraquedismo ou passeios de compras."
show y happy
y "Eu prefiro passar meus dias tranquilamente, com a pessoa que amo, conversando do crepúsculo até o amanhecer."
show y laugh
y "Apenas aproveitando a companhia um do outro, sabe? Isso é o melhor."
show y worried
y "Está... está tudo bem para você?"
m "Claro que está, Yui."
m "Ter a chance de aprender mais sobre você, de experimentar as coisas que você gosta... é aí que está a verdadeira diversão."
m "Eu também prefiro isso a fazer coisas malucas o tempo todo."
m "Embora eu ache que passeios de compras não estão realmente na mesma categoria que paraquedismo."
show y laugh
y "Eles estão quando você vive no interior!"
m "Ei, você está a fim de uma pequena competição?"
show y happy
y "Claro! Vamos fazer isso! O que é?"
m "Quer ver quem consegue pegar mais peixes?"
show y laugh
stop music
play sound AnimeShine
y "..."
play music CarpeDiem
show y angry
y "Você está dentro! Hmph!"
"aparentemente, eu havia atiçado as chamas do espírito competitivo de Yui."
"Durante as próximas horas, continuamos com isso, enquanto desfrutávamos da conversa e da companhia um do outro."
show y surprised
"Yui era uma natural. Ela estava pegando peixes à esquerda e à direita."
show y neutral
"Cada vez que ela pegava um, ela o deixava de volta no oceano, e a cada vez, eu me perguntava quando meu primeiro iria morder."
"...Eu nunca acabei pegando um único."
show y happy
"Mas isso não importava. O que importava era que estávamos nos divertindo."
stop music
play music LoveTheme
show y neutral
y "Obrigado por me acompanhar, [name]."
m "Ei, eu também me diverti muito, Yui. Não se preocupe com isso."
show y laugh
y "Você não precisa mentir."
show y worried
y "Eu... sei que não sou como as outras garotas."
show y sad
y "Eu cresci sem nada, e... isso se reflete em como eu passo meu tempo, o que eu visto, tudo."
show y neutral
y "...Eu te amo tanto, você sabe?"
show y happy
y "Se eu tivesse você, eu te daria todo o amor do meu coração, a cada momento de cada dia."
show y blush
y "Eu realmente viveria pelo amor. Isso é o que sempre quis."
show y sad
y "Mas eu sei que nunca poderia te dar todas as coisas que todo mundo poderia. O dinheiro, o reconhecimento, a emoção."
show y worried
y "E eu me pego preocupada, e se você me escolhesse, e no segundo em que deixássemos esta ilha..."
show y sad
y "...Você percebe que eu não posso te dar a vida que você merece, e você começa a me odiar."
show y laugh
y "Eu... não sei o que eu faria se chegássemos a isso."
show y happy
y "Então, antes que isso aconteça, eu quero te perguntar."
show y blush
y "...Só eu seria o suficiente?"

if playthrough == 1 and currentDay == 6:
    jump LastDateYui
elif playthrough == 2 and currentDay == 9:
    jump LastDateYui
else:
    jump NotLastDateYui

label NotLastDateYui:

menu:
    "Sim":
        jump YuiYes
    "Não":
        jump YuiNo

label YuiYes:

$ YuiDate3Good=1
m "Claro que você seria o suficiente, Yui."
show y happy
m "Eu não preciso estar no centro das atenções, eu não preciso ser rico."
show y blush
m "Mais do que tudo isso... eu quero você, e apenas você."
show y blush
y "...Eu esperei tanto tempo para ouvir você dizer isso."
"Ela me puxou para perto e me beijou."
show y laugh
y "Eu te amo tanto. Eu sempre amei, e sempre amarei."
show y happy
y "Eu sempre colocarei nossa felicidade em primeiro lugar. Eu vou te fazer tão feliz todos os dias..."
m "Eu farei o mesmo, eu prometo."
show y laugh
y "Me belisque... eu devo estar sonhando."
m "Isso é o mais real que existe, Yui."
m "A partir de agora, será apenas eu e você."
show y blush
y "Eu... Eu simplesmente não consigo mais me segurar, [name]."
"Ela me empurrou para a areia quente da praia e se pressionou contra mim."
m "Yui..."
"Ela me beijou mais uma vez. Suas mãos se envolveram em torno de mim enquanto as minhas a puxavam para mais perto."
hide y with dissolve
y "Vamos compensar o tempo perdido, [name]..."
"O que aconteceu a seguir foi a imaginação ganhando vida."
"Eu perdi toda a noção do tempo e do mundo exterior - apenas Yui importava."
"...E eu não teria de outra forma."
jump postDateSelector

label YuiNo:

$ YuiDate3Good=0
stop music
play music Smile
"...Embora eu saiba como me sinto, não é preciso ser um gênio para dizer que isso seria uma péssima ideia para a audiência."
"Depois de tudo, quanto mais garotas estiverem na disputa, maiores serão as audiências."
m "...Claro que você seria o suficiente, Yui."
show y happy
m "Eu não preciso estar no centro das atenções, eu não preciso ser rico."
show y blush
m "Mais do que tudo isso... eu quero você, e apenas você."
show y blush
y "...Eu esperei tanto tempo para ouvir você dizer isso."
"Ela me puxou para perto e me beijou."
show y laugh
y "Eu te amo tanto, eu sempre amei, e sempre amarei."
show y happy
y "Eu sempre colocarei nossa felicidade em primeiro lugar. Eu vou te fazer tão feliz todos os dias..."
"...Desculpe, Yui."
m "A partir de agora, será apenas eu e você."
show y blush
y "Eu... Eu simplesmente não consigo mais me segurar, [name]."
"Ela me empurrou para a areia quente da praia e se pressionou contra mim."
m "Yui..."
"Ela me beijou mais uma vez. Suas mãos se envolveram em torno de mim enquanto as minhas a puxavam para mais perto."
"...Mas meu coração não está nisso."
$ yuiAffection=3

jump postDateSelector


label LastDateYui:

show y surprised
stop music
play music Smile
"...Minha respiração foi levada antes que eu tivesse a chance de dizer o que queria."
"Eu vi algo que nunca tinha visto antes - e nunca veria novamente."
hide y with dissolve
play sound Shutdown
"O céu rapidamente se transformou de um azul brilhante para o preto, como se estivesse sendo afogado na tinta mais escura."
show bg Black with dissolve
"Então o sol brilhante no céu... se apagou, como uma vela ao vento."
play sound GroupRun

"A última coisa que vi foi Yui gritando enquanto figuras sombrias a agarravam por trás."
stop sound #@stopsfx GroupRun
"Um segundo depois, estava tudo escuro. Eu não conseguia nem ver minhas mãos se estendendo para tentar salvá-la."
"Então eu senti alguém me agarrar por trás. Não, não era alguém - devia haver várias pessoas."
play sound Hit
"Eles me forçaram ao chão e me algemaram atrás das costas."
play sound Handcuffs
"Eu gritei, mas não havia som."
"Eu tentei lutar, mas não havia como escapar."
"Eu gritei por Yui, para que ela corresse o mais longe que pudesse - mas não ouvi resposta."
"Então... nada."

if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending
