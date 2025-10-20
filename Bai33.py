text = input("Nhập chuỗi cần kiểm tra: ")
clean_text = text.replace(" ", "").lower()

is_palindrome = True
for i in range(len(clean_text) // 2):
    if clean_text[i] != clean_text[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"'{text}' là một Palindrome.")
else:
    print(f"'{text}' không phải là một Palindrome.")
