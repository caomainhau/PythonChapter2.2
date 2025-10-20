nums = []
while True:
    line = input("Nhập số nguyên: ")
    if line == "":
        break
    nums.append(int(line))

neg = [x for x in nums if x < 0]
zero = [x for x in nums if x == 0]
pos = [x for x in nums if x > 0]

result = neg + zero + pos
print("Kết quả:", result)
