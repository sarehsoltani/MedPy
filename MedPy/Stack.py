import numpy as np
import pydicom as dicom
import os
import matplotlib.pyplot as plt
from glob import glob
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage
from skimage import morphology
from skimage import measure
from skimage.transform import resize
from sklearn.cluster import KMeans
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
#init_notebook_mode(connected=True)
INPUT_FOLDER = 'F:/University/S0000001119/dataset/'
patients = os.listdir(INPUT_FOLDER)
patients.sort()


#def load_scan(path):
  #  slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
 #   slices.sort(key = lambda x: int(x.InstanceNumber))
 #   try:
 #       slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
 #   except:
 #       slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
        
 #   for s in slices:
 #       s.SliceThickness = slice_thickness
        
 #   return slices
def load_scan(path):
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: float(x.ImagePositionPatient[2]))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
        
    for s in slices:
        s.SliceThickness = slice_thickness
        
    return slices

#def get_pixels_hu(scans):
 #   image = np.stack([s.pixel_array for s in scans])
    # Convert to int16 (from sometimes int16), 
    # should be possible as values should always be low enough (<32k)
  #  image = image.astype(np.int16)

    # Set outside-of-scan pixels to 1
    # The intercept is usually -1024, so air is approximately 0
   # image[image == -2000] = 0
    
    # Convert to Hounsfield units (HU)
    #intercept = scans[0].RescaleIntercept
   # slope = scans[0].RescaleSlope
    
    #if slope != 1:
     #   image = slope * image.astype(np.float64)
      #  image = image.astype(np.int16)
        
    #image += np.int16(intercept)
    
    #return np.array(image, dtype=np.int16)

def get_pixels_hu(slices):
    image = np.stack([s.pixel_array for s in slices])
    # Convert to int16 (from sometimes int16), 
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)

    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    
    # Convert to Hounsfield units (HU)
    for slice_number in range(len(slices)):   
        intercept = slices[slice_number].RescaleIntercept
        slope = slices[slice_number].RescaleSlope
        
        if slope != 1:
            image[slice_number] = slope * image[slice_number].astype(np.float64)
            image[slice_number] = image[slice_number].astype(np.int16)
            
        image[slice_number] += np.int16(intercept)
    
    return np.array(image, dtype=np.int16)


#def plot_3d(image):
    
    # Position the scan upright, 
    # so the head of the patient would be at the top facing the   
    # camera
#    p = image.transpose(2,1,0)
    
#    verts, faces= measure.marching_cubes_lewiner(p)
#    fig = plt.figure(figsize=(10, 10))
#    ax = fig.add_subplot(111, projection='3d')
    # Fancy indexing: `verts[faces]` to generate a collection of    
    # triangles
#    mesh = plotly(verts[faces], alpha=0.70)
#    face_color = [0.45, 0.45, 0.75]
#    mesh.set_facecolor(face_color)
#    ax.add_collection3d(mesh)
#    ax.set_xlim(0, p.shape[0])
#    ax.set_ylim(0, p.shape[1])
#    ax.set_zlim(0, p.shape[2])
#    plt.show()

#data_path = "F:/University/S0000001119/dataset/"
#output_path = "F:/University/S0000001119/S0000001119/"
#id=0
#patient = load_scan(data_path)
#imgs = get_pixels_hu(patient)
#np.save(output_path + "fullimages_%d.npy" % (id), imgs)
    #sanity check
# run visualization 
#plot_3d(patient_pixels)    
#plt.imshow(patient_pixels, cmap=plt.cm.bone)
#plt.show()
#id = 0
#imgs_to_process = np.load(output_path+'fullimages_{}.npy'.format(id))

def sample_stack(stack, rows=4, cols=4, start_with=10, show_every=3):
    fig,ax = plt.subplots(rows,cols,figsize=[12,12])
    for i in range(rows*cols):
        ind = start_with + i*show_every
        ax[int(i/rows),int(i % rows)].set_title('slice %d' % ind)
        ax[int(i/rows),int(i % rows)].imshow(stack[ind],cmap='gray')
        ax[int(i/rows),int(i % rows)].axis('off')
    #plt.show()
#sample_stack(imgs_to_process)
#print("Slice Thickness: %f" % patient[0].SliceThickness)
#print ("Pixel Spacing (row, col): (%f, %f) " % (patient[0].PixelSpacing[0], patient[0].PixelSpacing[1]))
#imgs_to_process = np.load(output_path+'fullimages_{}.npy'.format(id))
#print("Transposing surface")

#def resample(image, scan, new_spacing=[1,1,1]):
    print("11")
    # Determine current pixel spacing
    spacing = np.array([scan[0].SliceThickness] + list(scan[0].PixelSpacing), dtype=np.float32)
    #spacing = map(float, ([scan[0].SliceThickness] + list(scan[0].PixelSpacing)))
    print("12")
    spacing = np.array(list(spacing))
    print("3")
    resize_factor = spacing / new_spacing
    print("4")
    new_real_shape = image.shape * resize_factor
    print("5")
    new_shape = np.round(new_real_shape)
    print("6")
    real_resize_factor = new_shape / image.shape
    print("7")
    new_spacing = spacing / real_resize_factor
    print("8")
    
    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor)
    print("9")
    
    return image, new_spacing

print("Shape before resampling\t", imgs_to_process.shape)
imgs_after_resamp, spacing = resample(imgs_to_process, patient, [1,1,1])
print ("Shape after resampling\t", imgs_after_resamp.shape)
def make_mesh(image, threshold=-300, step_size=1):
    
    print("Transposing surface")
    p = image.transpose(2,1,0)
    
    print("Calculating surface")
    verts, faces, norm, val = measure.marching_cubes(p, threshold, step_size=step_size, allow_degenerate=True) 
    return verts, faces

def plotly_3d(verts, faces):
    x,y,z = zip(*verts) 
    print("Drawing")
    
    # Make the colormap single color since the axes are positional not intensity. 
#    colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
    colormap=['rgb(236, 236, 212)','rgb(236, 236, 212)']
    
    fig = FF.create_trisurf(x=x,
                        y=y, 
                        z=z, 
                        plot_edges=False,
                        colormap=colormap,
                        simplices=faces,
                        backgroundcolor='rgb(64, 64, 64)',
                        title="Interactive Visualization")
    iplot(fig)

def plt_3d(verts, faces):
    print("Drawing")
    x,y,z = zip(*verts) 
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
    face_color = [1, 1, 0.9]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_zlim(0, max(z))
    ax.set_facecolor((0.7, 0.7, 0.7))
    plt.show()

v, f = make_mesh(imgs_after_resamp, 350)
plt_3d(v, f)    