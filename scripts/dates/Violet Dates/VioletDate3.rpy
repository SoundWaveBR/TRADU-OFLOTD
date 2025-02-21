label VioletDate3:

$ violetAffection=3
#; A date where she can just be a regular girl
show bg KitchenMorning with dissolve
play music NightInVenice
show v happy at pos50v with dissolve
"Encontrei Violet no mesmo lugar que a conheci. Ela estava tirando uma fornada de biscoitos do forno."
m "Bom dia, Violet!"
"Eu deslizei para perto dela e peguei um dos biscoitos em um movimento suave."
m "Ai! Quente."
"Eu joguei o biscoito na minha boca de qualquer maneira."
m "Valeu a pena a dor! Caramba, estava delicioso."
show v laugh
v "Espere um momento, seu ganso bobo!"
show v happy
v "Você nunca deixa de me fazer rir, [name]. Eu admiro muito isso."
"Fiz uma reverência zombeteira, com os braços atrás das costas, e coloquei meu melhor sotaque chique."
m "O prazer é todo meu, milady."
show v laugh
v "Pare, você!"
"Eu devorei outro biscoito. Claro que sim."
show v surprised
v "Você sabe que elas são para compartilhar com todos, certo?"
m "Eu sou parte de todos - qual é o problema aqui?"
"Nós rimos juntos na parte que estávamos fazendo."
show v blush
v "Ah, isso me lembra... [name]."
m "O que foi, Violet?"
show v worried
v "Chegou ao meu conhecimento... que esse show vai acabar muito em breve."
m "...Sim, vai."
show v sassy
v "Oh, anime-se, por favor! Não pretendo sentir pena de mim mesmo."
show v neutral
v "Em vez disso... quero usar o tempo que nos resta aqui para fazer algo que... sempre desejei fazer."
m "E o que é isso?"
show v blush
v "O que eu quero... é ir a um encontro, do tipo que pessoas normais vão."
show v happy
v "O tipo sobre o qual eu só li! Fazer um piquenique! Assistir a um filme no cinema! Longas caminhadas na praia! Até mesmo algo louco, como... uma noite de pintura!"
show v blush
v "E então podemos assistir ao pôr do sol juntos, e seria tão romântico..."
"O entusiasmo dela era adorável. Ela estava praticamente quicando pela sala como uma bola de pingue-pongue."
m "...Acho que podemos fazer isso acontecer."
show v happy
v "Podemos agora! Qual deles!"
m "Por que não todos eles?"
"Ela tem o sorriso mais lindo, droga."
show v surprised
v "Sério? Você só pode estar brincando comigo."
m "Pode contar comigo, Violet. Eu farei acontecer."
show v laugh
with vpunch # params:Violet
v "Yay!"
"Ela fez um pequeno grito de alegria e dançou. Nossa, não consigo parar de sorrir olhando para ela."
"Dito isso... não tenho ideia do que fazer. Acho que isso vai ser arriscado!"
show v happy
v "Não seria justo se você descobrisse tudo. Deixe-me cuidar do piquenique!"
"Ela puxou uma cesta de trás dela."
show v laugh
v "Quer se juntar a mim no lindo ar livre?"
m "Eu não perderia isso por nada no mundo, Violet."
hide v with dissolve
show bg Hills with dissolve # time:2
show bg VioletPicnic with dissolve # time:2
"We walked outside for a while, then settled on a lovely spot with a nice mix of shade and sunlight for our picnic."
"The way her silver hair caught the sunlight - it was enough to make you believe in angels."
"She was so beautiful."
v "Dig in! I've brought plenty. Please don't hold yourself back!"
m "I've got to be the luckiest person alive."
v "Save that talk for after you try this! I'm letting you have the first bite."
m "Should I be worried?"
"I smiled as she mock-pouted."
m "Just kidding."
"She laughed and smiled as she spoon-fed me a delicious egg roll."
m "...Called it! I'm the luckiest person alive."
m "Not just because the food's delicious, but because you're here next to me, Violet."
m "You've made this week so special."
v "I feel the same way, [name]."
v "And there is more where that came from!"
m "You're absolutely right - I've got something prepared for just the two of us next."
play sound Intercom
k "You owe me one, [name]."
v "...?"
"We enjoyed the delicious food and conversation over the rest of the afternoon."
show bg Hills with dissolve # time:2

"We walked back to the mansion hand in hand, smiling all the while."
show bg GamesRoomMorning with dissolve # time:2
"Next stop... the only movie theatre on the island."
show v surprised at pos50v with dissolve
v "I didn't know we had a room like this in the mansion!"
m "I'm not surprised. Terra's pretty terra-torial about this room, from what I've seen and heard."
show v happy
m "But right now, it's our very own private movie theatre!"
"I did a little jazz hands at the TV."
show v laugh
"Violet clapped, as if I had just put on a performance of a lifetime."
"I made a dramatic bow, then took a look at what movies we had in store."
show v neutral
"Let's see... we have romcoms, fantasy medieval movies, war movies, a few superhero movies, and last, but not least, a horror movie."
show v happy
"I'll put on a romcom. From what Violet was saying earlier, this would definitely be her favorite."
show v blush
"I started the movie, then went back and sat next to Violet, with my arm around her."
show v surprised
"The story was about a girl who moved to a place called New York to become a writer, falls in love with a boy she meets there, and eventually, realizes her dream and her love."
show v blush
"It wasn't anything special, but Violet was thoroughly entranced for the whole movie."
"Me... I was more entranced by her."
"After the credits rolled, Violet practically burst into tears."
show v sad
v "This was the best movie I've ever seen in my whole life! My whole life!!"
m "Then how about... we take a scene you liked from the movie... and turn it into a painting?"
show v surprised
v "Oh my gosh, you didn't...!"
m "Just wait right here for a second."
show v happy
v "Okay."
hide v with dissolve
show bg MansionIndoorsNoon with dissolve
"I had no idea where to find art supplies, but I knew if there was anyone who could, it was Kat."
m "Kat? I think you know the sitch."
play sound Intercom
#show k laugh
k "You got some nerve putting this together at the last minute... but I like that about you!"
#show k neutral
k "Four! Set up everything they need for a paint night in the main hall of the mansion, stat!"
#show b4 worried
b4 "Aw man, I just finished my shift!"
#show k laugh
k "Even better! You've got free time for this!"
show bg MansionIndoorsNight with dissolve
show v happy at pos50v with dissolve
"And so we started painting on canvases in the main hall."


