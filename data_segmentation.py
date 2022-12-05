# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:58:30 2022

data_segmentation module:
    This module gets all recived data from txt file and separate them into lists
    
    Functions:
        split_data: funtions that split data into lists
"""

def split_data(keys,values):

    """
   Function to split data
   
   Takes values from the dictionary, takes out spaces and split them.
   If it's a number convert the string into a float value, if it's a string 
   just save the value readed
   
   Input: type value (sorting_algorithms and sense algorithm 
          when separated by "," unsorted_lists by "|") and values of dictionary 
   Output: data splited and if its a number a list of float numbers
   """
    data_splited = []
    if keys == 'f':
       values = values.strip('{').strip('}').split(',')
       for item in values:
           data_splited.append(item.replace(')->('," ").replace('(','').replace(')','').split(' '))
    elif keys == 'b' or keys == 'q0':
        data_splited = values.split()
    else:
        data_splited = values.strip('{').strip('}').split(',')
            
    return data_splited #Return our splited list