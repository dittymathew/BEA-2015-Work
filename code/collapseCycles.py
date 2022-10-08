import networkx as nx
import operator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cStringIO import StringIO

from IPython.display import Image

def wordFrequency():
  freq_data =open('data/wordfrequency.txt').read().strip().split('\n')
  word_freq ={}
  for line in freq_data:
    line_con = line.split('\t')
    w=line_con[0].lower()
    freq =line_con[1]
    word_freq[w] =int(freq)
  return word_freq

def cumulativeFrequency(scc_nodes):
  imp=0
  for n in scc_nodes:
    n= n.lower()
    if n in word_freq:
      imp += word_freq[n]
  return imp

word_freq=wordFrequency()
G=nx.DiGraph()
cls='5'
#G=nx.read_gpickle("data/brown/graph_brown_cls"+cls+".gpickle")
G=nx.read_gpickle("data/brown/graph_brown_cls8.gpickle")
#G=nx.read_gpickle("data/brown/SCC_nodes10.gpickle")
dag=nx.condensation(G)
dag_edges= dag.edges(data=True)
dag_nodes=dag.nodes(data=True)
sorted_nodes= nx.topological_sort(dag)

##Assigning Cumulative Frequency
cum_freq ={}
for i in range(len(sorted_nodes)):
  i_nodes= dag_nodes[sorted_nodes[i]][1]['members']
  
  cum_freq[i]= cumulativeFrequency(i_nodes)
##Backpropagating
j =len(sorted_nodes)-1
#comp_prop_score={}
prop_score=0
while j>=0:
  out_neighbours =dag.successors(sorted_nodes[j])
  for comp in out_neighbours:
    cum_freq[j] += cum_freq[comp]
  j -=1
sort_cum_freq= sorted(cum_freq.iteritems(),key=operator.itemgetter(1))
n= len(sort_cum_freq)-1
k=0
while n>=0:
  if k==50:
    break
  comp =sort_cum_freq[n][0]
  comp_cum_freq =sort_cum_freq[n][1]
#  if comp_cum_freq >0:
  scc_nodes= dag_nodes[sorted_nodes[comp]][1]['members']
  if len(scc_nodes)>1:
      print scc_nodes
      k+=1
  n -=1
print k
