string = input("Введите строку: ")
if string.startswith("abc"):
    result = "www" + string[3:]
else:
    result = string + "zzz"
print("Измененная строка: ", result)