from PIL import Image
import os, sys

path = "p_raw/"
fns = os.listdir( path )


for fn in fns:
    fpath=path+fn
    im = Image.open(fpath)
    imResized = im.resize((40,40), Image.LANCZOS)
    name=fn.split(".")[0]
    imResized.save('p/'+name + '.png', quality=90)

