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
    encrypt = ""
    while (len(InputString) % chainSize != 0):
        InputString = InputString + " "
    lenInput = len(InputString)
    inputbit0 = Xor2bin(initValue,char2bit(InputString[:chainSize]))
    precipher = SPN_encrypt.SPN_block(key,inputbit0)
    encrypt = encrypt + precipher
    for i in range(chainSize,lenInput-chainSize,chainSize):
        cur_inputbit = Xor2bin(precipher,char2bit(InputString[i:i+chainSize]))
        precipher = SPN_encrypt.SPN_block(key,cur_inputbit)
        encrypt = encrypt + precipher

    return encrypt
def CFB(initValue, key, InputString, chainSize = 2):
    while(len(InputString)% chainSize!=0):
        InputString = InputString + " "
    lenInput = len(InputString)
    precipher = Xor2bin(char2bit(InputString[:chainSize]),SPN_encrypt.SPN_block(key,initValue))
    cipher = ""
    cipher = cipher + precipher
    for i in range(chainSize,lenInput-chainSize,chainSize):
        precipher = Xor2bin(char2bit(InputString[i:i+chainSize]),SPN_encrypt.SPN_block(key,precipher))
        cipher = cipher + precipher

    return cipher

def OFB(initValue, key, InputString, chainSize =2 ):
    while (len(InputString)%chainSize!=0):
        InputString = InputString + " "

    lenInput = len(InputString)
    cipher = ""
    preElement = SPN_encrypt.SPN_block(key,initValue)
    for i in range(0,lenInput-chainSize,chainSize):
        precipher = Xor2bin(preElement,char2bit(InputString[i:i+chainSize]))
        cipher = cipher + precipher
        preElement = SPN_encrypt.SPN_block(key,preElement)

    return cipher
def test():
    initValue = getInitRandom()
    print("getRandom: ", initValue)
    intputString = "hello"
    key = "00111010100101001101011000111111"
    cipher = CBC(initValue,key,intputString)
    cipher1 = CFB(initValue,key,intputString)
    cipher2 = OFB(initValue,key,intputString)
    print("cipher CBC: ",cipher)
    print("cipher CFB: ",cipher1)
    print("cipher OFB: ",cipher2)




if __name__ == "__main__":
    test()