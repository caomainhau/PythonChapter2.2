a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b and a > c:
    tonhat = a
elif b > a and b > c:
    tonhat = b
elif c > a and c > b:
    tonhat = c
print("Số lớn nhất trong",a,",",b,",",c,"là: ",tonhat)