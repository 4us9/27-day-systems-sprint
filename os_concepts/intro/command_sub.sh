#! /bin/bash

current_processes=`ps`
now=$(date)

echo -e "the processes as of $now is \n $current_processes"

echo -e 'Using literal: the processes as of $now is \n $current_processes'