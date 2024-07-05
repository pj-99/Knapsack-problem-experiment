#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 folder_path suffix1 [suffix2 ... suffixN]"
    exit 1
fi

folder=$1
shift

for suffix in "$@"
do
    find "$folder" -type f -name "*${suffix}" -exec rm {} \;
    echo "All files ending with ${suffix} in ${folder} have been removed."
done