def check(ch):
    g = 0
    for i in range(len(str(ch))):
        g = g + int(str(ch)[i-1])**int(len(str(ch)))
    if g == ch:
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
