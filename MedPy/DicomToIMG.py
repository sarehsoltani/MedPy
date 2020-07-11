import pydicom as dicom
import os
import matplotlib.pylab as plt, cm
import numpy as np
import glob

PathDicom = "F:/University/S0000001119/S0000001119"
DCMFiles = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            DCMFiles.append(os.path.join(dirName,filename))        

FirstFile = dicom.read_file(DCMFiles[0])
PixelDims = (int(FirstFile.Rows), int(FirstFile.Columns), len(FirstFile))
ConstPixelSpacing = (float(FirstFile.PixelSpacing[0]), float(FirstFile.PixelSpacing[1]), float(FirstFile.SliceThickness))

x = np.arange(0.0, (PixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(0.0, (PixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
#z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])
ArrDicom = np.zeros(PixelDims, dtype=FirstFile.pixel_array.dtype)

for j in DCMFiles:
    ds = dicom.read_file(j)
    ArrDicom [:, :, DCMFiles.index(j)] = ds.pixel_array
    
#Plot    
plt.figure(dpi=150)
plt.axes().set_aspect('equal', 'datalim')
#plt.set_cmap(plt.gray())
plt.pcolormesh(x, y, np.flipud(ArrDicom))
plt.imshow(ArrDicom)
plt.show()