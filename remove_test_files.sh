#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 suffix1 [suffix2 ... suffixN]"
    exit 1
fi

for suffix in "$@"
do
    find ./tests -type f -name "*${suffix}" -exec rm {} \;
    echo "All files ending with ${suffix} have been removed."
done
