label VioletMorning2:

#; This works, but due to Violet Date 1 being not the baking, and 2 being the baking, gotta move this to Morning 2... so we need a new Morning 1."
play music JazzBrunch
show bg KitchenMorning with dissolve
show s neutral at pos10s with dissolve
show t happy at pos30t with dissolve

show y happy at pos70y with dissolve
show a happy at pos90a with dissolve# former ,,-1
show v neutral  at pos50v with dissolve# former ,,-1
"Fui até a cozinha, onde as meninas estavam tomando café da manhã."
show s happy
s "Então, como foi o encontro?"
show a laugh
a "Sim, conte-nos!"
"Terra estava furiosamente rabiscando notas, com o título {b}Planos de Guerra{/b} em negrito."
show v blush
v "Foi... realmente muito legal."
show v happy
v "Na verdade, fizemos este bolo e os biscoitos ontem, juntos. [name] e eu."
show v blush
v "Eu... eu espero que todos vocês gostem."
show s happy
s "Eles são incríveis, Violet. Obrigada por fazer isso para nós!"
show y laugh
y "Muito obrigada! Eles são tão deliciosos!"
show a laugh
show t annoyed
"Terra rabiscou: {b}Guerra de Atrito provavelmente não é uma opção{\b}."
show a surprised
a "O que você está escrevendo aí, Terra?"
show t surprised
t "Naaaaaaaalguma coisa..."
#; comments just be made based on the other's affection levels
show s surprised
s "Então... como é que tem massa de biscoito em todo lugar?"
show s laugh
s "Não importa para onde eu olhe, consigo ver massa em todas as superfícies da cozinha."
"Não foi só a massa. Violet e eu derrubamos algumas coisas no nosso tiroteio."
show v blush
v "Ah, isso é..."
show a laugh
a "Tem certeza que era só assar junto?"
m "Ah, pensei que fosse mais do que isso."
show v surprised
"Eu fingi que estava com o coração partido."
show a laugh
a "Tenho que admitir, Violet! Não achei que você fosse capaz!"
show a sassy
a "Hubba Hubba."
show v surprised
v "Espera... não! Nada... assim aconteceu!"
"Allie e eu rimos e fizemos armas de dedo uma para a outra."
show y surprised
y "Não entendi."
show a laugh
a "É porque você é uma boa pessoa, Yui."
show s happy
s "Ah, acho que o que Allie está tentando dizer é que Violet e [name] -"
show a happy at pos15a with easeinleft
"Allie enfiou um biscoito na boca de Scarlett antes que ela pudesse terminar a frase."
show s surprised
s "Mmmphh!"
show a surprised # t pos90a
a "Uau, esses biscoitos são muito úteis!"
show a laugh
a "Você tem que me ensinar a fazer isso um dia, Violet!"
show v happy
v "Seria um prazer, Allie!"
show s happy
s "Ooh, me ensina também!"
show s flirt
s "Por que [name] deveria ter todas as coisas boas?"
show v blush
v "Aah..."
"Passamos o resto da manhã brincando na cozinha."
jump postMorningSelector
