x = float(input("Введите точку х: "))
y = float(input("Введите точку у: "))
r = float(input("Введите радиус: "))
def in_circle(x, y, r):
    if x*x + y*y <= r*r:
        return "Принадлежит."
    else:
        return "Не принадлежит."
print(in_circle(x, y, r))