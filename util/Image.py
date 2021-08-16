import cv2
import numpy as np
from numpy.lib.stride_tricks import as_strided


def transf(img, rows, stride = 3, th = 70):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h = img.shape[0], img.shape[1]
    cols = rows * h // w
    size_new = (cols * stride, rows * stride)
    img = cv2.resize(img, dsize=size_new, interpolation=cv2.INTER_CUBIC)
    imgArray = np.array(img)
    imgArray = (imgArray < th)*1
    imgArray = pool2d(imgArray,stride,stride)
    return imgArray.tolist(), imgArray.T.tolist()

def pool2d(A, kernel_size, stride):
    output_shape = ((A.shape[0] - kernel_size)//stride + 1,
                    (A.shape[1] - kernel_size)//stride + 1)
    kernel_size = (kernel_size, kernel_size)
    A_w = as_strided(A, shape = output_shape + kernel_size, 
                        strides = (stride*A.strides[0],
                                   stride*A.strides[1]) + A.strides)
    A_w = A_w.reshape(-1, *kernel_size)
    return A_w.max(axis=(1,2)).reshape(output_shape)