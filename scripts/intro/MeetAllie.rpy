label MeetAllie:

$ meetAllie=1
show bg Hills with dissolve
play music AlmostNew
"Uau. Chamar isso de quintal é como chamar o que aconteceu com o Titanic de vazamento. O campo vai além do que os olhos podem ver."
"Meus olhos foram rapidamente atraídos para uma garota correndo voltas pelo campo."
"Ela é rápida! Ela está chegando mais perto, mais perto, e..."
show a happy at pos50a with easeinright
"Ela parou na minha frente."
show a laugh
a "Oi oi, sou Allie, É um prazer conhece-lo? :3"
show a happy
a "Você é o [name], certo?"
m "Ah, eu s -"
show a laugh

menu:
    a "Aah, eu realmente não me importo. Mas quer correr?"

    "Claro!":
        jump SureJog
    "Não obrigado!":
        jump NoJog

label SureJog:
    m "Claro, isso parece -"
    jump StartJog

label NoJog:
    m "Na verdade, eu preferiria -"
    jump StartJog

label StartJog:
stop music
play music LeGrandChase
with vpunch
show a sassy
a "Tudo bem, VAMOS LÁÁÁ!!!!!!"
#@spawn ShakeCharacterlabel1 params:Allie,0 wait:false
play sound Whoosh
with vpunch
"Ela agarrou minha mão e me puxou com ela numa velocidade alucinante."
$ renpy.sound.play("audio/sfx/running_on_grass.mp3", loop=True) # running on grass
with vpunch
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!"
"Ela é tão rápida!! Preciso de tudo que tenho para acompanhá-la."
"O vento no meu rosto é agradável, no entanto. Por algum motivo, sinto que perdi isso."
with vpunch
"Na verdade, acho que nunca fui tão rápidoAAAAAAAAAAAAAAAAAHHH!!"
show a laugh
a "Vamos, vamos! Continue assim! Nós vamos deixar você em ótima forma em pouco tempo, soldado!"
"Quaisquer pensamentos bons que eu tinha flutuando na minha cabeça foram jogados fora pelo meu sargento instrutor recém-designado."
"Eu pensei que tinha me inscrito para um programa de namoro, não um programa de fitness...!"
with vpunch
"*haa* *haa*"
"Tudo bem, tudo bem... Estou começando a atingir um ritmo confortável."
show a sassy
a "É só isso que você tem?"
"Allie estava aumentando a distância entre nós, com um sorriso no rosto."
"Pode me chamar de simplório, mas comecei a correr o mais rápido que pude."
with vpunch
m "Ahhhh!!!!!!!!!!"
"Eu ganhei mais e mais velocidade, e observei Allie lentamente ficando para trás."
show a surprised
a "Uau, você está correndo ainda mais rápido do que meu pai quando ele foi embora."
with vpunch
show a sassy
"Mas que -"
"Eu inconscientemente desacelerei, meu rosto contorcido em choque."
"Naquele único momento, ela me alcançou e rapidamente me ultrapassou."
show a laugh
a "Estou brincando, nossa! Não precisa levar tudo tão a sério."
show a happy
a "O bastardo morreu antes mesmo de ter uma chance."
m "Oh, eu estou tão m-"
show a angry
"Não sinta, eu mesmo o matei."
with vpunch
show a sassy
"O qu -"
show a laugh
a "A expressão no seu rosto é hilária!!"
show a happy
a "Não se preocupe tanto, [name]. Estou brincando, brincando."
show a angry
a "Ou eu sou?"
"Senti meu coração começar a ceder menos por causa da corrida e mais por causa da montanha-russa emocional."
"..."
stop music
show a happy
play music CheeryMonday
stop sound # RunGrass
"Terminamos de correr alguns minutos depois."
"Estou completamente sem fôlego."
show a laugh
a "Isso foi divertido, [name]!"
m "*haa*"
show a neutral
a "Vamos correr de novo algum dia."
"Eu caí de joelhos para recuperar o fôlego e observei enquanto ela se afastava sem esforço."
show a sassy
a "Mas você terá que ser mais rápido do que isso para me acompanhar, pretendente!"
hide a with dissolve
"Deitei na grama, como uma morsa obesa ofegante."
"É assim que eu morro?"
"*haa* *haa*"
"Não acho que terei que me preocupar em contar a verdade para Allie, com o quão difícil é respirar."
"*haa*"
"...Acho que vou viver, pelo menos por enquanto."
"Rolei de costas e relaxei por um momento."

if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsA

menu:
    n "Depois que eu acordar, acho que vou até..."

    "A Biblioteca" if meetScarlett != 1:
        jump MeetScarlett
    "A cozinha" if meetViolet != 1:
        jump MeetViolet
    "A sala de jogos" if meetTerra != 1:
        jump MeetTerra
    "O quintal" if meetAllie != 1:
        jump MeetAllie


label MetAllGirlsA:
stop music
play music ItemStore2
play sound Intercom
k "Certo, certo, chega de brincadeira."
k "Se você estiver no programa e não for um soldado mal pago, venha para a frente da mansão."
"Acho que isso me inclui. Eu deveria começar a ir até lá."
with vpunch
k "Isso inclui você também, Terra! Eu posso ver você jogando, sabia!"
t "Você não é meu chefe!"
"No que eu fui me meter?"
jump MetAllGirls
