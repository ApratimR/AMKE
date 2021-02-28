import numpy as np
import secrets

#
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

#XORarray = np.array()

#IMP
#generate Common array
def generateArray():
    numpy_array = np.zeros((16,16),dtype=np.uint8)
    for temp1 in range(16):
        for temp2 in range(16):
            numpy_array[temp1][temp2]=secrets.randbelow(64)
    return numpy_array


def arrayToString(theArray=None):
    emptyString=""
    for temp1 in range(16):
        for temp2 in range(16):
            emptyString+=charset[theArray[temp1][temp2]]
    return emptyString


def stringToArray(theString=None):
    emptyArray = np.zeros((16,16),dtype=np.uint8)
    stringcounter = 0
    for temp1 in range(16):
        for temp2 in range(16):
            emptyArray[temp1][temp2]=charset.index(theString[stringcounter])
            stringcounter+=1
    return emptyArray


def splitArrayTo4SubArrays(theArray):
    array1 = np.array((theArray[0: 8,0: 8]),dtype=np.uint8)
    array2 = np.array((theArray[0: 8,8:16]),dtype=np.uint8)
    array3 = np.array((theArray[8:16,0: 8]),dtype=np.uint8)
    array4 = np.array((theArray[8:16,8:16]),dtype=np.uint8)
    return array1,array2,array3,array4


def instructionseperator (inp):
    inp = list(str(inp))
    
    #FIXME - need attention on referenceing the character from inp
    inp = list(map((charset.index()),inp))
    return inp


def theOneWayFunction(theArray,instructions):
    
    #pre-preocess the arrat and instruction
    instructions = instructionseperator(instructions)
    array1,array2,array3,array4 = splitArrayTo4SubArrays(theArray)
    
    #TODO apply ARX operation based on the instructions
    
    
    return theArray


temparray = generateArray()


randombit = secrets.token_urlsafe(256)
randombit = instructionseperator(randombit)
print(randombit)


#print(splitArrayTo4SubArrays(temparray))
