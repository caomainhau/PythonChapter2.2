def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print("Các số hoàn hảo từ 1 đến 10000:")
for i in range(1, 10001):
    if is_perfect(i):
        print(i)
