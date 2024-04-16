#!/bin/bash

while read line; do
    echo $line

if [[ -n $line ]]
then
    echo 0
    ver=$(cat result.txt | jq '.Verified')
    echo $ver
    exit 0
elif [[ -z $line ]]
then
    echo 1
    exit 1
fi
done < "result.txt"