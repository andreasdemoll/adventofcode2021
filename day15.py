''' 
recursive solution for small matrices:
Call cost for final row/col. Call cost for decremented row and for
decremented col and return the minimum of both plus the current cost.
When we get out of shape (row or col < 0), return inf (no further call). This
stops recursion and discardes result. When we get to origin, return zero (do
not count this value).
This results in building a tree of pathes from (10,10) to many destinations.
Final destinatins are out of shape or origin. Function always discards the
branch with higher cost. Finally only one branch is left at
highest level function call which is the optinal weight path from origin to
(10,10).
'''
import numpy as np
with open('day15ChitonTest.txt', 'rt') as f:
  C = np.array([[int(v) for v in list(l.strip())] for l in f.readlines()])

def cost(C, r, c):
  #print('Call at r= ',r,', c= ',c)
  if c < 0 or r < 0: ret = np.inf
  elif r == 0 and c == 0: ret = 0
  else:
    #print(f'calling next: r={r-1}, c={c}')
    ret = C[r, c] + min(cost(C, r-1, c), cost(C, r, c-1))
  #print('ret: ',ret)
  return ret

print(f'sum of path of the example: {cost(C,len(C)-1,len(C)-1)}')
''' This obviously does not work with a matrix of 100x100, as the number of
pathes increases dramatically. Dijkstra is the way to go.
'''

# day15.part1 ----------------------------------------------------------------
import dijkstra
with open('day15Chiton.txt', 'rt') as f:
  C = np.array([[int(v) for v in list(l.strip())] for l in f.readlines()])

#extend the map with surrounding inf's s.th we do not need to care about
#edges or corners in the later algorithm.
I = np.ones((C.shape[0]+2,C.shape[1]+2))*np.inf
I[1:-1,1:-1] = C

# convert our matrix to a graph, where each (directed) edge has the weight of
# the node it points to. So the g.edges is not symmetrical!
def genEdgescorrectly(g,I):
  n = I.shape[0]
  If = I.flatten()
  for idx in range(len(If)):
    if If[idx] != np.inf:
      #print('adding single edge from ',idx,' with distances 1 and ' ,n)
      g.add_single_edge(idx,idx+1,If[idx+1])
      g.add_single_edge(idx,idx-1,If[idx-1])
      g.add_single_edge(idx,idx-n,If[idx-n])
      g.add_single_edge(idx,idx+n,If[idx+n])
  return g

if 0:
  g = dijkstra.Graph(I.shape[0]*I.shape[1]) #generate graph
  g = genEdgescorrectly(g,I) #generade all edges according to I
  resCosts = dijkstra.dijkstra(g, I.shape[0]+1) #solve dijkstra for startnode
  costToEnd = list(resCosts.values())[-(I.shape[0]+2)] #extract cost of endnode  
  print('the total cost from start to end is ',costToEnd)

# day15.part2 ----------------------------------------------------------------
def incC(C):
  C+=1
  C[C>9]=1

C2 = np.zeros((C.shape[0]*5,C.shape[1]*5))
for idxI in range(5):
  for idxJ in range(5):
    Ccopy = C.copy()
    for inc in range(idxI+idxJ): incC(Ccopy)
    C2[idxI*C.shape[0] : (idxI+1)*C.shape[0],
       idxJ*C.shape[0] : (idxJ+1)*C.shape[0]] = Ccopy.copy()

I2 = np.ones((C2.shape[0]+2,C2.shape[1]+2))*np.inf
I2[1:-1,1:-1] = C2
g2 = dijkstra.Graph(I2.shape[0]*I2.shape[1]) #generate graph
g2 = genEdgescorrectly(g2,I2) #generade all edges according to I
resCosts2 = dijkstra.dijkstra(g2, I2.shape[0]+1) #solve dijkstra for startnode
costToEnd = list(resCosts2.values())[-(I2.shape[0]+2)] #extract cost of endnode  
print('the total cost from start to end is ',costToEnd)