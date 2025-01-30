
label AllieDate1:

play music CarpeDiem
show bg RoadMorning with dissolve
$ allieAffection=1

"Como eu deixei a Allie me convencer a isso, eu nunca vou saber."
m "Tem certeza que isso é uma boa ideia?"
show a laugh at pos50a with dissolve
a "Só tem um jeito de descobrir, não é?"
"Allie segurou minha mãe e me puxou em direção à ladeira da colina."
show a happy
a "Relaxa, [name]. Qual é o pior que pode acontecer?"
m "Bem, eu posso morrer."
"Será pedir demais participar de um programa de TV que não termina comigo morto?"
show a laugh
a "Não se preocupe. Eu cuido de você -"
show a surprised
stop music
play music LeGrandChase
show a surprised with vpunch
a "Ah merd-"
"Allie escorregou nos patins, me puxando para baixo da colina com ela."
"Tentei dar um passo para trás por reflexo, mas era tudo que eu podia fazer para continuar de pé com os patins."
m "Ah por-"
with vpunch
play sound Rollerblade
"Começamos a descer a colina - cada vez mais rápido, cada vez mais rápido."
with vpunch # Allie
"Allie estava rolando colina abaixo para trás a toda velocidade. Eu podia ver pânico em seus olhos."
"Eu não conseguia descobrir como parar, estávamos indo cada vez mais rápido."
with vpunch # Allie
"Eu gritei -"
show a laugh
"Allie riu e apontou para mim."
show a happy
a "Nossa, seu rosto não tem preço! Eu o amo."
stop music
play music CarpeDiem
"Allie se virou sem esforço e, de alguma forma, deslizou para perto de mim, sem nunca ter soltado minha mão."
"Nosso ritmo alucinante ficou cada vez mais lento enquanto ela nos guiava para frente e para trás repetidamente."
"Antes que eu percebesse, estávamos deslizando pelas estradas suavemente."
"O vento estava tão bom."
hide a with dissolve
show bg AllieRollerblading with dissolve
#show a laugh
a "Agora você pegou o jeito!"
m "Você tem um jeito engraçado de ensinar."
#show a happy
a "A melhor maneira de ensinar um pássaro a voar é jogando-o de um penhasco, não?"
m "Essa é definitivamente uma... maneira de ver as coisas."
#show a neutral
a "Não se preocupe com isso! Você nunca esteve em perigo."
m "Você anda de patins há muito tempo?"
#show a laugh
a "Não!"
#show a neutral
a "Na verdade, eu só aprendi hoje."
m "Err... o que foi aquilo sobre nunca estar em perigo?"
show bg Hills with dissolve
show a happy at pos50a with dissolve
a "Shhhh."
m "Você é muito ousado, não é?"
show a laugh
a "O que revelou isso?"
with vpunch
"Ela riu e me deu um tapinha nas costas."
show a happy
a "Você sabe que aprende bem rápido!"
show a neutral
a "Você aprendeu a andar de patins quase tão rápido quanto eu."
m "Bem, eu tenho uma ótima professora."
m "É muito divertido sair com você, Allie."
show a laugh
a "Puxa, eu me sinto da mesma forma, [name]!"
show a happy
a "É ótimo estar perto de alguém disposto a embarcar em uma aventura."
show a laugh
a "O mundo enlouqueceu, todos nós vamos morrer, você pode muito bem estar perto de pessoas que fazem a vida valer a pena."
m "Eu não poderia dizer melhor."
show a sassy
a "Sabe, aposto que você não consegue patinar para trás."
# with vpunch # Allie
show a sassy with vpunch
play sound Rollerblade
"Allie deu marcha ré e começou a patinar para trás, como se quisesse me provocar."
m "Ah? Por quê?"
show a happy
a "Eu só acho que é um pouco assustador para uma pessoa que grita quando começa a descer um pequeno buraco."
show a worried
a "'Eu sou [name], e não consigo lidar com um pequeno solavanco!! AAAAAAH!! ME AJUDEM!!!'"
m "Vamos, era uma colina!"
show a laugh
a "Sim, sim."
"Senti uma luz de fogo dentro de mim."
m "Vamos lá, Allie!"
show a surprised
a "Ah, você tem certeza?"
m "Eu gaguejei?"
"Chega um momento na vida de cada pessoa em que sabemos que estamos fazendo uma aposta idiota, mas fazemos mesmo assim."
play sound Rollerblade

