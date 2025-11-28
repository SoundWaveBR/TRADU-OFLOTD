label YuiMorning1:

show bg MansionMorning with dissolve
play music Morning
"De manhã, as meninas e eu decidimos passar um tempo no jardim em frente à casa."
show t happy at pos30t with dissolve
show y surprised at pos50y with dissolve # former ,,-1
show s happy at pos70s with dissolve
y "Nossa! Tem todo tipo de flor aqui que eu nunca vi antes!"
show s surprised
s "Sério! Você nunca viu uma tulipa?"
show y happy
y "Na minha terra natal, eu e a minha avó só cultivávamos jacintos, então não."
show t surprised
t "Nem mesmo na internet.?"
show t happy
t "E pensei que precisava sair mais."
show s neutral
s "Posso acreditar nisso, as únicas flores com as quais trabalho são dioneias (plantas carnívoras).."
show t surprised
t "O que você faz com eles?"
show s laugh
s "Bem, nós fazemos muitos experimentos no laboratório."
show s happy
s "Você já parou para pensar: "Não seria legal criar uma planta carnívora que pudesse andar... e falar?""
show y surprised
y "..."
show t surprised
t "Literalmente nunca."
show s sad
s "Ah, tanto faz. Ela fugiu há dois anos."
show s neutral
s "Meus dois vizinhos também perderam seus gatos de estimação no mesmo dia."
show s sad
s "Sinto sua falta, Fluffy..."
show y surprised
y "Tem certeza de que estavam perdidos?"
show v happy at pos10v with easeinleft # former look:right
v "O chá está pronto!"
m "Obrigado, Violet!"
"Comprei uma xícara para cada um. O aroma do chá realmente me abriu o apetite."

if violetAffection <= 1:
    jump treatversion1
if violetAffection == 2:
    jump treatversion2

label treatversion1:
show v happy
v "Preparei algumas guloseimas para nós também. Aproveitem!"
jump aftertreats

label treatversion2:
show v laugh
v "Preparei algumas guloseimas para nós também. Aproveitem!"
show v happy
v "Eles não estão à altura do lote que fizemos, [name], mas fique tranquilo, você também não encontrará reclamações sobre isso."
m "Quem poderia reclamar de biscoitos surpresa?"
show v neutral
v "Você está certo."
show v happy
v "Vamos fazer mais juntos em breve. Tenho outras receitas que gostaria de experimentar!"
jump aftertreats

label aftertreats:
"Passamos o resto da manhã comendo guloseimas deliciosas e tomando um chá delicioso, enquanto teorizávamos o que poderia ter acontecido com Fluffy."
"Pessoalmente, aposto que os felinos são os culpados. Cada Kat que conheci teve uma surpresa desagradável na manga."
jump postMorningSelector
