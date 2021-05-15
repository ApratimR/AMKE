import numpy as np
from FNNH import FNNH
import secrets

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


#NOTE : make another variable for private rounds and use that for processing
current_private_key = None        # =A     (Do not share)
current_private_key_rounds = None # =A1    (Do not share)
current_public_string = None      # =G     (sharable)
current_public_key = None         # =AxG   ()
current_shared_secret_key = None  # =AxGxB ()

temp = 0
# generates key for any use
def generate_key():
    randombit = secrets.token_urlsafe(48)
    return randombit

def generate_rounds():
    return secrets.randbelow(10)

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


def main_UI():
    global current_private_key,current_public_string,current_public_key,current_shared_secret_key
    print("""
    Select your operation:
    1.Generate yout own private key.
    2.Set a previously generated shared secret key
    3.create a public string and your public key with that public string for sending
    (in: ->out: public_string public_key)
    4.process the incoming public string and other users public key
    (in:public_string senders_public_key ->out:your_public_key AND set: shared_secretkey)""")

    option = int(input())

    if option==1:

        current_private_key = generate_key()


    elif option==2:
        current_shared_secret_key = str(input())
        if current_shared_secret_key !=64:
            current_shared_secret_key = None
            raise Exception("Invalid KEY")

    elif option==3:
        if current_public_string==None:
            current_public_string = generate_key()

        if current_private_key == None:
            current_private_key = generate_key()

        #mixkey(current_public_string,current_private_key)





if __name__ == "__main__":

    main_UI()