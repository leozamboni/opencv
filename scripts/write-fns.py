#!/usr/bin/python
from PIL import Image
import os

path = "n_samples"
fns = os.listdir( path )
f = open("n.txt", "a")

i=0
for fn in fns:
    # if i==600: break
    fpath=path+fn
    f.write(f'{path}/{fn}\n')
    i+=1

f.close()

