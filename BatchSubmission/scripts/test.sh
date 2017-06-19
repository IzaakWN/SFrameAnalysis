#!/bin/bash

while getopts "m:" opt; do
    case $opt in
        m) multi+=("$OPTARG");;
        #...
    esac
done
shift $((OPTIND -1))

echo "The first value of the array 'multi' is '$multi'"
echo "The whole list of values is '${multi[@]}'"

echo "Or:"

for val in "${multi[@]}"; do
    echo " - $val"
done
