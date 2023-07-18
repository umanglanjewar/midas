# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:54:18 2023

@author: coolu
"""

# def corner(n):
#     return 2**n

# print(corner(3))

def edge(n):
    if n==1:
        return 1
    else:
        return edge(n-1)*2+2**(n-1)
    

# print(edge(2))

def face(n):
    if n==2:
        return 1
    else:
        return face(n-1)*2+edge(n-1)
    
print(face(5))