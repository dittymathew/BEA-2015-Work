import operator
import random
from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

def coverage(G,a):
  return G.successors(a)

def reachability(G,b):
  return G.predecessors(b)

def relativeCoverage(G,a):
  relCov=0
  for b in coverage(G,a):
    relCov += 1.0/float(len(reachability(G,b)))
  return relCov

def wordFrequency():
  freq_data =open('data/count_big.txt').read().strip().split('\n')
  word_freq ={}
  for line in freq_data:
    line_con = line.split('\t')
    w=line_con[0].lower()
    freq =line_con[1]
    word_freq[w] =int(freq)
  max_freq = max(word_freq.iteritems(), key=operator.itemgetter(1))[1]
  word_Normfreq = { w:float(word_freq[w])/float(max_freq) for w in word_freq}
  return (word_freq,word_Normfreq)

def getFrequency(a):
  if a in wordFreq:
    return wordFreq[a]
  else:
    return 0
  
def getNormFrequency(a):
  if a in wordNormFreq:
    return wordNormFreq[a]
  else:
    return 0
  

def frequencyScore(G,a):
  cov_a = coverage(G,a)
  cov_score =0
  for b in cov_a:
    cov_score += getNormFrequency(b)
  freq_score= 0.5*getNormFrequency(a) +0.5*cov_score
  return freq_score

def wn_WUPSim(w1,w2):
  word1=wn.synsets(w1)
  word2=wn.synsets(w2)
  l1= len(word1)
  l2= len(word2)
  sim =0
  for i in range (0,l1):
    for j in range (0,l2):
      simk =wn.wup_similarity(word1[i],word2[j])
      if simk > sim :
        sim =simk
  return sim


def normRelatednessWRTb(G,a,b):
  reach_b = reachability(G,b)
  rel_ab = wn_WUPSim(a,b)
  if rel_ab ==0:
    return 0
  norm_c =0
  for a_ in reach_b:
    norm_c += wn_WUPSim(a_,b)
  norm_sim = rel_ab/norm_c
  return norm_sim

def importance(G,a):
  cov_a = coverage(G,a)
  imp=0
  for b in cov_a:
    imp += frequencyScore(G,b)*normRelatednessWRTb(G,a,b)
  return imp


def ImpScore(G,method):
  nodes =G.nodes(data=True)
  imp_nodes={}
  for n in nodes:
    n=n[0].lower()
    if method =='rel':
      imp_nodes[n] = relativeCoverage(G,n)
    if method =='imp':
      imp_nodes[n] = importance(G,n)

  sort_imp= sorted(imp_nodes.iteritems(),key=operator.itemgetter(1))
  return sort_imp  # descending order of importance

def PageRank(G):
  pr=nx.pagerank(G)
  sort_pr= sorted(pr.iteritems(),key=operator.itemgetter(1))
  return sort_pr # descending order of pagerank

def PageRank_RelCov(G,method):
  nodes =G.nodes(data=True)
  node_weight={}
  for n in nodes:
    if method == 'pr_imp':
      node_weight[n[0]]=importance(G,n[0])
    if method == 'pr_rel':
      node_weight[n[0]]=relativeCoverage(G,n[0])
  pr=nx.pagerank(G,personalization=node_weight)
  sort_pr= sorted(pr.iteritems(),key=operator.itemgetter(1))
  return sort_pr

def adjacentNodes(G,node):
  return G.successors(node)

def DFS(G,node, goal, visitedNodes):
 
   visitedNodes.append(node)
   for adjNode in adjacentNodes(G,node):
      if adjNode not in visitedNodes:
         if DFS(G,adjNode, goal, visitedNodes):
            return True
      elif adjNode == goal:
        return True
 
   return False

def randomList(a):
  b = []
  for i in range(len(a)):
    element = random.choice(a)
    a.remove(element)
    b.append(element)
  return b

def randomOrder(G2):
  nodes =[n[0] for n in G2.nodes(data=True)]
  rand_order= randomList(nodes)
  return rand_order

def degreeBasedOrder(G):
  nodes =[n[0] for n in G.nodes(data=True)]
  node_degree={}
  for n in nodes:
    degree =G.in_degree(n)+G.out_degree(n)
    node_degree[n]=degree
  sort_degree= sorted(node_degree.iteritems(),key=operator.itemgetter(1))
  return sort_degree

  

def groundConcepts(G,method): # method ='imp' for ImpScore method ='pr' for pagerank
  if method in ['imp','rel']:
    order_nodes = ImpScore(G,method) #descending order
  if method == 'pr':
    order_nodes =PageRank(G) #descending order
  if method in ['pr_imp','pr_rel']:
    order_nodes =PageRank_RelCov(G,method) #descending order
  if method == 'rand':
    order_nodes =randomOrder(G.copy())
  if method == 'degree':
    order_nodes=degreeBasedOrder(G)
  grounded_nodes=[]
  for i in range(len(order_nodes)-1,-1,-1): # decrementing from len(order_nodes)-1 to 0
    if method !='rand':
      cur_node =order_nodes[i][0]
    else:
      cur_node =order_nodes[i]
