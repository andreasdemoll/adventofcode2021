from collections import defaultdict

# get every node as key and its corresponding neighbours as values
c = defaultdict(list)
with open('data/day12Pathes.txt', 'r') as txt:
  for l in txt:
    n0,n1 = l.strip().split('-')
    c[n0].append(n1)
    c[n1].append(n0)

# recursively find paths and add them to pathes (resulting path list)
# get connected nodes of current node and potentially add them.
# always pass the visited nodes to the next called instance.
# if an instance reaches end, simply return it. All returned pathes
# will due to the iteration be added up to pathes.



def visit1(c, node, visited):
  pathes = []
  visitedNew = visited + [node]
  if node == 'end':
    #print("visit1 returning on node end with ", [visitedNew])
    return [visitedNew] # new path found, return it.
  for n in c[node]:     # iterate over all nodes where node leads to
    if n != 'start':    # cannot go over start.
      if n not in visited or n.isupper(): # not yet visited (for small nodes)
        #print("calling visit1 for node ",n)
        path = visit1(c, n, visitedNew)
        #print("visit1 returned with path ",path)
        pathes.extend(path)
  return pathes

print('Part 1 result is:', len(visit1(c, 'start', [])))

# recursion principle here: call visit1 again and again,
# always with the current path and the next node to examine
# in the current path taken. If the node is "end", the path
# is returned and added to pathes. When all nodes on all ways
# through the tree have been checked, the pathes list will
# contain all pathes that came to node "end".
# This result will then be returned. 

def visit2(c, node, visited):
  # recursively find paths - and add 'em to res (resulting list)
  pathes = []
  # next visited node
  visitedNew = visited + [node]
  if node == 'end':
    return [visitedNew]
  for n in c[node]:
    if n != 'start':
      # uppercase nodes can be visited any time
      if n.isupper():
        path = visit2(c, n, visitedNew)
        pathes.extend(path)
      else:
        # any lowercase node - just one can be visited twice
        lowers = [i for i in visitedNew if i.islower()]
        twice = any([True for i in lowers if lowers.count(i) > 1])
        if (twice and visitedNew.count(n) < 1) or (not twice and visitedNew.count(n) < 2):
          path = visit2(c, n, visitedNew)
          pathes.extend(path)
  return pathes

print('Part 2 result is:', len(visit2(c, 'start', [])))