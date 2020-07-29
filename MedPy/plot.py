import pydicom
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob

# load the DICOM files
PathDicom = "F:/University/S0000001119/S0000001119"
files = []
#print('glob: {}'.format(sys.argv[1]))
for fname in glob.glob(sys.argv[1], recursive=False):
    #print("loading: {}".format(PathDicom))
    files.append(pydicom.read_file(PathDicom))

print("file count: {}".format(len(files)))

# skip files with no SliceLocation (eg scout views)
slices = []
skipcount = 0
for f in files:
    if hasattr(f, 'SliceLocation'):
        slices.append(f)
    else:
        skipcount = skipcount + 1

print("skipped, no SliceLocation: {}".format(skipcount))

# ensure they are in the correct order
slices = sorted(slices, key=lambda s: s.SliceLocation)

# pixel aspects, assuming all slices are the same
ps = slices[0].PixelSpacing
ss = slices[0].SliceThickness
ax_aspect = ps[1]/ps[0]
sag_aspect = ps[1]/ss
cor_aspect = ss/ps[0]

# create 3D array
img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
img3d = np.zeros(img_shape)

# fill 3D array with the images from the files
for i, s in enumerate(slices):
    img2d = s.pixel_array
    img3d[:, :, i] = img2d

# plot 3 orthogonal slices
a1 = plt.subplot(2, 2, 1)
plt.imshow(img3d[:, :, img_shape[2]//2])
a1.set_aspect(ax_aspect)

a2 = plt.subplot(2, 2, 2)
plt.imshow(img3d[:, img_shape[1]//2, :])
a2.set_aspect(sag_aspect)

a3 = plt.subplot(2, 2, 3)
plt.imshow(img3d[img_shape[0]//2, :, :].T)
a3.set_aspect(cor_aspect)

plt.show()


#for i in ArrayDicom:
 #   plt.figure(dpi=10)
  #  plt.imshow(ArrayDicom)


    #print(ArrayDicom[1])
    #plt.imshow(ArrayDicom[0])
    #plt.show()

    #rows=6 
    #cols=6
    #start_with=10
    #show_every=3
    #fig,ax = plt.subplots(rows,cols,figsize=[2,2])
    #for i in range(rows*cols):
    #    ind = start_with + i*show_every
    #    #ax[int(i/rows),int(i % rows)].set_title('slice %d' % ind)
    #    ax[int(i/rows),int(i % rows)].imshow(ArrayDicom[ind],cmap='gray')
    #    ax[int(i/rows),int(i % rows)].axis('off')
    #plt.show()
  

#cnt = 1
#fig, axes = plt.subplots(7, 4 , figsize=(5, 5))
#for i, row in enumerate(axes):
 #   for j, axe in enumerate(row):
  #      if i > 3:
   #         if j > 3 - cnt:
    #            axe.set_visible(False)
   # if i > 3:
    #    cnt += 1 
#print(ArrayDicom[1])  