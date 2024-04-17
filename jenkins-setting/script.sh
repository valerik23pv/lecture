#!/bin/bash

while read line; do
    echo $line

if [[ -n $line ]]
then
    ver=$(cat result.txt | jq '.Verified')
    echo $ver
    exit 1
elif [[ -z $line ]]
then

    exit 0
fi
done < "result.txt"