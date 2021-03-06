import cv2
import numpy as np
import time
import os
from time import ctime,sleep

def process():

    for i in range (100) :
        result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)


if __name__ == "__main__":
    # print('當前母程序:{}'.format(os.getpid()))
    
    img = cv2.imread('Lime.jpg')


    # cv2.setUseOptimized(False) # AVX
    cv2.setUseOptimized(True) # AVX
    print(cv2.useOptimized())


    gray        = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh  = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)

    for j in range (3, 11, 2):

        kernel    = np.ones((j,j),np.uint8)
        print(kernel.shape)

        Start_time  = time.time()
        process()
        End_time    = time.time()

        cv2.imshow('result', result)
        cv2.waitKey(0)

        print("用時{}秒".format((End_time-Start_time)))
# -----------------------------------------------------
cv2.destroyAllWindows()