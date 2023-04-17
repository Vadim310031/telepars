import hashlib

from salt import salt 

def pasword(password):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

if pasword("овшуоа") == pasword("овшуоа"):
    print("да")