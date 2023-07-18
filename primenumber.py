# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:25:32 2023

@author: coolu
"""
b=[]
d=[4,3,6,7,5,8,4,2,11]
e=[]
for i in range(1,101):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        b.append(i)
print(b)

q=2
for k in range(q):
    for l in range(0,len(d)):
        if d[l-1]%b[k]==0:
            e.append(d[l-1])
            
        
        
print(e)
