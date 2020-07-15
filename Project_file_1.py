# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)


dataDir='..'
dataType='val2017'
annFile='C:/Users/Rishabh Jain/OneDrive/Desktop/Project/annotations/instances_val2017.json'.format(dataDir,dataType)

# initialize COCO api for instance annotations
coco=COCO(annFile)


# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())


Fa = input("Enter the first word to be in the picture = ")
Sa = input("Enter the second word to be in the picture = ")
Ta = input("Enter the first word to be in the picture = ")

#Wording = input("Enter the word which you want to draw = ")

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=[Fa,Sa,Ta]);
imgIds = coco.getImgIds(catIds=catIds );
imgIds = coco.getImgIds(imgIds =imgIds)
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

# load and display image
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# use url to load image
I = io.imread(img['coco_url'])

plt.figure()
plt.axis('off')
plt.imshow(I)
plt.show()