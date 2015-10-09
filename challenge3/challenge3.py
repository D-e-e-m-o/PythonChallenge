#!/usr/bin/python3.4

import re

text=open('text').read()
find=''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))
print(find)
