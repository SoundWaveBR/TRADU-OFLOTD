label ScarlettDate2:

show bg MansionMorning with dissolve
$ scarlettAffection=2
show s sad at pos50s with dissolve
play music Sincerely
"Encontrei Scarlett dando uma volta do lado de fora da mansão."
"Ela parecia um pouco deprimida."
m "Ei, Scarlett. Você está bem?"
show s surprised with vpunch
s "A-Ah! Caramba!"
show s worried
s "Ah... É só você, [name]. Você quase me deu um ataque cardíaco."
m "Desculpe, eu não queria."
show s neutral
s "Não é, uh, sua culpa. Só estou um pouco nervoso depois de toda essa coisa de... encontro zumbi? Seja lá o que for."
show s worried
s "Acho que estou me sentindo um pouco triste com tudo isso."
m "Por quê? Você salvou todo mundo."
show s sad
s "Não precisaríamos salvar ninguém se não fosse por mim."

menu:
    "Não se preocupe com isso":
        jump sd2_c1
    "Pelo menos você resolveu a situação":
        jump sd2_c2


label sd2_c1:
m "Todos nós cometemos erros, Scarlett. Não se preocupe mais com isso."
show s annoyed
s "A maioria das pessoas não comete erros que transformam todo mundo em zumbis."
m "Bem, sim, mas ei, isso rende uma boa TV!"
jump after_sd2_c1

label sd2_c2:
m "Ei, pelo menos não temos mais zumbis banana correndo por aí."
m "Sem sua ajuda, eles ainda estariam correndo soltos."
show s annoyed
s "Ainda assim, eles não estariam correndo por aí em primeiro lugar se não fosse por mim."
m "Bem, isso é verdade, mas ei, isso rende uma ótima TV!"

label after_sd2_c1:
"O que, inadvertidamente, é muito bom para me manter vivo... mas vou ficar quieto sobre isso."
m "Além disso, você fez isso porque estava tentando me ajudar a recuperar minhas memórias."
show s happy
m "Isso significa mais para mim do que posso dizer."
show s sad
s "...Sinto muito por não ter conseguido."
show s surprised
s "Se estiver tudo bem para você, tentarei novamente, e tenho certeza que dessa vez -"
m "Não vamos nos preocupar com isso por enquanto. Mas obrigada. Eu aprecio isso."
show s happy
m "Por enquanto, só quero te conhecer melhor, Scarlett."
show s neutral
m "Fomos... interrompidos, da última vez. Para dizer o mínimo."
m "Quer se juntar a mim para compensar o tempo perdido?"
show s happy
s "Isso seria fantástico!"
show s neutral
s "Há um lugar que eu gostaria de ir, se estiver tudo bem para você...?"
m "Mostre o caminho!"
show s laugh
s "Você não vai se arrepender!"
show s worried
show s neutral
show s worried
show s neutral
s "Pelo menos, acho que não vai."
m "Devo me preocupar?"
show s laugh
s "Vamos, vamos!"
"Ela agarrou minha mão e me puxou junto com ela."
"Quem poderia dizer não a uma garota que poderia te transformar em um zumbi?"
hide s with dissolve
show bg Black with dissolve # time:3
$ renpy.pause(delay = 2.0, hard = False)
stop music
play music ElectroCabello
show bg ScarlettNightclub with dissolve # time:2
s "Vejam!!!"
m "...Tem uma boate na mansão?"
s "Agora tem! Eu mesmo a fiz!"
s "Claro, eu a uso mais como um campo de testes do que uma boate de verdade, mas a equipe realmente queria algo para desabafar..."
s "E tudo bem, eu trapaceei um pouco, fiz um robô que fez a boate para mim, mas ainda conta."
m "Acho que você é provavelmente a primeira pessoa a dizer algo assim."
m "Além disso, eu não sabia que você sabia construir robôs! Isso é incrível."
s "Claro que sim, é legal."
s "Tenho a sensação de que construir coisas para deixar as pessoas mais felizes era o que eu mais gostava antes de vir para cá."
m "...O que você quer dizer com isso?"
show bg Nightclub with dissolve
show s laugh at pos50s with dissolve
s "Você não acreditaria se eu contasse!"
show s surprised
s "Na verdade... talvez você seja a única pessoa que faria isso, talvez valha a pena tentar."
"Ela poderia... ser como eu?"
stop music

