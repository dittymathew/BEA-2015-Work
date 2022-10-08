import networkx as nx
import os,re,nltk

def getGraph():
  graph ={} # topdown graph bu Networkx Graph G is bottomup graph
  filedata =open('data/brown/brown_dict.txt').read().split('\n')
  for l in filedata:
    l_con = l.strip().split(':')
    node =l_con[0]
    if len(l_con)>1:
      neighbours =l_con[1].split(',')
      for n1 in neighbours :
  
#        if n1 not in blanket_words and node not in blanket_words and n1 !=node :
#          G.add_edge(n1,node)
        if node not in graph:
          graph[node]=[]
        graph[node].append(n1)
  for node in graph:
    for n1 in graph[node]:
      
      if n1 not in blanket_words and node not in blanket_words and n1 !=node and n1 in graph:
          G.add_edge(n1,node)
#    if G.number_of_nodes()>750:
#      break
  return graph



def simple_cycles2(G):
    comps = nx.strongly_connected_component_subgraphs(G)
    all_cycles = []
    for c in comps:
        if len(c) == 1:
            continue
        else:
            for cycles in nx.simple_cycles(c):
                all_cycles.append(cycles)
    return all_cycles


wnl = nltk.WordNetLemmatizer()
cls='1'
blanket_words=open('data/textwords_upto'+cls+'.txt').read().split('\n')
#blanket_words=[]
G=nx.DiGraph()
topdown_graph=getGraph()
nx.write_gpickle(G,"data/brown/graph_brown_cls"+cls+".gpickle")
print G.number_of_nodes()
print G.number_of_edges()
