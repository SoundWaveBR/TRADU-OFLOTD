label MeetScarlett:

$ meetScarlett=1
show bg Library with dissolve
play music Sincerely
"A biblioteca era como uma biblioteca de filme. Grandiosa. Majestosa."
"Nada como uma biblioteca comum, que vira um cenário pornô depois do horário de fechamento."
"Dei alguns passos para frente e notei uma garota de cabelo vermelho no fundo da biblioteca."
show s serious at pos50s with dissolve
play sound PageFlip
"Ela estava lendo uma revista, ou assim parecia à primeira vista."
"Se você esticasse a cabeça um pouco para o lado, poderia ver outro livro escondido atrás da revista."
play sound PageFlip
"'Teste A/B após o Apocalipse - 1ª edição, por DB'."
m "Ei, o que você está lendo?"
show s surprised
q "Ah, isso? Só mais um elementar -"
show s happy
q "Quero dizer, uma bomba de chá com uma verdade absoluta, yaassssss!"
m "..."
show s surprised
q "Você acredita que essa celebridade iria, tipo, namorar outra celebridade???"
q "Eu nem consigo! É quase como se fossem pessoas!"
m "Eu consigo ver o que você está realmente lendo, sabia?"
show s worried
q "...! Oh meu Deus, isso é tão embaraçoso."
m "Por que isso seria embaraçoso? O livro que você está lendo parece muito mais interessante."
show s sad
q "De onde eu venho, as pessoas zombam de quem... faz o que eu faço, eu acho."
show s laugh
q "Para eles, uma biblioteca é apenas um lugar para filmar pornografia depois do horário de fechamento."
m "*tosse*"
show s neutral
s "A propósito, sou Scarlett. Você é [name], correto?"
m "Sou eu. É um prazer conhecê-la, Scarlett."
show s flirt
s "É um prazer conhecê-lo também, [name]."
m "Estou curioso, então o que você está realmente lendo?"
show s laugh
s "Achei que você nunca perguntaria!"
#@char Scarlet
#Her face lit up like fireworks. Wow."
show s surprised
s "Aqui, deixe-me mostrar - Ah!"
stop music
play sound BookDrop
"Scarlett deixou cair a revista e o livro atrás dela no chão... revelando uma segunda revista em suas mãos."
play music RocketPower
m "Ah..."
show s worried
s "..."
hide s with dissolve
play sound Whoosh
"Ela saiu correndo tão rápido que nem tive tempo de dizer mais nada."

if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsS

menu:
    n "Acho que não há muito mais o que fazer aqui. Vou descer para..."

    "A Biblioteca" if meetScarlett != 1:
        jump MeetScarlett
    "A Cozinha" if meetViolet != 1:
        jump MeetViolet
    "A Sala de Jogos" if meetTerra != 1:
        jump MeetTerra
    "O Quintal" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsS:

stop music
play music ItemStore2
play sound Intercom
k "Certo, certo, chega de brincadeira."
k "Se você estiver no programa e não for um soldado mal pago, venha até a entrada principal da mansão."
"Acho que isso me inclui. Eu deveria começar a ir até lá."
with vpunch
k "Isso inclui você também, Terra! Eu posso ver você jogando, sabia!"
t "Você não é meu chefe!"
"No que eu fui me meter?"
jump MetAllGirls