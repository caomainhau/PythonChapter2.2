import random
def random_password():
    length = random.randint(7, 10)
    pwd = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return pwd
print("Mật khẩu ngẫu nhiên:", random_password())
