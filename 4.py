import random
c= ''
a,b=map(float,input().split())
for i in range(5):
    c+=str(format(random.uniform(a,b),".3f"))+' '
    
print(c[:-1])
