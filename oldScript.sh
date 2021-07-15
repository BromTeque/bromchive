#!/bin/bash

declare -a entries_array

# echo Please Enter path to YT archive folder:
# read archivePath
# echo path: $archivePath

# Temporary Variable for Debugging
archivePath=/home/bromteque/tstest

# Checks if Path is Valid
[ ! -d $archivePath ] && echo "Directory $archivePath DOES NOT exists. Enter valid path"

for entry in "$archivePath"/*
do
    entries_array+=( $entry )
done

echo ${entries_array[*]}

exit 0