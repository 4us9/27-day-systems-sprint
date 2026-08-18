#! /bin/bash

my_array=(1 2 "three" "four" 5)

echo ${my_array[@]}

#First Way
for item in ${my_array[@]}; do
    echo $item
done

#Second Way
for 