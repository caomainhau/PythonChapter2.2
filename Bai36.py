numbers = []
while True:
    n = int(input("Nhập số nguyên: "))
    if n == 0:
        break
    numbers.append(n)
numbers.sort()
print("Các số đã nhập:")
for num in numbers:
    print(num)
