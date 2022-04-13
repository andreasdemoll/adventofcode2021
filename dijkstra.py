# https://stackabuse.com/dijkstras-algorithm-in-python/

from queue import PriorityQueue

class Graph:
  def __init__(self, num_of_vertices):
    self.v = num_of_vertices
    self.edges = [[-1 for i in range(num_of_vertices)]
                  for j in range(num_of_vertices)]
    self.visited = []
  def add_edge(self, u, v, weight):
    if u >= self.v or v >=self.v:
      raise ValueError("edges vertex index exceeds number of verteces")
    self.edges[u][v] = weight
    self.edges[v][u] = weight
  def add_single_edge(self, u, v, weight):
    if u >= self.v or v >=self.v:
      raise ValueError("edges vertex index exceeds number of verteces")
    self.edges[u][v] = weight

def dijkstra(graph, start_vertex):
  D = {v: float('inf') for v in range(graph.v)} #dict with all vertices' costs
  D[start_vertex] = 0
  
  pq = PriorityQueue() # distance from start of all unmarked verteces
  pq.put((0, start_vertex)) #(priority = distance from start, vertex name)
  
  while not pq.empty():
    (dist, current_vertex) = pq.get() #get least cost vertex from the unvisited
    graph.visited.append(current_vertex)

    for neighbor in range(graph.v):
      if graph.edges[current_vertex][neighbor] != -1:
        distance = graph.edges[current_vertex][neighbor]
        if neighbor not in graph.visited:
          old_cost = D[neighbor]
          new_cost = D[current_vertex] + distance
          if new_cost < old_cost:
            pq.put((new_cost, neighbor))
            D[neighbor] = new_cost
  return D

