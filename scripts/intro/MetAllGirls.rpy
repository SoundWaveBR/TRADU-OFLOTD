label MetAllGirls:

play music Morning
show bg MansionMorning with dissolve

show a surprised at pos15a with dissolve # former look:right
show y neutral at pos90y with dissolve # former look:left
show v neutral at pos30v with dissolve # former look:left
show t neutral at pos75t with dissolve # former look:left
show s happy at pos60s with dissolve # former look:left


show k neutral at pos45k with dissolve # former ,,-1 # former look:left
"Quando cheguei lá, Kat e as meninas estavam em volta de um quadro negro coberto de rabiscos e equações matemáticas."
show k flirt
k "...E é por isso que [name] é a alma gêmea perfeita para cada um de vocês."
show s surprised
"Desculpe, você acabou de desenhar um monte de números e símbolos que não significam nada."
show t surprised
t "É como a matemática idiota que mostram na tela de um filme!"
show k happy
k "Ah, você está atrasado para a festa, [name]!"
show k flirt
k "Mas você chegou bem a tempo para o primeiro segmento 'tempo sozinho'!"
m "Segmento de tempo sozinho?"
show k laugh
k "Você não pode encontrar sua alma gêmea sem passar um tempinho sozinho, juntos!"
show k neutral
show y blush
show a laugh
show s tease
show t neutral
show k flirt
k "É hora de escolher sua primeira candidata a alma gêmea - uma das duas adoráveis moças com quem você passará um tempo esta semana."
show k neutral
k "Então, sem mais delongas... quem vai ser?"
m "Espera, eu já tenho que escolher?"
m "Eu nem tive a chance de realmente falar com nenhum deles ainda."
show k flirt
k "Não pense dessa forma! Pense mais como, bem... com quem você mais quer falar agora."
m "Tudo bem, eu acho."

menu:
    m "Gostaria de passar o tempo sozinho de hoje com..."

    "Allie":
        jump MetAllGirlsAllie
    "Scarlett":
        jump MetAllGirlsScarlett
    "Terra":
        jump MetAllGirlsTerra
    "Violet":
        jump MetAllGirlsViolet
    "Yui":
        jump MetAllGirlsYui

label MetAllGirlsAllie:
show a surprised
m "Allie."
show a happy
$ selectedDate="Allie"
show k happy
k "Nós faremos isso acontecer!"
show k angry
k "Vamos começar a filmar, pessoal! Vamos ter uma jornada turbulenta no primeiro dia!"
b "Sim, senhora!"
show k flirt
k "Agora seja gentil e nos dê um minuto para preparar o cenário, hein?"
jump DateSelector

label MetAllGirlsScarlett:
show s laugh
m "Scarlett."
$ selectedDate="Scarlett"
show s happy
show k happy
k "Tudo bem! Nós faremos isso acontecer."
show k angry
k "Lugares, pessoal! Vamos fazer com que [name] comece na mansão... e você sabe para onde levar Scarlett."
b "Sim, senhora!"
show k happy
k "Dê-nos um minuto para preparar a cena e depois vá procurá-la!"
jump DateSelector

label MetAllGirlsTerra:
show t surprised
m "Terra."
show t happy
$ selectedDate="Terra"
show k happy
k "Tudo bem! Temos muito trabalho pela frente."
show k angry
k "Lugares, pessoal! Vocês sabem onde colocar Terra."
b "Sim senhora!"
show k happy
k "Dê-nos um minuto para preparar a cena e depois vá procurá-la!"
jump DateSelector

label MetAllGirlsViolet:
show v happy
m "Violet."
show v sassy
$ selectedDate="Violet"
show k happy
k "Tudo bem! Nós faremos isso acontecer."
show k angry
k "Lugares, pessoal! Vamos fazer com que [name] comece na mansão... e você sabe onde colocar Violet."
b "Sim, senhora!"
show k happy
k "Dê-nos um minuto para preparar a cena e depois vá procurá-la!"
jump DateSelector

label MetAllGirlsYui:
show y surprised
m "Yui."
$ selectedDate="Yui"
show k happy
show y blush
k "Simmm! Desembucha, Quatro! Ganhei a aposta."
b4 "Mas esse era todo o meu salário!! Como é que eu vou -"
show k laugh
k "E ótima escolha, [name]! Eu sabia que podia contar com você!"
m "..."
show k angry
k "Tudo bem, lugares, pessoas! Vamos começar o show!"
b "Sim, senhora!"
show k flirt
k "E... Ação!"
jump DateSelector
