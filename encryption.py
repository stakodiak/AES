#!/usr/bin/python2.7
# coding=utf-8
import getpass
from Crypto.Cipher import AES

    
def pad_string(text, block_size=32, padding=' '):
    """Pads `text` to be `block_size` chars long."""
    padded = text.ljust(block_size, padding)
    pruned = padded[:block_size]
    return padded

def main():
    # Create cipher from padded password.
    pwd = getpass.getpass()
    key = pad_string(pwd)
    cipher = AES.new(key)

    print "'{}'".format(key), len(key)

if __name__ == '__main__':
    main()
