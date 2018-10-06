#!/bin/bash

for ((num=1; num<=99; num++))
do
    if [ $((num%2)) -eq 1 ];
        then
            echo "$num"
    fi
done