menu:
    n "Com o poder da confiança e adrenalina deslocadas, pulei alto no ar..."

    "...e fiz uma rotação de 360!":
        jump rotation360
    "...e deu um mortal para trás!":
        jump backflip

label rotation360:
"...e fez uma rotação de 360!!"
"Espera, eu estou girando, ou o mundo está girando? Não tenho certeza."
jump after_stunt

label backflip:
"...e deu um mortal para trás!!!"
"Espera aí, eu estou dando um mortal ou o mundo está virando? Não tenho certeza."

label after_stunt:
"Então me dei conta."
show a surprised
m "Ah caralh-"
hide a with dissolve
show bg Black with dissolve
stop music
stop sound
# @stopsfx Rollerblade
play sound Hit
play music Smile
"..."
play sound Glitch1
# "Here's a {glitch=50}{color=#0f0}{b}Some Dialogue{/b}{/color} Tag{/glitch}"
q "{glitch=50}{b}Não. Eu não vou deixar você matar[name].{/b}{/glitch}"
"O que...?"
play sound Glitch2
q "{glitch=50}{b}Você vai desejar que tivéssemos feito isso.{/b}{/glitch}"
stop music
show bg RoomMorning with dissolve
"O que foi...?"
show a worried at pos50a with dissolve
m "Mas que merda?"
show a surprised
play music CarpeDiem
a "Você está acordado! Você está bem, [name]?"
show a worried
a "Tente não se mover. Você está um pouco machucado agora, mas ficará bem em breve."
show a happy
a "Kat e eu tratamos dos seus ferimentos. Muito bem, se é que posso dizer!"
m "O que... o que aconteceu?"
show a laugh
a "Você, uh... bem, 'patinou para trás'."
show a worried
a "Estamos definindo patinação de forma bem liberal, hein?"
m "Como cheguei aqui?"
show a neutral
a "Eu carreguei você até aqui."
m "Cara, minha cabeça..."
show a worried
a "Calma. Faz apenas algumas horas que você se nocauteou."
show a blush
a "Hum, bem, é meio que culpa minha, mas..."
show a worried
a "Eu fiz um pouco de comida para você, deve ajudar você a recuperar suas forças rapidamente."
m "Obrigada, Allie. Isso é muito legal da sua parte."
show a laugh
a "Não espere algo que Violet faria!"
show a worried
a "Tudo o que posso prometer é que a comida provavelmente é mais saudável do que minha última sugestão antes de você se nocautear."
m "Vou arriscar."
"Dei uma mordida na comida com cuidado."
show a surprised
m "Gah!!!! Eu- *Tosse* Eu- Eu estou morrendo...! *Tosse*"
show a worried
"Por um momento, Allie ficou com os olhos arregalados de choque e horror."
show a angry
m "Haha, estou só brincando com você. A comida está deliciosa. Obrigada, Allie."
m "Só pensei que conseguiria um pouco de vingança."
show a laugh
a "Sabe, ninguém te forçou a pular!"
"Ela riu e me deu um tapa no ombro, depois passou a mão no meu cabelo e o coçou."
"Eu me vi sorrindo e admirando o azul dos olhos dela."
show a happy
a "Estou ansioso pela nossa próxima aventura, [name]."
show a laugh
a "Mas prometa não ser tão idiota de novo, ok?"
m "Vou tentar o meu melhor. Mas as pessoas não conseguem evitar fazer coisas idiotas para impressionar uma garota bonita."
show a blush
a "Acho que 'impressionado' é como vamos chamar."
"Passamos o resto do dia tirando sarro um do outro por quão estúpidos estávamos sendo."
"De alguma forma, de alguma forma, Allie conseguia pegar o comum e transformá-lo em uma aventura."
"Eu estava rindo tanto que mal conseguia sentir dor."
hide a with dissolve
show bg Black with dissolve

"Antes que eu percebesse, já era noite."

$ allieAffection=1
jump postDateSelector
