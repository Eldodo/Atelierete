from random import random
import turtle
from math import sqrt

A=(-250,-250);B=(250,-250);C=(0,(sqrt(3)/2*500)-250)
n=10000
M=(0,-250)
turtle.hideturtle()
turtle.speed(0)
turtle.up()
turtle.setpos(A)
turtle.dot(2)
turtle.setpos(B)
turtle.dot(2)
turtle.setpos(C)
turtle.dot(2)
turtle.setpos(M)
turtle.dot(2)
def milieux (A,B):
    x=(A[0]+B[0])/2.0
    y=(A[1]+B[1])/2.0
    return (x,y)

for i in range (n):
    r=random ()
    if r <1/3.0:
        M=milieux (A,M)
    elif r <2/3.0:
        M=milieux (B,M)
    else:
        M=milieux (C,M)
    turtle.setpos(M)
    turtle.dot(2)
