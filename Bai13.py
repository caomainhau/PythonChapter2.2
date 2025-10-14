lines = []
while True:
    s = input("Nhập chuỗi: ")
    if s == "done":
        break
    lines.append(s.upper())
for sentence in lines:
    print(sentence)
