# day8 part 1 ----------------------------------------------------------------
import numpy as np
test = np.zeros((10,4),dtype=str)

pick = (2,3,4,7)
out_1478 = 0
with open("data/day8DigitCodes.txt","rt") as f:
    for line in f:
        d = line.split(" | ")[1].split()
        l = [len(x) for x in d]
        out_1478 += sum([ele in pick for ele in l])
print(f'There are {out_1478} numbers with digits 1,4,7 or 9.')

# day8 part 2 ----------------------------------------------------------------
#  aa
# b  c
# b  c
#  dd
# e  f
# e  f
#  gg
#
# [0gfedcba] --> code

code = [119,36,93,109,46,107,123,37,127,111] #segments encoded for each digit

def lettersToByte(s):
    # convert the unsorted segments to a byte
    by=0
    s = list(s)    
    for c in s:
        by |= 1 << ord(c)-97
    return by

def sumOfBits(val):
    return sum([int(x) for x in list(bin(val).replace("0b", ""))])

size2num = {2:1,3:7,4:4,7:8}

sumOutput = 0
with open("data/day8DigitCodes.txt","rt") as f:
    for line in f:
        d0 = line.split(" | ")[0].split()
        d1 = line.split(" | ")[1].split()
        
        #find the decoding unsing d0
        decode = {} # this will be number:bytes pairs for each line.
        for n in d0:               # for (n umber) in (d igits)
            b = lettersToByte(n)   # number as (b ytes) to be sort-independent
            s = len(n)             # number of segments (s ize)
            if s in pick:          # direct decoding possible.
                decode[size2num[s]]=b
                
        #iterate again as all direct encoded numbers must be already present!
        for n in d0:
            b = lettersToByte(n)   # number as (b ytes) to be sort-independent
            s = len(n)             # number of segments (s ize)
            if s==5: #2,3 or 5
                if sumOfBits(b & decode[4]) == 2:
                    decode[2]=b
                elif sumOfBits(b & decode[1]) == 2:
                    decode[3]=b
                else:
                    decode[5]=b
            elif s==6:
                if sumOfBits(b & decode[1]) != 2:
                    decode[6]=b
                elif sumOfBits(b & decode[4]) == 4:
                    decode[9]=b
                elif sumOfBits(b & decode[8]) == 6:
                    decode[0]=b
                 
        #decode d1 unsing "decode" dict
        key_list = list(decode.keys())
        val_list = list(decode.values())
        
        sumOutput += \
        key_list[val_list.index(lettersToByte(d1[0]))] * 1000 + \
        key_list[val_list.index(lettersToByte(d1[1]))] * 100 + \
        key_list[val_list.index(lettersToByte(d1[2]))] * 10 + \
        key_list[val_list.index(lettersToByte(d1[3]))] * 1
    print(sumOutput)