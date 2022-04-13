# day 11 part 1 --------------------------------------------------------------
import numpy as np

array=np.zeros((10,10),dtype=int)
with open('data/day11Octopus.txt','rt') as f:
    for idx,line in enumerate(f):
        array[idx]=[int(x) for x in list(line)[:-1]]

# in jedem Zeitschritt:
#alle elemente ++. Alle die 10 werden, in Nullerliste aufnehmen und nullen.
# -> Nullerliste.
# Schleife für jeden Nuller in Nullerliste:
    #alle elemente, die um den 0er sind ++, außer 0er.
    #wird ein element null, so dieses in die Nullerliste aufnehmen.
# Anzahl elemente in Nullerliste ist anzahl der leuchtenden Oktopusse im Zeitschritt.

def clamp(val, mini=0, maxi=10):
    return max(min(maxi, val), mini)
    
totalFlashes = 0
allFlash = [] # day 11 part 2
for idx in range(500): #timesteps // great enough to find first allflash
    
    #increment and reset array
    array+=1
    array[array==10]=0
    
    #put zero elements positions into nullList
    [yn,xn] = np.where(array==0)
    nullList=[(y,x) for y,x in zip(yn,xn)]
    
    for (y,x) in nullList:
        #inc all elements around x,y, respect borders!
        a = array[clamp(y-1):clamp(y+2),clamp(x-1):clamp(x+2)]
        
        # this is the initial zero's position in the a!
        x0, y0 = (x!=0)*1, (y!=0)*1
        
        a[a!=0]+=1 #increment all values despite 0
                
        #are elements == 10? -> push positions to nullList and set to zero.
        yn,xn = np.where(a==10) # new elements that are zero
        nullList.extend([(yadd,xadd) for yadd,xadd in zip(yn-y0+y,xn-x0+x)]) # add to nullList
        
        a[a==10]=0 #set 10 to zero
        
        #update array
        array[clamp(y-1):clamp(y+2),clamp(x-1):clamp(x+2)]=a
        
        #print(f'{y,x}: \n{a}')
    totalFlashes +=sum(sum(array==0))
    if idx==99: print(f'There were {totalFlashes} flashes in {idx+1} steps.')
    if sum(sum(array)) == 0: allFlash.append(idx+1)
print(f'All octupus are first time flashing together in step {allFlash[0]}')