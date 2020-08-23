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

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

#nx.draw(ER_graph(50,0.1), node_size=40, node_color= "gray")

G1 = ER_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = ER_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = ER_graph(500, 0.08)
plot_degree_distribution(G3)
plt.show()
