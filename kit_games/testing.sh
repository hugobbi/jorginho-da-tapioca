#!/bin/bash

for num in {1..10}
do
    if ((num % 2 == 0)); then
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_mask.py advsearch/jorginho_da_tapioca/othello_minimax_count.py
    else
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_count.py advsearch/jorginho_da_tapioca/othello_minimax_mask.py
    fi
done

