import random
arr = []
while len(arr) != 10:
    n = random.randint(-100, 100)
    if n % 2 == 0:
        arr.append(n)
    arr.sort()
print(arr)
