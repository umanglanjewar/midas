# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:33:06 2023

@author: coolu
"""

class node():
    def __init__(self,val):
        self.val=val
        self.next=None
        

class stack():
    def __init__(self):
         self.head=None      
    def insert(self,newval):
        if self.head==None:
            self.head=node(newval)
        else :
            newnode=node(newval)
            newnode.next=self.head
            self.head=newnode
                        