from collections import defaultdict  
 
class Graph:  
 def __init__(self,vertices):  
  self.graph = defaultdict(list) 
  self.V = vertices  
 
 def addEdge(self,u,v):  
  self.graph[u].append(v)   
 
 def topologicalSort(self):  
  in_degree = [0]*(self.V)  
 
  for i in self.graph:  
   for j in self.graph[i]:  
    in_degree[j] += 1 
  queue = []  
 
  for i in range(self.V):  
   if in_degree[i] == 0:  
    queue.append(i)  
  cnt = 0 
  top_order = []   
 
  while queue:  
   u = queue.pop(0)  
   top_order.append(u)  
 
   for i in self.graph[u]:  
    in_degree[i] -= 1 
    if in_degree[i] == 0:  
     queue.append(i)  
   cnt += 1 
 
  if cnt != self.V:  
   print ("There exists a cycle in the graph") 
  else :  
   print (top_order)  
 
g= Graph(6)  
g.addEdge(1, 0); 
g.addEdge(1, 5); 
g.addEdge(1, 4);  
g.addEdge(2, 1);  
g.addEdge(3, 1);  
g.addEdge(3, 4); 
g.addEdge(5, 4); 
 
print ("Topological Sort:") 
g.topologicalSort()