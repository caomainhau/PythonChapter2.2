thang = input("Nhập tên tháng: ").strip().lower()
thang_31 = ["january", "march", "may", "july", "august", "october", "december"]
thang_30 = ["april", "june", "september", "november"]
thang_28_29 = ["february"]

if thang in thang_31:
    print("Tháng này có 31 ngày.")
elif thang in thang_30:
    print("Tháng này có 30 ngày.")
elif thang in thang_28_29:
    print("Tháng này có 28 hoặc 29 ngày.")
else:
    print(" Tên tháng không hợp lệ.")
