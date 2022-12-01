# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:48:14 2022

@author: PC GOAT
"""
def transition_function(transition,index,mylist):
    actual_state = transition[2]
    mylist[index] = transition[3]
    if transition[4] == 'L':
        index -= 1
    elif transition[4] == 'R':
        index += 1
    elif transition[4] == 'S':
        index = index
    return [actual_state,mylist,index]    

def turing_machine(testing,validation,blank,rules,initial_state,final_state):
    test = []
    blank_space = blank[0]*4
    for test_list in testing:
        test_list = blank_space + test_list+ blank_space
        test.append(list(test_list))
        
        
    actual_state = initial_state[0]
    i = 4
    for actual_test in test:
        for i in range(4, len(actual_test)-4):
            for states in rules:
                if actual_test[i] == states[1] and actual_state == states[0]:
                    actual_state,actual_test,i = transition_function(states, i+4, actual_test)

                
                        
                    
    
        
        
        
    