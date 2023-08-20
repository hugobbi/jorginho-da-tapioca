#!/bin/bash

for num in {1..20}
do
    if ((num % 2 == 0)); then
        python server.py othello advsearch/jorginho_da_tapioca/othello_minimax_mask.py advsearch/randomplayer/agent.py
    else
        python server.py othello advsearch/randomplayer/agent.py advsearch/jorginho_da_tapioca/othello_minimax_mask.py
    fi
done

