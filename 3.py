import random
c= ''
a,b=map(int,input().split())
for i in range(5):
    c+=str(random.randint(a,b))+' '
    
print(c[:-1])
