# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:08:15 2022

Module Show data:
    This module has all functionsto display our results in tables and show them 
    
    Contains:
        Create_table: function to create our table of results
        Show_data: Function to show our results in display or save it in a txt file.
"""
from prettytable import PrettyTable


def create_table(dictionary,results):
    """
    Function to create table with results

    Parameters
    ----------
    dictionary : dict
        DESCRIPTION. Dictionary with data readed from txt file
    results : list
        DESCRIPTION. List of accepted or rejected results 

    Returns
    -------
    table : table
        DESCRIPTION. Returns a table of results with tested string, result expected
        and result obtained
    """
    table = PrettyTable()
    table.field_names = ['Tested','Validation','Result']
    
    for item, res, val in zip(dictionary['test'],results,dictionary['val']):
        table.add_row([item, res, val])
    
    return table


def show_data(inputs,outputs,results,dictionary):
    """
    Function to show our results in display or save it in a txt file.
    This function call our function to create tables, then checks how is going 
    to be shown our results 

    Parameters
    ----------
    inputs : str
        DESCRIPTION. txt file name to read
    outputs : str
        DESCRIPTION. txt file name to save results
    results : List
        DESCRIPTION. List of accepted or rejected results
    dictionary : dict
        DESCRIPTION.Dictionary with data readed from txt file

    """
    #Call function to generate tables of results
    results_table = create_table(dictionary,results)
    #Verify if it is going to show data in display
    if inputs != None and outputs == None:
        #Print tables
        print(results_table)

        
    #Verify if it is going to save data in a text file
    if outputs != None:
        try:
          #x is used to create a file only if it does not exist
           fp = open(outputs, 'w')#Create file with specified name
           fp.write(str(results_table)) #Write our results table
           fp.close()
           print("File created")
        
        except FileExistsError:
            print("The file already exists")