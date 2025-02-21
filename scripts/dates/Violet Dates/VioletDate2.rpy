label VioletDate2:

show bg MansionMorning with dissolve
play music JazzBrunch
$ violetAffection=2

show v neutral at pos50v with dissolve
"Encontrei Violet dando uma volta do lado de fora da mansão."
m "Ei, Violet, o que houve?"
show v happy
v "Olá, [name]. Só pensei em dar uma boa caminhada à tarde. Este lugar realmente traz lembranças de casa."
m "Você morava em sua própria ilha particular?"
show v laugh
v "Nada tão... burguês."
m "De qualquer forma, tenho uma surpresa para você. Quer ver?"
show v surprised
v "Para mim? Eu..."
show v neutral
"Fiz sinal para que ela me seguisse até a mansão."
show bg MansionIndoorsMorning with dissolve #time:1
$ renpy.pause(delay = 1.0, hard = False)
show bg KitchenMorning with dissolve #time:1
show v surprised
stop music
play music CrinolineDreams
m "Pedi para Kat mexer alguns pauzinhos e, bem... agora temos tudo o que precisamos para assar o que quisermos."
show v happy
v "Oh meu..."
"Violet olhou para mim com uma admiração infantil em seus olhos."
show v laugh
v "Vamos direto ao assunto, por que não?"
"Ela estava praticamente tremendo de excitação. Seu sorriso e risada eram positivamente contagiosos."
show v happy
"Decidimos fazer um bolo de chocolate. Era o sabor favorito dela, e eu não lembro do meu."
"Dito isso, eu também não lembro de nada sobre como fazer bolos... mas com Violet, isso não era um problema."
show v laugh
"Ela me colocou no ritmo com uma mão suave e firme, e em pouco tempo, tínhamos o bolo no forno, assando."
"Gostaria que demorasse mais para fazer. Ver Violet fazer o que ela mais amava foi um deleite."
"Quando ela tirou o bolo do forno, parecia uma criança no dia de Natal."
hide v with dissolve
show bg VioletBaking with dissolve
v "Agora, só para os retoques finais...! Um pouco mais aqui, um pouco mais ali..."
"Ela estava em seu próprio mundo, cantarolando enquanto dançava ao redor do bolo, decorando-o conforme avançava."
"Eu não pude deixar de sorrir e observá-la em adoração."
"Ela é pura felicidade agora. Eu queria poder aproveitar este momento e congelá-lo no tempo, para mantê-lo seguro."
v "Mal posso esperar para compartilhar isso com os outros!"
v "Mas primeiro... [name], você se importaria em testar?"
m "Você não precisa perguntar, acredite em mim! Eu sou o primeiro da fila para experimentar."
show bg KitchenMorning with dissolve
show v worried at pos50v with dissolve
v "Obrigado, eu só... não tenho certeza se o que eu faço vale a pena comer... ou não."
m "Por quê?"
show v happy
v "A cuidadora da minha família, Shirley, foi quem me ensinou a cozinhar."
show v neutral
v "Além da minha irmã, Shirley foi a única que se preocupou em experimentar o que eu fiz."
show v worried
v "...Às vezes me preocupo que me disseram que é delicioso só para me fazer sentir melhor."
"Tirei um pouco do topo do bolo dela com meu dedo e lambi."
m "É delicioso, Violet. Pode acreditar!"
show v blush
v "...Você quer me ajudar um pouco mais? Estou me divertindo muito para parar agora."
show v laugh
v "Acabei de começar a fazer alguns biscoitos e acho que gosto bastante da sua companhia e ajuda, [name]."
m "Eu adoraria! Me diga como posso ajudar."
"Violet me passou uma tigela cheia de massa de biscoito, depois uma bandeja."
show v happy
v "Tudo o que você precisa fazer é moldar pequenos pedaços dessa massa em formato de biscoito e colocá-los na assadeira."
show v worried
v "Tente não colocar nenhum deles muito perto um do outro na bandeja, ou ele se tornará algo como um biscoito mutante no forno."
m "Entendi. Nenhum biscoito mutante aqui."
"Eu arranquei um pedaço de massa da tigela e enrolei no tamanho e formato de um biscoito."
show v laugh
v "Perfeito. Você tem um talento natural."
m "Obrigado, Violet! Eu..."
"Uau."
"No tempo que levei para fazer um, Violet fez seis biscoitos perfeitos."
"Ela se movia com eficiência mecânica enquanto amassava bolas de massa em biscoitos de formato perfeito."
m "Uau. Eu achava você ótima antes, mas você é realmente incrível. Há quanto tempo você faz isso?"
show v neutral
v "Talvez... desde que eu tinha, digamos, cinco anos?"
show v happy
v "Até hoje, continua sendo a única coisa em que consigo superar minha irmã."
"Acabei de fazer outro biscoito enquanto Violet terminava mais três."
show v neutral
"Ela levantou um dos biscoitos e o levou até o rosto."
show v happy
v "Você se tornou bastante habilidoso nisso, [name]."
show v laugh
v "Só queria dizer de novo... obrigada por organizar isso. Estou no topo do mundo agora."
m "Foi um prazer, Violet."
"Nossa, ela fica adorável quando sorri."
"Por alguns segundos, continuamos trabalhando nos biscoitos em um silêncio amável, nossos olhos fixos um no outro."
m "Você disse que tinha uma irmã?"
show v happy
v "Sim, de fato! Viola Valentine. Primeiras gêmeas na família. Ela..."
show v surprised
v "Oh, I'm out of my room on my tray."
show v laugh
stop music
play music TheShowMustBeGo
"Ela lançou um sorriso malicioso na minha direção, logo antes de atirar levemente uma bola de massa no meu rosto."
m "O que há com essa atrevida -"
play sound Hit
show v laugh
with vpunch
"Antes que eu pudesse reagir, ele espirrou e grudou no meu rosto."
"Ela caiu na gargalhada infantil."
v "Boa pegada, [name]! Talvez você possa tentar usar as mãos da próxima vez?"
m "Ah, está ligado."
show v happy
"Não consegui parar de sorrir enquanto pegava um pouco de 'munição' da minha própria bandeja de biscoitos e jogava nela."
play sound Whoosh
show v neutral at pos30v
show v happy  at pos50v
"Ela os desviou com facilidade e riu."
show v laugh
v "É bem engraçado como um velho zelador conseguiu fazer o que você está lutando para fazer agora."
"Eu interrompi sua alegria com outro arremesso de bola de massa."
show v surprised
play sound Hit
with vpunch
"Dessa vez, fez um 'SPLAT!' satisfatório contra sua bochecha esquerda."
m "BATIIIIIIIIII!!!!!!!"
show v serious
v "Ah... você está indo muito mal."
show v laugh
"Seu sorriso se tornou diabólico quando ela pegou outra bola de massa."
"Oh merda."