menu:
    n "I think I'll paint a picture of..."

    "Violet and I watching a movie together":
        jump vd3_c1
    "A scene from the movie":
        jump vd3_c2

label vd3_c1:
"...Violet and I watching the movie together."
"This counts, right?"
#Violet. I know I said I'd paint a scene from the movie too, but it'd be a crime not to at this point."
show v happy
v "What are you painting, [name]?"
m "...I'm painting a picture of us, watching the movie together."
show v blush
m "It's the most beautiful scene 'from the movie', you know? It'd be a shame not to capture it."
show v laugh
v "You are quite the flirt, you know that?"
show v happy
v "...But I like that about you."
"Her smile could melt the coldest heart."
m "So which scene are you painting, Violet?"
jump vd3_pc

label vd3_c2:
"...A scene from the movie."
"Agh, there's too many to pick from!"
show v sassy
v "Which scene are you painting, [name]?"
m "Haven't decided yet. How about you?"

label vd3_pc:

show v happy
v "I'm drawing the scene where the girl runs out in the rain to tell the boy that she loves him. It was just... so romantic."
"She sighed like a lovestruck teenager."
"I could tell she was putting her whole heart into her painting - she captured the scene perfectly."
"As for me... let's just say I was more focused on making the people have the right number of heads, and was working from there."
show v laugh
"An hour or so later, we finished and compared our final artworks."
"She's an incredibly talented artist. Me, not so much."
show v happy
"That was... embarassing, but man, it was worth it just to see her smile and break into laughter."
show v surprised
"Her laughter was interrupted by a gurgle from her stomach."
show v laugh
v "Mother would punish me for sure if she heard me make that sound - but who cares now!"
"Violet was unstoppable at this point."
m "Is it time for dinner?"
show v sassy
v "I do believe it is!"
stop music
play music RomanticJazz
show v laugh
show bg Palace with dissolve # time:2
"I volunteered to cook, but she wanted to go back to the restaurant that we went to on our first date. So we did."
"Apparently, she was trying too hard to be prim and proper back then, and didn't actually get to eat as much as she wanted."
show v happy
"She ate up a storm. Almost literally. Almost."
"We spent dinner wolfing down delicious food without a care in the world, and laughing about scenes in the movie and our little artsy adventure."
"Then finally... we went for the long-awaited walk on the beach."
show bg BeachEvening with dissolve
"We held hands as we walked along the ocean. The waves of the ocean seemed to play music for us as we skirted by."
show v laugh
"At times, we talked without end."
show v blush
"At other times, we enjoyed each other's company and warmth in silence."
"Either way, we were as happy as can be."
"We talked about the how the past, the present, and future, were so different than before because of each other."
show v happy
v "You know, [name]... if you asked me to marry you, right now... without a doubt, I'd accept."
show v laugh
v "I know it sounds quite crazy, to say that in such a short period of time... but I just know."
show v blush
"She kissed me passionately, with everything she had."

if playthrough == 1 and currentDay == 6:
    jump LastDateViolet
elif playthrough == 2 and currentDay == 9:
    jump LastDateViolet
else:
    jump NotLastDateViolet

label LastDateViolet:

"We fell together onto the soft sand of the beach."
m "...Will you marry me, Violet?"
"I looked at her and saw the most beautiful smile from the most beautiful girl there was."
m "I know the final ceremony's tomorrow, but... I want you to know how I feel."
"A moment passed. It felt like my heart was trapped in my throat."
show v happy
v "Of course. I know what I said, [name]."
"And then I saw something I'd never seen before - and would never see again."
stop music
play music Smile
show v worried
show bg BeachNight with dissolve
play sound Shutdown
"The sky outside rapidly turned from bright blue to black, as if it were water being drowned in the darkest ink."
hide v with dissolve
show bg Black with dissolve
"Then the bright sun in the sky... went out, like a candle in the wind, as the warmth of the beach sand disappeared in an instant."
play sound Intercom

q "Please collect the cast - the experiment is complete."
stop sound #@stopsfx GroupRun
play sound GroupRun
"The last thing I saw was Violet screaming as shadowy figures grabbed her from behind."
"A second later, and I couldn't even see my hands reaching for Violet's, desperately trying to pull her back to me."

"Then I felt somebody grab me from behind - no, not somebody - there must have been several people."

play sound Hit
"They forced me to the ground and cuffed me behind my back."
play sound Handcuffs
"I screamed, but there was no sound."
"I couldn't hear anything. Not even the sound of the waves."
"I tried to fight, but there was no way out."
"I screamed for Violet, for her to run as far as she could - but I heard no response."
"Then... nothing."
stop sound
if playthrough == 1:
    jump P1Ending
if playthrough == 2:
    jump P2Ending

label NotLastDateViolet:

"And what came next... was the perfect ending to our lovely date."
show v blush
v "...Come closer."
$ violetAffection=3
jump postDateSelector
