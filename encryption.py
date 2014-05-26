#!/usr/bin/python2.7
# coding=utf-8
import getpass
import sys
from Crypto.Cipher import AES

    
def pad_string(text, block_size=32, padding=' '):
    """Pads `text` so length is a multiple of `block_size`."""
    padded = text + (block_size - len(text) % block_size) * padding
    return padded

def encrypt(cipher, data):
    """Encrypts `data` with `cipher`."""
    padded = pad_string(data)
    encrypted = cipher.encrypted(padded)
    return encrypted

def decrypt(cipher, encrypted_data):
    """Decrypt AES-encrypted data with `cipher`."""
    decrypted = cipher.decrypt(encrypted_data)
    return decrypted

def main():
    # Create cipher from padded password.
    pwd = getpass.getpass()
    key = pad_string(pwd)
    cipher = AES.new(key)

    # Encrypt given text.
    data = sys.stdin.read()
    padded_data = pad_string(data)
    encrypted = cipher.encrypt(padded_data)

    print encrypted

    decrypted = decrypt(cipher, encrypted)
    print decrypted
    print "'{}'".format(key), len(key)

if __name__ == '__main__':
    main()
