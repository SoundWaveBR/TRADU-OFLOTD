label VioletDate1:

$ violetAffection=1
show bg MansionMorning with dissolve
play music Morning
"Eu tinha acabado de sair da mansão para encontrar Violet, quando uma limusine branca apareceu e parou na minha frente."
show b1 neutral at pos50b with dissolve
"Um saiu do banco do motorista e caminhou em minha direção."
b1 "[name], bom dia. Por favor, entre."
m "O que há com essa conversa formal?"
show b1 worried
b1 "Por favor, entre no carro, [name]! Você já ouviu o que ela fez com meu mano!"
m "...?"
show b1 serious
"Ele abriu a porta do passageiro e me conduziu para dentro."
hide b1 with dissolve
show bg Black with dissolve
"Dei de ombros e entrei. Qual é a pior coisa que pode acontecer em um programa de namoro sobre jogos mortais?"
stop music
"Ficamos sentados em silêncio enquanto Um me levou até o que parecia ser um restaurante chique e depois me acompanhou para dentro."
show bg Palace with dissolve
play music CrinolineDreams
show v happy at pos50v with dissolve
v "Bonjour, pretendente! Espero que meu novo mordomo tenha trazido você aqui em segurança?"
m "Sim, ele trouxe. O que está acontecendo, Violet?"
show v laugh
v "Pensei em lhe dar uma chance de ter um tempo a sós com a estrela do show, só isso."
show v neutral
v "Disseram-me que é isso que as pessoas fazem quando estão... 'namorando'."
m "...Você nunca teve um encontro antes?"
show v surprised
v "C-Claro que sim! E eu li todos os manuais sobre o assunto."
show v sassy
v "Quero que você saiba que estudei todos os livros da série 'The Lusty New Asian Maid' e sei todos eles de cor."
show v laugh


menu:
    v "Impressionado, tenho certeza."

    "Estou impressionado":
        jump vd1c1
    "...Claro":
        jump vd1c2

label vd1c1:
m "...Eu estou impressionado, Violet."
show v sassy
v "Ah, não foi nada."
jump vd1pc

label vd1c2:
m "Isso é... sim, uma palavra para isso."

label vd1pc:

show v neutral at pos30v with dissolve
show b1 happy at pos70b with dissolve

b1 "Perdoem minha interrupção. Trouxe sua comida. Por favor, sentem-se, convidados honrados."
"Violet e eu nos sentamos em uma mesa no centro do palácio, enquanto Um colocava cada prato na mesa, um por um."
show b1 worried
"Ele parecia demorar-se nas almôndegas enquanto as trazia."
show v happy
v "Obrigado, Um."
hide b1 with dissolve
show v laugh at pos50v with dissolve # former look:left
v "Por favor, não se segure."
m "Não pense que vou! Esta comida parece incrível e provavelmente vale mais que minha vida."
show v happy
v "Você está certo em ambos os aspectos, [name]."
show v laugh
v "Estou em êxtase que você tenha gostado da variedade. Eu mesmo planejei!"
m "Você é um chef?"
show v blush
v "...Você poderia dizer isso."
m "...? O que você quer dizer?"
show v neutral
v "...De qualquer forma, conte-me mais sobre você, [name]."
m "Não há muito a dizer. Amnésia é uma droga e tanto."
show v surprised
v "Você não... lembra do seu passado?"
m "É. Que pena, né?"
show v happy
v "Então fique tranquila, eu encontrarei os melhores cientistas de toda a terra para ajudar você a recuperar sua memória quando isso acabar."
m "Isso... isso seria ótimo. Obrigada, Violet."
show v neutral
v "Não pense nisso. É dever daqueles que têm mais para retribuir, não?"
show v worried
stop music
play music MysteryLoop
v "Embora... você já pensou, por acaso, que isso é na verdade uma bênção disfarçada?"
m "O que você quer dizer?"
show v sad
v "Muitos de nós seríamos mais felizes sem saber o que nos arrasta para baixo."
m "...Isso pode ser verdade, mas ainda assim, preciso saber."
show v happy
v "Você soa exatamente como os exemplos de referência nos manuais de romance! Considere-me impressionado."
m "...Você sabe, esses manuais... são apenas romances de ficção comuns, certo?"
stop music
play music CrinolineDreams
show v laugh
v "Hah! Você é bem engraçada, [name]. Uma característica admirável de se ter... Eu gosto disso."
m "..."
m "De qualquer forma, você não me contou sobre você, Violet."
m "Quem é você, o que você faz para se divertir? Eu gostaria de saber!"
show v worried
v "...Ser o herdeiro dos Valentines não deixa muito tempo para diversão, receio."
show v laugh
v "Mesmo neste programa, passo a maior parte do meu tempo acordado gerenciando os negócios dos restaurantes do Valentine's."
show v happy
v "Mas suponho que... se eu tiver um tempo, eu aproveito..."
show v blush
v "...Cozinhar..."
m "Não entendi, por que você tem vergonha de gostar de cozinhar?"
m "Todo mundo tem um hobby."
show v sad
v "Cozinhar é uma espécie de... hobby de servo, de acordo com meus pais."
show v worried
v "Quando descobriram que eu estava gostando daquilo... bem, eles fizeram questão de me impedir de fazer isso de novo, com todo esse trabalho em restaurantes."
show v laugh
v "É um pouco irônico, não é?"
m "...Quer saber?"
show v surprised
v "Eu sei o que é 'o quê', mas... o que você quer dizer?"
show v neutral
m "Quem se importa com o que seus pais pensam? Aqui, nesta ilha a um milhão de milhas de distância, eles não podem te impedir."
m "Que tal encontrarmos um tempo juntos para... recuperar o tempo perdido?"
show v happy
"Ela riu como uma criança."
v "Isso seria... Isso seria maravilhoso, [name]."
show v laugh
v "Vou reservar um tempo na minha agenda para você."
"Passamos as próximas horas aproveitando a melhor refeição que o dinheiro pode comprar."
"Cada prato era melhor que o anterior - assim como cada capítulo de 'The Lusty New Asian Maid', de acordo com Violet."
"Algo me diz que o mesmo se aplica a cada momento que compartilharei com Violet."
$ violetAffection=1
jump postDateSelector
