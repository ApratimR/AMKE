import numpy as np
import FNNH as fn
import secrets


charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

#XORarray = np.array()
#THE XOR Field
xorarray = np.zeros((64,64),dtype=np.uint8)
temp = np.arange(0,64,1,dtype=np.uint8)
for temp1 in range(64):
    xorarray[temp1] = temp
    temp=np.roll(temp,1)


# generates key for any use
def generate_privatekey():
    randombit = secrets.token_urlsafe(192)
    return randombit


# takes in array of 16*16 and return a string of lenght 16*16
def arrayToString(theArray=None,size=16):
    emptyString=""
    for temp1 in range(size):
        for temp2 in range(size):
            emptyString+=charset[theArray[temp1][temp2]]
    return emptyString


# takes in string of 16*16 and return a array of int with size 16*16
def stringToArray(theString=None,size=16):
    emptyArray = np.zeros((size,size),dtype=np.uint8)
    stringcounter = 0
    for temp1 in range(size):
        for temp2 in range(size):
            emptyArray[temp1][temp2]=charset.index(theString[stringcounter])
            stringcounter+=1
    return emptyArray


# string to 1D list[int]
def string_to_int(inp):
    inp = list(str(inp))
    inp = [charset.index(x) for x in inp]
    return inp


# 1D list[int] to string
def int_to_string(inp):
    emptyString=""
    for temp in range(256):
        emptyString+=charset[inp[temp]]
    return emptyString


#makes multiple keys related to the mainn key
def instruction_expansion(publicpart,privatepart):
    #need to work on counter OVERFLOW NOTE
    counter = 0
    for _ in range(4):
        for temp1 in range(16):
            for temp2 in range(16):
                publicpart[temp1][temp2]+= publicpart[(temp1+1)%16][temp2]
                publicpart[temp1][temp2]=(publicpart[temp1][temp2]+privatepart[counter])%64
                counter+=1
                counter = counter%256

                publicpart[temp1][temp2]+= publicpart[temp1][(temp2+1)%16]
                publicpart[temp1][temp2]=(publicpart[temp1][temp2]+privatepart[counter])%64
                counter+=1
                counter = counter%256

                publicpart[temp1][temp2]+= publicpart[(temp1+17)%16][temp2]
                publicpart[temp1][temp2]=(publicpart[temp1][temp2]+privatepart[counter])%64
                counter+=1
                counter = counter%256

                publicpart[temp1][temp2]+= publicpart[temp1][(temp2+17)%16]
                publicpart[temp1][temp2]=(publicpart[temp1][temp2]+privatepart[counter])%64
                counter+=1
                counter = counter%256

                shadow = privatepart[(publicpart[temp1][temp2]*publicpart[7][8])%256]
                publicpart[temp1][temp2]=(publicpart[temp1][temp2]+shadow)%64
    publicpart = np.reshape(publicpart,256)
    return publicpart



def theOneWayFunction(theArray,instructions):
    array_length = len(theArray)
    if array_length**2 != len(instructions):
        raise Exception("instruction lenght invalid")

    for temp1 in range(array_length):
        for temp2 in range(array_length):
            temp1 = temp2
            temp2 = temp1
            pass

    #pre-preocess the arrat and instruction
    #instructions = instruction_seperator(instructions)




    return theArray


def printf(inp):
    print(f"""
\u001b[31m\u001b[1m========PUBLIC/PRIVATE VARIABLE START HERE========\u001b[0m
\u001b[7m{inp}\u001b[0m
\u001b[31m\u001b[1m========PUBLIC/PRIVATE VARIABLE ENDS HERE========\u001b[0m
""")


def main():
    print("""
      enter :
        1. for generating public key (this will be shared)
        2. for generating your own private key(DO NOT SHARE IT WITH ANYONE)
        3. for processing the the public key with your own key(this will be shared)
        4. for processing the the shared key recived form other with your own key(DO NOT SHARE THIS)
      """)
    option = int(input())

    if option not in (1,2,3,4):
        raise Exception("ENTER A VALID OPTION")



def AMKE_generatekey():

    temp=generate_privatekey()
    return(temp)
    #os.system(f"echo {temp}|clip")


def AMKE_processkey(publicstring,privatestring):

    if len(publicstring)!=256:
        raise Exception("INVALID PUBLIC KEY")

    if len(privatestring)!=256:
        raise Exception("INVALID PUBLIC KEY")

    if publicstring==privatestring:
        raise Exception("PUBLIC and PRIVATE KEY BOTH ARE SAME")

    publicstring = stringToArray(publicstring)  #this is 2D
    privatestring = string_to_int(privatestring)  #this is 1D
    temp = instruction_expansion(publicstring,privatestring)
    temp = int_to_string(temp)
    return(temp)


    # print(publicstring)
    # print(privatestring)

if __name__ == "__main__":
    main()
