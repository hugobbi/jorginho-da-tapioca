# Trabalho 4 IA

Grupo:
Nome:              Cartão:   Turma:
Matheus Silveira   316271    B
Henrique Gobbi     334932    B
Leandro Boniatti   324060    B

# Avaliação do TTTM
(I): "O minimax sempre ganha do randomplayer?"

O minimax (jogando de Brancas),em duas séries de 10 testes, contra o randomplayer (jogando de Pretas),venceu as 20 partidas.    
O minimax (jogando de Pretas), contra o randomplayer (jogando de Brancas), teve um comportamento diferente:

Foram realizadas 7 séries de testes com 10 partidas em cada série: 

na 1ª série o minimax ganhou 6 partidas,e aconteceram 4 empates;   
na 2ª série o minimax ganhou 5 partidas,e aconteceram 5 empates;   
na 3ª série o minimax ganhou 4 partidas,e aconteceram 6 empates;   
na 4ª série o minimax ganhou 8 partidas,e aconteceram 2 empates;   
na 5ª série o minimax ganhou 8 partidas,e aconteceram 2 empates;   
na 6ª série o minimax ganhou 7 partidas,e aconteceram 3 empates;   
na 7ª série o minimax ganhou 4 partidas,e aconteceram 6 empates.

Nas 70 partidas realizadas, 42 partidas foram vencidas pelo minimax e 28 foram empates.     
A porcentagem de vitórias do minimax foi de 60%. 
    

(II): "O minimax sempre empata consigo mesmo?"  
Foram realizadas 3 séries de testes,com 10 partidas cada, todas elas empataram.


(III): "O minimax sempre empata contra as jogadas perfeitas recomendadas pelo
https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ?"
Foram realizadas 2 séries de testes de 5 partidas para esta verificação:    
A 1ª série foi realizada com o humano jogando com as peças pretas e o minimax jogando com as brancas.   
A 2ª série foi realizada com o minimax jogando com as peças pretas e o jogador humano com as brancas.

Todos os resultados, utilizando as jogadas perfeitas do site e registrando as jogadas realizadas pelo minimax,em ambas situações, foram empates.

# Avaliação Othello

(I): Função de avaliação customizada

A função de avaliação customizada utiliza a combinação de 3 fatores: o valor das casas do tabuleiro, o número de peças e a quantidade de movimentos.
Para cada um desses valores, um peso, entre 0 e 1, é multiplicado, dando mais relevância a alguma característica. Assim, a avaliação ocorre da seguinte forma:
se é um estado terminal, a utilidade do estado é retornada. Senão, é calculado o valor estimado daquele estado. Para isso, para cada posição no tabuleiro, 
é verificado se há uma peça do player, somando o valor daquela casa em um acumulador, ou se há uma peça do oponente, descontando o valor da casa do 
acumulador. Além disso, com outro acumulador, é contado o número de peças do player e descontado o número de peças do oponente. Ademais, é tomada a quantidade
de movimentos legais que o player pode fazer naquele estado - subtraído pela quantidade de movimentos legais que o oponente pode fazer naquele estado. Com  isso, o valor dessas três variáveis é retornado, e cada um é multiplicado a um peso, p_valor, p_peça e p_mobilidade respectivamente.

(II): Descrição do critério de parada

Para o nosso algoritmo do minimax, temos três critérios de parada: uma profundidade limite (d), se o estado atual é terminal ou se o temporizador atingiu o 
limite de tempo por jogada. No trabalho, foram dados 5 segundos para calcular o próximo movimento, dessa forma, como medida de segurança para não ser 
desqualificado por demorar tempo demais, foi implementado um temporizador que conta um número máximo de segundos que uma chamada de minimax pode levar. Dessa 
forma, é como se tivéssemos uma profundidade dinâmica, indo mais fundo na área de busca enquanto tivermos tempo. Não colocamos 5 segundos de temporizador nem 
mais do que 4.5, pois, em alguns testes, era comum sofrermos penalidade por tempo, mesmo com essa restrição de tempo, já que o algoritmo tinha ainda que responder todas as  chamadas recursivas do minimax. 

Para o MCTS, por outro lado, deixamos um tempo fixo de 4.9 segundos, que não nos deu problemas. Assim, ele simula vários jogos aleatoriamente enquanto tiver tempo disponível.

(III): Resultado da avaliação

Os testes demonstraram que a função de avaliação customizada obteve melhores resultados contra todos os outros algoritmos, incluíndo o MCTS. Os valores dos 
pesos associados a cada avaliação do estado foram os seguintes: p_valor = 0.3, p_peça = 0.1 e p_mobilidade = 0.6. Além disso, a profundidade máxima com 
melhor desempenho foi a de 15, sendo que o tempo limite por lance foi marcado em 4.5 segundos. Nos testes, de 10 jogos contra cada um dos outros algoritmos, 
a função custom ganhou todos os 10, somando 30 vitórias.

(IV): Implementação escolhida para o torneio

A implementação escolhida para o torneio foi a customizada, p_valor = 0.3, p_peça = 0.1 e p_mobilidade = 0.6, profundidade máxima 15 e tempo limite de 4.5 segundos.

Feedback:

O trabalho foi bastante divertido de se fazer, se nós tivéssemos mais tempo (fora da correria do fim de semestre) seria muito interessante explorar outras
heurísticas e outros métodos para aprimorar nossa IA. Mesmo assim, no geral, foi uma experiência positiva e gratificante.

A utilização de assistentes de IA com certeza facilitou a implementação dos algoritmos, pois nos dá uma visão customizada de todos os pontos do algoritmo.
O maior problema, porém, foi a diferença entre a representação do jogo pela IA e a representação do jogo que nos foi dada. Isso afeta bastante o retorno do
algoritmo, e, portanto, tivemos dificuldade quanto a isso. Além disso, a IA foi muito boa para bolar novas heurísticas para o jogo.

