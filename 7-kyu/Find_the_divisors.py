def divisors(integer):
    i = 2
    arr = []
    while i < integer:
        if integer % i == 0:
            arr.append(i)
        i = i + 1
    if arr == []:
        return str(integer) + " is prime"
    return arr
