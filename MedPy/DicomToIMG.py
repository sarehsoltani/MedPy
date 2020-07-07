import pydicom as dicom
import os
import matplotlib.pylab as plt
import numpy as np
import glob

PathDicom = "F:/University/S0000001119/S0000001119"
DCMFiles = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            DCMFiles.append(os.path.join(dirName,filename))        

FirstFile = dicom.read_file(DCMFiles[0])
ConstPixelDims = (int(FirstFile.Rows), int(FirstFile.Columns))
ConstPixelSpacing = (float(FirstFile.PixelSpacing[0]), float(FirstFile.PixelSpacing[1]), float(FirstFile.SliceThickness))

x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
#z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])
ArrayDicom = np.zeros(ConstPixelDims)

for filenameDCM in DCMFiles:
    ds = dicom.read_file(filenameDCM)
    ArrayDicom = ds.pixel_array
    
  
#Plot    
plt.figure(dpi=150)
plt.axes().set_aspect('equal', 'datalim')
#plt.set_cmap(plt.gray())
plt.pcolormesh(x, y, np.flipud(ArrayDicom))
plt.imshow(ArrayDicom)
plt.show()