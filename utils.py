import bcrypt

def hash_password(pw: str):
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password, salt)

    print(hashed)
    return hashed


