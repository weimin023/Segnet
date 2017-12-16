import os 
import tensorflow as tf 
from PIL import Image  

#current dir /trainset---house, nohouse
#or
#current dir /validset---house, nohouse
#


#image path
###
cwd = os.getcwd()+'/trainset/'


#file path
filepath = cwd

bestnum = 1000

num = 0

recordfilenum = 0

###
classes=['house_sliced',
         'nohouse_sliced']
         
ftrecordfilename = ("training.tfrecords-%.3d" % recordfilenum)
writer= tf.python_io.TFRecordWriter(ftrecordfilename)

for index,name in enumerate(classes):
    print(index)
    print(name)
    class_path=cwd+name+'/'
    for img_name in os.listdir(class_path): 
        num=num+1
        if num>bestnum:
          num = 1
          recordfilenum = recordfilenum + 1
          
          ftrecordfilename = ("training.tfrecords-%.3d" % recordfilenum)
          writer= tf.python_io.TFRecordWriter(ftrecordfilename)
        '''
        print(num)
        print(recordfilenum)
        print(img_name)
        '''
        img_path = class_path+img_name #each image path
        img=Image.open(img_path)
        img_raw=img.tobytes()
        example = tf.train.Example(
             features=tf.train.Features(feature={
             
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
        })) 
          
        writer.write(example.SerializeToString()) 
writer.close()
