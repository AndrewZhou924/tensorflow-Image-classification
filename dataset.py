import tensorflow as tf
import numpy as np
import cv2
import sys
import os


def _parse_function(filename, label):
    image_string = tf.read_file(filename)
    # 读取图片
    image_decoded = tf.image.decode_png(image_string, channels=3)
    # 调整大小
    image_resized = tf.image.resize_images(image_decoded, [28, 28])
    return image_resized, label

def list_all_files(rootdir):
    # 返回某目录下的所以文件（包括子目录下的）
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files




