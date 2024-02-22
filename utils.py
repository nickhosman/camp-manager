import bcrypt

from random import randint

def hash_password(pw: str):
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password, salt)

    print(hashed)
    return hashed

def random_num(a, b):
    print(randint(a, b))
    return randint(a, b)


random_num(1, 10)
