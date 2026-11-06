from pwdlib import PasswordHash


class PasswordHandler:
    password_hash = PasswordHash.recommended()

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.password_hash.hash(password)

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.password_hash.verify(plain_password, hashed_password)
