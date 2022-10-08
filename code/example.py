import networkx as nx
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import nltk,re

def extractDefn(word):
  synsets = wn.synsets(word)
  if synsets ==[]:
    return []
  defn = synsets[0].definition()
  defn = re.sub('[\`\)\\\(\,!\.\:\;\'\"\?0-9]', '', defn.lower())
  def_words =defn.split()
  new_defWords = [wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.VERB),pos=wn.NOUN),wn.ADJ),wn.ADV) for w in def_words if w not in stop]
  return new_defWords

G =nx.DiGraph()
w= 'climate'
w_def= extractDefn(w)
for i in range(0:2):
  for wdef in w_def:
    G.add_edge(wdef,w)
  w_def = 
  
