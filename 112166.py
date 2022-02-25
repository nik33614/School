from math import*
x,y = map(float,input().split())
if(x>=0) and (x<=pi) and (y<=sin(x)) and (y<=0.5) and (y>=0):#(y>=0)and(y<0,5)and(y<sin(x))and(x>0)and(x<=3)and(x<=pi)
    print("YES")
else:
    print("NO")
#(y>=0)and(y<0,5)and(y<sin(x))and(x>0)and(x<=3)and(x<=pi)