play music Bittersweet
show s worried
s "Eu... tem tanta coisa da minha vida que não consigo lembrar, por algum motivo."
"Não pude deixar de levantar uma sobrancelha."
show s sad
s "...Havia muita gente destruída depois da guerra na Nova Ásia."
show s serious
s "Não apenas ossos quebrados e membros faltando... mas mentes despedaçadas. Pessoas presas em suas próprias cabeças."
show s neutral
s "... Disseram-me que eu tinha um dom para a pesquisa — um dom que poderia ajudar essas pessoas a recuperarem suas vidas."
show s serious
s "Então terminei a escola mais cedo e fiz meu doutorado. Liderei uma força-tarefa dedicada a ajudar os sobreviventes."
show s neutral
s "Nós os ajudamos a esquecer suas memórias mais dolorosas e traumáticas... e seguir em frente."
show s laugh
s "Era o trabalho da minha vida, sabia! Mas agora..."
show s worried
s "...Não consigo lembrar o que era. Como funcionava, se chegamos a algum lugar com nossa pesquisa."
show s laugh
s "Para ser completamente honesto, eu também não consigo lembrar como cheguei aqui."
m "Sinto muito perguntar, mas... como diabos isso aconteceu?"
show s sad
s "Se eu sabia antes, agora definitivamente não sei."
show s worried
s "Talvez os testes tenham se tornado perigosos e eu não estivesse disposto a testar em outra pessoa."
show s sad
s "Talvez eu... eu não sei. Eu não sei."
stop music
play music SmoothLovin
show s laugh
s "O mais louco é... eu fui disso... para algum tipo de programa de namoro? Que diabos?"
m "Eu acho que parece bem estranho."
show s surprised
s "E a ideia de se casar em uma semana? Quem escreveu isso, um idiota?"
"Não consegui deixar de rir."
show s happy
s "Mas... o que eu tenho a perder neste momento?"
m "Eu não olharia dessa forma."
m "Eu também não consigo lembrar de nada, mas... eu estou vivo."
m "Enquanto eu estiver vivo - eu tenho tudo a perder e tudo a ganhar."
show s laugh
s "Um otimista, hein. Isso... vale alguma coisa."
show s sad
s "Acho que você entenderia melhor do que ninguém."
show s neutral
s "...O que você planeja fazer depois que tudo isso acabar?"
m "Sinceramente, não sei."
m "Quero minhas memórias de volta, mas se não puder recuperá-las... tentarei fazer o melhor das coisas."
show s tease
s "Que plano!"
m "Ainda estou trabalhando nos detalhes, me dá um tempo!"
m "Pelo menos você lembra de algumas coisas, eu nem conseguia lembrar do meu nome no começo!"
show s laugh
s "Você me venceu!"
show bg MansionIndoorsNight with dissolve # time:2
"Conversamos por horas sobre como ambos nos sentíamos em relação às nossas situações."
"As coisas boas, as coisas ruins, sobre esquecer quem você é."
"Nós rimos sobre esquecer os momentos embaraçosos que provavelmente atormentaram os outros por uma vida inteira."
"Nós lamentamos os momentos que realmente fizeram a vida valer a pena - os momentos que tornaram sua vida única."
show s neutral
s "...É bom ter alguém que entende."
show s laugh
s "Sabe, tenho uma ideia boba, se estiver interessado."
m "Fala aí!"
show s happy
s "...Ficar noivo em uma semana é estúpido, e uma pessoa que concorda com isso é ainda mais estúpida do que isso."
show s neutral
s "Mas eu... acho que diria sim se fosse você, [name]. Só para ver onde a vida vai com alguém como você."
m "Isso é..."
show s annoyed
s "Shhh, shh, deixa eu terminar."
show s happy
s "Independente de quem você perguntar no último dia, eu gostaria... de sua amiga no tempo que há de vir."
show s worried
s "S-Se.... você ser meu. Eu não consigo me lembrar da última vez que eu tive um amigo para só... conversar, como eu me sinto."
show s happy
s "Eu acho que essa foi a primeira vez... eu me sinto um pouco melhor sobre o que aconteceu."
show s laugh
s "Eu gostaria que você se sentisse melhor sobre o passado também."
show s sad
s  "Eu não quero que você se sinta sozinho nesse mundo. Isso é muito triste, você não acha?"
show s neutral
s "E talvez eu esteja sendo tola, mas quem sabe. Talvez se nós continuarmos em outras vidas depois de tudo isso, seremos capazes de ajudar um ao outro a retomar as vidas que queríamos."
show s laugh
s "O que você disse?"
m "Eu estava pensando a mesma coisa, Scarlett."
show s flirt
s "Eu estou feliz. Mas, uh, como dizer..."
show s happy
s "Eu ainda preferiria que você me escolhesse. O que posso dizer, sou um pouco competitiva!"
show s angry
s "Pensando bem, sou muito competitiva!"
show s happy
s "Só estou dizendo, mas de todas as garotas, eu sou a mais educada, tive a carreira mais ilustre, ganhei o primeiro lugar na Exposição Nacional de Novas Ciências Asiáticas e -"
show s neutral
"Eu ri alto enquanto ela listava suas realizações uma por uma. Ela fez caretas de raiva para mim em falsa raiva."
show s happy
s "Mas acima de tudo... quero que você tenha uma vida feliz, e acho que outra pessoa pode... errar."
"Passamos o resto da noite aproveitando a companhia um do outro."
"As risadas e os sorrisos nunca pararam, e ela nunca soltou minha mão durante nossa caminhada."
$ scarlettAffection=2
jump postDateSelector