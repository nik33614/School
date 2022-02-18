import math
a, b = map(float, input().split())
c, d = map(float, input().split())
print(format(math.sqrt((c-a)**2+(d-b)**2), '.3f'))
