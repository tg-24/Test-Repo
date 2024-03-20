import math
def drawtriangle(a,b):
    temp=0
    if(a>b):
        temp=-1
    else:
        temp=1
    for i in range(a,b+temp,temp):
        print(i,end=" ")
drawtriangle(20,1)
