# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:59:37 2023

@author: coolu
"""

class node():
    def __init__(self,val):
        self.root=val
        self.left=None
        self.right=None
    
class tree():
    def __init__(self,head):
        self.head=None
    def insert(self,root):
        if self.head==None:
            self.head=node(root)
        else:
            newnode=node(root)
            self.root.left=
        