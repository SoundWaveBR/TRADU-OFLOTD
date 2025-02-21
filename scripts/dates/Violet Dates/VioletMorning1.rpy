label VioletMorning1:

show bg KitchenMorning with dissolve
play music BlippyTrance
show v neutral at pos70v with dissolve# former look:left
show t worried at pos30t with dissolve # former look:right
v "...Então você coloca a carne em torno de... 300 graus por 40 minutos."
show t serious
t "Mmhm, ok... entendi."
"Terra rabiscou furiosamente as notas."
show t surprised
t "Espere um minuto! Eu não poderia simplesmente cozinhá-lo a 600 graus por 20 minutos?"
show v worried
v "Não é bem assim que funciona, infelizmente."
show t worried
t "Mas a matemática confere!"
m "O que está acontecendo?"
show v happy
v "Ah! Bom dia, [name]. Como vai?"
show v laugh
v "Estou ensinando a Terra a maneira correta de preparar um assado."
show t happy
show v worried
t "Até agora eu diria que está indo muito bem!"
show v happy
v "...Terra será quem preparará o almoço hoje, em vez de mim."
show t annoyed
"Terra girou um dos botões do fogão o máximo que pôde para a direita."
show t happy
t "E o aluno... superou o mestre."
show v worried
v "Pensando bem... talvez eu prepare um prato alternativo. Um momento, por favor."
hide v with dissolve
show t angry
t "Ó homens de pouca fé!!"
hide t with dissolve
show bg Black with dissolve
"É hora do momento da verdade: o almoço está servido!"
show bg KitchenMorning with dissolve

show y neutral at pos10y with dissolve # former look:left
show a happy at pos90a with dissolve # former look:right
show s neutral at pos70s with dissolve # former look:left
show t neutral at pos50t with dissolve# former look:right
show v neutral at pos30v with dissolve# former ,,-1 # former look:left


show t worried at pos50t
t "..."
"Terra estava nervosamente apertando as mãos com força."
show s surprised
s "...!"
show y surprised
y "...!"
show a happy
a "...!"
m "...!"
show s happy
show y laugh
show t surprised
show a happy
show v happy
stop music
play music CheeryMonday
all "Está uma delícia!"
show t happy with vpunch
t "...! Eu consegui, meu Deus!!!"
"Terra fez uma dancinha em comemoração e deu um high five para Violet."
show t surprised
t "...Devo me tornar um Vlogger de comida? Sou um gênio da culinária. Esse talento não deve ser desperdiçado..."
#hide t
show t happy at pos30t
show v happy at pos50v
# show s happy at pos70s

with dissolve
m "Psiu, oi, Violet."
#show v happy at pos50v with dissolve
v "O que é isso, [name]?"
m "Foi isso que você cozinhou ou foi isso que Terra cozinhou?"
show v happy
"Violet sorriu e piscou para mim."
show v laugh
v "Não sei do que você está falando."
"Ela tomou um gole da sopa contente."
"Não pude deixar de sorrir de volta para ela. Droga, essa foi a melhor refeição que já comi."

if currentDay == 1:
    jump OneDayOnly

"...É verdade que minha memória só remonta a [currentDay] dias, mas ainda assim, isso conta para alguma coisa!"
jump postMorningSelector

label OneDayOnly:
"...É verdade que minha memória só remonta a [currentDay] dia, mas ainda assim, isso conta para alguma coisa!"
jump postMorningSelector
