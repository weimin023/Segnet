import numpy as np
from PIL import Image as im
import os 

fname = 'list.txt'
filename = []
with open(fname,encoding = 'utf8') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
filename = [x.strip() for x in content] 
print (len(filename))

for i in filename:
    file_read = i
    print (os.path.splitext(os.path.basename(file_read))[0])
    if (os.path.splitext(os.path.basename(file_read))[1]) == '.tif':
        image = im.open(file_read)
        image.save(os.path.splitext(os.path.basename(file_read))[0]+'.png')


