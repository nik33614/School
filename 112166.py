from math import*
x,y = map(float,input().split())
if(x>=0) and (x<=pi) and (y<=sin(x)) and (y<=0.5) and (y>=0):
    print("YES")
else:
    print("NO")
