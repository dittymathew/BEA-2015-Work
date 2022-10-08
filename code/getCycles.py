import operator
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
G=nx.read_gpickle("data/brown/largest_SCC.gpickle")
nodes=[c[0] for c in G.nodes(data=True)]
deg =G.degree(nodes)
sorted_nodes_degree= sorted(deg.iteritems(),key=operator.itemgetter(1))
#node_high_degree= sorted_nodes_degree[len(sorted_nodes_degree)-1][0]
#G.remove_node(node_high_degree)
i =0
print len(G.nodes(data=True))
print len(G.edges(data=True))
for c in nx.simple_cycles(G):
  if len(c)<50:
    print c
  i +=1
