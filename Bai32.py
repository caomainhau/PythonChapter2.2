shift_table = {}

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

for s in range(26):
    shift_table[s] = {}
    shift_table[s]['encrypt'] = {}
    shift_table[s]['decrypt'] = {}
    for i in range(26):
        shift_table[s]['encrypt'][alphabet_upper[i]] = alphabet_upper[(i + s) % 26]
        shift_table[s]['encrypt'][alphabet_lower[i]] = alphabet_lower[(i + s) % 26]
        shift_table[s]['decrypt'][alphabet_upper[i]] = alphabet_upper[(i - s) % 26]
        shift_table[s]['decrypt'][alphabet_lower[i]] = alphabet_lower[(i - s) % 26]

message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển (0–25): ")) % 26
mode = input("Chọn chế độ (encrypt/decrypt): ").strip().lower()

if mode not in ("encrypt", "decrypt"):
    print("Chế độ không hợp lệ Vui lòng nhập 'encrypt' hoặc 'decrypt'.")
else:
    result = ""
    for ch in message:
        if ch in shift_table[shift][mode]:
            result += shift_table[shift][mode][ch]
        else:
            result += ch
    print("Kết quả sau khi", "mã hóa:" if mode == "encrypt" else "giải mã:", result)
