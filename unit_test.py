# -*- coding:utf8 -*-
# Created by Helic on 2018/12/4
import tensorflow as tf
print(tf.__version__)

tf.enable_eager_execution()

a = tf.constant(tf.ones([2, 3]))
b = tf.constant(tf.zeros([2, 3]))
print(a * b)

print(tf.get_variable('v1', shape=[10]))