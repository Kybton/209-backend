from bcrypt import checkpw, gensalt, hashpw


class PasswordService():
    password: str     
    hashed_password: str

    def __init__(self, password="", hashed_password=""):
        self.password = password
        self.hashed_password = hashed_password
        self.salt = gensalt()

    def hash_it(self):
        self.hashed_password = hashpw(
            self.password.encode(), self.salt).decode()

    def check_password(self) -> bool:
        return checkpw(self.password.encode(), self.hashed_password.encode())