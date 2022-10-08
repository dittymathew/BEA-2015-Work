import networkx as nx

G=nx.DiGraph()
G=nx.read_gpickle("data/brown/largest_SCC.gpickle")
for cycle in nx.simple_cycles(G):
  if len(cycle)<10:
    print cycle
