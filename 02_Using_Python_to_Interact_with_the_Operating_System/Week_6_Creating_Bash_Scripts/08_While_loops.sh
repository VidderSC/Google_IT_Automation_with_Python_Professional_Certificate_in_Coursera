#!/bin/bash

# Advanced Bash Concepts
# While Loops in Bash Scripts

clear 

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

