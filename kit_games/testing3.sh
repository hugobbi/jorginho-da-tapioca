#!/bin/bash

for num in {1..10}
do
    if ((num % 2 == 0)); then
        echo "p1 mcts %"
        python server.py othello advsearch/jorginho_da_tapioca/mcts.py advsearch/jorginho_da_tapioca/othello_minimax_custom.py
    else
        echo "p1 custom %"
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_custom.py advsearch/jorginho_da_tapioca/mcts.py
    fi
done

