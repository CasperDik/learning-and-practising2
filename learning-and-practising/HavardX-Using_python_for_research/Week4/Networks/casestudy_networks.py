from collections import Counter
import numpy as np
import pandas as pd
import networkx as nx

def marginal_prob(chars):
    keys = chars.values()
    values = []
    counter = list(Counter(chars.values()).values())
    for char in counter:
        mp = char / np.sum(counter)
        values.append(mp)
    return dict(zip(keys, values))

def chance_homophily(chars):
    mp = marginal_prob(chars)
    x = np.array(list(mp.values()))
    return np.sum(x**2)

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)

pid1 = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv", dtype=int)['0'].to_dict()
pid2 = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv", dtype=int)['0'].to_dict()

df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = df.loc[df.village == 1]
df2 = df.loc[df.village == 2]

sex1      = dict(zip(df1.pid, df1.resp_gend))
caste1    = dict(zip(df1.pid, df1.caste))
religion1 = dict(zip(df1.pid, df1.religion))

sex2      = dict(zip(df2.pid, df2.resp_gend))
caste2    = dict(zip(df2.pid, df2.caste))
religion2 = dict(zip(df2.pid, df2.religion))

A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)


print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1), "chance homophily: ", chance_homophily(sex1))
print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2), "chance homophily: ", chance_homophily(sex2))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1), "chance homophily: ", chance_homophily(caste1))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2), "chance homophily: ", chance_homophily(caste2))
print("Village 1 observed proportion of same religion :", homophily(G1, religion1, pid1), "chance homophily: ", chance_homophily(religion1))
print("Village 2 observed proportion of same religion :", homophily(G2, religion2, pid2), "chance homophily: ", chance_homophily(religion2))
