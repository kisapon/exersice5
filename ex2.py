arr = [2, 80, -4, 2, -4, 1, 90, -6, 33, 20, 1, -14]
def sum_multiply(arr):
    multiply = 1
    summ = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            summ += arr[i]
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)
    for i in range(start_index, end_index):
        multiply *= arr[i]
    return summ, multiply
print(sum_multiply(arr))
