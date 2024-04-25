from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#simple_key = get_random_bytes(32)
#print(simple_key)
def encrypt():
    salt = b'\xc82\xdf\xcf/\xa2:\xde\xca|\xa7\x0f\xf9#\x0fgqZ\x88\xdc\x1c\xddy\xdb@\n\x1f\xba\x8d\xdc}\x06'

    code = "skm#RWSF$TE%$DTGs3efg89s"

    key = PBKDF2(code, salt, dkLen=32)

    with open('unsecured_data.txt', 'r') as f:
        message = f.read()

    message_bytes = bytes(message, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message_bytes, AES.block_size))

    with open('secured_data.bin', 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphered_data)

    return(key)

def decrypt(key):
    with open('secured_data.bin', 'rb') as f:
        iv = f.read(16)
        decrypt_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

    print(original)

def main():
    key = encrypt()
    decrypt(key)

if __name__ == '__main__':
    main()