import random

import SPN_encrypt


def char2bit(c):
    bit = ''.join(format(ord(i), '08b') for i in c)
    return bit
def Xor2bin(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        if (bin1[i]==bin2[i]):
            result= result + '0'
        else :
            result = result + '1'

    return result
def getInitRandom(sizeOfBit=16):
    init = ""
    for i in range(sizeOfBit):
        r= random.randint(0,2)
        if (r>=1):
            init = init + "1"
        else :
            init = init + "0"
    return  init

def CBC(initValue, key,InputString, chainSize = 2):
    lenInput = len(InputString)
    encrypt = ""
    while (len(InputString) % chainSize != 0):
        InputString = InputString + " "
    inputbit0 = Xor2bin(initValue,char2bit(InputString[:chainSize]))
    precipher = SPN_encrypt.SPN_block(key,inputbit0)
    encrypt = encrypt + precipher
    for i in range(chainSize,lenInput-chainSize,chainSize):
        cur_inputbit = Xor2bin(precipher,char2bit(InputString[i:i+chainSize]))
        precipher = SPN_encrypt.SPN_block(key,cur_inputbit)
        encrypt = encrypt + precipher

    return encrypt
def test():
    initValue = getInitRandom()
    print("getRandom: ", initValue)
    intputString = "hello"
    key = "00111010100101001101011000111111"
    cipher = CBC(initValue,key,intputString)
    print("cipher: ",cipher)


if __name__ == "__main__":
    test()