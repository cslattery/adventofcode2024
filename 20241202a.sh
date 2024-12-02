#!/bin/bash

data="./inputs/02/20241202.txt"
report_count=0
while read line; do # ignores last line of file if no CR

    line=$(echo "$line" | tr -d '[:punct:]' | sed 's/\r//g')
    IFS=' ' read -r -a array <<< "$line"
    echo line: $line
    first=${array[0]}
    second=${array[1]}
    previous=$first
    direction=0
    if (( first - second > 0 )); then
        direction=1 # 1 means decreasing
        echo "********Decreasing***************"
    elif (( $first - $second == 0 )); then
        echo "********Not increasing nor decreasing***************"
        direction=2
    else
        direction=0 # 0 means increasing
        echo "********Increasing***************"
    fi
    for ((i=1; i<${#array[@]}; i++)); do
        update=1
        echo "Position $i"
        element=${array[i]}
        diff=$(( element - previous ))
        echo "Direction $direction, Element $element, Previous $previous, Difference: $diff"
        if (( direction == 0 )) && ((( diff > 3 )) || (( diff <= 0 ))); then
            echo "No longer increasing"
            previous=$element
            update=0
            break
        elif (( direction == 1 )) && ((( diff >= 0 )) || (( diff < -3 ))); then
            echo "No longer decreasing"
            previous=$element
            update=0
            break
        elif (( direction == 2 )); then
            echo "Not increasing nor decreasing"
            previous=$element
            update=0
            break
        fi
        previous=$element
    done
    report_count=$((report_count+update))
    echo "Report count: $report_count"
done < $data