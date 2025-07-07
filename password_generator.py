import random
import string

def generator(size: int = 4):
    word = string.ascii_letters + string.digits
    password = ''.join(random.choice(word) for i in range(size))
    if "O" and "0" in password:
        word = string.hexdigits
        password = ''.join(random.choice(word) for i in range(size))
    return password
otp = generator()
print("Your OTP is:",otp)