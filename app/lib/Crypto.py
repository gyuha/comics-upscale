import cryptocode

CRYPT_KEY = '5c289a75-7fc7-4814-b817-a0dbe2c773c2'
class Crypto: 
    @staticmethod
    def encrypt(text: str) -> str:
        return cryptocode.encrypt(text, CRYPT_KEY)
    
    @staticmethod
    def decrypt(text: str) -> str:
        return cryptocode.decrypt(text, CRYPT_KEY)
