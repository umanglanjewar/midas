# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 20:23:54 2023

@author: coolu
"""

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))


def fab(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
    
print(fab(11))
print(fab(10))