#!/bin/python3
# Used to scrape pages for tigerhacks project

from lxml import html
import requests
import sys
import subprocess

page = requests.get(sys.argv[1])
tree = html.fromstring(page.content)

print(sys.argv[1])

headline = tree.xpath('//header[@class="content-header "]//text()')
textContent = tree.xpath('//div[@class="content-text"]//text()')

# clean up content
ht = [a.strip() for a in headline]
tct = [a.strip() for a in textContent]

for x in ht:
    if x == "":
        ht.remove(x)

for x in tct:
    if x == "":
        tct.remove(x)

print(ht)
print(tct)

# Write to file
fmode = "a"
category = sys.argv[2]

out = subprocess.run(["mkdir", sys.argv[2]])

hf = open(category + "/headers.txt", fmode)
for item in ht:
    hf.write("%s\n" % item)
hf.close()

cf = open(category + "/content.txt", fmode)
for item in tct:
    cf.write("%s\n" % item)
cf.close()
