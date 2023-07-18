# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:20:35 2023

@author: coolu
"""

class node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def insert(self,new_val):
        checker = self
        if checker.val<new_val:
            if checker.left == None:
                checker.left = node(new_val)
            else:
                checker.left.insert(new_val)
        else:
            if checker.right == None:
                checker.right = node(new_val)
            else:
                checker.right.insert(new_val)
                
    # def inorder(self):
    #     if self.left.left!=None:
    #         self.left.inorder()
    #     else:
    #         print(self.left.val)
    #     print(self.val)
    #     if self.left.right!=None:
    #         self.right.inorder()
    #     else:
    #         print(self.right.val)
            
    # def postorder(self):
    #     if self.left.left!=None:
    #         self.left.postorder()
    #     else:
    #         print(self.left.val)
        
    #     if self.left.right!=None:
    #         self.right.postorder()
    #     else:
    #         print(self.right.val)
    #     print(self.val)
        
    # def preorder(self):
    #     print(self.val)
    #     if self.left.left!=None:
    #         self.left.preorder()
    #     else:
    #         print(self.left.val)
        
    #     if self.left.right!=None:
    #         self.right.preorder()
    #     else:
    #         print(self.right.val)
            
    def inorder(self):
        if self.left.left!=None:
            self.left.inorder()
        else:
            print(self.left.val)
        print(self.val)
        if self.left.right!=None:
            self.right.inorder()
        else:
            print(self.right.val)
    
            
    
        
        
                
                
a = node(10)
a.insert(5)
a.insert(11)
a.insert(6)
a.insert(12)
a.insert(8)
a.insert(4)
a.insert(10.5)
a.insert(5.5)
a.insert(13)
a.insert(11.5)
a.insert(10.6)
a.insert(10.4)
a.insert(4.5)
a.insert(3)


a.inorder()
# a.postorder()
# a.preorder()

