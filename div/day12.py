# day 11 part 1 --------------------------------------------------------------

import numpy as np

def genAdjMat(file='day12Pathes.txt'):
    # read in graph, store names and adjacence matrix
    nodeNames = ['start','end']
    with open(file,'rt') as f:
        for line in f:
            fr, to = line.strip().split('-')
            if fr not in nodeNames: nodeNames.append(fr)
            if to not in nodeNames: nodeNames.append(to)
        nodeNames.append(nodeNames.pop(1)) #move end to end
        adjMat = np.zeros((len(nodeNames),len(nodeNames)),dtype=np.byte)
        f.seek(0)
        for line in f:
            fr, to = line.split()[0].split('-')
            adjMat[min(nodeNames.index(fr),nodeNames.index(to)),
                   max(nodeNames.index(fr),nodeNames.index(to))] = 1
    adjMat = np.maximum(adjMat, adjMat.T)
    return adjMat, nodeNames

def fillup(adj, nodeNames, path, forks):
    _adjMat = adj.copy()
    row = path[-1]
    while(1):
        #deadlock reached
        if sum(_adjMat[row,1:])==0: break
    
        #select next row, store the branches to forks.
        nodesNxt = np.where(_adjMat[row,1:])[0]+1
        rowNxt = nodesNxt[0]
        forks.append(nodesNxt[1:].tolist())
        
        #delete all small-letter-node connections
        if row>0 and row<len(nodeNames)-1 and nodeNames[row].islower():
            _adjMat[row]*=0
            _adjMat[:,row]*=0
        row = rowNxt
        
        path.append(row)
        
        #check for end reached
        if row==len(nodeNames)-1: break
    return _adjMat, path, forks

def modifyadjidenceMatrix(adj,path,nodeNames):
    _adjMat = adj.copy()
    for node in path[:-1]:
        #delete all small-letter-node connections
        if node>0 and node<len(nodeNames)-2 and nodeNames[node].islower():
            _adjMat[node]*=0
            _adjMat[:,node]*=0
    return _adjMat


adjMat, nodeNames = genAdjMat()
pathes= []  # this list stores all valid pathes found.
path  = [0] # the currently followed path
forks = []  # the nodes that were not tanken for each step in path

print(f'processing network with {adjMat.shape[0]} nodes and '
      f'{int(sum(sum(adjMat))/2)} edges')

#initial filling up
adj, path, forks = fillup(adjMat, nodeNames, path, forks)
if path[-1]==len(nodeNames)-1:
    pathes.append(path.copy())

while(1):
    #pop empty forks from fork and from path. End if forks is empty.
    while len(forks)>0:
        if forks[-1]==[]:
            forks.pop()
            path.pop()
        else: break
    else: break
    
    #attach smallest fork to path
    path[-1] = min(forks[-1])
    forks[-1].remove(min(forks[-1]))
    
    #recalc adjidence matrix for the current path and fillup the path.   
    adj = modifyadjidenceMatrix(adjMat,path,nodeNames)
    if path[-1]!=len(nodeNames)-1:
        adj,path,forks = fillup(adj,nodeNames,path,forks)
    if path[-1]==len(nodeNames)-1:
        pathes.append(path.copy())
#for path in pathes:        
#    print(','.join([nodeNames[i] for i in path ]))
print(f'\nlength of pathes: {len(pathes)}')