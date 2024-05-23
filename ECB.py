import SPN_encrypt

def char2bit(c):
    bit = ''.join(format(ord(i), '08b') for i in c)
    return bit
def ECB(key, InputString, chainSize = 2):
    lenInput = len(InputString)
    encrypt = ""
    while(len(InputString)%chainSize!=0):
        InputString = InputString + " "

    for i in range(0,lenInput,chainSize):
        inputbit = char2bit(InputString[i:i+chainSize])
        encrypt = encrypt + SPN_encrypt.SPN_block(key,inputbit)
    return  encrypt

def test():
    intputString = "hello"
    key = "00111010100101001101011000111111"
    encrypt = ECB(key, intputString)
    print("encrypt: ",encrypt)


if __name__ == "__main__":
    test()
