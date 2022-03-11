a,b = map(int,input().split())
c,d = map(int,input().split())
y = 10000
i = ''

while y < 100000:
    if(y % a == b) and (y % c == d):
        i = i + str(y)+" "
    y+=1

if i=="":
    print("-1")
else:
    print(i)
