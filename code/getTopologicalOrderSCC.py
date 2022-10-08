import networkx as nx

G=nx.DiGraph()
G=nx.read_gpickle("data/brown/graph_brown_cls5.gpickle")
dag=nx.DiGraph()
dag=nx.condensation(G)
#print dag.edges(data=True)
dag_nodes=dag.nodes(data=True)
sorted_nodes= nx.topological_sort(dag)
k=0
for i in range(len(sorted_nodes)):
  nodes= dag_nodes[sorted_nodes[i]][1]['members']
  if len(nodes)>1:
    print nodes
    k +=1
print k
