# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:57:49 2022

@author: PC GOAT
"""
import re
#%%Create functions
#Function to validate our input
"""
   This function check's if there is an error introducing our data by 
   command window
   
   Inputs: readed file and output file introduced as args in command window
   Outputs: if the user forgets to add txt to input or output file name it
            raises an exception. If there is no error shows if the results will 
            show in comand window or saved in a txt file
"""
def validate_input(inputs,outputs):
    #Verify if it is going to show data in display
    if outputs == None:
        if inputs.endswith('.txt'):#Check if ends with txt
            print("Results will be displayed in console")
        else:
            raise Exception("Error in input file name, please check it")
        
    #Verify if it is going to save data in a text file
    elif outputs != None:
        if outputs.endswith('.txt'):#Check if ends with txt
            print("Results will be saved in a txt file")
        else:
            raise Exception("\nError in output file name, please check it")

#Function to get data and validate our file
"""
    This function checks if our file has the correct patterns and information,
    first declare all patterns to find and make a list of it. Then open our file 
    and check by line if it match with a pattern and the line were was found
"""
def patterns(arguments):
    #All patterns to read
    q_pattern = '@(\s*Q\s*)\s*=\s*({(\s*q\d\d*\s*)+(,\s*q\d\d*\s*)*})'
    sigma_pattern = '@(\s*sigma\s*)\s*=\s*({(\s*\d\s*)+(,\s*\d\s*)*})'
    gamma_pattern = '@(\s*gamma\s*)\s*=\s*({\s*\d\s*,\s*\d\s*,\D\s*,\s*\D\s*,\s*\D\s*})'  
    starter_pattern = '@(\s*q0\s*)\s*=\s*(\s*\D\d\d*\s*)'  
    space_pattern = '@(\s*b\s*)\s*=\s*(\s*\D\s*)'
    final_state_pattern = '@(\s*F\s*)\s*=\s*({(\s*\D\d\d*\s*)+(,\s*\D\d\d*\s*)*})'
    transition_pattern = '@(\s*f\s*)=\s*({\(\s*q\d+ \s*\w\s*\)\s*->\s*\(\s*q\d+ \s*\w \s*\D\)\s*(,\s*\(\s*q\d+ \s*\w\s*\)\s*->\s*\(\s*q\d+ \s*\w \s*\D\)\s*)*})'
    test_pattern = '@(\s*test\s*)\s*=\s*({(\s*\d*\s*)+(,\s*\d*\s*)*})'
    eval_pattern = '@(\s*val\s*)\s*=\s*({(\s*\D*\s*)+(,\s*\D*\s*)*})'
    #Create list of patterns
    patterns =[q_pattern,sigma_pattern,gamma_pattern,starter_pattern
               ,space_pattern,final_state_pattern,transition_pattern
               ,test_pattern,eval_pattern]   
    
    check = []
    #Check every line of our file 
    for i, line in enumerate(open(arguments)):
        for pat in patterns:
            #Check if there´s a match
            for match in re.finditer(pat, line):
                print ('Found on line %s: %s' % (i+1, match.group()))
                #Add to our check list to make sure all arguments are in the file
                check.append(match.group(1))
    
    #Create list with our names to check
    names = ['Q','sigma','gamma','q0','b','F','f','test','val']
    #Check if theres no missing line
    for name in names:
         if name not in check:
             raise Exception("One data is missing in input file, add or check {} line".format(name))
    print('Your data has been readed successfully')
             
                