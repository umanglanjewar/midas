# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 19:52:41 2023

@author: coolu
"""

a=[10,5,9,8]
b=[8,4,3,-1]
e=[]
for i in range(len(a)):
    e.append(a[i]-b[i])
      
z=0    
# print(e)
for i in range(len(e)):
    # e[i]**2
    z=z+e[i]**2
    
MSE=z/len(e)
# MSE=(e[0]**2 + e[1]**2 + e[2]**2 + e[3]**2)/len(e) 
print("mean square error", MSE)

x=0
for i in range(len(e)):
    x=x+e[i]
    
MAE=abs(x)/len(e)    
print("mean apsolute error",MAE)

y=0
v=0
for i in range(len(e)):
    y=(y+e[i]/a[i])
    v=abs(y)/len(e)
    
MAPE=abs(y)/len(e)    
print("mean apsolute percentage error",MAPE)
        