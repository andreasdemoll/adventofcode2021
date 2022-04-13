import numpy as np

# day 6 part 1 ---------------------------------------------------------------
def getLanternfishList(file='data/day6Lanternfish.txt'):
    with open(file,'tr') as f:
        lis = [int(val) for val in f.readline().split(',')]
    return lis

lis = getLanternfishList()
lis_prev = lis.copy()

for idxDay in range(80):
    lis = [f-1 if f>0 else 6 for f in lis ]
    lis.extend(sum([(i-j)>1 for i,j in zip(lis,lis_prev)])*[8])
    lis_prev = lis.copy()
    #print(f'day {idxDay+1}: {len(lis)} fishes')
    
print(f'There are {len(lis)} fishes after 80 days.')
# mutch too slow to count up to 256. Better only save the number of fishes
# of a certain age, corresponding to a histogram.

# day 6 part 2 ---------------------------------------------------------------
lis = getLanternfishList()
hist = [0,0,0,0,0,0,0,0,0]
histmap = np.zeros([256,9])
for val in lis:
    hist[val]+=1
for idxDay in range(256):
    new=hist[0]
    hist = hist[1:]
    hist.append(new)
    hist[6]+=new
    histmap[idxDay] = hist
print(f'There are {sum(hist)} fishes after 256 days!')
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#ax.set_yscale('log')
#for num in range(histmap.shape[1]):
#    ax.plot(histmap[:,num])