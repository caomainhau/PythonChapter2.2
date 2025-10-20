y = int(input("Nhap so nam: "))
if y % 400 == 0:
    print("Day la nam nhuan")
elif y % 100 == 0 and y % 400 != 0:
    print("Day khong phai la nam nhuan")
elif y % 4 == 0 :
    print("Day la nam nhuan")
else:
    print("Day khong phai la nam nhuan")