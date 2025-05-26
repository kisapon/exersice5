a = float(input("Введите число а: "))
b = float(input("Введите число b: "))
def counter(a, b):
    result = (a + 4 * b) * (a - 3 * b) + a * 2
    return result
print(counter(a, b))