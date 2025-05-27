arr = [1, -5, 0, 3, -4]
def reversing(arr):
    result = []
    for i in arr:
        result.append(-i)
    return result
print("Преобразованный массив: ", reversing(arr))
