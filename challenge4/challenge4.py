#!/usr/bin/python2

import urllib2
import re

url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num='12345'
pattern=re.compile('(\d*)')
for i in range(400):
    full_url=url+num
    text=urllib2.urlopen(full_url).read()
    num=''.join(pattern.findall(text))
    print(text)
