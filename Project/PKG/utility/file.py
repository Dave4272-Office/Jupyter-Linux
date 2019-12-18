#!/usr/bin/env python
# coding: utf-8

import os

def filelister(path, outpath):
    """
    ==========
    filelister
    ==========
    
    Utility Function to get the path of PNG Images in a directory.
    
    Arguments
    =========
    path         String containing the path to search for PNG files
    
    outpath      String containing the path to return for output path
                 of processed Image
                 
    Returns
    =======
    files        List of Tuple(s)
                 Where each element is of the format:
                 ( path/filename.png, outpath/filename.png )
    """
    files = list()
    for dirName, subdirList, fileList in os.walk(path):
        temp = list()
        for i in fileList:
            _,e = os.path.splitext(i)
            if e == '.png':
                temp.append((os.path.join(dirName,i), os.path.join(outpath,i)))
        files.extend(temp)
    return files

