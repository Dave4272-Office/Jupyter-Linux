#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt #imread, imsave

from .utility import file #filelister

# ### The Method to Convert RGB to Gray-scale image

def RGB_to_Gray(X):
    """
    ===========
    RGB_to_Gray
    ===========
    
    This Method Gives the Luminosity(Y) of an RGB Image.
    
    Arguments
    =========
    X            RGB Image as numpy.ndarray
    
    Returns
    =======
    lum          numpy.ndarray containing the Luminosity Image
    """
    x, y, _ = X.shape
    shape = (x,y) 
    lum = np.zeros(shape, dtype=X.dtype)
    lum[:,:] = 0.299*X[:,:,0] + 0.587*X[:,:,1] + 0.114*X[:,:,2]
    return lum


def RGB2Gray(path, outpath):
    """
    ========
    RGB2Gray
    ========
    
    Wrapper function to convert all Colour PNG files
    from path to outpath
    
    Arguments
    =========
    path         String containing the path to search for PNG files
    
    outpath      String containing the path to return for output path
                 of processed Image
    """
    #list files using utility.file submodule
    file_list = file.filelister(path, outpath)
    #convert each file and save it
    for (i,j) in file_list:
        #image read
        colour_image = plt.imread(i)
        #Gray image
        gray_image = RGB_to_Gray(colour_image)
        #image save
        plt.imsave(j, gray_image, cmap='gray')
    return
