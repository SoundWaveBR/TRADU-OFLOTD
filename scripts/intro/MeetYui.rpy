label MeetYui:

$ meetYui=1
show bg MansionIndoorsMorning with dissolve
play music Wholesome
m "Alguém em casa?"
show y worried at pos50y with dissolve
"Meus olhos foram atraídos por uma garota usando um vestido branco, andando de um lado para o outro no saguão."
m "Ei, eai?"
show y surprised
q "Uau! Não vi você aí, me desculpe!"
show y laugh
q "Meu Deus! É você mesmo, [name]!"
m "Sou eu! Como você sabia meu nome?"
show y surprised
q "Não faz tanto tempo assim, né?"
show y happy
y "Sou eu, Yui! Yui Fushikawa!"
m "...?"
show y neutral
y "Nós estudamos na mesma escola antigamente?"
m "Como assim?"
show y annoyed
y "Yeep! Você não mudou nada!"
y "Sempre esquecendo tudo que é importante!"
show y angry
y "GRRRRRR!!!"
m "Espera, se acalma! Eu sei como parece, mas estou com amnésia!"
show y annoyed
y "Você não ache que eu vou acreditar em você né?"
show y angry
y "Você não pode mentir para o presidente do seu conselho estudantil! Isso é perjúrio!"
m "É verdade, sério! Eu não mentiria sobre isso."
show y worried
y "...Você realmente não consegue se lembrar de nada?"
m "Sério. Eu não brincaria sobre isso, prometo."
show y sad
y "...Oh."
show y angry
y "Eu não acredito que você se esqueceu -"
show y blush
y "...!"
y "Pensando bem, isso pode ser uma coisa boa!"
m "Como diabos pode ser bom esquecer tudo?"
show y annoyed
y "Você sabe, seguir em frente é a melhor maneira de viver, e tudo mais!"
show y happy
y "Todo mundo tem coisas do ensino médio que prefere esquecer, certo?"
show y blush
y "Ha. Ha. Ha."
show y shy
y "Sim, sim, sim. Mmhm."
show y happy
y "Heh heh heh. É bom ver você, [name]. Você não mudou."
show y laugh
y "É como quando costumávamos brincar naquela época."
show y blush
y "Er... brincar, como se fosse um jeito familiar! Promessa de mindinho!"
m "É bom ver você também, Yui."
m "O que te traz aqui?"
show y happy
y "Ah, você sabe."
show y neutral
y "Para ser honesto, aplicativos de namoro ou programas e tudo isso realmente não são minha praia."
show y laugh
y "Mas eu vi que você estava..."
show y blush
y "...!"
show y angry with vpunch
# with vpunch # Yui,1

y "O que você está me fazendo dizer!!"

show y neutral
y "Hum, além disso, bem-vindos à mansão!"
show y surprised
y "É gigantesco."
show y annoyed #at pos50y
y "Vou poupá-lo da vergonha de me perguntar e lhe mostrar onde fica meu quarto."
show y surprised
y "Ah, espere um segundo! Eu ainda não limpei!"
play sound Whoosh
hide y with dissolve

"Ela saiu correndo antes que eu pudesse dizer uma palavra. De alguma forma, tenho a sensação de que isso já aconteceu antes."
"Acho que a verei mais tarde."

menu:
    n "Eu deveria voltar a explorar a casa. Para onde vou agora?"

    "A Biblioteca":
        jump MeetScarlett
    "A Cozinha":
        jump MeetViolet
    "A Sala de Jogos":
        jump MeetTerra
    "O Quintal":
        jump MeetAllie
