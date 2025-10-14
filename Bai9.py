my_str = "Hello this Is an Example With cased letters"
ds_tu = my_str.split()
ds_tu.sort(key=str.lower)
print("Các từ đã được tách và sắp xếp theo Alphabet:")
for tu in ds_tu:
    print(tu)
