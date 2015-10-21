#!/usr/bin/env python3.5

import pickle

data = pickle.load(open('banner.p','rb'))
for line in data:
    print(''.join(s[0]*s[1] for s in line))
