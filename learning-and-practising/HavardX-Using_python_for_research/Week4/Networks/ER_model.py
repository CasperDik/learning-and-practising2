import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def ER_graph(N,p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

nx.draw(ER_graph(50, 0.08), node_size=40, node_color="gray")
plt.show()