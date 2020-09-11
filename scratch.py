import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(len(a)-1, 0, -1):
    j = random.randint(0, i + 1)
    a[i], a[j] = a[j], a[i]

print(a)