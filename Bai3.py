chuoi = input("Nhập chuỗi: ")
timchuoi = input("Nhập chuỗi cần tìm: ")
if timchuoi in chuoi:
    print("Đã tìm thấy chuỗi, ở vị trí", str(chuoi.find(timchuoi)))
else:
    print("Không tìm thấy")