import turtle
from math import sqrt

A=(-250,-250);B=(250,-250);C=(0,(sqrt(3)/2*500)-250)
n = 7

def milieux (A,B):
    x=(A[0]+B[0])/2.0
    y=(A[1]+B[1])/2.0
    return (x,y)

def triangle(a,b,c,n):
    if(n == 0):
        return
    n = n-1
    turtle.up()
    turtle.goto(a)
    turtle.down()
    turtle.goto(b)
    turtle.goto(c)
    turtle.goto(a)
    triangle(a,milieux(a,b,),milieux(a,c),n)
    triangle(milieux(a,b),b,milieux(b,c),n)
    triangle(milieux(a,c),milieux(b,c),c,n)

turtle.pensize(2)
turtle.speed(0)
triangle(A,B,C,n)
    
