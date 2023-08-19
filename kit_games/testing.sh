#!/bin/bash

for num in {1..5}
do
    python server.py othello advsearch/randomplayer/agent.py  advsearch/jorginho_da_tapioca/mcts.py
done

