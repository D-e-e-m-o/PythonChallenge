#!/usr/bin/python3

import re

text=open('text').read()
pattern = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',re.MULTILINE)
find=''.join(pattern.findall(text))
print(find)
