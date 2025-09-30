chuoi = input("Nhập kí tự cần kiểm tra: ")
Tong_chuoi_in = 0
Tong_chuoi_thuong = 0
for c in chuoi:
    if c.isupper() :
        Tong_chuoi_in += 1
    elif c.islower() :
        Tong_chuoi_thuong += 1
    else:
        pass
print("Tổng chuỗi in là: ",Tong_chuoi_in)
print("Tổng chuỗi thường: ",Tong_chuoi_thuong)
