# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:48:14 2022

turingMAchine Module:
    This module executes all funtions to handle our turing machine.
    
    Functions:
        transition_function:Function to execute transitions of turing machine.
        turing_machine: Function of turing machine, it's how it works

"""
def transition_function(transition,index,mylist):
    """
    Function to execute transitions of turing machine, changes our actual state 
    changes our tape, and adjust our index (head) 

    Parameters
    ----------
    transition : List
        DESCRIPTION.This list contains our state transition 
    index : int
        DESCRIPTION.This index value tell us where is the head of our turing machine
    mylist : list
        DESCRIPTION.This list represents our tape in turing machine

    Returns
    -------
    list
        DESCRIPTION. Returns a list with our updated state, tape and index or 
        our head
    """
    #Change our state
    actual_state = transition[2]
    #Change our tape
    mylist[index] = transition[3]
    #Adjust head
    if transition[4] == 'L':
        index -= 1
    elif transition[4] == 'R':
        index += 1
    elif transition[4] == 'S':
        index = index
    return [actual_state,mylist,index]    

def turing_machine(testing,validation,blank,rules,initial_state_machine,final_state_machine):
    """
    Function of turing machine
    First adds blank spaces to all our tests, then gets a test value and initializes
    our turing machine with initial (actual_state),final state(final_state)
    and head position (i). Then moves over all our posible transition states, if 
    there is a match between readed value and actual state calls function to make
    transition, it means this test is accepted, if after execute all transition 
    states does not find a matching result verify if there is none transition state 
    that matches our actual value and state, if not the test is rejected

    Parameters
    ----------
    testing : List
        DESCRIPTION.Lsit of all our testing values
    validation : List
        DESCRIPTION.List of accepted or rejected
    blank : List
        DESCRIPTION.A string of blank space
    rules : List
        DESCRIPTION.A list of our transition functions
    initial_state_machine : List
        DESCRIPTION.Our initial state of turing machine
    final_state_machine : List
        DESCRIPTION.Final state of turing machine

    Returns
    -------
    results : List
        DESCRIPTION.List of accepted and rejected tests

    """
    results = []
    test = []
    blank_space = blank[0]*4
    for test_list in testing:
        test_list = blank_space + test_list+ blank_space
        test.append(list(test_list))
        

    for index, actual_test in enumerate(test):
        actual_state = initial_state_machine[0]
        final_state = final_state_machine[0]
        i = 4
        #Flag to get out of while when is accepted
        flag = False
        while flag != True:
            for states in rules:
                if actual_test[i] == states[1] and actual_state == states[0]:
                    actual_state,actual_test,i = transition_function(states, i, actual_test)
                    if actual_state == final_state:
                        flag = True
                        i = 4
                        results.append('accepted')
                        break
                #Execute in the last state
                if states == rules[-1]:
                    #Flag to check if the line is rejected by turing machine
                    rejected_flag = False
                    for states in rules:
                        if actual_test[i] == states[1] and actual_state == states[0]:
                           rejected_flag = True
                    if rejected_flag == False:
                        flag = True
                        results.append('rejected')
    
    return results
                        

                    
                    
                        
                    
    
        
        
        
    