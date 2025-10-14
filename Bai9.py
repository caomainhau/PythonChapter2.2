# Khai báo chuỗi ban đầu
my_str = "Hello this Is an Example With cased letters"

# Nếu muốn người dùng nhập vào thì thay bằng lệnh sau:
# my_str = input("Enter a string: ")

# Tách từ trong chuỗi và lưu vào danh sách ds_tu
ds_tu = my_str.split()

# Sắp xếp các phần tử (từ) trong danh sách ds_tu
ds_tu.sort(key=str.lower)

# Hiển thị các từ trong danh sách
print("Các từ đã được tách và sắp xếp theo Alphabet:")
for tu in ds_tu:
    print(tu)
