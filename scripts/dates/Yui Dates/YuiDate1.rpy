label YuiDate1:

show bg Hills with dissolve
$ yuiAffection=1

play music Meadow

"A floresta ao norte da casa era tão serena quanto possível."
"A cada passo à frente, eu sentia a terra macia ceder sob meus pés, e o vento acariciar minha pele."
"Verde até onde os olhos podem ver... e ela, em um vestido branco esvoaçante, parada no meio de tudo."
show y happy at pos50y with dissolve
y "Ei, [name]. O que você está fazendo aqui fora?"

menu:
    "Eu estava procurando você":
        jump yd1c1
    "Eu ia te perguntar a mesma coisa":
        jump yd1c2

label yd1c1:
m "Eu estava procurando por você, Yui."
show y laugh
m "Eu esperava que poderiamos passar um tempo juntos."
show y happy
y "Então me considere a garota mais sortuda do mundo!"
"Yui tinha uma risadinha fofa, do tido que coloca um sorriso no seu rosto instataneamente."
show y happy
y "Bem, você me encontrou agora."
show y laugh
y "Se importa de se juntar a mim para uma caminhada?"
m "...Eu adoraria."
jump yd1pc

label yd1c2:
m "Eu ia te perguntar a mesma coisa."
show y laugh
y "Acho que sim!"
"Yui tinha uma risadinha fofa, do tido que coloca um sorriso no seu rosto instataneamente."
show y happy
y "Se importa de se juntar a mim para uma caminhada?"
m "...Eu adoraria."

label yd1pc:

hide y with dissolve
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True)
show bg YuiInField with dissolve # time:1
"Nós começamos a andar floresta a dentro."
"Eu não pude deixar de ficar fascinado pelo cabelo dela, fluindo como água ao vento."
#show y neutral
y "Eu duvido que você se lembre, mas..."
#show y laugh
y "Eu sou do interior. Cresci cercada por animais, natureza, você nomeia!"
#show y happy
y "Era só eu, minha avó, minhas irmãs, as alpacas, meus coelhos Bun e Bunbun, as galinhas, e... muitos animais de fazenda para contar!"
#show y happy
y "Para responder sua pergunta de antes... a natureza me leva de volta para casa."
m "Você ainda mora lá?"
#show y laugh
y "Sim! Não teria de outra forma."

#show y neutral
y "Embora eu tenha me mudado para a cidade por um tempo, lá atrás."
#show y happy
y "Você sabe, você sabe, foi quando eu te conheci!"
m "Como nos conhecemos?"
#show y neutral
y "Bem..."
stop sound
show bg Hills with dissolve
show y sad at pos50y with dissolve

y "Sabe, uma coisa que eu odiava na cidade... é que todo mundo está sempre com pressa."
show y serious
y "As pessoas simplesmente passam umas pelas outras como se fossem obstáculos a serem superados, em vez de... bem, pessoas."
show y sad
y "Eu vim para a cidade sozinha. Não sabia a minha esquerda da direita."
show y laugh
y "E... eu me perdi! Eu juro que todos os prédios parecem iguais."
m "Você pode dizer isso de novo."
show y sad
y "Eu tentava perguntar às pessoas direções para onde eu moraria, ou onde era a escola, mas ninguém me dava a hora do dia."
show y blush
y "Exceto por você."
m "Eu te ajudei?"
show y laugh
y "Sim. Você nem me conhecia, mas tirou um tempo para me ajudar a encontrar meu caminho."
show y blush
y "Nossa, eu nunca fiquei tão envergonhada na minha vida."
m "Por que você ficou envergonhada?"
show y neutral
y "Uh... você sabe."
show y blush
y "Hehe. Tímida."
m "?"
show y neutral
y "Descobrimos depois que estudamos na mesma escola, mas nunca conversamos muito depois disso."
m "Aw, sinto muito por isso."
show y surprised
y "Ah, não foi sua culpa, [name]! Eu tive que voltar para casa pouco tempo depois, de qualquer forma."
m "Bem, estou feliz por ter uma segunda chance de te conhecer melhor, Yui."
show y happy
y "Eu sinto o mesmo, [name]!"
show y blush
y "Você é exatamente como eu me lembro."
show y surprised
y "Bem, na verdade, toda essa história de tentar namorar 5 garotas ao mesmo tempo surgiu do nada, mas... a vida é cheia de surpresas, eu acho."
show y laugh
stop music
play sound MysteryPiano
y "Não deve demorar muito para removê-las da equação."
m "Desculpe, o que você disse? Eu não consegui ouvir."
play music Meadow
show y shy
y "Era só uma piadinha. Hehe..."
show y neutral
y "Eu só estava dizendo, estou tão feliz por te ver novamente!"
show y happy
y "Um brinde ao futuro!"
show y laugh
"Nós passamos o resto do dia aproveitando a natureza e compensando o tempo perdido."
"Aparentemente, eu sempre acabava me metendo em encrenca naquela época."
show y happy
"Eu acho que não mudou muito..."
"Algo sobre a Yui tornava tão fácil se abrir. Eu me peguei quase contando a verdade sobre o show várias vezes."
"Mesmo que eu não pudesse contar a ela toda a verdade, eu poderia contar a ela apenas o suficiente do que estava me preocupando para me fazer sentir em casa e à vontade."
show y laugh
y "O que quer que esteja te incomodando... tenho certeza de que tudo ficará bem."
show y happy
y "Não importa o que aconteça... eu estou do seu lado, [name]."
$ yuiAffection=1
jump postDateSelector
