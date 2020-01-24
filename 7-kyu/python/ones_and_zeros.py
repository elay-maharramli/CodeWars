def binary_array_to_number(arr):
    res = int("".join(str(x) for x in arr), 2)
    return res
