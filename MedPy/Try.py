import pydicom as dicom
import os
import matplotlib.pylab as plt
import numpy as np

PathDicom = "F:/University/S0000001119/"
lstFilesDCM = []  # create an empty list
count = 0
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))
            count = count +1
            #print(lstFilesDCM)
print(count)           
# Get ref file
RefDs = dicom.read_file(lstFilesDCM[0])
#print(RefDs)
# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
print(ConstPixelDims)
# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

# The array is sized based on 'ConstPixelDims'
ArrayDicom = np.zeros(ConstPixelDims)
print("ArrayDicom.shape",ArrayDicom.shape)
# loop through all the DICOM files
for filenameDCM in lstFilesDCM:
    # read the file
    ds = dicom.read_file(filenameDCM)
    #image = ds.pixel_array 
    #print(lstFilesDCM.index(filenameDCM))
    #print(image.shape)
    #plt.imshow(image)
    #plt.show()
    # store the raw image data
    ArrayDicom = ds.pixel_array

