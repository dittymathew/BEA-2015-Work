import operator
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
  freq_data =open('data/wordfrequency.txt').read().strip().split('\n')
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


def edgeStrength(G,method):
  edges =[(u,v) for (u,v,nil) in G.edges(data=True)]
  edge_strength ={}
  for i in range(len(edges)):
    (u,v)= edges[i]
    if method =='rel':
      u_score = relativeCoverage(G,u)
      v_score = relativeCoverage(G,v)
    if method =='imp':
      u_score = importance(G,u)
      v_score = importance(G,v)
    if u_score ==0 and v_score==0:
      weight =0
    else:
      weight = (2*u_score*v_score)/(u_score+v_score)
#      weight = float(u_score+v_score)/2.0
    edge_strength[i]= weight
  sort_edge_strength= sorted(edge_strength.iteritems(),key=operator.itemgetter(1))
  return (edges, sort_edge_strength)  # (edges, dictionary of descending order of edge_strength with key as indices of edges)
    


def PageRank_RelCov(G,method):
  edges =G.edges(data=True)
  edge_strength =[]
  for i in range(len(edges)):
    (u,v,d)= edges[i]
    if method =='pr_rel':
      u_score = relativeCoverage(G,u)
      v_score = relativeCoverage(G,v)
    if method =='pr_imp':
      u_score = importance(G,u)
      v_score = importance(G,v)
    if u_score ==0 and v_score==0:
      weight =0
    else:
      weight = (2*u_score*v_score)/(u_score+v_score)
    d['weight']=weight
  pr=nx.pagerank(G)
  sort_pr= sorted(pr.iteritems(),key=operator.itemgetter(1))
  print sort_pr
  return sort_pr

def adjacentNodes(G,node):
  return G.successors(node)

def DFS(G,node, goal, visitedNodes):
   if node == goal:
      return True
 
   visitedNodes.append(node)
   for adjNode in adjacentNodes(G,node):
      if adjNode not in visitedNodes:
         if DFS(G,adjNode, goal, visitedNodes):
            return True
 
   return False


def findDep(G,method):
  if method in ['imp','rel']:
    (edges,edge_strength) =edgeStrength(G,method)
    
  elim_edges=[]
  for i in range(len(edge_strength)-1,-1,-1): # decrementing from len(edge_strength)-1 to 0
    (cur_u,cur_v) =edges[edge_strength[i][0]] # current_edge = cur_u -> cur_v
    print cur_u,cur_v,nx.is_directed_acyclic_graph(G),DFS(G,cur_v,cur_u,[])
    if nx.is_directed_acyclic_graph(G):
      break
    if DFS(G,cur_v,cur_u,[]):
      G.remove_edge(cur_u,cur_v)
      elim_edges.append((cur_u,cur_v))
#  elim_edges = list(set(edges)-set(non_elim_edges))
  print 'No of edges in the graph :' ,len(edges)
  print 'No of dependencies eliminated :',len(elim_edges) 
  return  elim_edges

(wordFreq,wordNormFreq) =wordFrequency()
G1=nx.DiGraph()
G1=nx.read_gpickle("data/largest_SCC.gpickle")
print len(findDep(G1,'rel'))
#print len(groundConcepts(G1,'pr_rel'))


