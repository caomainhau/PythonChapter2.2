st1 = "!()-[]{};:'\",<>./?@#$%^&*_~"
my_str = input("Nhập chuỗi: ")
st2 = ""
for char in my_str:
    if char not in st1:
        st2 = st2 + char
print(st2)
