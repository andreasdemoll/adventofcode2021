# day 3 part 1 ---------------------------------------------------------------
import numpy as np
file = 'data/day3Diagnostics.txt'
numCols = 12

def fileToMatrix(file):
    diag = np.zeros((numCols,0),dtype=np.uint8)
    with open(file, 'rt') as f:
        for line in f:
            temp = np.array([int(x) for x in list(line.split('\n')[0])],
                            dtype=np.uint16)
            diag = np.c_[diag,temp]
    return diag.T

def mostCommonNumber(diag):
    return ((sum(diag) >= diag.shape[0]/2) * 1).tolist()

def bitListToNum(bitlist):
        out = 0
        for bit in bitlist:
            out = (out << 1) | bit
        return out

def calcGammaEpsilon(file):
    diag = fileToMatrix(file)
    bitlist = mostCommonNumber(diag)
    gamma = bitListToNum(bitlist)
    epsilon = bitListToNum([(not i) * 1 for i in bitlist])
    return gamma*epsilon

print(f'Power consumption: {calcGammaEpsilon(file)}')

# day 3 part 2 ---------------------------------------------------------------
def calcLifeSupport(file):
    diag = fileToMatrix(file)
    test = diag.copy()
    
    def iterate(test, mode='mc'):
        colIdx=0
        while colIdx<numCols:
            mc =  mostCommonNumber(test)
            if(mode=='lc'):
                mc = [(not i) * 1 for i in mc]
            col = test[:,colIdx:colIdx+1]
            test = test[(col==mc[colIdx]).ravel()]
            #print(f'remaining rows of test: {test.shape[0]}')
            if test.shape[0] == 1:
                break
            colIdx+=1
        return bitListToNum(test.ravel().tolist())
    return iterate(test, 'mc') * iterate(test, 'lc')

print(f'life support rate {calcLifeSupport(file)}')