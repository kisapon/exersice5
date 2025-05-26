n = input("Введите целое число: ")
try:
    summ = int(n) * (int(n) + 1) // 2
    print("Сумма равна", summ)
except ValueError:
    print("Введите ЦЕЛОЕ число.")


