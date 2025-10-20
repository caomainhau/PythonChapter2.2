words = []
while True:
    w = input("Nhập từ: ")
    if w == "":
        break
    if w not in words:
        words.append(w)

print("\nCác từ sau khi loại bỏ trùng:")
for w in words:
    print(w)
