#!/bin/python3
# Used to scrape pages for tigerhacks project

from lxml import html
import requests
import sys
import subprocess

def main(arg1, arg2):

    page = requests.get(arg1)
    tree = html.fromstring(page.content)

#	print(arg1)

    headline = tree.xpath('//header[@class="content-header "]//text()')
    textContent = tree.xpath('//div[@class="content-text"]//text()')

    # clean up content
    ht = [a.strip() for a in headline]
    tct = [a.strip() for a in textContent]

    for x in ht:
        if x == "":
            ht.remove(x)

    htencoded = ht
    for line in htencoded:
        line.encode("ascii", "ignore")

    print(ht)
    print(htencoded)
    for x in tct:
        if x == "":
            tct.remove(x)

#	print(ht)
#	print(tct)

    # Write to file
    fmode = "a"
    category = arg2

    out = subprocess.run(["mkdir", category], stderr = subprocess.DEVNULL)

    hf = open(category + "/headers.txt", fmode)
    for item in ht:
        hf.write("%s\n" % item)
    hf.close()

    cf = open(category + "/content.txt", fmode)
    for item in tct:
        cf.write("%s\n" % item)
    cf.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
