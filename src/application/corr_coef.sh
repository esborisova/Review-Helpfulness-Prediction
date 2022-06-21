#!/bin/bash

file_names=('pearson'
            'spearman');         

for my_file_name in "${file_names[@]}"; do
    IFS=' ' read f_type func  <<< $my_file_name

    echo "Run: " $my_file_name
    python3 plot_correlation.py $my_file_name

done