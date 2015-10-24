#!/usr/bin/env python3.5

import re,zipfile

num = '90052'
pattern = re.compile('(\d*)')
zfile = zipfile.ZipFile('channel/channel.zip','r')
comments = []
for i in range(909):
    data = open('channel/'+num+'.txt').read()
    comments.append(zfile.getinfo(num+'.txt').comment.decode())
    #print(data)
    num = ''.join(re.findall(pattern,data))
print(''.join(comments))
