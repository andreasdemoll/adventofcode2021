# day9 part 1 ----------------------------------------------------------------
import numpy as np

#array = np.zeros((5,10))
array = np.zeros((100,100))

with open('data/day9LavaTubes.txt','rt') as f:
    for idx, line in enumerate(f):
        array[idx,:] = list(line.split()[0])

#shift array to all sides
array_r = np.roll(array,1,1)
array_l = np.roll(array,-1,1)
array_u = np.roll(array,-1,0)
array_d = np.roll(array,1,0)
       
#check value to all sides
mask_r = (array < array_r)*1
mask_l = (array < array_l)*1
mask_d = (array < array_d)*1
mask_u = (array < array_u)*1

#remove invalid border vectors
mask_r[:,0]=0  #invalid fist col
mask_l[:,-1]=0 #invalid last col
mask_d[0,:]=0  #invalid first row
mask_u[-1,:]=0 #invalid last row

#combine masks
mask = mask_r + mask_l + mask_u + mask_d

#desired mask has sum of 4 everywhere in middle, 3 at borders and 2 at edges.
mask_desired = np.ones(array.shape)*4
mask_desired[0,:]=3
mask_desired[-1,:]=3
mask_desired[:,0]=3
mask_desired[:,-1]=3
mask_desired[0,0]=2
mask_desired[0,-1]=2
mask_desired[-1,0]=2
mask_desired[-1,-1]=2

indicator = (mask>=mask_desired)

print(f'the sum of the risk levels is {sum(array[indicator]+1)}')

# day9 part 2 ----------------------------------------------------------------
(yLow,xLow) = np.where(indicator)
basinSizes =[]
for idx in range(len(yLow)):
    basin=[]
    basin.append((yLow[idx],xLow[idx]))

    for (y,x) in basin:
        #print(f'x:{x}, y:{y}')
        
        #check for each potential neighbor:
        #no neighbor available due to border,
        #curr element == 8 (no further increase inside basin possible),
        #already contained in basin,
        #non-increasing slope (basin constraint) or
        # neighbor == 9 (not part of basin per definition)
        
        #RIGHT NEIGHBOR
        if x+1<array.shape[1]:
            if  array[y,x]==8 or\
                (y,x+1) in basin or\
                array[y,x+1] <= array[y,x] or\
                array[y,x+1] == 9: pass
            else:
                basin.append((y,x+1))
        
        #LEFT NEIGHBOR
        if x-1>=0:
            if  array[y,x]==8 or\
                (y,x-1) in basin or\
                array[y,x-1] <= array[y,x] or\
                array[y,x-1] == 9: pass
            else:
                basin.append((y,x-1))
            
        #BOTTOM NEIGHBOR
        if y+1<array.shape[0]:
            if  array[y,x]==8 or\
                (y+1,x) in basin or\
                array[y+1,x] <= array[y,x] or\
                array[y+1,x] == 9: pass
            else:
                basin.append((y+1,x))
    
        #TOP NEIGHBOR
        if y-1 >= 0:
            if  array[y,x]==8 or\
                (y-1,x) in basin or\
                array[y-1,x] <= array[y,x] or\
                array[y-1,x] == 9: pass
            else:
                basin.append((y-1,x))
        
    basinSizes.append(len(basin))
print(f'product of 3 largest basins: '
      f'{np.prod(sorted(basinSizes,reverse=True)[:3])}')
            
            