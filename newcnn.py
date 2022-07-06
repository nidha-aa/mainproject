# coding: utf-8

# In[ ]:
import os


import tensorflow as tf

import keras
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
# import the opencv library
import cv2

import winsound 


#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =4
batch_size = 40
epochs = 5
#------------------------------

import os, cv2, keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2
import matplotlib
import matplotlib.pyplot as plt
# import seaborn as sns

# get_ipython().run_line_magic('matplotlib', 'inline')



def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

def predictcnn(fn):
    dataset=read_dataset1(fn)
    (mnist_row, mnist_col, mnist_color) = 48, 48, 1

    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    mo = load_model("model1.h5")
    dataset /= 255
    # predict probabilities for test set

    yhat_classes = mo.predict_classes(dataset, verbose=0)
    print(yhat_classes)
    return yhat_classes[0]

#
#     print(yhat_classes)



def capturess(path): 
  
    # import the opencv library

  
  
# define a video capture object
    vid = cv2.VideoCapture(path)

      
    while(True):
          
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
      
        # Display the resulting frame
        cv2.imshow('frame', frame)
        cv2.imwrite("static/file.jpg",frame)
        s=predictcnn("static/file.jpg")
        print(s)
        if s==0:
            print("Non Violence")
            nval="Non Violence"
        elif s==1:
            print("Violence")
            nval="Violence"
            break
        

            # break
          
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return nval
# c=capturess(0)

# s=predictcnn("static/dataset/violence/images.jpg")