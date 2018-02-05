import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("England",edible=True)
G.add_node("Egypt")
G.add_node("Brazil")
G.add_node("Spain")
G.add_node("China")

G.add_edges_from([('England','Egypt'),('Brazil','Spain'),('China','Egypt'),('China','Brazil'),('England','Spain'),('Spain','China'),('Brazil','Brazil')])

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=False)
nx.draw_networkx_labels(G, pos)
plt.show()

nx.write_gexf(G, "test.gexf")


print (G.node)
print (G.edges)
print(G.nodes(data=True))