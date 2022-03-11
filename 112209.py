a, b = map(int, input().split())
for i in range(a, b + 1):
    f = set(int(f) for f in str(i))
    if all(d != 0 and i % d == 0 for d in f):
        print(i, end=' ')
