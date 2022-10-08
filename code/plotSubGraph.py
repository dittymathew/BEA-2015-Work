
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cStringIO import StringIO

from IPython.display import Image



G=nx.DiGraph()
cls=''
G=nx.read_gpickle("data/gutenberg/graph_guten_cls"+cls+".gpickle")
#w =['accusation', 'exoneration', 'violate', 'off-color', 'indelicate', 'pornographer', 'misbranded', 'transgression', 'burglary', 'infraction', 'misdemeanor', 'violation', 'lockup', 'incarcerate', 'hoffa', 'imprisonment', 'imprison', 'convict', 'hoosegow', 'detective', 'perpetration', 'tenderloin', 'crook', 'indict', 'felon', 'alibi', 'notification', 'rico', 'racketeer', 'criminal', 'complicity', 'felony', 'capo', 'abduction', 'bop', 'outlaw', 'felonious', 'treason', 'presentment', 'recrimination', 'allegation', 'blame', 'accuse', 'calumny', 'lodgment', 'respondent', 'chargeable', 'remand', 'worcester', 'jail', 'accusingly', 'bail', 'defendant', 'australia', 'fingerprint', 'thief', 'gangster', 'hoodlum', 'firebug', 'law-breaking', 'thug', 'pretrial', 'hood', 'stealer', 'acquit', 'underworld', 'mobster', 'scaffold', 'crime', 'arrest', 'tojo', 'exonerate', 'bounty', 'prosecutor', 'lam', 'blackmailer', 'murderer', 'prosecution', 'dragnet', 'perjury', 'syndicate', 'criminality', 'punk', 'imputation', 'incendiary', 'gang']
#w=['blame',  'violation', 'felony', 'jail', 'crime', 'accusation', 'accuse', 'convict', 'criminal']
#w=['violate', 'off-color', 'indelicate', 'pornographer', 'misbranded', 'transgression', 'burglary', 'infraction', 'misdemeanor', 'violation', 'detective', 'perpetration', 'tenderloin', 'crook', 'indict', 'felon', 'alibi', 'notification', 'rico', 'racketeer', 'criminal', 'complicity', 'felony', 'capo', 'abduction', 'bop', 'outlaw', 'felonious', 'treason', 'presentment', 'fingerprint', 'thief', 'gangster', 'hoodlum', 'firebug', 'law-breaking', 'thug', 'bail', 'pretrial', 'hood', 'stealer', 'acquit', 'underworld', 'mobster', 'scaffold', 'crime', 'arrest', 'tojo', 'exonerate', 'bounty', 'prosecutor', 'lam', 'blackmailer', 'murderer', 'prosecution', 'dragnet', 'perjury', 'syndicate', 'criminality', 'punk', 'imputation', 'incendiary', 'gang']
w=['stubborn', 'obstinate', 'stubbornly', 'tenaciously']
w=['deceit', 'fraudulent', 'dishonest', 'deceive', 'defraud']
"""
w=['logical','truth','verification','proof','judgment','opinion', 'conclusion','inference', 'logic', 'valid','empress', ]
for w1 in ['logical','truth','verification','proof','judgment','opinion', 'conclusion','inference', 'logic', 'valid','empress', ]:
  w_succ =G.successors(w1)
  for w2 in w_succ:
    for w3 in ['logical','truth','verification','proof','judgment','opinion','conclusion', 'inference', 'logic', 'valid','empress', ]:
      if w3 in G.successors(w2) or w3 in G.predecessors(w2):
        w.append(w2)
        break
  w_pred =G.predecessors(w1)
  for w2 in w_pred:
    for w3 in ['logical','truth','verification','proof','judgment','opinion', 'inference','conclusion', 'logic', 'valid','empress', ]:
      if w3 in G.successors(w2) or w3 in G.predecessors(w2):
        w.append(w2)
        break
"""
H=G.subgraph(w)
#H_nodes =[n[0] for n in H.nodes(data=True)]
#for n in H_nodes:
#  print H.successors(n)
#  if H.successors(n)== [] or H.predecessors(n)==[]:
#    H.remove_node(n)


d = nx.to_pydot(H)
d.write_png('data/brown/class'+cls+'_subgraph.png')
