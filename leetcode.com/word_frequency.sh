#!/usr/bin/env bash


# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr ' ' '\n' | grep -v "^$" | sort | uniq -c | sort | tac | awk '{print $2" "$1}'
