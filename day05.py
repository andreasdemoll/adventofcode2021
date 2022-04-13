import numpy as np

# day 5 part 1 and 2 ---------------------------------------------------------
def getHydroLines(file='data/day5HydrothermalVenture.txt'):
    array = np.zeros((500,4),dtype=int)
    with open(file, 'rt') as f:
        for idx,line in enumerate(f):
            lines = [x.split(',') for x in line.split()[0:3:2]]
            array[idx] = [item for subl in lines for item in subl]
    return array

def getDangerousLines():
    li = getHydroLines()
    
    #calculate the sheet size
    xmin, xmax = int(li[:,[0,2]].min()), int(li[:,[0,2]].max())
    ymin, ymax = int(li[:,[1,3]].min()), int(li[:,[1,3]].max())
    sheet = np.zeros((xmax-xmin+2,ymax-ymin+2)) # something wrong with max...
    
    for idx in range(li.shape[0]): #iterate over all lines
        #normalize the row to fit the sheet
        rowNorm = li[idx] - [xmin, ymin, xmin, ymin]
        
        #separate between vertical, horizontal and diagonal lines.
        if rowNorm[0]==rowNorm[2]: #vertical line
            mini = min(rowNorm[1], rowNorm[3])
            maxi = max(rowNorm[1], rowNorm[3])+1
            #print(f'vertical: col {rowNorm[1]}, row {mini}:{maxi}')
            sheet[mini:maxi,rowNorm[0]] += 1
        elif rowNorm[1]==rowNorm[3]: #horizontal line
            mini = min(rowNorm[0], rowNorm[2])
            maxi = max(rowNorm[0], rowNorm[2])+1
            #print(f'horizontal: row {rowNorm[1]}, col {mini}:{maxi}')
            sheet[rowNorm[1],mini:maxi] += 1
        else: #diagonal, part 2 ----------------------------------------------
            #print(f'{rowNorm} is diagonal with length {abs(rowNorm[0]-rowNorm[2])}')
            
            if rowNorm[0]-rowNorm[2] == rowNorm[1]-rowNorm[3]:
                #print('falling')
                if rowNorm[0]<rowNorm[2]: #increasing
                    #print('increasing')
                    sheet[range(rowNorm[1],rowNorm[3]+1),
                          range(rowNorm[0],rowNorm[2]+1)]+=1
                else:
                    #print('decreasing')
                    sheet[range(rowNorm[3],rowNorm[1]+1),
                          range(rowNorm[2],rowNorm[0]+1)]+=1
            else:
                #print('rising')
                if rowNorm[0]<rowNorm[2]: #increasing
                    #print('increasing')
                    sheet[range(rowNorm[1],rowNorm[3]-1,-1),
                          range(rowNorm[0],rowNorm[2]+1)]+=1
                else:
                    #print('decreasing')
                    sheet[range(rowNorm[3],rowNorm[1]-1,-1),
                          range(rowNorm[2],rowNorm[0]+1)]+=1
    return sum(sum(sheet>1)), sheet

points,sheet = getDangerousLines()
print(f'There are {points} dangerous points!')