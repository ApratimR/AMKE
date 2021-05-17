import numpy as np
from FNNH import FNNH
import secrets

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


temp = 0
# generates key for any use
def generate_key():
    randombit = secrets.token_urlsafe(48)
    return randombit

def generate_rounds():
    return secrets.randbelow(10) #chage this to some other amount

# string to 1D list[int]
def string_to_int(inp):
    #print("this is inp:",inp)
    inp = list(str(inp))
    inp = [charset.index(x) for x in inp]
    return inp


# 1D list[int] to string
def int_to_string(inp):
    emptyString=""
    for temp in range(len(inp)):
        emptyString+=charset[inp[temp]]
    return emptyString


def mixkey(public_key,private_key,private_rounds):
    if public_key == None and private_key == None:
        raise Exception("parameter entered empty")

    if len(public_key) != 64 and len(private_key) != 64:
        raise Exception("parameter entered invalid")

    derived_key = FNNH(data=private_key,hash_size=64,rounds=private_rounds,returnmode="string",maxreturnval=64)

    public_key = string_to_int(public_key)
    private_key = string_to_int(private_key)
    derived_key = string_to_int(derived_key)

    public_key = np.reshape(public_key,(8,8))
    private_key = np.reshape(private_key,(8,8))
    derived_key = np.reshape(derived_key,(8,8))
    
    return_key = (public_key+private_key)%64
    return_key = (return_key+derived_key)%64
    
    return_key = np.reshape(return_key,64)
    return_key = int_to_string(return_key)
    return return_key
