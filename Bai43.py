def compare_strings(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print(a)
        print(b)
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
compare_strings(s1, s2)
