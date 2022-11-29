# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:42:03 2022

@author: Marcos Daniel Rodríguez Farfán
"""
import argparse
import inputValidation as inpVal
import data_segmentation as data

#%%
if __name__ == '__main__':
    Data_dictionary = {}
    mylist = []
    
    #Create our parser
    parser = argparse.ArgumentParser()
    #input
    parser.add_argument('-i', help = 'Enter your filename', required = True)
    #Output
    parser.add_argument('-o', help = 'Save data in text file')
    args = parser.parse_args()
    
    #Verify inputs    
    inpVal.validate_input(inputs = args.i,outputs = args.o)

    Data_dictionary = inpVal.patterns(args.i)
    
    for key,value in Data_dictionary.items():
        print(key,'\n',value)
        #Call function to split data 
        Data_dictionary[key] = data.split_data(key, value)
