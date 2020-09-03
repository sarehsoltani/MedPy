import pydicom
import numpy as np
import cv2
import os


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from scipy import ndimage
import skimage.morphology as morph

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

def load_and_plot_image(file_path, save=False):
    #medical_image = pydicom.read_file(file_path)
    #image = medical_image.pixel_array
   #data_set = dicom.read_file(path)
    #pixel_array = data_set.pixel_array
    #size_of_array = image.shape
    ct_dicom = pydicom.read_file(file_path)   
    img = ct_dicom.pixel_array
    img_2d = img.astype(float)

## Step 2. Rescaling grey scale between 0-255
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0

## Step 3. Convert to uint
    img_2d_scaled = np.uint8(img_2d_scaled)


# Show information of input and output in above code
## (1) Show information of original CT image 
    print(img.dtype)
    print(img.shape)
    print(img)

## (2) Show information of gray image of it 
    print(img_2d_scaled.dtype)
    print(img_2d_scaled.shape)
    print(img_2d_scaled)

## (3) Show the scaled gray image by matplotlib
    plt.imshow(img_2d_scaled, cmap='gray', vmin=0, vmax=255)
    plt.show()
    #print(chanR)
    #print(image)
    #print(image.dtype)
    #print(image.shape)
  
    
    #hu_image = transform_to_hu(medical_image, image)
    #brain_image = window_image(hu_image, 40, 80)
    #bone_image = window_image(hu_image, 400, 1000)
    
    #plt.figure(figsize=(20, 10))
    #plt.style.use('grayscale')

    #plt.subplot(200)
    #plt.imshow(image)
    #plt.title('Original')
    #plt.axis('off')
    #plt.show()
    

    #plt.subplot(152)
    #plt.imshow(hu_image)
    #plt.title('Hu image')
    #plt.axis('off')
    

    #plt.subplot(153)
    #plt.imshow(brain_image)
    #plt.title('brain image')
    #plt.axis('off')

    #plt.subplot(154)
    #plt.imshow(bone_image)
    #plt.title('bone image')
    #plt.axis('off')
    #plt.show()
    
    #if save:
     #   mpimg.imsave(os.path.join(output_path, f'{file_path[:-4]}-original.png'), image)
        #mpimg.imsave(os.path.join(output_path, f'{file_path[:-4]}-hu_image.png'), hu_image)
        #mpimg.imsave(os.path.join(output_path, f'{file_path[:-4]}-brain_image.png'), brain_image)
        #mpimg.imsave(os.path.join(output_path, f'{file_path[:-4]}-bone_image.png'), bone_image)


#final_image = remove_noise("F:/University/S0000001119/sample/sam.dcm")
#plt.imshow(final_image)
#plt.show()

load_and_plot_image("F:/University/Terms/term9/AI/DetectionMRI/MedPy/dataset/I0000470285.dcm")
