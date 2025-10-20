x=int(input("Nhập số cần tính giai thừa:"))
def giaithua(x):
    if x == 0:
        return 1
    return x * giaithua(x - 1)
print(giaithua(x))