shift = {}
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alphabet_upper)):
    shift[alphabet_upper[i]] = alphabet_upper[(i + 3) % 26]
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alphabet_lower)):
    shift[alphabet_lower[i]] = alphabet_lower[(i + 3) % 26]
text = input("Nhập tin nhắn cần mã hóa: ")
encrypted = ""
for ch in text:
    if ch in shift:
        encrypted += shift[ch]
    else:
        encrypted += ch
print("Tin nhắn sau khi mã hóa:", encrypted)
