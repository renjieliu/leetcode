#!/bin/bash
# Read from the file file.txt and output all valid phone numbers to stdout.
cat file.txt | grep '^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$\|^([0-9][0-9][0-9]) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$'
