def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(input("Nhập số: "))
print(f"Giai thừa của {n} là {factorial(n)}")
8