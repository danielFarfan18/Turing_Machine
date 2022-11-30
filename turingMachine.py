# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:48:14 2022

@author: PC GOAT
"""

def turing_machine(testing,validation,blank,rules):
    test = []
    blank_space = blank[0]*4
    for test_list in testing:
        test_list = blank_space + test_list+ blank_space
        test.append(list(test_list))
        
        
        
    