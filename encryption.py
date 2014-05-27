#!/usr/bin/python2.7
# coding=utf-8
"""
 Example:
   cat file | ./encryption.py --encrypt > encrypted.dat
   cat encrypted.dat | ./encryption.py --decrypt > decrypted.txt
"""
import base64
import getpass
import sys
from Crypto.Cipher import AES

PADDING = ' '
BLOCK_SIZE = 32

def main():
    """Handles program flow."""
    args = parse_args()
    if args.file:
        with open(args.file) as inf:
            data = inf.read()
    else:
        data = sys.stdin.read()
    # Create cipher from padded password.
    pwd = getpass.getpass()
    key = pad_string(pwd)
    cipher = AES.new(key)
    if args.encrypt:
        # Encrypt given text.
        encrypted = encrypt(cipher, data)
        print encrypted
    elif args.decrypt:
        decrypted = decrypt(cipher, data)
        print decrypted

def pad_string(text):
    """Pads `text` so length is a multiple of `block_size`."""
    padded = text + (BLOCK_SIZE - len(text) % BLOCK_SIZE) * PADDING
    return padded

def encrypt(cipher, data):
    """Encrypts `data` with `cipher` with base-64 encoding."""
    padded = pad_string(data)
    encrypted = cipher.encrypt(padded)
    encoded = base64.b64encode(encrypted)
    return encoded

def decrypt(cipher, encrypted_data):
    """Decrypt AES-encrypted data with `cipher`."""
    decoded = base64.b64decode(encrypted_data)
    decrypted = cipher.decrypt(decoded).strip(PADDING)
    return decrypted

def parse_args():
    """Pull relevant command-line arguments.

    Args:
        -e: encrypt file
        -f: file to encrypt
        -d: decrypt file
        -p: password for decrypting

    Returns -
       An object with `encrypt`, `file`, etc. as attributes.
    """
    import argparse
    import textwrap
    parser = argparse.ArgumentParser(
        prog="encryption.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
        Example:
          cat file | ./encryption.py --encrypt > encrypted.dat
          cat encrypted.dat | ./encryption.py --decrypt > decrypted.txt
        """))
    parser.add_argument(
        '-e', '--encrypt', action='store_true',
        help="encrypt given file")
    parser.add_argument(
        '-d', '--decrypt', action='store_true',
        help="decrypt given file")
    parser.add_argument(
        '-f', '--file', required=False,
        help="encrypted file or text to encrypt")
    parser.add_argument(
        '-p', '--password', required=False,
        help="password for decrypting file")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
