# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:42:03 2022

@author: Marcos Daniel Rodríguez Farfán

Main function that controls all turing machine
"""
import argparse
import inputValidation as inpVal
import data_segmentation as data
import turingMachine as TM
import show_data as sd

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
        #Call function to split data
        Data_dictionary[key] = data.split_data(key, value)
            
    #Check if something is wrong in language or states
    inpVal.alphabet_validation('gamma','sigma', Data_dictionary)   
    inpVal.alphabet_validation('Q','q0', Data_dictionary)   
    inpVal.alphabet_validation('Q','F', Data_dictionary)   
    inpVal.transition_validation('gamma', 'Q', 'f', Data_dictionary)
    inpVal.verify_test(Data_dictionary['test'], Data_dictionary['val'])
    
    #Create dictionary with results from turing machine
    dict_results = TM.turing_machine(Data_dictionary['test'], Data_dictionary['val'],
                      Data_dictionary['b'], Data_dictionary['f'],
                      Data_dictionary['q0'],Data_dictionary['F'])
    
    #Call function to display results in display or save it in a txt file
    sd.show_data(args.i, args.o, dict_results, Data_dictionary)
    
    