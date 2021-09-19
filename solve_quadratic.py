import math

def solve_quadratic (a,b,c):
    d=b*b-4*a*c
    if d>0:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        return x1,x2

    if d<0:
        x1= -b/2*a
        return x1


    else:

        return 0

test1 =solve_quadratic (1,0,4)

print(test1)