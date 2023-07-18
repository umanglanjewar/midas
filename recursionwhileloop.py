# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:19:05 2023

@author: coolu
"""

def check(a):
    print(a)
    if a == 0:
        return 0
    for i in range(a):
        check(a-1)
        
    
check(4)
    