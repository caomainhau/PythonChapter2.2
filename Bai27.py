canh = input(str("Nhap co canh cua hinh: "))
danhsach = {"3": "Tam giac", "4": "Tu giac", "5": "Ngu giac", "6": "Luc giac", "7": "That giac", "8": "Bat giac", "9": "Cuu giac","10": "Thap giac"}
if canh in danhsach:
    print(danhsach[canh])
else:
    print("Loi!!!")