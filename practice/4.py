def factorial(num):
    if num == 0:
        return 1
    total = 1
    for i in range (num, 1, -1):
        total *= i
    return total