#!/usr/bin/env python3

import string

text = open('text').read();
table = text.maketrans(\
	string.ascii_lowercase,\
	string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print(text.translate(table))
