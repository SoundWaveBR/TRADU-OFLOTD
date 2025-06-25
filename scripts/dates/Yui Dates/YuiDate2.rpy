label YuiDate2:

show bg Hills with dissolve
play music Meadow
$ yuiAffection=2

"Eu podia ver Yui acenando para mim do topo da colina."
show y happy at pos50y with dissolve
y "Oi, [name]! É bom te ver de novo!"
m "É bom te ver também, Yui!"
m "Você queria me mostrar algo?"
"Agora que eu estava mais perto, pude ver que Yui estava segurando uma mão atrás das costas."
show y laugh
y "Acredite, é a coisa mais incrível que você já viu."
show y angry
y "Eis!!!!"

hide y with dissolve
stop music
play music LoveTheme
show bg YuiHoldingBunny with dissolve

y "É um coelhinho!!!"
"Era de fato um coelhinho."
m "De onde veio esse pequeno?"
#show y surprised
y "Para ser honesta, não faço ideia."
m "Eu me pergunto se ele é um selvagem, ou talvez o animal de estimação de alguém."
#show y worried
y "Eu perguntei por aí, mas não parece que ele pertença a ninguém."
#show y neutral
y "Então, eu... eu tenho cuidado dele desde que o encontrei."
#show y laugh
y "Eu simplesmente não consegui me controlar, sabe?"
"A expressão de Yui era tão sincera quanto poderia ser."
m "Você não tinha um coelhinho de estimação em casa?"
#show y happy
y "Eu tinha dois! Bun e Bunbun!"
#show y surprised
y "Ambos eram uns travessos. Mas Bunbunbun aqui é um bom garoto, não é?"
"Ela esfregou a cabeça de Bunbunbun."
#show y happy
y "Sim, você é ~
Nuzzle, nuzzle. (Ela esfregou o nariz contra o coelho.)"
"Nós brincamos com o coelhinho por um tempo."
"Ela pegou o coelhinho e o segurou em seus braços. Bunbunbun parecia bastante contente."
m "Você sabe, você é incrível com animais, Yui."
show bg Hills with dissolve
show y laugh at pos50y with dissolve
y "Bem, eu estive cercada por animais a minha vida toda!"
show y neutral
y "De volta para casa, bem... para ser honesta, era mais um celeiro do que qualquer outra coisa."
show y happy
y "Como minhas irmãs eram muito novas, e minha avó já estava ficando velha, eu cuidava de todos os animais."
show y neutral
y "A vovó cuidou deles desde que nasceram."
show y sad
y "Meus pais deveriam cuidar deles depois que a vovó se aposentasse, mas..."
show y happy
y "Bem, você sabe... a vida acontece. Eu só estou feliz por ter o que tenho."
show y surprised
y "Ah!"
"Bunbunbun conseguiu escapar de suas mãos e saiu correndo."
show y angry
y "Temos que pegá-lo! Vamos!"
m "Estou indo!"
"Eu corri o mais rápido que pude atrás de Bunbunbun, mas não adiantou - a distância só aumentava."
"Antes de muito tempo, não conseguimos nem vê-lo mais."
show y worried
m "Desculpe, eu não consegui pegá-lo... ele é realmente rápido, para algo tão pequeno."
show y happy
y "Ah, não se preocupe com isso! Bunbunbun gosta de fazer isso o tempo todo. Ele é um pouco travesso, mas não fará nada perigoso."
show y laugh
y "Podemos levar nosso tempo procurando por ele."
show y neutral
y "Se você estiver disposto a ajudar!"
m "Claro, Yui!"
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) #loop:true
"Nós começamos a andar em direção aonde vimos Bunbunbun pela última vez, logo depois que recuperamos o fôlego."
show y happy
y "Nossa... não é tão bom estar lá fora? O cheiro do ar fresco, a brisa?"
show y laugh
y "Não há nada como isso!"
m "Realmente não há!"
"Eu sorri."
show y happy
stop sound
y "No começo, eu estava realmente animada para ir para a cidade."
show y neutral
y "Há tantas pessoas, tantas coisas para fazer, tantas coisas bonitas..."
show y happy
y "...E, acima de tudo, eu conheci você!"
m "Ah, você vai me fazer ficar vermelho."
show y laugh
"Ela riu e tocou meu braço."
show y neutral
y "Mesmo assim, a cidade simplesmente não é a minha praia."
show y sad
y "...É um pouco engraçado. Embora a razão pela qual eu tive que voltar para casa de repente fosse terrível, eu... uma pequena parte de mim estava feliz por estar em casa."
show y neutral
y "Você já teve esse tipo de sentimento antes?"
m "Eu já. É estranho, mas às vezes, há coisas boas no ruim - e às vezes, essa coisa boa pode superar a ruim."
show y laugh
y "Exatamente. Você entende, [name]."
show y happy
y "Minha família nunca esteve tão unida."
show y laugh
y "E isso é tudo o que eu quero."
show y neutral
y "Eles me disseram para ganhar muito dinheiro na cidade... fazer algo de mim mesma, tudo isso."
show y worried
y "Pode parecer... antiquado, mas eu só quero colocar as pessoas que amo em primeiro lugar."
show y happy
y "Isso é tudo o que realmente importa na vida!"
show y neutral
#y "I'm curious... what do you put first in life?"

