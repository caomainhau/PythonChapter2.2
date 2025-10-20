numbers = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")
num_list = [int(x) for x in numbers.split(",")]
odd_list = [x for x in num_list if x % 2 != 0]
print("Các số lẻ là:", odd_list)
