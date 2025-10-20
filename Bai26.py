chucai = input("Nhập chữ cái: ").lower()

chu_cai_nguyen_am = ["a", "e", "i", "o", "u"]
chu_cai_co_the_la_nguyen_am_hoa_phu_am = ["y"]

if chucai in chu_cai_nguyen_am:
    print("Đây là nguyên âm.")
elif chucai in chu_cai_co_the_la_nguyen_am_hoa_phu_am:
    print("Chữ 'y' có thể là nguyên âm hoặc phụ âm.")
else:
    print("Đây là phụ âm.")
