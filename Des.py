
def Check_Des_Valid_Input(PrimaryKey, inputBit, lenKey, lenBit):
    if ( len(PrimaryKey) != lenKey ):
         return False
    else:
        if (len(inputBit) != lenBit):
            return False
    return True

def DesEncrypt(PrimaryKey ,InputBit, NumberOfRound=16, lenKey = 56, lenBit = 64):
    if Check_Des_Valid_Input(PrimaryKey,InputBit, lenKey, lenBit) :
       keys = gentKey(PrimaryKey, NumberOfRound)
       mid = len(InputBit)//2
       L0 = InputBit[:mid]
       R0 = InputBit[mid:]
       Left_List = []
       Right_List = []
       Left_List.append(L0)
       Right_List.append(R0)
       for i in range (NumberOfRound):
           left = Right_List[i]
           right = Left_List[i]^Ffunction(Right_List[i],keys[i])
           Left_List.append(left)
           Right_List.append(right)

       return  Right_List[-1] + Left_List[-1]
    else :
        raise ValueError("Invalid Input")


def Ffunction(intput , key):
    output = ""
    return output

def gentKey(InputKey, NumberofKey =10):
    keys = []
    return keys

