# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:57:49 2022

@author: Marcos Daniel Rodríguez Farfán

inputValidation module:
    This module contains everything to make validations in our readed file
    
    Functions:
        validate_input:This function check's if there is an error introducing our data by 
        command window.
        patterns: Function to get data and validate our file using regular expresions.
        alphabet_validation: verify if something is included in our language.
        transition_validation: verify if everything in our transition state is
        defined.
        verify_test: verify if tests and values are the same lenght.
"""
import re

def validate_input(inputs,outputs):
    """
   Function to validate our input
   
   This function check's if there is an error introducing our data by 
   command window

    Parameters
    ----------
    inputs : TYPE
        readed file and output file introduced as args in command window.
    outputs : TYPE
        if the user forgets to add txt to input or output file name it
        raises an exception. If there is no error shows if the results will 
        show in comand window or saved in a txt file.

    Raises
    ------
    Exception
        When the input or output file name is not correct.

    Returns
    -------
    None.

    """
    #Verify if it is going to show data in display
    if outputs == None:
        if inputs.endswith('.txt') or inputs.endswith('.def'):#Check if ends with txt
            print("Results will be displayed in console")
        else:
            raise Exception("Error in input file name, please check it")
        
    #Verify if it is going to save data in a text file
    elif outputs != None:
        if outputs.endswith('.txt'):#Check if ends with txt
            print("Results will be saved in a txt file")
        else:
            raise Exception("\nError in output file name, please check it")


def patterns(arguments):
    """

        Function to get data and validate our file.
        
        This function checks if our file has the correct patterns and information,
        first declare all patterns to find and make a list of it. Then open our file 
        and check by line if it match with a pattern and the line were was found

    Parameters
    ----------
    arguments : args
        Out input file name to open.

    Raises
    ------
    Exception
        Raise an exception when it does not find all fields we need to to
        execute the program.

    Returns
    -------
    myDict : Dict
        Returns a dictionary containing all the information found on the txt file.

    """
    myDict = {}
    #All patterns to read
    q_pattern = '@(\s*Q\s*)\s*=\s*({(\s*\w+\s*)+(,\s*\w+\s*)*})'
    sigma_pattern = '@(\s*sigma\s*)\s*=\s*({(\s*\w+\s*)+(,\s*\w+\s*)*})'
    gamma_pattern = '@(\s*gamma\s*)\s*=\s*({(\s*\w+\s*)+(,\s*\w+\s*)*})'  
    starter_pattern = '@(\s*q0\s*)\s*=\s*(\s*\w+\s*)'  
    space_pattern = '@(\s*b\s*)\s*=\s*(\s*\w\s*)'
    final_state_pattern = '@(\s*F\s*)\s*=\s*({(\s*\w+\s*)})'
    transition_pattern = '@(\s*f\s*)=\s*({\(\s*\w+ \s*\w+\s*\)\s*->\s*\(\s*\w+ \s*\w+ \s*\w+\s*\)\s*(,\s*\(\s*\w+ \s*\w+\s*\)\s*->\s*\(\s*\w+ \s*\w+ \s*\w+\s*\)\s*)*})'
    test_pattern = '@(\s*test\s*)\s*=\s*({(\s*\w+\s*)+(,\s*\w+\s*)*})'
    eval_pattern = '@(\s*val\s*)\s*=\s*({(\s*\w+\s*)+(,\s*\w+\s*)*})'
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
                #print ('Found on line %s: %s' % (i+1, match.group()))
                #Add to our check list to make sure all arguments are in the file
                check.append(match.group(1))
                myDict[match.group(1)] = match.group(2)
                
    
    #Create list with our names to check
    names = ['Q','sigma','gamma','q0','b','F','f','test','val']
    #Check if theres no missing line
    for name in names:
         if name not in check:
             raise Exception("Something went wrong trying to laod data file, maybe one data is missing or wrong written, add or check {} line".format(name)) 
    return myDict

def alphabet_validation(key,field_name, dictionary):
    """
    Function to check errors introduced in our automaton
    This function takes two important variables, 'key' and 'field_name'
    Key is used to get language or states of our automaton, field name 
    gets a field that is suposed to be defined in our language or states.Then
    compares if all data in our field is defined in our language or states, if 
    not raises an exception.

    Parameters
    ----------
    key : String
        This variable gets the key of our dictionary to check if a 
        element exists.
    field_name : String
        Name of field we want to verify if it is defined in our language or states.
    dictionary : Dict
        Dictionary that contains all the information.

    Raises
    ------
    Exception
        Raise an exception when it finds something that does not belog to our 
        language or states.

    Returns
    -------
    None.

    """
    alphabet = dictionary[key]
    field = dictionary[field_name]
    for element in field:
        if element not in alphabet:
            raise Exception('The element "{}" in {} is not defined in {}'.format(element,field_name,key))
def transition_validation(lang,state,field_name,dictionary):
    """
    Function to check errors introduced in our automaton
    This function takes two important variables, 'key' and 'field_name'
    Key is used to get language or states of our automaton, field name 
    gets a field that is suposed to be defined in our language or states.Then
    compares if all data in our field is defined in our language or states, if 
    not raises an exception.

    Parameters
    ----------
    key : String
        This variable gets the key of our dictionary to check if a 
        element exists.
    field_name : String
        Name of field we want to verify if it is defined in our language or states.
    dictionary : Dict
        Dictionary that contains all the information.

    Raises
    ------
    Exception
        Raise an exception when it finds something that does not belog to our 
        language or states.

    Returns
    -------
    None.

    """
    alphabet = dictionary[lang]
    states = dictionary[state]
    field = dictionary[field_name]
    
    for element in field:
        for item in element:
            if item in alphabet or item in states or item == 'R' or item == 'L' or item == 'S':
                pass
            else:
                raise Exception('The item "{}" in {} is not defined in {} or {}'.format(item,field_name,lang,state))
    
def verify_test(testing,validation):
    """
    Function to verify lenght of test values and validation

    Parameters
    ----------
    testing : List
        DESCRIPTION. List of testing values
    validation : List
        DESCRIPTION. List of accepted and rejected

    Raises
    ------
    Exception
        DESCRIPTION. Exception when lenghts does not match

    Returns
    -------
    None.

    """
    if len(testing) == len(validation):
        pass
    else:
        raise Exception('Please verify  test and val lines, they are not the same lenght')
        