menu:
    y "Estou curiosa... o que você coloca em primeiro lugar na vida?"

    "Família":
        jump Family
    "Carreira":
        jump Career
    "Felicidade":
        jump Happiness

label Family:
m "Isso teria que ser família, sem dúvida."
jump AfterValue

label Career:
m "Isso teria que ser minha carreira."
jump AfterValue

label Happiness:
m "Felicidade. Se você não tem isso, o que você tem?"
jump AfterValue

label AfterValue:

show y happy
y "Oh, é mesmo!"
show y laugh
y "Acho que formaríamos uma ótima equipe, então."
"Nós conversamos por várias horas sobre o que queríamos da vida. Parecíamos combinar perfeitamente. Eu estava radiante o tempo todo."
"Era difícil acreditar que -"
show y surprised
stop sound # stopsfx
y "É Bunbunbun!!"
"Yui apontou para frente, e com certeza, lá estava Bunbunbun, mordendo um arbusto."
show y angry at pos95y #used to be 100
play sound Whoosh
"Eu nunca vi ninguém se mover tão rápido - Yui desceu sobre Bunbunbun como uma águia e o agarrou em um instante."
show y annoyed  at pos50y with easeinright
y "Você vai voltar para sua toca, você coelhinho travesso!"
show y happy
y "Mas estou feliz que você está seguro."
"Ela esfregou o rosto contra o pelo dele. Bunbunbun estava praticamente ronronando de alegria."
show y blush
"Então ela olhou bem para mim."
show y happy
y "Eu não posso prometer que poderia te dar a vida mais emocionante, com as reviravoltas mais inesperadas a cada esquina..."
show y neutral
y "Mas eu posso prometer que, se você me escolher, eu sempre estarei ao seu lado. Não importa o que aconteça."
show y blush
y "Onde quer que você esteja... eu viria correndo, sempre."
"Ela deu um passo em direção a mim e beijou minha bochecha."
"Nós nos encaramos, e por aquele momento, tudo o que eu podia ver era ela, e quão bonita ela era."
show y happy
"Bunbunbun parecia estar um pouco com ciúmes depois disso."
show y laugh
y "Obrigado novamente pela ajuda, [name]. Estar com você fez tudo isso acontecer muito mais rápido... e tornou tudo realmente especial para mim."
m "A qualquer momento, Yui. Estou feliz em ajudar."
"Nós voltamos juntos para a mansão, de mãos dadas e sorrindo o tempo todo."
jump postDateSelector
