num = int(input("Enter a number: "))
level = int(input("Bậc: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** level
   temp //= 10
if num == sum:
   print(num, "is Amstrong, level : ", str(level))
else:
   print(num, "is not Amstrong")
