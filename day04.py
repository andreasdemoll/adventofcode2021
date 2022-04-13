import numpy as np

# day 4 part 1 ---------------------------------------------------------------
drawn = [26,55,7,40,56,34,58,90,60,83,37,36,9,27,42,19,46,18,49,52,75,17,70,
         41,12,78,15,64,50,54,2,77,76,10,43,79,22,32,47,0,72,30,21,82,6,95,
         13,59,16,89,1,85,57,62,81,38,29,80,8,67,20,53,69,25,23,61,86,71,68,
         98,35,31,4,33,91,74,14,28,65,24,97,88,3,39,11,93,66,44,45,96,92,51,
         63,84,73,99,94,87,5,48];

#drawn = [7,4,9,5,11,17,23,2,0,14,21,24,10,
#         16,13,6,15,25,12,22,18,20,8,19,3,26,1];

def getBingoArrays(file='data/day4BingoArrays.txt'):
    arrays=[]
    array=np.zeros((5,5))
    rowIdx=0
    with open(file, 'rt') as f:
        for line in f:
            if rowIdx<5:
                array[rowIdx,:] = line.split()
                rowIdx+=1
            else:
                arrays.append(array.copy())
                rowIdx=0
    return arrays

def drawAndCheck():
    arr = getBingoArrays()
    for n in drawn:
        for idx, a in enumerate(arr):
            a[a==n]=0
            if any(sum(a)==0) or any(sum(a.T)==0):
                return int(sum(sum(a)) * n)

print(f'The final score is {drawAndCheck()}')

# day 4 part 2 ---------------------------------------------------------------
def drawAndCheckToLoose():
    arr = getBingoArrays()
    winners = []
    drawns = []
    for n in drawn:
        for idx, a in enumerate(arr):
            if idx not in winners:
                a[a==n]=0
                if any(sum(a)==0) or any(sum(a.T)==0):
                    winners.append(idx)
                    drawns.append(n)
    return int(sum(sum(arr[winners[-1]])) * drawns[-1])

print(f'The final loosing score is {drawAndCheckToLoose()}')