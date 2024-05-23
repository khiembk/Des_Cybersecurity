# length of bit  m = 4
def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]

    return hex

def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

def hex2hexSubtitution(s):
    mp = {
        '0': 'E',
        '1': '4',
        '2': 'D',
        '3': '1',
        '4': '2',
        '5': 'F',
        '6': 'B',
        '7': '8',
        '8': '3',
        '9': 'A',
        'A': '6',
        'B': 'C',
        'C': '5',
        'D': '9',
        'E': '0',
        'F': '7'
    }
    hex=""
    for i in range(len(s)):
        hex = hex + mp[s[i]]

    return hex
def bin2binPermutation(s):
    mp = {
        '1':'1',
        '2':'5',
        '3':'9',
        '4':'13',
        '5':'2',
        '6':'6',
        '7':'10',
        '8':'14',
        '9':'3',
        '10':'7',
        '11':'11',
        '12':'15',
        '13':'4',
        '14':'8',
        '15':'12',
        '16':'16'
    }
    bin = ""
    for i in range(16):
        bin = bin + s[int(mp[str(i+1)])-1]

    return  bin
def Xor2bin(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        if (bin1[i]==bin2[i]):
            result= result + '0'
        else :
            result = result + '1'

    return result


def SPN(inputbit, keys, Nr = 4):
    w=[]
    u=[]
    v=[]
    u.append(inputbit)
    w.append(inputbit)
    v.append(inputbit)
    for i in range(1,Nr):
        cur_u = Xor2bin(w[i-1],keys[i-1])
        u.append(cur_u)
        cur_v = hex2bin(hex2hexSubtitution(bin2hex(cur_u)))
        v.append(cur_v)
        cur_w = bin2binPermutation(cur_v)
        w.append(cur_w)

    cur_u = Xor2bin(w[Nr-1],keys[Nr-1])
    cur_v = hex2bin(hex2hexSubtitution(bin2hex(cur_u)))
    return Xor2bin(cur_v,keys[Nr])


def key_schedule(key, subkeySize = 16, strike = 4):
    keys = []
    numkey = (len(key) - subkeySize)//strike + 1
    for i in range(numkey):
        cur_key = key[i*strike:i*strike + subkeySize]
        keys.append(cur_key)
    return keys

def SPN_block(key, inputbit):
    keys = key_schedule(key)
    Nr = len(keys)-1
    return SPN(inputbit,keys,Nr)
def demo():
    key = "00111010100101001101011000111111"
    plaintext = '0010011010110111' #16 bit
    ciphertext = SPN_block(key, plaintext)
    print("ciphertext:", ciphertext)
def testKey():
    key = "00111010100101001101011000111111"
    keys = key_schedule(key)
    for cur_key in keys :
        print("key :", cur_key)
if __name__ == "__main__":
    demo()