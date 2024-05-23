import random
def Check_Des_Valid_Input(inputBit, lenKey, lenBit):
    # if (len(inputBit) != lenBit):
    #         return False
    return True

def DesEncrypt(keys ,InputBit, NumberOfRound=16, lenKey = 64, lenBit = 64):
    if Check_Des_Valid_Input(InputBit, lenKey, lenBit) :
       mid = len(str(InputBit))//2
       L0 = InputBit[:mid]
       print("LO: ", L0)
       R0 = InputBit[mid:]
       print("R0: ",R0)
       Left_List = []
       Right_List = []
       Left_List.append(L0)
       Right_List.append(R0)
       for i in range (NumberOfRound):
           left = Right_List[i]
           right = (int(Left_List[i]))^Ffunction(Right_List[i],keys[i])
           Left_List.append(left)
           Right_List.append(right)

       return  str(Right_List[-1]) + str(Left_List[-1])
    else :
        raise ValueError("Invalid Input")

def DesDecrypt(keys ,InputBit, NumberOfRound=16, lenKey = 64, lenBit = 64):
    if Check_Des_Valid_Input(InputBit, lenKey, lenBit) :
       mid = len(InputBit)//2
       L0 = InputBit[:mid]
       R0 = InputBit[mid:]
       Left_List = []
       Right_List = []
       Left_List.append(L0)
       Right_List.append(R0)
       for i in range (NumberOfRound):
           left = Right_List[i]
           right = (int(Left_List[i]))^Ffunction(Right_List[i],keys[NumberOfRound-1-i])
           Left_List.append(left)
           Right_List.append(right)

       return  str(Right_List[-1]) + str(Left_List[-1])
    else :
        raise ValueError("Invalid Input")


def Ffunction(intput, key):
    output = (int(intput))^key
    return output
def genRandomKey(lenKey = 64):
    key = random.getrandbits(lenKey)
    return key

def generate_subkeys(key):
    """
    Generate 16 subkeys from the primary DES key using the key schedule process.
    """
    # Permuted Choice 1 (PC-1)
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    permuted_key = int(''.join(bin(key)[2:].zfill(64)[i - 1] for i in pc1), 2)

    # Split into Left and Right Halves
    c0 = permuted_key >> 28
    d0 = permuted_key & (2 ** 28 - 1)

    # Shift and Permute
    subkeys = []
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    for shift in shift_schedule:
        c0 = (c0 << shift) | (c0 >> (28 - shift))
        d0 = (d0 << shift) | (d0 >> (28 - shift))
        subkey = (c0 << 28) | d0
        subkey = int(''.join(bin(subkey)[2:].zfill(56)[i - 1] for i in pc2), 2)
        subkeys.append(subkey)

    return subkeys

# test
def testKey():
    PrimaryKey = genRandomKey()
    print("primaryKey:", PrimaryKey)
    subkeys = generate_subkeys(PrimaryKey)
    for key in subkeys :
        print("subkey: ", key)

def demo():
    PrimaryKey = genRandomKey()
    print("primaryKey:", PrimaryKey)
    subkeys = generate_subkeys(PrimaryKey)
    plaintext = random.getrandbits(64)
    print("plaintext: ", plaintext)
    cyphertext = str(DesEncrypt(subkeys,str(plaintext)))
    print("cypher text : ", cyphertext)
    print("decrypt text: ", DesDecrypt(subkeys,cyphertext))

# main function
if __name__ == "__main__":
    demo()