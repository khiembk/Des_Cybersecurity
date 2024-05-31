def Word2Int(Input):
    lenInput =len(Input)
    mul = 26**(lenInput-1)
    num = 0
    for i in range(lenInput):
        num += (ord(Input[i]) - ord('A')) * mul
        mul = mul/26
    num = int(num)
    return num
def Sen2Int(Input):
    split_lit = Input.split(" ")
    number_list = []
    for word in split_lit :
        if (word!=""):
           number_list.append(Word2Int(word))
    return number_list

def RSA_encrypt(Input, e, n):
    input_list = Sen2Int(Input)
    output_list = []
    for num in input_list :
        output_list.append(expo_algo(num,e,n))
    return output_list
def RSA_decrypt(Input ,d, n):
    output_list = []
    for num in Input :
        output_list.append(expo_algo(num,d,n))
    return output_list

def De2Bin(num):
    return [int(bit) for bit in bin(num)[2:]]
def expo_algo(intputNum ,e ,n):
    output = 1
    bin_e = De2Bin(e)
    len_e = len(bin_e)
    for i in range(len_e):
        output = (output**2)%n
        if (bin_e[i]!= 0):
          output = (output*intputNum)%n
    return output

def test():
    intput = "DOG AND CAT"
    print("output: ",Sen2Int(intput))
    encrypt =RSA_encrypt(intput,17,253)
    print("encrypt: ",encrypt)
    decrypt = RSA_decrypt(encrypt,13,253)
    print("decrypt: ", decrypt)

if __name__ == "__main__":
    test()