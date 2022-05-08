#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Helper class to return filenames or full file paths filtering away hidden files
#
##
from os import listdir

# 
def get_filenames(directory):
    """
    Get filenames in directory filtering out hidden files
    Parameters:
      directory - directory to return filenames from
    Returns:
      filenames - list of filtered filenames
    """
    print("directory = {}".format(directory))
    filename_list = listdir(directory)
    print("len(directory) = {}".format(len(filename_list)))
    filtered_filenames = []
    for idx in range (0, len(filename_list), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if filename_list[idx][0] != ".":
            filtered_filenames.append(filename_list[idx])
   
    print("len(filtered_filenames) = {}".format(len(filtered_filenames)))
    return filtered_filenames

def get_full_filenames(directory):
    """
    Get full filenames with path in directory filtering out hidden files
    Parameters:
      directory - directory to return filenames from
    Returns:
      filenames - list of filtered full filenames
    """
    print("directory = {}".format(directory))
    filename_list = listdir(directory)
    print("len(directory) = {}".format(len(filename_list)))
    filtered_filenames = []
    for idx in range (0, len(filename_list), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if filename_list[idx][0] != ".":
            filtered_filenames.append(directory + "/" + filename_list[idx])
   
    print("len(filtered_filenames) = {}".format(len(filtered_filenames)))
    return filtered_filenames