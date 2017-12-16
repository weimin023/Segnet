import os 
import tensorflow as tf 
from PIL import Image  

###output folder
swd = os.getcwd()+'/show/'

###解析哪一個record
filename_queue = tf.train.string_input_producer(["training.tfrecords-000"]) 
reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)  
features = tf.parse_single_example(serialized_example,
                                   features={
                                       'label': tf.FixedLenFeature([], tf.int64),
                                       'img_raw' : tf.FixedLenFeature([], tf.string),
                                   }) 
 
 ###image size要改
image = tf.decode_raw(features['img_raw'], tf.uint8)
image = tf.reshape(image, [500,500,3])
label = tf.cast(features['label'], tf.int32)
with tf.Session() as sess: 
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
 
    coord=tf.train.Coordinator()
    threads= tf.train.start_queue_runners(coord=coord)
    for i in range(5):
        example, l = sess.run([image,label]) 
        img=Image.fromarray(example, 'RGB') 
        img.save(swd+str(i)+'_''Label_'+str(l)+'.png') #格式可能改變
        #print(example, l)
    coord.request_stop()
    coord.join(threads)
