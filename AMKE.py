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
    return secrets.randbelow(2048) #chage this to some other amount

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


def mixkey_phase1(public_key,private_key,private_rounds):
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
    
    return_key = (public_key*private_key)%64
    return_key = (return_key*derived_key)%64
    
    return_key = np.reshape(return_key,64)
    return_key = int_to_string(return_key)
    return return_key



def mixkey_phase2(processed_public_key,public_key,private_key,private_rounds):
    if processed_public_key == None and private_key == None:
        raise Exception("parameter entered empty")

    if len(processed_public_key) != 64 and len(private_key) != 64:
        raise Exception("parameter entered invalid")
    last_addkey = FNNH(data=public_key,hash_size=64,rounds=16,returnmode="string",maxreturnval=64)
    derived_key = FNNH(data=private_key,hash_size=64,rounds=private_rounds,returnmode="string",maxreturnval=64)

    processed_public_key = string_to_int(processed_public_key)
    private_key = string_to_int(private_key)
    derived_key = string_to_int(derived_key)
    last_addkey = string_to_int(last_addkey)

    processed_public_key = np.reshape(processed_public_key,(8,8))
    private_key = np.reshape(private_key,(8,8))
    derived_key = np.reshape(derived_key,(8,8))
    last_addkey = np.reshape(last_addkey,(8,8))
    
    return_key = (processed_public_key*private_key)%64
    return_key = (return_key*derived_key)%64
    return_key = (return_key+last_addkey)%64
    
    return_key = np.reshape(return_key,64)
    return_key = int_to_string(return_key)
    return return_key