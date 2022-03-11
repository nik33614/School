def check(ch):
    g = ch**2
    h = str(g)[-len(str(ch)):]
    
     
    if h == str(ch):
        return True
    else:
        return False
u = ''
a,b = map(int,input().split())
for i in range(a,b+1):
    if check(i):
      u=u+str(i)+' '
if u == "":
    print("-1")
else:
    print(u)
