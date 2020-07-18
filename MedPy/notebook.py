import numpy as np
import pandas as pd
from skimage.io import imread
import seaborn as sns
import matplotlib.pyplot as plt
from glob import glob
import pydicom as dicom
import os


PATH = "F:/University/S0000001119/dataset"
#print(os.listdir(Path))
print("Number of DICOM files:", len(os.listdir(PATH)))
# extract voxel data  
def extract_voxel_data(list_of_dicom_files):  
    datasets = [dicom.read_file(f) for f in list_of_dicom_files]  
    try:  
         voxel_ndarray, ijk_to_xyz = np.combine_slices(datasets)  
    except np.DicomImportException as e:  
     # invalid DICOM data  
         raise  
    return voxel_ndarray 