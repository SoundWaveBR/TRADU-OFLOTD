
label AllieDate2:

show bg BeachMorning with dissolve
play music CarpeDiem
$ allieAffection=2

show a sassy at pos50a with dissolve
a "Oi Oi, [name]. Preparado para o round 2?"
show a laugh
a "Imaginei que você poderia querer ficar em algum lugar onde patins não funcionam!"
m "Ah, passei a noite toda sonhando com a próxima chance de usar essas duas pequenas máquinas de morte."
show a happy
a "Então acho que você vai adorar o que temos guardado para hoje! Não há rodas para onde estamos indo."
m "O que você quer dizer?"
show a neutral
a "Você verá. Vem comigo!"
show a surprised
a "Ah, primeiro preciso que você feche os olhos."
m "...Não tenho certeza se gosto de onde isso está indo."
show a laugh
a "Nada para se preocupar, [name]. Eu estarei bem ao seu lado o tempo todo."
m "Porque isso sempre deu certo."
show a happy
a "Não é mesmo?"
hide a with dissolve
show bg Black with dissolve
"Allie se moveu para trás de mim e cobriu meus olhos com as mãos."
a "Agora vamos continuar andando para frente. Confie em mim!"
$ renpy.sound.play("audio/sfx/walking_on_dirt.mp3", loop=True) # loop:true volume:0.6
m "Certo..."
"Eu estaria mentindo se dissesse que não estou gostando um pouco disso. Meu coração pulou uma batida quando ela colocou os braços em volta de mim."
"Eu cautelosamente dei um passo após o outro para frente."
stop sound
play sound Waves # loop:true volume:75
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)

"Primeiro, senti sujeira... depois areia... depois... água?"
m "Você está tentando me fazer me afogar?"
a "Claro que não! Embora, eu tenha que admitir, isso se parece muito com a forma como eles matavam as pessoas antigamente."
m "..."
a "Ah, você vai querer dar um passo bem alto para frente, ou vai doer."
play sound MetalImpact
"Levantei minha perna direita o mais alto que pude, então dei um passo à frente. Algo fez barulho, como metal."
play sound MetalImpact
"Em seguida, trouxe minha perna esquerda."
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)
a "Mantenha os olhos fechados por mais um segundo! Só preciso fazer uma coisa."
"Allie me soltou e deu alguns passos para frente."
a "Prepare-se!"
play sound Engine # loop:true
#; SOUND OF THE ENGINE
m "Espere, o que é -"
$ renpy.sound.play("audio/sfx/beach_waves.mp3", loop=True)

stop music
hide a with dissolve
show bg AllieBoat with dissolve
play music AlmostBliss
"Fui derrubado pelo movimento repentino e abri os olhos por reflexo."
"Água espirrou no meu corpo enquanto eu lutava para recuperar o equilíbrio."
#show a happy
a "Todos a bordo do S.S. St. Allie!"
m "...Quando e onde você conseguiu um barco?"
#show a laugh
a "Bem legal, né? Eu encontrei esse bebê nos fundos da mansão esta manhã."
m "Você acabou de 'encontrá-lo'?"
#show a neutral
a "...De qualquer forma, perguntei a Kat se eu poderia dar uma volta."
#show a happy
a "Ela disse que, se ficássemos a poucos passos da ilha, tudo bem, ou o motor desligaria automaticamente."
#show a laugh


menu:
    a "Então pensei: por que não dar uma volta pela ilha?"

    "Gostei do som disso":
        jump allieDatec1
    "O que poderia dar errado?":
        jump allieDatec2

label allieDatec1:
m "Gostei do som disso."
#show a happy
a "E lá vamos nós!"
jump ad1_post_choice

label allieDatec2:
m "O que poderia dar errado?"
#show a laugh
a "Não há graça em pensar nisso, não é?"
#show a happy
a "Então por que se incomodar!"
"Por que mesmo, pensei que a pessoa estava presa em um programa de namoro de vida ou morte."
jump ad1_post_choice

label ad1_post_choice:

"Nós navegamos pela ilha por um tempo, observando os diferentes edifícios que a cobriam."
"A mansão parecia tão pequena daqui."
"Horas voaram enquanto navegávamos."
show bg BeachEvening with dissolve
show a serious at pos50a with dissolve
stop music
play music TouchingMomentsOne
"Allie respirou fundo e suspirou."
m "Você está bem, Allie? Você não parece tão alegre como sempre."
#show a laugh
show a sad
a "...Acho que estou com um pouco de saudades de casa."
show a surprised
a "Não tem nada a ver com você, prometo! Eu só..."
show a worried
a "Só estou preocupado com meu velho."
m "Desculpe, seu pai não era...?"
show a serious
a "Ah, sim, ele se foi há muito tempo. Você conhece a velha história sobre a Nova Ásia."
show a neutral
a "Estou falando do Bill. Ele era um bom amigo do meu pai e cuidou de mim e de muitas outras crianças."
m "Parece um cara legal."
show a laugh
a "Você realmente tem um jeito com as palavras, não é? [name]?"
show a neutral
a "Eu não me detenho muito no passado. Ele só te atrasa."
m "Eu não poderia concordar mais."
show a laugh
a "É a amnésia falando?"
m "Quem sabe?"
"Ela riu enquanto colocava a mão carinhosamente em minha bochecha."
show a happy
a "Estou mais preocupado que ele se meta em problemas se eu não estiver por perto para mantê-lo sob controle."
m "Como ele é?"
show a worried
a "Digamos que muito do meu comportamento vem dele, mas... sou muito mais contido."
show a surprised
m "Se você é assim, acho que eu não sobreviveria nem um dia sequer saindo com ele."
show a angry
a "Ei! O que isso quer dizer?"
m "Ah, nada mesmo."
show a laugh
with vpunch
"Allie fez uma curva fechada. A força repentina quase me jogou para fora do barco."
m "Ei! O que foi isso?"
show a happy
a "Ah, nada mesmo."
"Não pude deixar de sorrir para ela. Ela estava praticamente brilhando quando tinha aquele sorriso diabólico."
show a neutral
m "Tenho certeza de que ele está bem, Allie."
m "Ele provavelmente está assistindo agora, só para ter certeza de que você está segura."
show a surprised
a "Agora que penso nisso, você provavelmente está certo."
show a neutral
a "Ele sempre desperdiça o dia assistindo a reality shows de merda."
show a laugh
a "O que me dá uma ideia..."
m "O que é isso?"
stop music
play music CarpeDiem
show a blush
"Com uma mão no volante, Allie se virou para mim e me beijou nos lábios."
"Eu a beijei de volta. Parecia que um raio estava correndo em minhas veias."
with vpunch
"O barco começou a balançar para frente e para trás de forma cada vez mais incontrolável, mas não paramos."
show a laugh
a "Isso deve ter dado um ataque cardíaco no Bill!"
show a angry
a "Sério! Que tipo de pai deixa a filha ir a um show trash como esse?"
"Não consegui deixar de rir."
show a sassy
a "Eh, tanto faz. Tem sido uma viagem divertida até agora."
show a laugh
a "E aqui vai para o próximo com você, [name]!"
"Ela me beijou de novo, deixando o barco em um frenesi errático."
"Passamos o resto do dia juntos navegando no barco, até que ficamos sem luz do dia."
stop sound
jump postDateSelector
