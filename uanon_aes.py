#!/usr/bin/python3

import base64
import sys
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = self._pad_key(key.encode())

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b16encode(iv + cipher.encrypt(raw.encode())).lower()

    def decrypt(self, enc):
        enc = base64.b16decode(enc.upper())
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        dec_padded = cipher.decrypt(enc[AES.block_size:])
        dec = self._unpad(dec_padded)
        return dec.decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _pad_key(self, key):
        return key + (self.bs - len(key) % self.bs) * b"\0"
    
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


def main(): 
    try:
        key = sys.argv[1]
        payload = sys.argv[2]
        print(f'Key: {key}\nPayload: {payload}')
        aes = AESCipher(key)
        dec = aes.decrypt(payload)
        print(dec)
    except:
        print('Decrypt failed')


if __name__ == "__main__":
    main()