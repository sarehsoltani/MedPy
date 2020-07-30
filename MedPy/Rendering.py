from __future__ import print_function
import sys
import pydicom as dicom
import os
from matplotlib import pyplot, cm
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import SimpleITK as sitk
from glob import glob
from skimage.util import montage as montage2d

    
PathDicom  = 'F:/University/S0000001119/S0000001119/'
#def safe_sitk_read(folder_name, *args, **kwargs):
#    dicom_names = sitk.ImageSeriesReader().GetGDCMSeriesFileNames(folder_name)
#    return sitk.ReadImage(dicom_names, *args, **kwargs)

#def sitk_to_np(in_img):
    # type: (sitk.Image) -> Tuple[np.ndarray, Tuple[float, float, float]]
#    return sitk.GetArrayFromImage(in_img), in_img.GetSpacing()
    
#patient_folders = glob('F:/University/S0000001119/S0000001119/')
#print(patient_folders)
#first_pat = safe_sitk_read(patient_folders[0])
#pat_img, pat_spc = sitk_to_np(first_pat)    
#pyplot.imshow(montage2d(pat_img), cmap = 'bone')
#pyplot.show()
flair_file = 'F:/University/S0000001119/S0000001119/I0000470284.dcm'

images = sitk.ReadImage(flair_file)
print("Width: ", images.GetWidth())
print("Height:", images.GetHeight())
print("Depth: ", images.GetDepth())

print("Dimension:", images.GetDimension())
print("Pixel ID: ", images.GetPixelIDValue())
print("Pixel ID Type:", images.GetPixelIDTypeAsString())