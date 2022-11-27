# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:42:03 2022

@author: PC GOAT
"""
import argparse
import inputValidation as inpVal

#%%
if __name__ == '__main__':
    
    #Create our parser
    parser = argparse.ArgumentParser()
    #input
    parser.add_argument('-i', help = 'Enter your filename', required = True)
    #Output
    parser.add_argument('-o', help = 'Save data in text file')
    args = parser.parse_args()
    
    #Verify inputs    
    inpVal.validate_input(inputs = args.i,outputs = args.o)

    inpVal.patterns(args.i)
    #Call function to check line with regular expresion
    #Dict = data.check_line(file)