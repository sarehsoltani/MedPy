import pydicom
import matplotlib.pylab as plt
import numpy as np
#import cv2
import os

def transform_to_hu(medical_image, image):
    intercept = medical_image.RescaleIntercept
    slope = medical_image.RescaleSlope
    hu_image = image * slope + intercept
    return hu_image

def window_image(image, window_center, window_width):
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    window_image = image.copy()
    window_image[window_image < img_min] = img_min
    window_image[window_image > img_max] = img_max
    return window_image    

file_path = "F:/University/S0000001119/sample/CT_small.dcm"
output_path = "./"
medical_image = pydicom.read_file(file_path)
print(medical_image.pixel_array)
image = medical_image.pixel_array 
print(image.shape)
hu_image = transform_to_hu(medical_image, image)
brain_image = window_image(hu_image, 40, 80)
#print(brain_image)
bone_image = window_image(hu_image, 400, 1000)
#plot the image using matplotlib
plt.imshow(image)
plt.show()


#ds = pydicom.filereader.dcmread('F:/University/S0000001119/sample/sam.dcm')
