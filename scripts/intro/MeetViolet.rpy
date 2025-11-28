label MeetViolet:

$ meetViolet=1
play sound Kitchen # loop:true
show bg KitchenMorning with dissolve
play music Morning
show b1 worried at pos60b with dissolve# former look:left at pos60
show b2 worried at pos75b with dissolve# former look:left at pos75
show b3 worried at pos90b with dissolve# former look:left at pos90
show v serious at pos30v with dissolve# former look:right at pos30
q "Um... Essas costelas estão bem passadas."
show b1 happy
b1 "Obrigado, senhora!!!"
show v angry
with vpunch
q "Eles deveriam estar malpassados! Por favor, refaça todos antes que a hora acabe."
show b1 sad
show v annoyed
b1 "Eu sabia que deveríamos ter trabalhado em contabilidade!"
show v laugh
q "Então eu tenho a oportunidade certa para você, Um - Acabei de comprar uma das ilhas vizinhas e preciso de alguém para equilibrar as contas."
show v happy
q "Por favor, termine isso até o anoitecer - e não se esqueça das costelas!"
show b1 worried
b1 "Eu retiro o que disse!!"
show v laugh
q "Os acompanhamentos são magníficos, Two! Continue assim, seu trabalhador diligente!"
show v happy
show b2 blush
b2 "Ah, droga! Você é muito gentil, senhora."
show b2 happy
b2 "Não entendi do que você está reclamando, mano."
show b2 laugh
b2 "Violet é incrível, e ela até se voluntariou para ajudar nós, humildes peões!"
show v laugh
v "Esta sopa é simplesmente deliciosa! Bom trabalho, Três."
show b3 blush
b3 "O-obrigado, Violet! Cara, ela é cem vezes melhor do que quando o Quatro manda na gente."
show b2 laugh
b2 "Não poderia concordar mais, mano!"
show v annoyed
v "Primeiro, se você insiste em demorar tanto para fazer as almôndegas, talvez possamos usar as suas."
show v laugh
v "Brincadeira. Mas pensando melhor, você nunca precisaria deles de qualquer maneira, então talvez...?"
show b3 laugh
b3 "Ela é um anjo."
show b1 sad
b1 "Estamos falando da mesma pessoa?"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve
m "Olá, tem um segundo para conversar?"
show v surprised  at pos50v with dissolve # former look:left
v "Pardon me, Não vi você aí. Só um segundo."
show v sassy
v "Eu tenho que limpar a sopa que Um colocou fogo antes - isso é possível?"
m "Tudo é possível se você se dedicar a isso."
show v worried
v "Evidentemente, o mesmo é verdade... se você não tem uma mente completamente. Ah, educação pública..."
show v laugh
v "...Brincadeirinha."
show v laugh at pos30v with dissolve # former look:right
show b1 sad at pos60b with dissolve# former look:left
b1 "Ei, isso foi desnecessário!"
show b1 worried
show b2 worried at pos75b with dissolve # former look:left
b2 "Na verdade... pensamos o mesmo sobre você diariamente."
show b3 laugh at pos90b with dissolve # former look:left
b3 "Posso confirmar isso!"
show b1 sad
b1 "Gostaria que mamãe nunca tivesse tido vocês!"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve

show v sassy  at pos50v with dissolve # former look:left
v "Desculpe pela demora, já terminei. Eu sou Violet, Violet Valentine."
show v happy
v "O prazer é seu, [name]."
m "Você já sabe quem eu sou?"
show v laugh
v "Imagino que cada concorrente faça isso - Voar até aqui, por uma semana inteira, para um encontro às cegas? ...Ninguém poderia ser tão pouco inteligente."

if meetTerra == 0:
    jump pastTerraJoke

if meetTerra == 1:
    jump TerraJoke

label TerraJoke:
    show bg GamesRoomMorning # with dissolve
    hide v # with dissolve
    show t worried  at pos50t # with dissolve
    with vpunch
    t "*espirra*"
    t "...?"
    hide t #with dissolve
    show bg KitchenMorning #with dissolve
    show v sassy at pos50v #with dissolve
    jump pastTerraJoke

label pastTerraJoke:
    # former look:left
v "Espero que você seja digno de ser o pretendente - você descobrirá que cortejar uma moça é um esporte diferente do que cortejar outras garotas."
show b2 surprised at pos85b with dissolve
b2 "É verdade! Ela é uma das duas filhas da Família Valentine!"
show b3 laugh at pos15b with dissolve # former look:left
b3 "Eles são ainda mais ricos que a Royal Black Media!"
#show d annoyed
play sound Intercom
d "Tudo bem, Three. Seu pagamento foi reduzido em 50%. Aproveite seu macarrão instantâneo ainda pior."
show b3 sad
b3 "...É tarde demais para voltar para a escola?"
hide b3 with dissolve
hide b2 with dissolve
show v laugh  at pos50v # former look:left
v "Estou, como dizer, fascinado... Gostaria de ver o que torna você tão especial."
show v sassy
v "Você parece... bem comum para mim."
m "Acho que você vai se surpreender, Violet."
show v happy
v "Eu gosto de um -"
stop music
#; BOOOM!!!"
stop sound # Kitchen
play sound Explosion
with vpunch
show v surprised

"Uma explosão ensurdecedora ocorreu na cozinha."
show v annoyed
v "..."
show v laugh
play music Morning
v "O espaguete hoje à noite será, como dizer, um pouco diferente - espero que você não se importe."
m "Você não está realmente colocando o One no menu, certo?"
show v neutral
v "....."
m "......."
show v laugh
hide v with dissolve
with vpunch
v "...Um, por que tem um buraco no teto?"
"...Parece que eles vão ficar ocupados na cozinha por um tempo."


if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsV

menu:
    n "Decidi ir para..."

    "A Biblioteca" if meetScarlett != 1:
        jump MeetScarlett
    "A Cozinha" if meetViolet != 1:
        jump MeetViolet
    "A Sala de Jogos" if meetTerra != 1:
        jump MeetTerra
    "O Quintal" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsV:
    stop music
    play music ItemStore2
    play sound Intercom
    k "Certo, certo, chega de brincadeira."
    k "Se você estiver no programa e não for um soldado mal pago, venha até a entrada principal da mansão."
    "...Acho que isso me inclui. Eu deveria começar a ir até lá."
    with vpunch
    k "...Isso inclui você também, Terra! Eu posso ver você jogando, sabia!"
    t "Você não é meu chefe!"
    "...No que eu fui me meter?"
    jump MetAllGirls
