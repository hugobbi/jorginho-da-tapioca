#!/bin/bash

for num in {1..10}
do
    if ((num % 2 == 0)); then
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_count.py advsearch/jorginho_da_tapioca/othello_minimax_custom.py
    else
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_custom.py advsearch/jorginho_da_tapioca/othello_minimax_count.py
    fi
done

