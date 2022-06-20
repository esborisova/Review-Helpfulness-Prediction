#!/bin/bash

file_names=('votes_up'
            'weighted_vote_score');         

for my_file_name in "${file_names[@]}"; do
    IFS=' ' read f_type func  <<< $my_file_name

    echo "Run: " $my_file_name
    python3 plot_hist_labels.py $my_file_name

done