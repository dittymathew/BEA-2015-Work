import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cStringIO import StringIO

from IPython.display import Image



G=nx.DiGraph()
cls='4'
G=nx.read_gpickle("data/gutenberg/graph_guten_cls"+cls+".gpickle")
comps = nx.strongly_connected_component_subgraphs(G)
comp_nodes=nx.strongly_connected_components(G)

i=0
freq ={}
k=0
for c in comps:
#  if c.number_of_nodes()>10 and c.number_of_nodes()<30:
#    d = nx.to_pydot(c)
#    d.write_png('data/brown/class'+cls+'_scc_nodes'+str(c.number_of_nodes())+'.png')
#    nx.draw_networkx(c)
#    plt.show()
  if len(c) >30:
    print len(c)
    print [n[0] for n in  c.nodes(data=True)]
  
    for cycle in nx.simple_cycles(c):
      if len(cycle)>1 and len(cycle)<=10:
        print cycle
#    print j
print i
  #if c.number_of_nodes()>5:
  #  print i+1,'th component:',c.number_of_nodes(), c.nodes(data=True)
  #i +=1
  #print '----------------------------------------------------------------------------------'
  #print i+1,'th component:',c.number_of_nodes(), len(c.nodes(data=True))
  #print [w[0] for w in c.nodes(data=True)]
#  if c.number_of_nodes()==11:
#    nx.draw_networkx(c)
#    nx.write_gpickle(c,"data/gutenberg/SCC_nodes11.gpickle")
#    for cycle in nx.simple_cycles(c):
#      print cycle
#  i +=1   
#  if c.number_of_nodes()>4 and c.number_of_nodes()<15 :
#    d = nx.to_pydot(c)
#    d.write_png('data/gutenberg/scc_nodes'+str(c.number_of_nodes())+'.png')

    

#    labels={}
#    nodes=[]
#    edges=[]
#    c_nodes=c.nodes(data=True)
#    for i in range(len(c_nodes)):
#      labels[i]=c_nodes[i][0]
#      nodes.append(c_nodes[i][0])
#    print labels
#    for e in c.edges(data=True):
#      edges.append((e[0],e[1]))
#    pos=nx.spring_layout(c)
#    nx.draw_networkx_nodes(c,pos,nodes,node_size=5000,node_color='w',node_shape='s')
#    nx.draw_networkx_edges(c,pos,edges)
#    nx.draw_networkx_labels(c,pos,font_size=16)
#    nx.draw(G, cmap = plt.get_cmap('jet'))
#    plt.show()
#    plt.savefig('data/gutenberg/scc_nodes'+str(c.number_of_nodes())+'.png')
#    nx.draw_networkx(c)
    #nx.write_gpickle(c,"data/largest_SCC.gpickle")
#    print i+1,'th component:',c.number_of_nodes(), len(c.nodes(data=True))
#  i +=1
#    for cycle in nx.simple_cycles(c):
 #     print cycle
