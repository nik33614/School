a = input()
p = 0
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        p+=1
print(p)
