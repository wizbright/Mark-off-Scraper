#!/bin/python3

# Used to call scrape.py by passing it a text file with multiple entries
# and categories

# File input should be <category> <url> Make sure a space is inbetween to parse correctly

import sys
import scrape

# print(sys.argv[1])

infile = open(sys.argv[1], "r")
count = 0

for item in infile:
    insplit = item.split(" ")
    category = insplit[0]
    url = insplit[1]
 #   print(url)
 #   print(category)
    scrape.main(url, category)
    count = count + 1

print(str(count) + " file(s) processed.")
