import os
import networkx as nx
import matplotlib.pyplot as plt

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    G = nx.Graph()
    with open(input_filepath) as file:
        for line in file:
            tokens = line.rstrip().split(": ")
            v0 = tokens[0]
            for v1 in tokens[1].split():
                G.add_edge(v0, v1)
    return G

def draw_graph(G: nx.Graph):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 800)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.show()