menu:
    n "Tenho apenas um segundo antes do próximo ataque dela, eu..."

    "Vá para a ofensiva":
        jump vd2c1
    "Fique na defensiva":
        jump vd2c2

label vd2c1:

play sound Hit
with vpunch
"Eu estava começando a pegar outra bola de massa da bandeja quando uma bola de massa espirrou na minha testa, me fazendo recuar para trás."
m "Ahhh!!!!"
jump vd2pc2

label vd2c2:
"Eu me abaixei atrás do balcão da cozinha."
"Um instante depois, uma bola de massa voou sobre minha cabeça."
m "Hah! Legal -"

play sound Hit
with vpunch
"Enquanto eu estava me gabando, Violet jogou uma bola de massa que espirrou na minha testa."
m "Aghhh!!!"

label vd2pc2:

with vpunch
play sound Hit
"E então outro pousou, bem ao lado dele."
m "Ahhhh!!!!! Misericórdia!!"
with vpunch
play sound Hit
"E então outro."
"Eu caí no chão em derrota."
show v laugh
v "Eu declaro isso... minha vitória, em absoluta confiança!"
"Ela riu enquanto apontava para toda a massa no meu rosto."
"Aproveitei a oportunidade para interromper seu discurso com outra bola de massa."
show v surprised
play sound Hit
with vpunch
"Atingiu bem na bochecha esquerda dela."
show v laugh
v "Esqueça sobreviver a esse programa de TV maluco - não sei se vou sobreviver aos próximos cinco minutos."
"Foi como olhar um tigre nos olhos."
"Violet recarregou sua munição e estava se preparando para outro arremesso."
"Foi tudo o que pude fazer para alcançar mais uma bola e gritar em desafio."
m "VAMOS LÁ!!!!!!!!"
play sound Explosion
"..."
"Alguns dizem que você ainda pode ouvir meus gritos naquela cozinha até hoje."
"..."
stop music
play music CrinolineDreams
"Terminamos de limpar depois da nossa guerra de comida improvisada e trouxemos as sobremesas que sobreviveram à grande guerra para a varanda."
"Seu sorriso e risada eram contagiantes."
show v laugh
v "Desculpe-me, mas acho que podemos descartar a possibilidade de você ser um jogador de beisebol antes de vir para esta ilha."
"Ela colocou a mão carinhosamente no meu rosto enquanto limpava um pouco da massa restante."
"Nós nos olhamos novamente. Os olhos dela eram praticamente magnéticos."
show v happy
v "Obrigado por participar, [name], eu... acho que já faz muito tempo que não me divirto tanto."
show v blush
v "Então... obrigada por satisfazer meu pequeno capricho."
m "Foi muito divertido para mim também, Violet. Não mencione isso."
m "Além disso, acho que consegui algumas boas tacadas para valer a pena."
show v laugh
v "Estou preocupada com você! Parece que sua amnésia está piorando ainda mais!"
"Violet riu enquanto pegava mais algumas migalhas do meu rosto e as lambia do dedo."
show v blush
"Seus olhos pareciam permanecer nos meus."
show v happy
v "Espero que possamos passar mais tempo juntos em breve, eu... gostei bastante disso."
m "Eu gostaria disso, Violet. Eu me diverti muito com você também."
m "Você é cheia de surpresas, sabia?"
show v laugh
v "Espere e veja, tem mais de onde isso veio!"
"Passamos o resto do dia conversando e comendo pequenas sobremesas juntos na varanda."
"Embora Violet parecesse bem distante quando a conheci, aprendi que a verdadeira Violet não era nada disso, e cheia de surpresas."
"Ela podia ser inesperadamente tímida em um momento, então travessa como uma criança em outro."
"Uma coisa é certa - estar perto dela faz meu coração pular uma batida, e o tempo voar."
hide v with dissolve
show bg Black with dissolve
"Antes que eu percebesse quanto tempo havia passado, já estava escuro como breu lá fora."
$ violetAffection=2
jump postDateSelector
