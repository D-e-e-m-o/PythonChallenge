#!/usr/bin/env python2

import Image

img = Image.open('oxygen.png')
#any row will be OK
row = [chr(img.getpixel((i,50))[0]) for i in range(0, 609, 7)]
print(''.join(row))
print(''.join(map(chr,[105,110,116,101,103,114,105,116,121])))
