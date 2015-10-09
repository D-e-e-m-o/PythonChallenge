#!/usr/bin/env python3.4

Str = open('text').read()
dic = {}
for i in Str:
	dic[i] = dic.get(i,0)+1
print(''.join(i for i in Str if dic[i]==1))
