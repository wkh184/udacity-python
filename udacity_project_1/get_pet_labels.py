#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

from dir_helper import get_filenames

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder image_dir
    filename_list = get_filenames(image_dir)

    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    # a List that contains only one item - the pet image label
    for idx in range(0, len(filename_list), 1):
        print("filename = {}".format(filename_list[idx]))
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if filename_list[idx][0] != ".":
            if filename_list[idx] not in results_dic:
                pet_name = get_pet_name(filename_list[idx])
                results_dic[filename_list[idx]] = [pet_name]
            else:
                print("** Warning: Key=", filename_list[idx], "already exists in results_dic with value =", results_dic[filename_list[idx]])

    #Iterating through a dictionary printing all keys & their associated values
    #print("\nPrinting all key-value pairs in dictionary results_dic:")
    #for key in results_dic:
    #    print("Filename=", key, "   Pet Label=", results_dic[key][0])
        
    return results_dic
    
def get_pet_name(filename):
    """
    Split the filename to get pet name
    Parameters:
     filename - filename of the file following the naming convention "Boston_terrier_02259.jpg"
    Returns:
      pet_name - pet name as retrieved from filename
    """

    # Sets string to lower case letters
    low_filename = filename.lower()

    # Splits lower case string by _ to break into words 
    word_list_filename = low_filename.split("_")

    # Create pet_name starting as empty string
    pet_name = ""

    # Loops to check if word in pet name is only
    # alphabetic characters - if true append word
    # to pet_name separated by trailing space 
    for word in word_list_filename:
        if word.isalpha():
            pet_name += word + " "

    # Strip off starting/trailing whitespace characters 
    pet_name = pet_name.strip()

    # Prints resulting pet_name
    #print("\nFilename=", filename, "   Label=", pet_name)

    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return pet_name
