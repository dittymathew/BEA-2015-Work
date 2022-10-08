import networkx as nx
import matplotlib.pyplot as plt
import operator

def edge_count_cycles(cycles,edges):
  cycle_edges={}
  for c in cycles:
    
    for i in range(0,len(c)):
      if i!=len(c)-1:
        e=(c[i],c[i+1])
      else:
        e =(c[i],c[0])

      edge_index=edges.index(e)
      if edge_index not in cycle_edges:
        cycle_edges[edge_index]=0
      cycle_edges[edge_index] +=1
  return cycle_edges
      

G=nx.DiGraph()
G=nx.read_gpickle("data/brown/SCC_nodes10.gpickle")
edges=[(v1,v2) for (v1,v2,d) in G.edges(data=True)]
#print edges

cycles=[c for c in nx.simple_cycles(G) if len(c)<=20]
cycle_edge_cnt=edge_count_cycles(cycles,edges)
sorted_cycle_edges= sorted(cycle_edge_cnt.iteritems(),key=operator.itemgetter(1))
no_cycle_edges=len(sorted_cycle_edges)
k=no_cycle_edges-1
while k>=0:
  print edges[sorted_cycle_edges[k][0]],'::',sorted_cycle_edges[k][1]
  k -=1
print
print 'No of Cycles :',len(cycles)

step=1
while cycles!=[]:
  print
  print 'Step ',step
  break_edge= edges[sorted_cycle_edges[no_cycle_edges-1][0]]
  print 'Breaking ',break_edge

  G.remove_edge(break_edge[0],break_edge[1])
  edges=[(v1,v2) for (v1,v2,d) in G.edges(data=True)]
  cycles=[c for c in nx.simple_cycles(G) if len(c)<=20]
  print 'No of Cycles :',len(cycles)
  cycle_edge_cnt=edge_count_cycles(cycles,edges)
  sorted_cycle_edges= sorted(cycle_edge_cnt.iteritems(),key=operator.itemgetter(1))
  no_cycle_edges=len(sorted_cycle_edges)
  step +=1 

