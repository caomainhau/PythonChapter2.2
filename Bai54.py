def format_words(words):
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

lst = []
while True:
    w = input("Nhập từ (Enter để dừng): ")
    if w == "":
        break
    lst.append(w)

print("Kết quả:", format_words(lst))
