#!/bin/bash

for num in {1..10}
do
    if ((num % 2 == 0)); then
        echo "mcts p1"
        python server.py othello advsearch/jorginho_da_tapioca/mcts.py advsearch/jorginho_da_tapioca/othello_minimax_custom.py
    else
        echo "cust p1"
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_custom.py advsearch/jorginho_da_tapioca/mcts.py
    fi
done