#    print cur_node,nx.is_directed_acyclic_graph(G),DFS(G,cur_node,cur_node,[])
    if nx.is_directed_acyclic_graph(G):
      break
    if DFS(G,cur_node,cur_node,[]): # implies cur_node involves in cycle
      G.remove_node(cur_node)
      grounded_nodes.append(cur_node)
  return grounded_nodes

def groundConceptsIncremental(G,method):
  if method =='imp':
    order_nodes = ImpScore(G) #descending order
  if method == 'pr':
    order_nodes =PageRank(G) #descending order
  if method == 'pr_rel':
    order_nodes =PageRank_RelCov(G) #descending order
  non_grounded_nodes=[]
  newG=nx.DiGraph()
  allnodes= [n[0] for n in order_nodes]
  for i in range(0,len(order_nodes)): # decrementing from len(order_nodes)-1 to 0
    if method !='rand':
      cur_node =order_nodes[i][0]
    else:
      cur_node =order_nodes[i]
    if nx.is_directed_acyclic_graph(newG)== False:
      break
    cur_node_neighbours =adjacentNodes(G,cur_node)
    for neighbour in cur_node_neighbours:
      newG.add_edge(cur_node,neighbour)
    non_grounded_nodes.append(cur_node)
  grounded_nodes = list(set(allnodes)-non_grounded_nodes)
  return  grounded_nodes

def per_val(a,b):
  return (float(a)/float(b))*100

def jaccard(A,B):
  return round(float(len(set(A).intersection(set(B))))/float(len(set(A).union(set(B)))),2)

(wordFreq, wordNormFreq) =wordFrequency()
G1=nx.DiGraph()
G1=nx.read_gpickle("data/gutenberg/largest_SCC_cls4.gpickle")
n_nodes =len(G1.nodes(data=True))
#print len(groundConcepts(G1,'rel'))
"""
pr_ground_concepts =groundConcepts(G1.copy(),'pr')
pr_goodnessScore = 0
for c in pr_ground_concepts:
  pr_goodnessScore += getFrequency(c)
pr_goodnessScore = float(pr_goodnessScore)/float(len(pr_ground_concepts))
print 'Pagerank'
print 'No of Grounded Concepts :',len(pr_ground_concepts)
print 'Goodness Measure :', pr_goodnessScore
"""
pr_rel_ground_concepts =groundConcepts(G1.copy(),'pr_rel')
pr_rel_goodnessScore = 0
for c in pr_rel_ground_concepts:
  pr_rel_goodnessScore += getFrequency(c)
pr_rel_goodnessScore =float(pr_rel_goodnessScore)/float(len(pr_rel_ground_concepts))

print 'Pagerank(Relative Coverage)'
print 'No of Grounded Concepts :',len(pr_rel_ground_concepts)
print 'Goodness Measure :', pr_rel_goodnessScore
print pr_rel_ground_concepts
"""
rel_ground_concepts =groundConcepts(G1.copy(),'rel')
rel_goodnessScore = 0
for c in rel_ground_concepts:
  rel_goodnessScore += getFrequency(c)
rel_goodnessScore = float(rel_goodnessScore)/float(len(rel_ground_concepts))
print 'Relative Coverage'
print 'No of Grounded Concepts :',len(rel_ground_concepts)
print 'Goodness Measure :', rel_goodnessScore

rand_ground_concepts =groundConcepts(G1.copy(),'rand')
rand_goodnessScore = 0
for c in rand_ground_concepts:
  rand_goodnessScore += getFrequency(c)
rand_goodnessScore = float(rand_goodnessScore)/float(len(rand_ground_concepts))

deg_ground_concepts =groundConcepts(G1.copy(),'degree')
deg_goodnessScore = 0
for c in deg_ground_concepts:
  deg_goodnessScore += getFrequency(c)
deg_goodnessScore = float(deg_goodnessScore)/float(len(deg_ground_concepts))

print 'Method & Percentage of concepts grounded & Goodness Measure'
print 'Pagerank & ', per_val(len(pr_ground_concepts),n_nodes),' & ', pr_goodnessScore,'\\\\'
print 'Pagerank (Relative Coverage) & ', per_val(len(pr_rel_ground_concepts),n_nodes),' & ', pr_rel_goodnessScore,'\\\\'
print 'Relative Coverage & ', per_val(len(rel_ground_concepts),n_nodes),' & ', rel_goodnessScore,'\\\\'
print 'Random & ', per_val(len(rand_ground_concepts),n_nodes),' & ', rand_goodnessScore,'\\\\'
print 'Degree & ', per_val(len(deg_ground_concepts),n_nodes),' & ', deg_goodnessScore,'\\\\'
"""
#print 'Overlap between Pagerank and Pagerank(rel cov) :', jaccard(pr_ground_concepts,pr_rel_ground_concepts)
#print 'Overlap between Pagerank and Relative Coverage :', jaccard(pr_ground_concepts,rel_ground_concepts)
#print 'Overlap between Pagerank(rel cov) and Relative Coverage :', jaccard(pr_rel_ground_concepts,rel_ground_concepts)
