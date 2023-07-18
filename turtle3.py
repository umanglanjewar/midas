# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:25:08 2023

@author: coolu
"""

import turtle
t=turtle.Turtle()
n=100
m=10
for i in range(11):
    t.left(90)
    t.penup()
    t.goto(0,10+m)
    t.pendown()
    t.right(90)
    t.circle(n,360)
    n-=10
    m+=10